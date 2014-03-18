%define  rev f58b1b7

Name:    pcmanfm-qt
Version: 0.1.0
Release: alt3.git%rev

Summary: PCManFM-Qt is the Qt port of the LXDE file manager PCManFM
License: GPLv2+
Group:   File tools
Url:     http://blog.lxde.org/?p=990

Source:  %name-%version.tar
Source1: %name.desktop

BuildRequires: gcc-c++ qt4-devel cmake
BuildRequires: libfm2-devel
BuildRequires: libXdmcp-devel

Requires: menu-cache

%description
PCManFM-Qt is the Qt port of the LXDE file manager PCManFM.
Libfm-Qt is a companion library providing components to build desktop
file managers.

%prep
%setup
subst 's/DESTINATION lib/DESTINATION lib${LIB_SUFFIX}/g' libfm-qt/CMakeLists.txt

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

# Clear development files
rm -rf %buildroot%_includedir/libfm-qt \
       %buildroot%_datadir/libfm-qt/translations/libfm-qt_template.qm \
       %buildroot%_datadir/pcmanfm-qt/translations/pcmanfm-qt_template.qm \
       %buildroot%_libdir/libfm-qt.so \
       %buildroot%_pkgconfigdir/libfm-qt.pc

install -D -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Detect all localization files
%find_lang --with-qt --all-name %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*.desktop
%_libdir/libfm-qt.so.*

%changelog
* Tue Mar 18 2014 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt3.gitf58b1b7
- New snapshot
- Fix requirement on development packages
- Link with libfm2

* Mon Apr 08 2013 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt2.gite99916f
- New snapshot

* Tue Mar 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus
