# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 2
%define libname libplayer%{major}
%define develname libplayer-devel

Name: libplayer
Version: 2.0.1
Release: alt1_11
URL: http://libplayer.geexbox.org/
Source:	http://libplayer.geexbox.org/releases/%{name}-%{version}.tar.bz2
Patch0: libplayer-2.0.1-link.patch
License: LGPLv2+
Summary: A multimedia A/V abstraction layer API
Group: System/Libraries
BuildRequires: pkgconfig(libxine)
BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(x11)
BuildRequires: mplayer mplayer-tools
Source44: import.info

%description
libplayer is a multimedia A/V abstraction layer API. Its goal is to
interact with Enna Media Center.

libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine and VLC.

Its main goal is to provide an unique API that player frontends can use
to control any kind of multimedia player underneath. For example, it
provides a library to easily control MPlayer famous slave-mode.

%package test
Summary: A multimedia A/V abstraction layer API - test program
Group: System/Libraries

%description test
libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine and VLC.

This package contains test program for libplayer.

%package -n %{libname}
Summary: A multimedia A/V abstraction layer API
Group: System/Libraries

%description -n %{libname}
libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine and VLC.

%package -n %{develname}
Summary: A multimedia A/V abstraction layer API
Group: System/Libraries
Provides: %{name}-devel = %{version}-%{release}
Requires: %libname = %version

%description -n %{develname}
libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine and VLC.

This package contains the headers required for compiling software that uses
the libplayer library.

%prep
%setup -q
%patch0 -p0

%build

./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--disable-static \
	--enable-shared \
	--enable-pic \
	--disable-gstreamer \
	--enable-mplayer \
	--enable-vlc \
	--enable-xine
%make_build

%install
%makeinstall_std

%files test
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_11
- new version

