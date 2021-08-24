%define _unpackaged_files_terminate_build 1

Name: lldpad
Version: 1.1
Release: alt2
Summary: Intel LLDP Agent

Group: Networking/Other
License: GPLv2
Url: http://open-lldp.org/
Vcs: https://github.com/intel/openlldp.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-systemd
BuildRequires: flex >= 2.5.33
BuildRequires: pkgconfig(libconfig) >= 1.3.2
BuildRequires: pkgconfig(libnl-3.0) >= 3.2
BuildRequires: libreadline-devel
BuildRequires: pkgconfig(systemd)

Provides: openlldp = %EVR

%description
This package contains the Linux user space daemon and configuration tool for
Intel LLDP Agent with Enhanced Ethernet support for the Data Center.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains header files for developing applications
that use %name.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sharedstatedir/%name
rm -f %buildroot%_libdir/*.{a,la}

%post
%systemd_post %name.service %name.socket

%preun
%systemd_preun %name.service %name.socket

%postun
%systemd_postun_with_restart %name.service %name.socket

%files
%doc COPYING README ChangeLog
%_sbindir/*
%_libdir/*.so.*
%dir %_sharedstatedir/%name
%_unitdir/*
%_datadir/bash-completion/completions/*
%_man8dir/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Wed Aug 25 2021 Alexey Shabalin <shaba@altlinux.org> 1.1-alt2
- Increased release for greater than in autoimports.

* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 1.1-alt1
- Initial build.

