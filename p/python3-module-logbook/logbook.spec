%define oname logbook

%def_with check

Name: python3-module-%oname
Version: 1.9.2
Release: alt1.1

Summary: A logging replacement for Python
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/Logbook
VCS: https://github.com/mitsuhiko/logbook

Source: %name-%version.tar
Source1: crates.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-rust

BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools-rust
BuildRequires: python3-module-notebook python3-module-setuptools
BuildRequires: python3-module-mock python3-module-brotlipy

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_basic_ng
BuildRequires: python3-module-furo
BuildRequires: python3-module-accessible-pygments

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
%setup -a1
%rust_prep

sed -i 's/sphinx-build/&-3/' docs/Makefile

%build
%pyproject_build

%install
%pyproject_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%pyproject_run_pytest

%files
%doc LICENSE AUTHORS CHANGES *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Sat Mar 28 2026 Grigory Ustinov <grenka@altlinux.org> 1.9.2-alt1.1
- Fixed FTBFS.

* Thu Jan 29 2026 Grigory Ustinov <grenka@altlinux.org> 1.9.2-alt1
- Automatically updated to 1.9.2.
- Built with check.

* Tue Jun 24 2025 Grigory Ustinov <grenka@altlinux.org> 1.8.2-alt1
- Automatically updated to 1.8.2.

* Thu Mar 20 2025 Grigory Ustinov <grenka@altlinux.org> 1.8.1-alt1
- Automatically updated to 1.8.1.

* Sun Oct 27 2024 Grigory Ustinov <grenka@altlinux.org> 1.8.0-alt1
- Automatically updated to 1.8.0.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Automatically updated to 1.7.0.

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

