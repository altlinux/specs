Name:     qtxdg-tools
Version:  4.0.0
Release:  alt1

Summary:  libqtxdg user tools
License:  LGPL-2.1
Group:    Graphical desktop/Other
Url:      https://github.com/lxqt/qtxdg-tools

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: lxqt2-build-tools
BuildRequires: qt6-base-devel
BuildRequires: libqt6xdg-devel

Requires: libqt6xdg >= %version
Obsoletes: qtxdg-mat <= %version

%description
%summary.

%package devel
Summary: cmake modules for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
cmake modules for %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/*
%doc *.md

%files devel
%_datadir/cmake/%name

%changelog
* Wed Jun 12 2024 Anton Midyukov <antohami@altlinux.org> 4.0.0-alt1
- New version 4.0.0

* Tue Apr 16 2024 Anton Midyukov <antohami@altlinux.org> 3.12.0-alt2
- Separate devel package

* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 3.12.0-alt1
- New version 3.12.0.

* Sun Apr 16 2023 Anton Midyukov <antohami@altlinux.org> 3.11.0-alt1
- New version 3.11.0.

* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 3.10.0-alt1
- new version 3.10.0

* Mon Jun 20 2022 Anton Midyukov <antohami@altlinux.org> 3.9.1-alt1
- Initial build for Sisyphus
