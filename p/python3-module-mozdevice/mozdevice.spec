%define _unpackaged_files_terminate_build 1

%define oname mozdevice

Name: python3-module-%oname
Version: 3.0.7
Release: alt2

Summary: Mozilla-authored device management
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozdevice/
BuildArch: noarch

Source0: https://pypi.python.org/packages/d5/bf/5a305d6b80f2b7e49904c366e95a6e2a67141a5a6c4d1472d4bfdfb82bff/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mozfile python3-module-mozlog
BuildRequires: python3-module-moznetwork python3-module-mozprocess
BuildRequires: python3-module-six


%description
Mozilla-authored device management.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0.7-alt2
- Version updated to 3.0.7
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.48-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.44-alt1
- Initial build for Sisyphus

