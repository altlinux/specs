Name: neovim-qt
Version: 0.2.17
Release: alt4.git2b4cb87

Summary: Neovim client library and GUI, in Qt6.

License: ISC
Group: Editors
Url: https://github.com/equalsraf/neovim-qt

Source: %name-%version-%release.tar

BuildRequires(pre): rpm-macros-cmake cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: libmsgpack-devel
BuildRequires: nvim
BuildRequires: qt6-svg-devel

Requires: neovim

ExcludeArch: armh

%description
Neovim client library and GUI, in Qt6.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DNVIM_VERSION_RELEASE=%release \
	-DUSE_SYSTEM_MSGPACK=ON \
	-DQT_PACKAGES=Qt6 \
	#
%cmake_build

%install
%cmake_install

%files
%doc README.md
%doc %_datadir/nvim-qt/LICENSE
%doc %_datadir/nvim-qt/runtime/doc/*
%_bindir/nvim-qt
%_desktopdir/nvim-qt.desktop
%_datadir/nvim-qt/runtime/plugin/nvim_gui_shim.vim
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg

%changelog
* Mon Jan 9 2023 Vladimir Didenko <cow@altlinux.org> 0.2.17-alt4.git2b4cb87
 - New version (git2b4cb87)
 - Switch to Qt6

* Tue Dec 13 2022 Vladimir Didenko <cow@altlinux.org> 0.2.17-alt3.git95ed0a3
 - New version (git95ed0a3)

* Thu Jul 14 2022 Vladimir Didenko <cow@altlinux.org> 0.2.17-alt2
- New version (0.2.17 release)

* Wed Jun 22 2022 Vladimir Didenko <cow@altlinux.org> 0.2.17-alt1.gite6115d55
- New version (gite6115d55)

* Fri Sep 24 2021 Vladimir Didenko <cow@altlinux.org> 0.2.16.1-alt5.gita8d7d71c
- New version (gita8d7d71c)

* Tue Jul 6 2021 Vladimir Didenko <cow@altlinux.org> 0.2.16.1-alt4.gite79fdbcf
- New version (gite79fdbcf)
- Enable package build on aarch64

* Mon May 31 2021 Vladimir Didenko <cow@altlinux.org> 0.2.16.1-alt3
- Fix build with a new cmake macros

* Mon Sep 14 2020 Vladimir Didenko <cow@altlinux.org> 0.2.16.1-alt2
- Add neovim to dependencies (closes: #38933)

* Mon Jun 22 2020 Vladimir Didenko <cow@altlinux.org> 0.2.16.1-alt1.1
- Don't build on armh

* Mon Jun 22 2020 Vladimir Didenko <cow@altlinux.org> 0.2.16.1-alt1
- New version.

* Fri Nov 8 2019 Vladimir Didenko <cow@altlinux.org> 0.2.15-alt1
- New version.

* Fri Sep 20 2019 Vladimir Didenko <cow@altlinux.org> 0.2.14-alt2
- Don't build on aarch64 platform(because we don't build neovim on it)

* Thu Sep 19 2019 Vladimir Didenko <cow@altlinux.org> 0.2.14-alt1
- New version.

* Tue Aug 6 2019 Vladimir Didenko <cow@altlinux.org> 0.2.12-alt3.gitbef46156
- New version.
- Add patch for unicode issues.

* Fri Aug 2 2019 Vladimir Didenko <cow@altlinux.org> 0.2.12-alt2.git78224e71
- New version.

* Wed Jan 16 2019 Vladimir Didenko <cow@altlinux.org> 0.2.12-alt1
- New version.

* Wed Jan 9 2019 Vladimir Didenko <cow@altlinux.org> 0.2.11-alt1
- New version.

* Thu Jul 5 2018 Vladimir Didenko <cow@altlinux.org> 0.2.8-alt2
- New version (v0.2.8-43-gfaef696).

* Thu Jul 5 2018 Vladimir Didenko <cow@altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus (v0.2.8-37-gfcb99d6).
