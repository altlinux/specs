%define version 1.1.4
%define release alt2.1
%setup_python_module postmarkup

Name: %packagename
Version: %version
Release: %release.1

Summary: Generates XHTML snippets from BBCode

License: BSD
Group: Development/Python
BuildArch: noarch
Url: http://code.google.com/p/postmarkup
Packager: Denis Klimov <zver@altlinux.org>

Source: %modulename-%version.tar

%description
Generates XHTML snippets from BBCode.

%prep
%setup -n %modulename-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt2.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt2.1
- Rebuilt with python 2.6

* Sun Feb 01 2009 Denis Klimov <zver@altlinux.org> 1.1.4-alt2
- more improve using setup_python_module macros
- use optimize and record options for install
- add BuildArch: noarch

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 1.1.4-alt1
- Initial build for ALT Linux

