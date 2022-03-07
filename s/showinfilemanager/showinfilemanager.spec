%def_disable snapshot
%define modname show-in-file-manager

Name: showinfilemanager
Version: 1.1.4
Release: alt1

Summary: Show in File Manager
Group: File tools
License: MIT
Url: http://pypi.python.org/pypi/%modname

%if_disabled snapshot
Source: https://pypi.io/packages/source/s/%modname/%modname-%version.tar.gz
%else
Vcs: https://github.com/damonlynch/show-in-file-manager.git
Source: %modname-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: pandoc

%description
Show in File Manager is a Python package to open the system file manager
and optionally select files in it. The point is not to open the files,
but to select them in the file manager, thereby highlighting the files
and allowing the user to quickly do something with them.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install
install -pD -m644 man/%name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.1*
%python3_sitelibdir_noarch/showinfm/
%python3_sitelibdir_noarch/*.egg-info
%doc README* CHANGELOG*

%changelog
* Mon Mar 07 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Tue Dec 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- first build for Sisyphus


