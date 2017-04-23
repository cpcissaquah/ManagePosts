import logging
import ManagePosts


domain = 'my-domain.org'

with ManagePosts.Posts(domain, 'wordpress_user', 'wordpress_pass') as mp:
    mp.set_post_audio('123', 'http://{}/wp-content/uploads/2017/03/aaron_test_sermon.mp3'.format(domain))
    mp.set_post_audio('124', 'http://{}/wp-content/uploads/2017/03/aaron_test_sermon.mp3'.format(domain))
