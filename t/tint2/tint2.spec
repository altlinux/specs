%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: tint2
Version: 17.0.2
Release: alt1
Summary: Simple panel/taskbar made for modern x window managers

Group: Graphical desktop/Other
License: GPLv2
Url: https://gitlab.com/o9000/tint2

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Sat Jul 03 2010
BuildRequires: cmake gcc-c++ imlib2-devel libXcomposite-devel libXdamage-devel libXinerama-devel libXrandr-devel libpango-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libcairo-devel libpixman-devel libexpat-devel
BuildRequires: libXdmcp-devel libXxf86vm-devel libharfbuzz-devel
BuildRequires: libgtk+3-devel librsvg-devel

%description
tint2 is a simple panel/taskbar made for modern x window managers.
It was specifically made for openbox3  but should also work with
other window managers (GNOME, KDE, etc...).

%prep
%setup -q %name-%version

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%cmake \
	-DENABLE_TINT2CONF=ON \
	-DENABLE_EXAMPLES=ON

%cmake_build

%install
%cmakeinstall_std

%find_lang tint2conf

%files -f tint2conf.lang
%doc %_datadir/doc/*
%_datadir/applications/*.desktop
%_datadir/%name
%_iconsdir/hicolor/scalable/apps/*.svg
%dir %_sysconfdir/xdg/%name/
%config(noreplace) %_sysconfdir/xdg/%name/tint2rc
%_bindir/*
%_man1dir/*
%_datadir/mime/packages/tint2conf.xml

%changelog
* Thu Dec 09 2021 Konstantin Rybakov <kastet@altlinux.org> 17.0.2-alt1
- Updated to upstream version 17.0.2

* Fri Jul 02 2021 Konstantin Rybakov <kastet@altlinux.org> 17.0.1-alt1
- Updated to upstream version 17.0.1

* Tue Nov 05 2019 Konstantin Rybakov <kastet@altlinux.org> 16.7-alt1
- Updated to upstream version 16.7 

* Wed Oct 30 2013 Afanasov Dmitry <ender@altlinux.org> 0.11-alt2.652.1
- fix default icon lookup

* Wed Oct 30 2013 Afanasov Dmitry <ender@altlinux.org> 0.11-alt2.652
- svn snapshot (revision 652)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.11-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Jul 2 2010 Andrew Clark <andyc@altlinux.org> 0.11-alt1
- version update to 0.11-alt1

* Tue Mar 23 2010 Andrew Clark <andyc@altlinux.org> 0.9-alt1
- initial build for ALT.

