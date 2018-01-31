%define name 		Xaw95
%define version 	1.1
%define release 	alt3

Name: %name
Version: %version
Release: %release

Summary: 3D Athena Widgets with Win95 look and feel
License: GPL
Group: System/Libraries

#Url: http://www.netsw.org/x11/libs/xaw95/
Url: http://ibiblio.org/pub/linux/libs/X/
Packager: Hihin Ruslan <ruslandh@altlinux.ru>
Source: %name-%version-src.tar.gz
Patch0: %name-%version.dif
Patch1: %name-%version-nocrash.patch
Patch2: %name-%version-secure.patch

%define libname lib%name

# Automatically added by buildreq on Mon Dec 01 2008
BuildRequires: flex gccmakedep imake libXext-devel libXmu-devel libXp-devel libXpm-devel xorg-cf-files

%description
Written by Eddie Hiu-Fung Lau, this widget set approximates
the look and feel of Windows 95.

Differences between Xaw3d and Xaw95 are primarily minor
changes in appearance to make widgets look more like Windows 95:

    * AsciiSink seems to handle clipping better.
    * Many widgets have different defaults for background
      pixel (gray) and border width (0)
    * Command, Repeater, Toggle are not drawn inverted when
      pressed, and the label is offset slightly when pressed.
    * Scrollbar is slightly wider and includes arrow buttons.
    * Menu items have a 3-d look.

%package -n %libname
Summary: Widget based on Xaw3d
Group: System/Libraries

%description -n %libname
3D Athena Widgets with Win95 look and feel

%package -n %libname-devel
Summary: Widget based on Xaw3d
Group: Development/C
Requires: %libname = %version

%package -n %libname-devel-static
Summary: Widget based on Xaw3d
Group: Development/C
Requires: %libname = %version

%description -n %libname-devel
3D Athena Widgets with Win95 look and feel

%description -n %libname-devel-static
3D Athena Widgets with Win95 look and feel

%prep
%setup -n %name-%version
%patch2 -p0 -b .nocrash
%patch1 -p0 -b .secure
%patch0
rm -rf laylex.c laygram.h laygram.c
rm -rf exports/
mkdir -p exports/include/X11/Xaw95
mkdir -p X11
ln -sf ../exports/include/X11/Xaw95 X11/Xaw95
xmkmf -a

%build
%make

%install
%makeinstall_std
rm -f %buildroot/%_x11libdir/Xaw95/*so*

%files -n %libname
%doc README.XAW3D
%_x11libdir/libXaw95.so.*

%files -n %libname-devel
%_x11libdir/libXaw95.so
%_includedir/X11/Xaw95/*

%files -n %libname-devel-static
%_x11libdir/libXaw95.a

%changelog
* Wed Jan 31 2018 Michael Shigorin <mike@altlinux.org> 1.1-alt3
- *correct* BuildRequires
- updated Url:
- minor spec cleanup

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1-alt2.qa2
- NMU: rebuilt for debuginfo.

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * distribution-tag for libXaw95-devel
  * distribution-tag for libXaw95
  * distribution-tag for libXaw95-devel-static
  * postclean-05-filetriggers for spec file

* Mon Dec 01 2008 Hihin Ruslan <ruslandh@altlinux.ru> 1.1-alt2
- correct BuildRequires

* Sat Sep 23 2006 Hihin Ruslan <ruslandh@altlinux.ru> 1.1-alt1
- first version for ALT-Linux

* Sun Dec 29 2002 Pingus <pingus77@ifrance.com>
- first version 1.1 for Xawdecode 1.6.6a based on Suse spec
