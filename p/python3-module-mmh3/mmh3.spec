%define oname mmh3

Name:        python3-module-%oname
Version:     2.5.1
Release:     alt1

Summary:     Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust hash functions.
License:     CC0 1.0
Group:       Development/Python3
Url:         https://github.com/hajimes/mmh3

Source:      %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-build-licenses
BuildPreReq:        python3-module-setuptools python3-devel
BuildRequires:      gcc-c++


%description
Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust hash functions.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/*

%changelog
* Wed Aug 14 2019 Ivan Razzhivin <underwit@altlinux.org> 2.5.1-alt1
- Initial build for ALT Linux Sisyphus


