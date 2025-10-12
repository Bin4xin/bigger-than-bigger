// ==UserScript==
// @name         Bilibili UI Modifications
// @namespace    http://tampermonkey.net/
// @version      0.4
// @description  Multiple UI modifications for bilibili.com including removing ad cards, position attribute, chat elements, and shield tool
// @match        *://*.bilibili.com/*
// @grant        none
// @updateURL    https://raw.githubusercontent.com/Bin4xin/bigger-than-bigger/master/assets/biliuiblock.js
// @downloadURL  https://raw.githubusercontent.com/Bin4xin/bigger-than-bigger/master/assets/biliuiblock.js
// ==/UserScript==

(function() {
    'use strict';

    // Function to apply all modifications
    function applyModifications() {
        // 1. Remove ad cards with class IconCardAdCard or IconCardAdCardBigNew
        const adCards = document.querySelectorAll('.IconCardAdCard, .IconCardAdCardBigNew');
        adCards.forEach(element => {
            element.remove();
        });

        // 2. Replace the position property of web-player-module-area-mask-panel
        const playerMask = document.getElementById('web-player-module-area-mask-panel');
        if (playerMask) {
            playerMask.style.position = '';
        }

        // 3. Set ChatRank div element height to 0
        const chatRank = document.querySelector('.ChatRank');
        if (chatRank) {
            chatRank.style.height = '0';
        }

        // 4. Remove is-active class from ChatTabContainer-content
        const chatTabContents = document.querySelectorAll('.ChatTabContainer-content.is-active');
        chatTabContents.forEach(element => {
            element.classList.remove('is-active');
        });

        // 5. Change is-noChecked to is-checked in ShieldTool-listItem
        const shieldItems = document.querySelectorAll('.ShieldTool-listItem.is-noChecked');
        shieldItems.forEach(element => {
            element.classList.remove('is-noChecked');
            element.classList.add('is-checked');
        });
    }

    // Apply modifications when page loads
    window.addEventListener('load', applyModifications);

    // Use MutationObserver to watch for dynamic changes
    const observer = new MutationObserver(function(mutations) {
        // Check if any of the target elements were added/modified
        const shouldApply = mutations.some(mutation => {
            return mutation.addedNodes.length > 0 ||
                   mutation.type === 'attributes';
        });

        if (shouldApply) {
            applyModifications();
        }
    });

    // Start observing the document with the configured parameters
    observer.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ['class']
    });
})();
