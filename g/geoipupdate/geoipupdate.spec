%define _unpackaged_files_terminate_build 1

Name: geoipupdate
Version: 2.3.1
Release: alt1

Summary: GeoIP Database Update program
Group: Networking/Other
License: GPLv2+
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
%config %_sysconfdir/GeoIP.conf
%_man5dir/GeoIP.conf.5.*
%_bindir/%name
%_man1dir/%name.1.*
%doc README.* ChangeLog.* conf/GeoIP.conf.default

%exclude %_datadir/doc/%name/

%changelog
* Sat Jan 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Tue Jan 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Apr 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- first build for Sisyphus

