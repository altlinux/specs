%define oname pyfactory

Name: python3-module-%oname
Version: 0.4.0
Release: alt2

Summary: Generic model factory framework
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyfactory/
BuildArch: noarch

# https://github.com/kiip/pyfactory.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python-tools-2to3


%description
PyFactory is a library for writing generic model factories useful for
unit testing.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
PyFactory is a library for writing generic model factories useful for
unit testing.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
PyFactory is a library for writing generic model factories useful for
unit testing.

This package contains documentation for %oname.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc CHANGELOG *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0-alt1.git20130326.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.git20130326.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.git20130326.1
- NMU: Use buildreq for BR.

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20130326
- Initial build for Sisyphus

