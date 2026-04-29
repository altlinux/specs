%def_disable snapshot
%define _name showinfilemanager
%define modname show-in-file-manager
%define pypi_name show_in_file_manager

Name: %_name
Version: 1.1.6
Release: alt1

Summary: Show in File Manager
Group: File tools
License: MIT
Url: http://pypi.python.org/pypi/%modname

Vcs: https://github.com/damonlynch/show-in-file-manager.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %modname-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling) python3(hatch_argparse_manpage)
BuildRequires: pandoc

%description
Show in File Manager is a Python package to open the system file manager
and optionally select files in it. The point is not to open the files,
but to select them in the file manager, thereby highlighting the files
and allowing the user to quickly do something with them.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
install -pD -m644 man/%name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.1*
%python3_sitelibdir_noarch/showinfm/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/
%doc README* CHANGELOG*

%changelog
* Wed Apr 29 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Mon Mar 07 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Tue Dec 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- first build for Sisyphus


