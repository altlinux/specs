Name: horizon
Version: 2.5.0
Release: alt1.1

Summary: Horizon is a free EDA package
License: GPL-3.0-or-later
Group: Engineering
Url: https://github.com/horizon-eda/horizon

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libgtkmm3-devel
BuildRequires: libsqlite3-devel
BuildRequires: libzip-devel
BuildRequires: libuuid-devel
BuildRequires: libepoxy-devel
BuildRequires: librsvg-devel
BuildRequires: libpodofo-devel
BuildRequires: libzeromq-cpp-devel
BuildRequires: libgit2-devel
BuildRequires: libcurl-devel
BuildRequires: libglm-devel
BuildRequires: boost-devel-headers
BuildRequires: opencascade-devel
BuildRequires: libsigc++2-devel
BuildRequires: libarchive-devel
BuildRequires: libspnav-devel

%description
%summary

%prep
%setup
%autopatch -p1

%build
%add_optflags -I%_includedir/glibmm-2.4 -I%_libdir/glibmm-2.4/include
%add_optflags -I%_includedir/glib-2.0 -I%_libdir/glib-2.0/include
%add_optflags -I%_includedir/sigc++-2.0
%add_optflags -I%_includedir/glm
export CXXFLAGS='%optflags' 
%make_build \
%ifarch loongarch64 riscv64
	GOLD= \
%endif
	%nil


%install
%makeinstall_std PREFIX=%prefix \
%ifarch loongarch64 riscv64
	GOLD= \
%endif
	%nil

%files
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*
%doc *.md

%changelog
* Mon Nov 20 2023 Ivan A. Melnikov <iv@altlinux.org> 2.5.0-alt1.1
- NMU: don't use gold for linking on loongarch64 and riscv64
  (gold does not work on these architectures)

* Mon Jun 26 2023 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Mon Jun 26 2023 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt2
- fix build with gcc13
- cleanup Packager
- patch from git diff

* Fri Apr 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- NMU: new version for opencascade-7.1.0

* Wed Dec 29 2021 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt2
- fix build without glm.pc (thanks aris@)

* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1.1
- NMU: rebuild with opencascade-devel

* Tue May 12 2020 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
