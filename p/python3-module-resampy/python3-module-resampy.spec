%define modulename resampy

Name:    python3-module-%modulename
Version: 0.2.2
Release: alt1

Summary: Efficient signal resampling.
License: MIT
Group:   Development/Python3
URL:     https://github.com/bmcfee/resampy

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

Requires: python3-module-numpy
Requires: python3-module-scipy
Requires: python3-module-numba
Requires: python3-module-six

BuildArch: noarch

Source:  %modulename-%version.tar.gz


%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md LICENSE PKG-INFO

%changelog
* Sun Oct 04 2020 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus.
