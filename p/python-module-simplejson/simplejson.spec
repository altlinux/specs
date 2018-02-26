%define shortname simplejson

Name: python-module-simplejson
Version: 2.5.0
Release: alt1

Summary: Simplejson is a simple, fast, extensible JSON encoder/decoder for Python
License: MIT/X Consortium
Group: Development/Python

Url: http://undefined.org/python/#simplejson

Packager: Python Development Team <python@packages.altlinux.org>

Source0: %shortname-%version.tar

BuildRequires: python-module-setuptools python-module-sphinx


%description
Simplejson is a simple, fast, complete, correct and extensible JSON
encoder and decoder for Python 2.3+. It is pure Python code with no
dependencies.

%package doc
Summary: Documentation for %name
Group: Development/Python
BuildArch: noarch

%description doc
Simplejson is a simple, fast, complete, correct and extensible JSON
encoder and decoder for Python 2.3+. It is pure Python code with no
dependencies.

This package contains documentation for simplejson.


%prep
%setup -n %shortname-%version

%build
%add_optflags -fno-strict-aliasing
%python_build_debug
./scripts/make_docs.py

%install
%python_install

%files
%python_sitelibdir/%shortname/
%exclude %python_sitelibdir/%shortname/tests
%python_sitelibdir/*.egg-info

%check
python setup.py check

%files doc
%doc docs/*

%changelog
* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1
- Version 2.5.0

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.3-alt1
- 2.1.3
- enable tests

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.2-alt2.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt2
- Rebuilt for debuginfo

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1.1
- Rebuilt with python 2.6

* Fri May 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.9-alt1
- 2.0.9
- numerous spec fixes
- package documentation
- don't package tests

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.7.4-alt1.1
- Rebuilt with python-2.5.

* Thu Nov 15 2007 Gennady Kovalev <gik@altlinux.ru> 1.7.4-alt1
- 1.7.4 release

* Wed Mar 22 2006 Gennady Kovalev <gik@altlinux.ru> 1.1-alt1
- Initial build
