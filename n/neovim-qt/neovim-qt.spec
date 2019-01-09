Name: neovim-qt
Version: 0.2.11
Release: alt1

Summary: Neovim client library and GUI, in Qt5.

License: ISC
Group: Editors
Url: https://github.com/equalsraf/neovim-qt

# git://git.altlinux.org/gears/n/neovim.git
Source: %name-%version-%release.tar

BuildRequires(pre): rpm-macros-cmake cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: libmsgpack-devel
BuildRequires: nvim

%description
Neovim client library and GUI, in Qt5.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DNVIM_VERSION_RELEASE=%release \
	-DUSE_SYSTEM_MSGPACK=ON \
	#
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%files
%doc %_datadir/nvim-qt/runtime/README.md
%doc %_datadir/nvim-qt/runtime/doc/*
%_bindir/nvim-qt
%_desktopdir/nvim-qt.desktop
%_datadir/nvim-qt/runtime/plugin/nvim_gui_shim.vim
%_datadir/pixmaps/nvim-qt.png

%changelog
* Wed Jan 9 2019 Vladimir Didenko <cow@altlinux.org> 0.2.11-alt1
- New version.

* Thu Jul 5 2018 Vladimir Didenko <cow@altlinux.org> 0.2.8-alt2
- New version (v0.2.8-43-gfaef696).

* Thu Jul 5 2018 Vladimir Didenko <cow@altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus (v0.2.8-37-gfcb99d6).
