%define modulename erpc

Name: python3-module-%modulename
Version: 1.13.0
Release: alt1

Summary: Python implementation of the eRPC infrastructure
License: BSD 3-Clause
Group: Development/Python3

Url: https://pypi.org/project/erpc
VCS: https://github.com/EmbeddedRPC/erpc
BuildArch: noarch
Source: %modulename-%version.tar
# https://github.com/beremiz/erpc
Patch0: 0001-Disable-CRC-in-case-of-TCP-transport-since-TCP-alrea.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary.

%prep
%setup -n %modulename-%version
%autopatch -p1
rm -r erpc.egg-info PKG-INFO
touch README_Pypi.md

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version.dist-info/

%changelog
* Tue Jun 17 2025 Anton Midyukov <antohami@altlinux.org> 1.13.0-alt1
- Initial build.
