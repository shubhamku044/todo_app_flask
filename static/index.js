'use strict';

let loader = document.getElementById('todo__loading-animation');
let mainContent = document.getElementById('main');
function showLoading() {
	window.addEventListener('load', () => {
		loader.style.display = 'none';
		mainContent.style.display = 'block';
	});
}

showLoading();
