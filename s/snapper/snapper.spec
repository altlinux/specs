# systemd units for snapper
%define snapper_svcs snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer snapperd.service

%define soname 7

Name: snapper
Version: 0.11.1
Group: System/Base
Release: alt1
Summary: Tool for filesystem snapshot management
License: GPL-2.0-only
Url: http://snapper.io
Source0: %name-%version.tar
VCS: https://github.com/openSUSE/snapper

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: rpm-macros-systemd

BuildRequires: /usr/bin/xsltproc
BuildRequires: docbook-style-xsl
BuildRequires: libbtrfs-devel
BuildRequires: libmount-devel
BuildRequires: libselinux-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: libacl-devel
BuildRequires: boost-devel
BuildRequires: e2fsprogs-devel
BuildRequires: libdbus-devel
BuildRequires: libjson-c-devel
BuildRequires: libe2fs-devel
BuildRequires: libncurses-devel
BuildRequires: libpam-devel
BuildRequires: zlib-devel
Requires: lib%name%soname = %EVR
Requires: diffutils

%description
This package contains snapper, a tool for filesystem snapshot management.

%package -n lib%name%soname
Summary: Library for filesystem snapshot management
Group: System/Base
Requires: util-linux
Requires: btrfs-progs
Requires: lib%name-common

%description -n lib%name%soname
This package contains the snapper shared library
for filesystem snapshot management.

%package -n lib%name-common
Summary: Commmon files for lib%name
Group: System/Base
Requires: lib%name%soname = %EVR

%description -n lib%name-common
This package contains common files for the snapper shared library.

%package devel
Summary: Header files and development libraries for lib%name
Group: Development/Other
Requires: lib%name%soname = %EVR
Requires: libstdc++-devel
Requires: libacl-devel
Requires: boost-devel
Requires: libbtrfs-devel
Requires: libxml2-devel
Requires: libmount-devel

%description devel
This package contains header files and documentation for developing with
snapper.

%package tests
Summary: Integration tests for snapper
Group: Development/Other
Requires: lib%name%soname = %EVR

%description tests
%summary.

%package -n pam_snapper
Summary: PAM module for calling snapper
Group: System/Base
Requires: %name = %EVR

%description -n pam_snapper
A PAM module for calling snapper during user login and logout.


%prep
%setup
# use libexecdir
find -type f -exec sed -i -e "s|/usr/lib/snapper|%_libexecdir/%name|g" {} ';'

%build
autoreconf -vfi
%configure \
  --disable-ext4 \
  --disable-zypp \
  --enable-selinux \
  --with-pam-security=%_pam_modules_dir \
  %nil
%make_build

%install
%makeinstall_std
install -Dpm0644 data/sysconfig.snapper %buildroot%_sysconfdir/sysconfig/%name
%find_lang %name
find %buildroot -name '*.la' -print -delete
rm -rf %buildroot%_sysconfdir/cron.hourly
rm -rf %buildroot%_sysconfdir/cron.daily
rm -rf %buildroot%_docdir/%name/COPYING
rm -rf %buildroot%_docdir/%name/AUTHORS

%check
make check

%post
%systemd_post %snapper_svcs

%preun
%systemd_preun %snapper_svcs

%postun
%systemd_postun_with_restart %snapper_svcs


%files -f snapper.lang
%doc AUTHORS COPYING
%_bindir/snapper
%_sbindir/mksubvolume
%_sbindir/snapperd
%config(noreplace) %_sysconfdir/logrotate.d/snapper
%_unitdir/%{name}*
%_datadir/bash-completion/completions/snapper
%_datadir/zsh/site-functions/_snapper
%_datadir/dbus-1/system.d/org.opensuse.Snapper.conf
%_datadir/dbus-1/system-services/org.opensuse.Snapper.service
%_mandir/man8/%name.8*
%_mandir/man8/mksubvolume.8*
%_mandir/man8/snapperd.8*
%_mandir/man5/snapper-configs.5*
%dir %_libexecdir/%name
%_libexecdir/%name/installation-helper
%_libexecdir/%name/systemd-helper

%files tests
%dir %_libdir/snapper
%_libdir/snapper/testsuite/

%files -n lib%name%soname
%_libdir/libsnapper.so.%{soname}*

%files -n lib%name-common
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/configs
%dir %_datadir/%name
%dir %_datadir/%name/config-templates
%_datadir/%name/config-templates/default
%dir %_datadir/%name/filters
%_datadir/%name/filters/*.txt
%config(noreplace) %_sysconfdir/sysconfig/%name

%files devel
%doc examples/c/*.c
%doc examples/c++-lib/*.cc
%_libdir/libsnapper.so
%_includedir/%name/

%files -n pam_snapper
%_pam_modules_dir/*
%prefix/lib/pam_snapper/
%_mandir/man8/pam_snapper.8*

%changelog
* Fri Jul 12 2024 Anton Farygin <rider@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Sat Apr 27 2024 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Sat Dec 30 2023 Anton Farygin <rider@altlinux.ru> 0.10.7-alt1
- 0.10.7

* Sun Nov 26 2023 Anton Farygin <rider@altlinux.ru> 0.10.6-alt1
- 0.10.6

* Mon Jun 26 2023 Anton Farygin <rider@altlinux.ru> 0.10.5-alt1
- 0.10.5
- fix pam module path (closes: #46653)

* Sat Jun 03 2023 Anton Farygin <rider@altlinux.ru> 0.10.4-alt1
- first build for ALT, based on specfile from Fedora project
