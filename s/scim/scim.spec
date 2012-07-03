%define scim_api 1.4.0

Name: scim
Version: 1.4.9
Release: alt2
Summary: Smart Common Input Method platform

License: LGPL
Group: System/Configuration/Other
Url: http://www.scim-im.org/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://dl.sourceforge.net/sourceforge/scim/%name-%version.tar.gz
Source1: xinput-scim
Source2: SCIM.txt

Patch1: scim-add-restart.patch
Patch2: gtkimm-clear-preedit-on-reset-174143.patch
Patch3: rawcode-unicode-maxlength.patch
Patch4: scim.pc-versioned-moduledir-179706.patch
Patch5: scim-panjabi-punjabi.patch
Patch31: scim-1.4.7-syslibltdl.patch
Patch32: scim-1.4.8-fix-dlopen.patch

# Automatically added by buildreq on Thu Sep 27 2007
BuildRequires: gcc4.3-c++ imake libXt-devel libgtk+2-devel xorg-cf-files xsltproc

#BuildRequires: doxygen fontconfig gcc-c++ glibc-devel-static graphviz imake libgtk+2-devel libXt-devel xorg-cf-files xsltproc
#BuildRequires: gcc-c++ glibc-devel-static graphviz imake libICE-devel libX11-devel libXt-devel libstdc++-devel linux-libc-headers pkg-config xorg-cf-files xorg-x11-proto-devel xsltproc libltdl libltdl-devel

%description
SCIM is a user friendly and full featured input method user interface and
also a development platform to make life easier for Input Method developers.

%package devel
Summary: Smart Common Input Method platform
Group: Development/Other

%description devel
The scim-devel package includes the header files for the scim package.
Install scim-devel if you want to develop programs which will use scim.

%package doc
Summary: Smart Common Input Method platform documentation
Group: Documentation

%description doc
SCIM development documentation files generated from the sourcecode.

%package libs
Summary: Smart Common Input Method libraries
Group: System/Libraries

%description libs
This package provides the libraries and GTK input method module for SCIM.

%prep
%setup -q
#patch31 -p1 -b .31-sysltdl
#patch32 -E -p1 -b .fix-dlopen

%build
export CC=gcc-4.3 CXX=g++-4.3
%configure
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -pm 755 $RPM_BUILD_ROOT/%_libdir/scim-1.0/{Config,FrontEnd,IMEngine,SetupUI,Helper}

find $RPM_BUILD_ROOT -name '*.la' | xargs rm

mkdir -pm 755 $RPM_BUILD_ROOT/%_sysconfdir/X11/xinit/xinput.d
install -pm 644 %SOURCE1 $RPM_BUILD_ROOT/%_sysconfdir/X11/xinit/xinput.d/scim

%find_lang %name

%clean
%define cjk_langs ja_JP ko_KR zh_CN zh_TW
%define indic_langs bn_IN gu_IN hi_IN kn_IN ml_IN pa_IN ta_IN te_IN
%define supported_langs %cjk_langs %indic_langs ne_NE th_TH

%post libs
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules
#%_bindir/update-gtk-immodules %_target_platform

%postun libs
[ "$1" = 0 ] && \
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules
#%_bindir/update-gtk-immodules %_target_platform

%files -f %name.lang
%doc AUTHORS COPYING NEWS README ChangeLog TODO
%dir %_sysconfdir/scim
%config(noreplace) %_sysconfdir/scim/*
%_sysconfdir/X11/xinit/xinput.d
%_bindir/*
%_libdir/scim-1.0
%exclude %_libdir/scim-1.0/%scim_api
%_datadir/scim

%files devel
%doc docs/developers
%_includedir/scim-1.0
%_libdir/libscim*.so
%_libdir/pkgconfig/*.pc

%files doc
%doc docs/html

%files libs
%_libdir/libscim-*.so.*
%_libdir/gtk-2.0/immodules
%_libdir/scim-1.0/%scim_api

%changelog
* Mon Feb 07 2011 Ilya Mashkin <oddity@altlinux.ru> 1.4.9-alt2
- rebuild for set-versions

* Wed Aug 05 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.9-alt1
- 1.4.9
- remove old ldconfig calls
- spec cleanup

* Thu Sep 27 2007 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.7-alt1
- Up to version 1.4.7.

* Tue Jun 06 2006 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.4-alt3
- fix spec.

* Tue May 16 2006 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.4-alt2
- fix spec.

* Wed May 10 2006 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.4-alt1
- first ALT release of SCIM.
