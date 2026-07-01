%define repo dde-manual-content

Name: deepin-manual-content
Version: 3.0.12
Release: alt1

Summary: Additional system assets for deepin-manual

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-manual-content
VCS: https://github.com/linuxdeepin/dde-manual-content

# Source-url: https://github.com/linuxdeepin/dde-manual-content/archive/%version/%repo-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake gcc-c++

%description
%summary.

%prep
%setup
%patch -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md debian/changelog
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/system/
%_datadir/deepin-manual/manual-assets/system/dde/

%changelog
* Wed Jul 01 2026 Leontiy Volodin <lvol@altlinux.org> 3.0.12-alt1
- New version 3.0.12.

* Mon Apr 13 2026 Leontiy Volodin <lvol@altlinux.org> 3.0.10-alt1
- New version 3.0.10.

* Fri Mar 20 2026 Leontiy Volodin <lvol@altlinux.org> 3.0.8-alt1
- New version 3.0.8.

* Wed Dec 10 2025 Leontiy Volodin <lvol@altlinux.org> 3.0.5-alt1
- Initial build for ALT Sisyphus (for deepin-manual).
