%define oname logbook

%def_without check

Name: python3-module-%oname
Version: 1.6.0
Release: alt1

Summary: A logging replacement for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Logbook/
# https://github.com/mitsuhiko/logbook.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx3 rpm-build-python3
BuildRequires: python3-module-Cython
BuildRequires: python3-module-notebook python3-module-setuptools
BuildRequires: python3-module-mock python3-module-brotlipy
BuildRequires: python3-module-sphinx


%description
An awesome logging implementation that is fun to use.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
An awesome logging implementation that is fun to use.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
An awesome logging implementation that is fun to use.

This package contains documentation for %oname.

%prep
%setup

sed -i 's/sphinx-build/&-3/' docs/Makefile

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
py.test3

%files
%doc LICENSE AUTHORS CHANGES *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Automatically updated to 1.6.0.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.3-alt3
- cleanup BR

* Tue Oct 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.3-alt2
- python2 -> python3

* Wed Mar 27 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.3-alt1
- Build new version for python3.7.
- Disable check.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Updated to upstream release 1.1.0.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.dev.git20141012.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1.dev.git20141012.1
- NMU: Use buildreq for BR.

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.dev.git20141012
- Initial build for Sisyphus

