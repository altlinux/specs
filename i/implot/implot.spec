%define _unpackaged_files_terminate_build 1

Name:    implot
Version: 1.0
Release: alt1

Summary: Immediate Mode Plotting
License: MIT
Group:   Other
Url:     https://github.com/epezent/implot
VCS:     https://github.com/epezent/implot.git

Source: %name-%version.tar

%description
%summary.

%package devel
Summary: Dev files and headers %name
Group: Development/C++
BuildArch: noarch

%description devel
%summary.

%prep
%setup

%install
install -d %buildroot%_includedir/%name
install -m 644 *.cpp %buildroot%_includedir/%name/
install -m 644 *.h %buildroot%_includedir/%name/

%files devel
%_includedir/%name/*

%changelog
* Thu Oct 08 2026 Artem Semenov <savoptik@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
