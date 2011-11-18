/**
 * jQuery.spotlight - Add a spotlight to any DIV
 *
 * @author Malachany jerry(at)malachany(dot)com
 * @version 1.1
 *
 *  Permission is hereby granted, free of charge, to any person obtaining a copy
 *	of this software and associated documentation files (the "Software"), to deal
 *	in the Software without restriction, including without limitation the rights
 *	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 *	copies of the Software, and to permit persons to whom the Software is
 *	furnished to do so, subject to the following conditions:
 *	
 *	The above copyright notice and this permission notice shall be included in
 *	all copies or substantial portions of the Software.
 *	
 *	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 *	THE SOFTWARE.
 *
 * 
 *  @param  overLayer  		This is the name of the layer inside
 *					   		your DIV that will hold the spotlight.
 *
 *  @param  spotLightImage  Location of the image for the spotlight.
 *							Must be PNG or GIF
 *
 *  @param  overLayerBg		Background color of the overLayer. Normally
 *							it should match the color of the spotlight
 *
 *  Example
 *  ------------
 *  <script language="JavaScript" type="text/javascript">
 *	$().ready(function() {
 *		$('#header').spotlight( {
 *			overLayer: "headerOver",
 *			spotLightImage: '/images/spotlight.png',
 *			overLayerBg: '#000'
 *		});
 *	})
 *	</script>
 *
 * 	<style type="text/css">
 *		#header {
 *			position: relative;
 *			width: 960px;
 *			height: 110px;
 *			border: 1px solid black;
 *			background: url(../images/header.png) no-repeat;
 *			overflow: hidden;
 *		}
 *	</style>
 *
 *  <div id="header">
 *		<div id="headerOver">
 *			<img src="images/spotlight.png" width="113" height="112" alt="" />
 *		</div>
 *	</div>
 *
 */
 
(function($){  
	$.fn.spotlight = function(options) {
		var defaults = { 
						overLayer: 		'layerOver',
						spotLightImage: '/images/spotlight.png',
						overLayerBg: 	'#000' 
					   };
  		
		var options = $.extend(defaults, options);
		
		return this.each(function() { 
			obj = $(this);
			
			//Get the width of div we are going to spotlight
			var objWidth  = obj.width();
			var objHeight = obj.height();

			//Get sizes of the image in overLayer
			var imgWidth  = $('#'+options.overLayer+' img').width();
			var imgHeight = $('#'+options.overLayer+' img').height();
			
			//Create new width and height of image to fit into underLayer
			var newImageHeight;
			var newImageWidth;
			if (imgWidth > objWidth) {
				newImageWidth  = objWidth;
				newImageHeight = imgHeight / (imgWidth / objWidth);
				newImageWidth  = Math.round(newImageWidth);
			} else {
				newImageHeight = imgHeight;
				newImageWidth  = imgWidth;
			}
			
			if (newImageHeight > objHeight) {
				var tempHeight     = newImageHeight;
				newImageHeight = objHeight;
				newImageWidth  = newImageWidth / (tempHeight/ objHeight);
				newImageWidth  = Math.round(newImageWidth);
			}
			
			//New Width and height of overLayer
			var overLayerWidth  = objWidth*3;
			var overLayerHeight = objHeight*3;
			
			//Set new width and height of overLayer
			$('#'+options.overLayer).width(overLayerWidth);
			$('#'+options.overLayer).height(overLayerHeight);
			
			//Decide where the spotlight image will be placed inside overLayer
			var topImage  = Math.round((overLayerHeight / 2) - (imgHeight / 2));
			var leftImage = Math.round((overLayerWidth / 2)  - (imgWidth / 2));
			
			//Add new div's to the overLayer
			var newHtml  = '<div style="background-color: '+options.overLayerBg+'; width: '+(leftImage-2)+'px; height: '+overLayerHeight+'px;"></div>';
				newHtml += '<div style="width: '+newImageWidth+'px; height: '+overLayerHeight+'px;">';
				
			if (newImageHeight < overLayerWidth) {
				newHtml += '<div style="background-color: '+options.overLayerBg+'; width: '+newImageWidth+'px; height: '+(topImage -1)+'px;"></div>';
			}
			
			newHtml += '<div style="background-image: url('+options.spotLightImage+'); width: '+newImageWidth+'px; height: '+newImageHeight+'px;"></div>';
			
			if (newImageHeight < overLayerWidth) {
				newHtml += '<div style="background-color: '+options.overLayerBg+'; width: '+newImageWidth+'px; height: '+(overLayerHeight-(topImage+newImageHeight)+1)+'px;"></div>';
			}
			
			newHtml += '</div>';
			newHtml += '<div style="background-color: '+options.overLayerBg+'; width: '+(overLayerWidth-(leftImage+newImageWidth))+'px; height: '+overLayerHeight+'px; "></div>';
			
			$('#'+options.overLayer).html(newHtml).css('position', 'relative');
			
			$('#'+options.overLayer+' div').css('position', 'relative')
										   .css('float'   , 'left');
										   
			//obj.mousemove(function(e) {
				//Get X,Y of mouse from header 
			//	var X = e.pageX - this.offsetLeft;
			//	var Y = e.pageY - this.offsetTop;
	
			//	var newLocationTop  = Y - (overLayerHeight/ 2);
			//	var newLocationLeft = X - (overLayerWidth / 2);
	
				//Reposition headerOver div
			//	$('#'+options.overLayer).css('top' , newLocationTop+'px')
			//							.css('left', newLocationLeft+'px');
				
			//});

            // edit
			obj.bind('touchmove', function(e) {
                //Get X,Y of mouse from header
				var event = e.originalEvent;
                event.preventDefault(); // Page stop to move
				var X = event.pageX - this.offsetLeft;
				var Y = event.pageY - this.offsetTop;
	
				var newLocationTop  = Y - (overLayerHeight/ 2);
				var newLocationLeft = X - (overLayerWidth / 2);
	
				//Reposition headerOver div
				$('#'+options.overLayer).css('top' , newLocationTop+'px')
										.css('left', newLocationLeft+'px');
				
			});
			obj.bind('mousemove', function(e) {
                //Get X,Y of mouse from header
				var event = e.originalEvent;
				var X = event.pageX - this.offsetLeft;
				var Y = event.pageY - this.offsetTop;
	
				var newLocationTop  = Y - (overLayerHeight/ 2);
				var newLocationLeft = X - (overLayerWidth / 2);
	
				//Reposition headerOver div
				$('#'+options.overLayer).css('top' , newLocationTop+'px')
										.css('left', newLocationLeft+'px');
				
			});
		});  
	};
})(jQuery);