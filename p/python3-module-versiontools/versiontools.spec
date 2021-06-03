%define oname versiontools

Name: python3-module-%oname
Version: 1.9.1
Release: alt2
Summary: Smart replacement for plain tuple used in __version__
License: LGPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/versiontools/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

%description
Smart replacement for plain tuple used in __version__.

%package tests
Summary: Tests for versiontools
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Smart replacement for plain tuple used in __version__.

This package contains tests for versiontools.

%package pickles
Summary: Pickles for versiontools
Group: Development/Python3

%description pickles
Smart replacement for plain tuple used in __version__.

This package contains pickles for versiontools.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv doc/

%build
%python3_build

export PYTHONPATH=$PWD
cp -f doc/conf.py ./
sphinx-build-3 -E -a -b html -c $PWD -d doctrees doc html
sphinx-build-3 -E -a -b pickle -c $PWD -d doctrees doc pickles

%install
%python3_install

cp -fR pickles %buildroot%python3_sitelibdir/%oname/

%files
%doc html/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests.py*
%exclude %python3_sitelibdir/%oname/pickles
%exclude %python3_sitelibdir/%oname/__pycache__/tests.*

%files pickles
%python3_sitelibdir/%oname/pickles

%files tests
%python3_sitelibdir/%oname/tests.py*
%python3_sitelibdir/%oname/__pycache__/tests.*

%changelog
* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.9.1-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.9.1-alt1.1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.1-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.1-alt1.1.1
- NMU: Use buildreq for BR.

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.9.1-alt1.1
- Rebuild with Python-3.3

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus

