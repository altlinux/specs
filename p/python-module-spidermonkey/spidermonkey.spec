Name: python-module-spidermonkey
Version: 0.0.10
Release: alt4.1.1
Summary: JavaScript/python bridge
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/python-spidermonkey
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: python-spidermonkey-%version.tar

BuildPreReq: python-module-setuptools python-module-Pyrex
BuildRequires: libnspr-devel xulrunner-devel python-module-nose

%description
Python/JavaScript bridge module, making use of Mozilla's spidermonkey
JavaScript implementation. Allows implementation of JavaScript classes,
objects and functions in Python, and evaluation and calling of JavaScript
scripts and functions respectively.

%prep
%setup

%build
%add_optflags -I/usr/include/mozjs
%python_build

%install
mkdir -p %buildroot
%python_install --install-data=%buildroot%_datadir --optimize=2 \
	--record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.10-alt4.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.10-alt4.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt4
- Fixed build

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt3
- Rebuilt for debuginfo

* Thu Mar 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt2
- Fixed underlinking

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt1
- Initial build for Sisyphus

