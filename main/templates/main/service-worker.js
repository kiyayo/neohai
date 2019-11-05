importScripts('https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js');

if(workbox){
    console.log('workbox is available!')
}
else{
    console.log('workbox did not load')
}

workbox.routing.registerRoute(
    /\.(?:js|css|png|gif|jpg|jpeg|svg)$/,
    new workbox.strategies.NetworkFirst()
  );

workbox.routing.registerRoute(new RegExp('https:.*min\.(css|js)'),
new workbox.strategies.NetworkFirst()
);
