%define version 1.0.8
%define release alt1.1
%setup_python_module TurboGears

Name: %packagename
Version: 1.0.9
Release: alt3.1

Summary: Back-to-front web development in Python

License: MIT/X11
Group: Development/Python
BuildArch: noarch
Url: http://www.turbogears.org
Packager: Denis Klimov <zver@altlinux.org>

Source: http://files.turbogears.org/eggs/%modulename-%version.tar

BuildPreReq: python-module-setuptools

%py_requires turbokid turbocheetah paste.script

# has no pythonX.Y() provides
Requires: python-module-decoratortools
Requires: python-module-PasteDeploy

# TurboGears needs old CherryPy
Requires: python-module-cherrypy2

%description
TurboGears brings together four major pieces to create an
easy to install, easy to use web megaframework. It covers
everything from front end (MochiKit JavaScript for the browser,
Kid for templates in Python) to the controllers (CherryPy) to
the back end (SQLObject).

The TurboGears project is focused on providing documentation
and integration with these tools without losing touch
with the communities that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.


%prep
%setup -n %modulename-%version
# fix for TurboJson
%__subst "s|, < 1.2||g" setup.py

%build
%python_build

%install
%python_install

%files
%doc README.txt
%_bindir/tg-admin
%python_sitelibdir/turbogears
%python_sitelibdir/TurboGears*.egg-info

%changelog
* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.9-alt3.1
- Rebuild with Python-2.7

* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt3
- add CherryPy 2 requires

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt2
- fix requires (ALT bug #19979)

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt1
- new version (1.0.9) import in git

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.1
- Rebuilt with python 2.6

* Sun Mar 29 2009 Denis Klimov <zver@altlinux.org> 1.0.8-alt1
- Initial build for ALT Linux

