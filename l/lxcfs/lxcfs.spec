Name:		lxcfs
Version:	2.0.0
Release:	alt1.rc2
Summary:	FUSE filesystem for LXC

Group:		Development/Other
License:	Apache v.2
URL:		https://github.com/lxc/lxcfs

Packager:	Denis Pynkin <dans@altlinux.ru>

Source0:	%name-%version.tar

Requires: libfuse

BuildRequires(pre): libpam-devel
BuildRequires: libfuse-devel
BuildRequires: help2man

%description
FUSE filesystem for LXC, offering the following features:
 - a cgroupfs compatible view for unprivileged containers
 - a set of cgroup-aware files:
   - cpuinfo
   - meminfo
   - stat
   - uptime

%set_pam_name pam_cgfs

%package -n %pam_name
Summary: %summary
Group: Development/Other

%description -n %pam_name
%summary
This package provides a Pluggable Authentication Module (PAM) to provide
logged-in users with a set of cgroups which they can administer.
This allows for instance unprivileged containers, and session
management using cgroup process tracking.

%prep
%setup

%build
/bin/bash bootstrap.sh
%configure --disable-static --with-init-script=systemd
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_localstatedir/%name

%files
%doc AUTHORS COPYING README.md
%_bindir/*
%_libdir/*.so*
%_man1dir/*
%_unitdir/*
%_datadir/lxc/config/common.conf.d/*
%dir %_datadir/%name
%_datadir/%name/*
%dir %_localstatedir/%name

%files -n %pam_name
%doc AUTHORS COPYING
%_pam_modules_dir/*

%changelog
* Tue Mar 01 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt1.rc2
- Removed devel package.
  liblxcfs.so is loaded via dlopen.

* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.rc2
- Version update

* Wed Feb 24 2016 Denis Pynkin <dans@altlinux.ru> 2.0.0-alt0.beta2
- Initial version
