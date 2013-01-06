%define version 0.8.3
%define release alt1
%setup_python_module werkzeug

Summary: Werkzeug is one of the most advanced WSGI utility modules
Name: %packagename
Version: %version
Release: %release
Source0: %modulename.tar
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://werkzeug.pocoo.org/

BuildRequires: python-module-setuptools python-modules-json

%description
Werkzeug started as a simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules. It includes a powerful debugger, fully featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

It does Unicode and doesn't enforce a specific template engine, database
adapter or anything else. It doesn't even enforce a specific way of
handling requests and leaves all that up to the developer.

%prep
%setup -q -n %modulename

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%check
%__python ./setup.py test

%files -f INSTALLED_FILES
%doc AUTHORS CHANGES LICENSE

%changelog
* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.8.3-alt1
- 0.8.3 (ALT #28297);
- minor packaging improvements.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Sergey Alembekov <rt@altlinux.ru> 0.6.2-alt1
- Initial release for ALTLinux
