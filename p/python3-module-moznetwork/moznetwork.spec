%define oname moznetwork

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Library of network utilities for use in Mozilla testing
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/moznetwork/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six
BuildRequires: python3-module-mozinfo python3-module-mozlog


%description
Library of network utilities for use in Mozilla testing.

%prep
%setup

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
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1
- Version updated ti 1.0.0
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.24-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt2
- Enabled testing

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt1
- Initial build for Sisyphus

