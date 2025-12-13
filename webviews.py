'''_

Let's create a simple web application framework. We'll need view
classes for each page on the site:

>>> home_view = HomePageView()
>>> home_view.render()
'<html><body>Welcome!</body></html>'
>>> home_view.body
'Welcome!'

>>> about_view = AboutPageView()
>>> about_view.render()
'<html><body>This is a simple website about nutrition.</body></html>'

To route URLs to views, we'll create a global webapp object.

>>> app = WebApp()

Routings - that is, a mapping from a URL to a view object - are
created with add_route(). Then you can get and render the view with
get().

>>> app.add_route("/", home_view)
>>> app.add_route("/about/", about_view)
>>> app.get("/")
'<html><body>Welcome!</body></html>'
>>> app.get("/about/")
'<html><body>This is a simple website about nutrition.</body></html>'

Some more views:

>>> class ContactView(HTMLView):
...     body = 'Get in touch at hello@example.com'
...
>>> app.add_route("/contact/", ContactView())
>>> app.get("/contact/")
'<html><body>Get in touch at hello@example.com</body></html>'

And let's add a helper to give us a sorted list of all URLs defined so far.

>>> app.urls()
['/', '/about/', '/contact/']

And we can have more specialized views, FOR EXAMPLE WHEN WE WANT TO
OUR WRITING TO MAKE AN IMPACT:

>>> issubclass(ShoutingHTMLView, HTMLView)
True

>>> class LegalView(ShoutingHTMLView):
...     body = 'you agree to our terms of service!'

>>> legal_view = LegalView()
>>> app.add_route("/legal/", legal_view)
>>> app.get("/legal/")
'<HTML><BODY>YOU AGREE TO OUR TERMS OF SERVICE!</BODY></HTML>'
>>> isinstance(legal_view, HTMLView)
True

Python lets you do something called "monkey patching".  It can lead to
hard-to-understand code, so don't overuse it. But it can be useful
when working with certain libraries whose source you cannot/do not
want to modify, for example.

The idea is you modify a method of an already-created object, or a
superclass deep in an inheritance hierarchy, by assigning to it
directly. It works because in Python, (a) everything is an object, and
(b) methods are just attributes that can be assigned to.

>>> original_htmlview_render = HTMLView.render
>>> def new_htmlview_render(self):
...     # Add <p> tag around content
...     return '<html><body><p>' + self.body + '<p></body></html>'
>>> HTMLView.render = new_htmlview_render

Now that HTMLView is modified, instances of its subclasses are
modified too - provided that subclass reuses that method defined in
the superclass:

>>> legal_view.render()
'<HTML><BODY><P>YOU AGREE TO OUR TERMS OF SERVICE!<P></BODY></HTML>'

'''

# Write your code here:
class WebApp:
    routes = [];
    views = {}
    def add_route(self, route, view):
        self.__class__.routes.append(route);
        self.__class__.views[route] = view;
    
    def get(self, route):
        return_view = self.__class__.views.get(route)
        return return_view;
    
    def urls(self):
        return WebApp.routes;

class HTMLView:
    def render(self):
        return f"<html><body>{self.body}</body></html>"
    
    def __repr__(self) -> str:
        return f"'<html><body>{self.body}</body></html>'"

class ShoutingHTMLView(HTMLView):
    def render(self):
        return f"<html><body><p>{self.body}<p></body></html>".upper();
    
    def __repr__(self) -> str:
        original_htmlview_render = HTMLView.render;

        return f"'{ original_htmlview_render(self).upper() }'"

class HomePageView(HTMLView):
    body = "Welcome!";

class AboutPageView(HTMLView):
    body = "This is a simple website about nutrition."

class ContactView(HTMLView):
    body = "Get in touch at hello@example.com"

class LegalView(ShoutingHTMLView, HTMLView):
    body = 'you agree to our terms of service!'

    def __repr__(self) -> str:
        return super().__repr__()

# Do not edit any code below this line!
if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# From Powerful Python. Copyright MigrateUp LLC. All rights reserved.
