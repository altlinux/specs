%define oname geographiclib

Name: python3-module-%oname
Version: 1.50
Release: alt1

Summary: This is a python implementation of the geodesic routines in GeographicLib.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/geographiclib/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
This is a python implementation of the geodesic routines in GeographicLib.

Although it is maintained in conjunction with the larger C++ library, this
python package can be used independently.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README.md
%python3_sitelibdir/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.50-alt1
- Initial build for Sisyphus

