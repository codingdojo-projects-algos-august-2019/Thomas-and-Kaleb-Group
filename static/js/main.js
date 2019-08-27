$(document).ready(function() {
	function navBar() {
		console.log('working');
		$.ajax({
			url: '/nav'
		}).done(function(res) {
			$('nav').html(res);
			var path = window.location.pathname;
			p2 = path.split('/');
			if (!parseInt(p2[p2.length - 1])) {
				liChild = $('li').has('a[href="' + path + '"]');
				$(liChild).addClass('active');
			} else {
				p2.length--;
				path = p2.join('/');
				liChild = $('li').has('a[href="' + path + '"]');
				$(liChild).addClass('active');
			}
		});
	}
	navBar();
});
