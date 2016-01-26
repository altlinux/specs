%define _unpackaged_files_terminate_build 1

Name: geoipupdate
Version: 2.2.2
Release: alt1

Summary: GeoIP Database Update program
Group: Networking/Other
License: GPL2+
URL: https://github.com/maxmind/geoipupdate

Source: %url/releases/download/v%version/%name-%version.tar.gz

BuildRequires: libcurl-devel zlib-devel

%description
The GeoIP Update program performs automatic updates of GeoIP2 and GeoIP Legacy
binary databases.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_sysconfdir/GeoIP.conf
%_sysconfdir/GeoIP.conf.default
%_man5dir/GeoIP.conf.5.*
%_bindir/%name
%_man1dir/%name.1.*
%doc README.* ChangeLog.*

%changelog
* Tue Jan 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Apr 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- first build for Sisyphus

