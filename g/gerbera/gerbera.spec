%define _unpackaged_files_terminate_build 1

Name: gerbera
Version: 1.12.1
Release: alt1

Summary: UPnP Media Server
Group: System/Servers
License: GPLv2 and MIT
Url: https://gerbera.io
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: %name-data = %EVR

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.18
BuildRequires: gcc-c++
BuildRequires: libupnp-devel >= 1.14.12
BuildRequires: libfmt-devel >= 7.1.3
BuildRequires: libspdlog-devel >= 1.8.5
BuildRequires: libuuid-devel
BuildRequires: libexpat-devel
BuildRequires: libsqlite3-devel >= 3.35.5
BuildRequires: libduktape-devel >= 2.5.0
BuildRequires: libcurl-devel
BuildRequires: libtag-devel >= 1.12
BuildRequires: libmagic-devel
BuildRequires: libpugixml-devel >= 1.10
BuildRequires: libexif-devel
BuildRequires: libexiv2-devel >= 0.26
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libavcodec-devel
BuildRequires: libffmpegthumbnailer-devel >= 2.2.0
BuildRequires: zlib-devel
BuildRequires: libebml-devel >= 1.4.2 libmatroska-devel >= 1.6.3
BuildRequires: libsystemd-devel
BuildRequires: libmysqlclient-devel

%description
Gerbera is a UPnP media server which allows you to stream your digital
media through your home network and consume it on a variety of UPnP
compatible devices.

%package data
Summary: Data files for Gerbera
BuildArch: noarch
Group: System/Servers

%description data
Data files for the Gerbera media server.

%prep
%setup
%patch -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DWITH_JS=YES \
    -DWITH_MYSQL=YES \
    -DWITH_CURL=YES \
    -DWITH_TAGLIB=YES \
    -DWITH_MAGIC=YES \
    -DWITH_AVCODEC=YES \
    -DWITH_EXIF=YES \
    -DWITH_EXIV2=YES \
    -DWITH_FFMPEGTHUMBNAILER=YES \
    -DWITH_INOTIFY=YES \
    -DWITH_SYSTEMD=YES \
    -DWITH_MYSQL=YES \
    -DUPNP_HAS_REUSEADDR=YES

%cmake_build

%install
mkdir -p %buildroot{%_sysconfdir,%_localstatedir,%_logdir}/%name
%cmakeinstall_std

%buildroot%_bindir/%name --create-config --home %_localstatedir/%name > %buildroot%_sysconfdir/%name/config.xml

mkdir -p %buildroot%_logrotatedir
cat > %buildroot%_logrotatedir/%name << 'EOF'
/var/log/gerbera/gerbera {
      monthly
      missingok
      create 0644 gerbera gerbera
      notifempty
      compress
}
EOF

touch %buildroot%_localstatedir/%name/{%name.db,%name.html}

%pre
groupadd -r -f %name >/dev/null 2>&1 ||:
useradd -r -n -g %name -d %_localstatedir/%name -s /dev/null \
    -c 'Gerbera UPnP Media Server' %name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service  %name

%files
%doc LICENSE.md AUTHORS CONTRIBUTING.md ChangeLog.md
%doc doc/*.rst
%dir %attr(750,root,%name) %_sysconfdir/%name
%config(noreplace) %attr(750,root,%name) %_sysconfdir/%name/config.xml
%attr(750,%name,adm) %_logdir/%name
%config(noreplace) %_logrotatedir/%name
%_bindir/%name
%_man1dir/*
%_unitdir/%name.service
%attr(3770,root,%name) %dir %_localstatedir/%name
%ghost %attr(775,%name,%name) %_localstatedir/%name/%name.db
%ghost %attr(775,%name,%name) %_localstatedir/%name/%name.html


%files data
%_datadir/%name

%changelog
* Sat Oct 14 2023 Nazarov Denis <nenderus@altlinux.org> 1.12.1-alt1
- New version 1.12.1.

* Fri Jul 22 2022 Vladimir Didenko <cow@altlinux.org> 1.11.0-alt1
- 1.11.0
- fix build with libfmt 9.0

* Fri Mar 04 2022 Alexey Shabalin <shaba@altlinux.org> 1.10.0-alt1
- 1.10.0

* Tue Feb 01 2022 Alexey Shabalin <shaba@altlinux.org> 1.9.2-alt2
- upstream master snapshot (fixed ftbfs)

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 1.9.2-alt1
- new version 1.9.2

* Sat Sep 04 2021 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt1
- new version 1.9.1

* Fri May 28 2021 Alexey Shabalin <shaba@altlinux.org> 1.8.1-alt1
- new version 1.8.1

* Sat Nov 14 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.4-alt1
- new version 1.6.4

* Tue Aug 04 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- new version 1.6.0

* Sun May 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- Initial build.
