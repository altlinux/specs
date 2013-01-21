%define _name lightmediascanner

Name: lib%_name
Version: 0.4.5.0
Release: alt1

Summary: Light Media Scanner Library
License: LGPLv2.1
Group: System/Libraries
Url: http://lms.garage.maemo.org/
#VCS: git://git.profusion.mobi/lightmediascanner.git

Source: http://packages.profusion.mobi/%_name/%_name-%version.tar.bz2

BuildRequires: libflac-devel libmpeg4ip-devel libsqlite3-devel libvorbis-devel

%description
LMS is a Light Media Scanner Library.
Lightweight media scanner meant to be used in not-so-powerful devices,
like embedded systems or old machines.

%package devel
Summary: Development package for LMS
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides headers and development libraries for LMS.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%_libdir/%_name/
%doc AUTHORS README

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Tue Jan 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.5.0-alt1
- first build for Sisyphus
- TODO: tremor (ivorbis) support

