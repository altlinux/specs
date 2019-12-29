Name: python3-module-i3ipc
Version: 2.1.1.g13d6e3c
Release: alt1
Summary: An improved Python library to control i3wm and sway
Group: Development/Python

License: BSD-3-Clause
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
%summary.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/i3ipc
%python3_sitelibdir_noarch/i3ipc*.egg-info

%changelog
* Sat Dec 28 2019 Alexey Gladkov <legion@altlinux.ru> 2.1.1.g13d6e3c-alt1
- Initial build (2.1.1.g13d6e3c).
