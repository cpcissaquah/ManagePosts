import logging
from splinter import Browser


class Posts(object):
    def __init__(self, domain, username, password):
        logging.debug('Initiating ManagePost object for domain:  {}'.format(domain))

        self.browser = Browser()
        self.domain = domain
        self.username = username
        self.password = password

    def _visit(self, site):
        logging.debug('Visiting:  {}'.format(site))
        self.browser.visit(site)

        if "Log In" in self.browser.title:
            logging.debug('Logging in')
            self.browser.find_by_id('user_login').type(self.username)
            self.browser.find_by_id('user_pass').type(self.password)
            self.browser.find_by_id('wp-submit').click()
        else:
            logging.debug('Already logged in')
        
    def set_post_audio(self, post_id, audio_link):
        logging.info('Adding audio link to post {} for {}:  {}'.format(post_id, self.domain, audio_link))
        site = 'http://{}/wp-admin/post.php?post={}&action=edit'.format(self.domain, post_id)
        self._visit(site)

        self.browser.find_by_name('_ctc_sermon_audio').type(audio_link)
        self.browser.find_by_id('publish').first.click()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        logging.debug('Cleaning up ManagePost object.')
        self.browser.quit()

