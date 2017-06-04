Name: python-module-billiard
Version: 3.3.0.23
Release: alt1

Summary: billiard is a fork of the Python 2.7 multiprocessing package
Source: %name-%version.tar
License: GPL
Group: Development/Python
Requires: python
Packager: Dmitry Derjavin <dd@altlinux.org>
Url: https://github.com/celery/billiard/

BuildRequires: python-devel gcc-c++ python-module-sphinx

%description
billiard is a fork of the Python 2.7 multiprocessing package.
The multiprocessing package itself is a renamed and updated version of
R Oudkerk's pyprocessing package. This standalone variant is intended
to be compatible with Python 2.4 and 2.5, and will draw it's
fixes/improvements from python-trunk.

%prep
%setup

%build
rm -f billiard/tests/test_multiprocessing.py
python setup.py build
python setup.py build_sphinx --builder="html" --source-dir=Doc

%install
mv build/sphinx/html html
python setup.py install --root=%buildroot --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc html LICENSE.txt CHANGES.txt

%changelog
* Wed May 31 2017 Lenar Shakirov <snejok@altlinux.ru> 3.3.0.23-alt1
- Version 3.3.0.23

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0.20-alt1
- Version 3.3.0.20

* Sat Oct 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0.18-alt1
- Version 3.3.0.18 (ALT #30404)

* Thu Apr 11 2013 Dmitry Derjavin <dd@altlinux.org> 2.7.3.26-alt2
- test_multiprocessing.py removed because of the wrong python2.7(test)
  dependency.

* Thu Apr 11 2013 Dmitry Derjavin <dd@altlinux.org> 2.7.3.26-alt1
- Initial ALTLinux build.


