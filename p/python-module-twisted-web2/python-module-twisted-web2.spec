%define version 8.1.0
%define release alt2
%define origname TwistedWeb2
%setup_python_module twisted-web2

Name:           %packagename
Version:        %version
Release:        %release.1
Summary:        Twisted HTTP/1.1 Server Framework, programmable in Python

Group:          Development/Python
License:        MIT
URL:            http://twistedmatrix.com/trac/wiki/TwistedWeb
Packager:	Sergey Alembekov <rt@altlinux.ru>
Source0:        http://tmrc.mit.edu/mirror/twisted/Web2/%origname-%version.tar.bz2

BuildRequires:  python-module-twisted-core >= 8.2.0
BuildRequires:  python-devel

Requires:       python-module-twisted-core

%description
Twisted.Web2 is the next generation web server built with 
Twisted. Web2 is under active development and its APIs should 
not be considered stable at this point. It is not a version 
of Twisted.Web and while the compatibility layer does support 
many, currently this is not the highest concern.

%prep
%setup -q -n %origname-%version

%build
%__python setup.py build

%install
%__python setup.py install --root $RPM_BUILD_ROOT --install-purelib %python_sitelibdir

%files
%doc README LICENSE NEWS doc/*

%python_sitelibdir/twisted/web2
%python_sitelibdir/Twisted_Web2-*.egg-info
%python_sitelibdir/twisted/plugins/twisted_web2.py*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 8.1.0-alt2.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.1.0-alt2
- Rebuilt with python 2.6

* Mon Oct 19 2009 Sergey Alembekov <rt@altlinux.ru> 8.1.0-alt1
- new version 8.1.0

* Sat Oct 27 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.0-alt1.1
- Fix build on x86_64
- Spec file cleanup

* Fri Mar 30 2007 Sergey Alembekov <rt@altlinux.ru> 0.2.0-alt1
 - Build for new upstream version
