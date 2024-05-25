%define oname unicodedata2

Name: python3-module-%oname
Version: 15.1.0
Release: alt1

Summary: Unicodedata backport for python 2 updated to the latest unicode version
License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/unicodedata2
VCS: https://github.com/fonttools/unicodedata2

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
The versions of this package match unicode versions, so
unicodedata2==7.0.0 is data from unicode 7.0.0. Additionally this
backports support for named aliases and named sequences to python2.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/unicodedata2-%version.dist-info
%python3_sitelibdir/unicodedata2.cpython*.so

%changelog
* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 15.1.0-alt1
- Automatically updated to 15.1.0.

* Mon Dec 12 2022 Grigory Ustinov <grenka@altlinux.org> 15.0.0-alt1
- Build new version.

* Wed Dec 15 2021 Grigory Ustinov <grenka@altlinux.org> 13.0.0.post2-alt1
- Build new version.

* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 12.1.0-alt1
- Version updated to 12.1.0
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 7.0.0.2-alt1.git20150807.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.0.2-alt1.git20150807
- Initial build for Sisyphus

