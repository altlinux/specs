Summary: python refactoring IDE
Name: ropeide
Version: 1.5.1
Release: alt1.1.1
License: GPL
Group: Development/Python
Url: http://rope.sf.net/ropeide.html
Packager: Eugene Ostapets <eostapets@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar.gz

# Automatically added by buildreq on Sat May 10 2008
BuildRequires: python-devel

%description
Ropeide is a python refactoring IDE.  It uses rope library to
provide features like refactoring, code assist, and auto-completion.
It is written in python.  The IDE uses Tkinter library.

%prep
%setup

%build
%__python setup.py build

%install
%__python setup.py install -O1 --skip-build --root="%buildroot" --prefix="%prefix"

%files
%_bindir/%name
%python_sitelibdir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.1-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.1
- Rebuilt with python 2.6

* Sat May 10 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.5.1-alt1
- Initial ALT build
