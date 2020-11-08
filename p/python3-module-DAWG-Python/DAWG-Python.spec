%define  modulename DAWG-Python

Name:    python3-module-%modulename
Version: 0.7.2
Release: alt1

Summary: Pure-python reader for DAWGs created by dawgdic C++ library or DAWG Python extension.

License: MIT
Group:   Development/Python3
URL:     https://github.com/pytries/DAWG-Python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/dawg_python
%python3_sitelibdir/*.egg-info

%changelog
* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus.
