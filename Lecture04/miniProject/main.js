// need jquery

'use strict';

var testJsonObject = {"postList": [
    {"postContent": "This is my First Post",
     "replyList": [
         "This is my first reply",
         "This is my second reply", 
         "Me three" ]
    }, {
     "postContent": "This is my Second Post",
     "replyList": [
         "Hahahah",
         "Hehehe" ]
    }
    ]
}

var content = $('#content');

var render_new_post = function(post) {

    var mainPost = $('<div/>', { 'class': 'mainPost' });
    mainPost.append($('<p/>', { 'html': post.postContent }));

    var replies = $('<div/>', { 'class': 'replies' });
    post.replyList.forEach(function(r) {
        replies.append($('<div/>', {
            'class': 'reply',
            'html': r
        }));
    });

    var textAreaDiv = $('<div/>', {'class': 'reply-area'});
    var textArea = $('<textarea/>');
    var textAreaBotton = $('<div/>', {'class': 'reply-botton', 'text': 'Send'});
    textAreaDiv.append([textArea, textAreaBotton]);
    replies.append(textAreaDiv);
    replies.hide();

    var seeReply = $('<div/>', {'class': 'seeReply'});
    var seeReplyButton = $('<span/>', {'html': 'see replies'});
    seeReply.append(seeReplyButton);

    var new_post = $('<div/>', { 'class': 'post' });
    new_post.append([mainPost, seeReply, replies]);
    content.prepend(new_post);
}

$(function() {
    var open_re = "see replies";
    var fold_re = "fold replies";
    content.on('click', '.post .seeReply span', function() {
        if ($(this).text() == fold_re) {
            $(this).text(open_re);
        }
        else {
            $(this).text(fold_re);
        }
        $(this).parent().siblings('.replies').slideToggle();
    });
    console.log('document loaded');
    testJsonObject.postList.forEach(function(r) {
        render_new_post(r);
    });
    console.log('post loaded');
});
