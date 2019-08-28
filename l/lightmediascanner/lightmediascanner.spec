%def_disable snapshot
%def_enable daemon
%def_disable magic

Name: lightmediascanner
Version: 0.5.2
Release: alt1

Summary: Light Media Scanner
License: LGPLv2.1
Group: System/Servers
Url: http://lms.garage.maemo.org/

#VCS: git://git.profusion.mobi/lightmediascanner.git
%if_enabled snapshot
#VCS: https://github.com/profusion/lightmediascanner.git
Source: %name-%version.tar
%else
Source: https://github.com/profusion/%name/archive/release_%version/%name-%version.tar.gz
%endif

Requires: lib%name = %version-%release

BuildRequires: libgio-devel libflac-devel libmpeg4ip-devel libsqlite3-devel libvorbis-devel
BuildRequires: libavcodec-devel libavformat-devel

%{?_enable_magic:BuildRequires: libmagic-devel}

%description
LMS is a Light Media Scanner.
Lightweight media scanner meant to be used in not-so-powerful devices,
like embedded systems or old machines.

%package -n lib%name
Summary: A Light Media Scanner Library
Group: System/Libraries

%description -n lib%name
This package provides a Light Media Scanner shared Library.

%package -n lib%name-devel
Summary: Development package for LMS
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides headers and development libraries for LMS.

%prep
%setup -n %name-release_%version

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_enable daemon} \
	%{subst_enable magic}
%make_build

%install
%makeinstall_std

%if_enabled daemon
%files
%_bindir/%{name}ctl
%_bindir/%{name}d
%_datadir/dbus-1/services/org.%name.service
%endif

%files -n lib%name
%_libdir/*.so.*
%_libdir/%name/
%doc AUTHORS README NEWS

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Wed Aug 28 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Mon Feb 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- release_0.5.1-18-gadfddb3 snapshot

* Tue Jan 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.5.0-alt1
- first build for Sisyphus
- TODO: tremor (ivorbis) support

