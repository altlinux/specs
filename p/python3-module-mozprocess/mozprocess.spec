%define _unpackaged_files_terminate_build 1
%define oname mozprocess

Name: python3-module-%oname
Version: 1.4.0
Release: alt1

Summary: Mozilla-authored process handling
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/mozprocess

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Mozilla-authored process handling.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc PKG-INFO
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Tue Aug 20 2024 Anton Vyatkin <toni@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Fri Jul 14 2023 Anton Vyatkin <toni@altlinux.org> 1.3.1-alt1
- new version 1.3.1

* Fri Mar 10 2023 Anton Vyatkin <toni@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8-alt1
- Version updated to 0.8
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.24-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21-alt1
- Initial build for Sisyphus

