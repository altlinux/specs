%define  modulename v4l2

Name:    python3-module-%modulename
Version: 0.2
Release: alt1

Summary: A Python binding for the v4l2 (video4linux2) userspace api
License: GPLv2
Group:   Development/Python3
URL:     https://pypi.org/project/v4l2/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar.gz

%description
A Python binding for the v4l2 (video4linux2) userspace api.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/__pycache__/v4l2.cpython*
%python3_sitelibdir/*.egg-info

%changelog
* Thu Apr 25 2019 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Initial build for Sisyphus.
