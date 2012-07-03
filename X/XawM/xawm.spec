%define name XawM
%define version 1.6
%define release alt2
%define prefix	/usr/X11R6

%define major 1
%define libname lib%name%major

Summary: Widget based on Xaw3d
Name: %name
Version: %version
Release: alt2.qa2
Url: http://sourceforge.net/projects/xawm/
Source: %name-%version.src.tar.gz
License: MIT
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Group: System/Libraries

# Automatically added by buildreq on Mon Dec 01 2008
BuildRequires: flex imake libXext-devel libXmu-devel libXp-devel libXpm-devel rpm-build-java xorg-cf-files

%description
An Athena-compatible widget set with a modern look and feel.

%package -n %libname
Summary: Widget based on Xaw3d
Group: System/Libraries

%description -n %libname
An Athena-compatible widget set with a modern look and feel.

%package -n %libname-devel
Summary: Widget based on Xaw3d
Group: Development/C
Requires: %libname = %version
Provides: libXawM-devel

%description -n %libname-devel
An Athena-compatible widget set with a modern look and feel.

%prep
%setup -q
xmkmf
%make clean

%build
xmkmf
%make

%install
%make	DESTDIR=%buildroot install

%files -n %libname
%doc TODO README.Linux README.XAW3D README.XawM
%_x11libdir/libXawM.so.*

%files -n %libname-devel
%_x11libdir/libXawM.so
%_includedir/X11/XawM/*

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.6-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * distribution-tag for libXawM1-devel
  * post_ldconfig for libXawM1
  * postun_ldconfig for libXawM1
  * distribution-tag for libXawM1
  * postclean-05-filetriggers for spec file

* Mon Dec 01 2008 Hihin Ruslan <ruslandh@altlinux.ru> 1.6-alt2
- correct BuildRequires

* Sat Sep 23 2006 Hihin Ruslan <ruslandh@altlinux.ru> 1.6-alt1
- first version for ALT-Linux

* Sat Dec 27 2002 Pingus <pingus77@ifrance.com>
- update 1.6 for Xawdecode 1.6.6a

* Tue Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5u-1mdk
- new & needed to update siag
