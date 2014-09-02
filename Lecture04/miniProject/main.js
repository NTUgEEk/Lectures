// need jquery

'use strict';

var content = $('#content');

var render_new_post = function(post) {
    var mainPost = $('<div/>', { 'class': 'mainPost' });
    mainPost.append($('<p/>', { 'html': post.mainPost }));
    var replies = $('<div/>', { 'class': 'replies' });
    post.replies.forEach(function(r) {
        replies.append($('<div/>', {
            'class': 'reply',
            'html': r
        }));
    });
    var new_post = $('<div/>', { 'class': 'post' });
    new_post.append([mainPost, replies]);
    content.prepend(new_post);
}

$(function() {
    console.log('document loaded');
});
