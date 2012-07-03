
Name: grilo-mediaserver2
Version: 0.1
Release: alt2
Summary: An implementation of the provider side of Rygel's Media Server Specification (version 2) based on the Grilo framework
Group: Sound
License: LGPLv2+
Url: http://live.gnome.org/Grilo

Source: %name-%version.tar

Requires: lib%name = %version-%release

BuildRequires: gnome-common
BuildRequires: glib2-devel libgio-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libgrilo-devel >= 0.1.13

%description
An implementation of the provider side of
Rygel's Media Server Specification (version 2) based on the Grilo framework.

%package -n lib%name
Summary: Libraries files for %name
Group: System/Libraries

%description -n lib%name
Libraries files for %name

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for %name

%prep
%setup

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static

%make_build

%install
%make_install DESTDIR=%buildroot install

# Remove files that will not be packaged
rm -f %buildroot%_bindir/test-client


%files
%doc AUTHORS NEWS README
%_bindir/grilo-ms2
%config(noreplace) %_sysconfdir/%name.conf

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Jul 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt2
- fix build with new grilo

* Mon May 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
