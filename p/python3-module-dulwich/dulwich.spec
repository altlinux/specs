%define _unpackaged_files_terminate_build 1
%define pypi_name dulwich

%def_enable check

Name: python3-module-%pypi_name
Version: 0.20.50
Release: alt1

Summary: Python Git Library
License: Apache-2.0 or GPL-2.0-or-later
Group: Development/Python3
Url: https://www.dulwich.io

Vcs: https://github.com/dulwich/dulwich.git
Source: https://pypi.io/packages/source/d/%pypi_name/%pypi_name-%version.tar.gz

%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
%{?_enable_check:BuildRequires: python3(tox)
BuildRequires: python3(urllib3)
BuildRequires: python3(fastimport)}
#gpg.errors.GPGMEError: GPGME: Invalid crypto engine
#BuildRequires: python3(gpg) /usr/bin/gpg

%description
Simple Python implementation of the Git file formats and protocols.
Dulwich is the place where Mr. and Mrs. Git live in one of the Monty
Python sketches.

All functionality is available in pure Python, but (optional) C
extensions are also available for better performance.

%package tests
Summary: Tests for dulwich
Group: Development/Python3
Requires: %name = %EVR

%description tests
Simple Python implementation of the Git file formats and protocols.
Dulwich is the place where Mr. and Mrs. Git live in one of the Monty
Python sketches.

All functionality is available in pure Python, but (optional) C
extensions are also available for better performance.

This package contains tests for dulwich.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%check
%tox_check

%files
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/contrib
%doc AUTHORS COPYING NEWS docs/*.txt
%doc docs/tutorial PKG-INFO README* examples

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/contrib

%changelog
* Sat Dec 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.20.50-alt1
- 0.20.50
- fixed Url, Vcs, Source and License tags
- ported to %%pyproject* macros
- enabled %%check

* Mon Aug 12 2019 Anatoly Kitaikin <cetus@altlinux.org> 0.19.11-alt1
- Release 0.19.11

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.3-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt1.git20120327.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20120327
- Initial build for Sisyphus

