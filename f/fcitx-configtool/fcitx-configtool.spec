Name:    fcitx-configtool
Version: 0.4.10
Release: alt4

Summary: A gtk based configure tool for fcitx
License: GPL-2.0
Group:   System/Internationalization
Url:     https://github.com/fcitx/fcitx-configtool

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libgtk+3-devel
BuildRequires: fcitx-devel
BuildRequires: iso-codes-devel

%description
%summary

%package -n fcitx-config-gtk3
Summary: A gtk3 based configure tool for fcitx 
Group: System/Internationalization
Requires: fcitx

%description -n fcitx-config-gtk3
%summary

%prep
%setup

%build
%cmake -GNinja
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
%find_lang %name

%files -f %name.lang -n fcitx-config-gtk3
%doc README
%_bindir/fcitx-config-gtk3

%changelog
* Tue Feb 22 2022 Andrey Cherepanov <cas@altlinux.org> 0.4.10-alt4
- Bumped release to keep version in Sisyphus greater than in autoimports.

* Mon Feb 21 2022 Andrey Cherepanov <cas@altlinux.org> 0.4.10-alt1
- Initial build for Sisyphus (ALT #40162).
