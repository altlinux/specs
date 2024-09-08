%define _unpackaged_files_terminate_build 1
%define widget_id de.davidhi.ddcci-brightness
%define py_module_name ddcci_plasmoid_backend
%def_with check

Name: kde-plasma-addon-ddcci
Version: 0.1.10
Release: alt3
Summary: KDE Plasma widget to adjust the brightness of multiple external monitors
License: MIT
Group: Graphical desktop/KDE
Url: https://github.com/davidhi7/ddcci-plasmoid
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-kf6
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
%endif

Requires: ddcutil
Requires: python3-module-%py_module_name = %EVR

Provides: kde5-plasma-addon-ddcci = %EVR
Obsoletes: kde5-plasma-addon-ddcci < %EVR

%description
This widget allows you to adjust the brightness of external monitors.
We accomplish that using DDC/CI, a protocol that allows your computer
to control monitors and change options like the brightness or contrast.
A seamless integration into the Plasma desktop is a major goal of this
project. The widget is versatile and can be used as a standalone widget
or integrated into the system tray. Notebook monitors are currently
unsupported because they use different interfaces to communicate with
the operating system.

%package -n python3-module-%py_module_name
Summary: Backend for ddcci-plasmoid
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%py_module_name
This package contains python3 backend for %name.

%prep
%setup

%build
cd backend && %pyproject_build

%install
mkdir -p %buildroot%_datadir/plasma/plasmoids/%widget_id
cp -pr plasmoid/* %buildroot%_datadir/plasma/plasmoids/%widget_id
cd backend && %pyproject_install

%check
cd backend && %pyproject_run_pytest

%files
%_datadir/plasma/plasmoids/%widget_id

%files -n python3-module-%py_module_name
%_bindir/%py_module_name
%python3_sitelibdir/%py_module_name
%python3_sitelibdir/%{pyproject_distinfo %py_module_name}

%changelog
* Sun Sep 08 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.10-alt3
- Build for KF6.

* Thu Apr 04 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.10-alt2
- Added requires to ddcutil (closes: #49894).

* Sun Mar 31 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.10-alt1
- Initial build for ALT.
