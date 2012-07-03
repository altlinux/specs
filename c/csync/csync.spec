Name: csync
Version: 0.50.6
Release: alt1

Group: Networking/Other
Summary: csync is a lightweight desktop synchronize utility

License: GPLv2+
Source0: %name-%version.tar
Requires: lib%name = %version-%release

BuildRequires: cmake libsqlite3-devel libiniparser-devel log4c-devel rpm-macros-cmake
BuildRequires: libsmbclient-devel libneon-devel libssh-devel

%description
csync is a lightweight utility to synchronize files between
two directories on a system or between multiple systems.
Supports sftp, and owncloud.

%package -n lib%name
Group: Development/C
Summary: library for desktop syncing

%description -n lib%name
This package contains runtime library for using csyncronizing from
other programs.

%package -n lib%name-devel
Group: Development/C
Summary: Development files for lib%name
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains development files for library for using
csyncronizing from other programs.

%prep
%setup

%build
%cmake -DSYSCONF_INSTALL_DIR=/etc -DCMAKE_VERBOSE_MAKEFILE=1

%install
%makeinstall_std -C BUILD

%find_lang %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/*
%_bindir/*
%_docdir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*
%_libdir/%name-*/*.so

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%changelog
* Thu May 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.50.6-alt1
- 0.50.6

* Wed Apr 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.50.0-alt1
- initial build

