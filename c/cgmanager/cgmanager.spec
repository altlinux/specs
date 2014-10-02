Name: cgmanager
Version: 0.32
Release: alt1

Summary: Linux cgroup manager
License: %lgpl2plus
Group: System/Base

URL: http://cgmanager.linuxcontainers.org
# git://github.com/cgmanager/cgmanager
Source: %name-%version.tar
Source1: %name.init
Source2: cgproxy.init
Patch: %name-%version-%release.patch

# From Debian
Patch1: 0001-fix-regression-introduced-by-recent-switch-to-nih_lo.patch
Patch2: 0002-gettasksrecursive-call-the-scm-completion.patch
Patch3: 0003-gettasksrecursive_scm-call-the-right-main-function.patch
Patch4: 0004-cgmanager-remount-sys-fs-cgroup-rw-if-needed.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libdbus-devel libnih-dbus-devel help2man

%description
CGManager is a central privileged daemon that manages all your
cgroups for you through a simple DBus API. It's designed to work
with nested LXC containers as well as accepting unprivileged requests
including resolving user namespaces UIDs/GIDs.

%package -n lib%name
Summary: Shared library files for %name
Group: System/Libraries

%description -n lib%name
This package contains libraries for running %name applications.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains header files and library needed for
development with lib%name.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Fix systemd units path
sed -i 's;^SYSTEMD_UNIT_DIR = .*$;SYSTEMD_UNIT_DIR = %systemd_unitdir;' config/init/systemd/Makefile.am

%build
%autoreconf
%configure \
	--disable-static \
	--with-distro=alt \
	--with-init-script=systemd

%make_build

%install
%makeinstall_std

install -pDm755 %SOURCE1 %buildroot%_initdir/%name
install -pDm755 %SOURCE2 %buildroot%_initdir/cgproxy

%files
%_bindir/*
%_sbindir/*
%_initdir/*
%_man1dir/*.1.*
%_man8dir/*.8.*
%_datadir/%name/
%systemd_unitdir/cgmanager.service
%systemd_unitdir/cgproxy.service


%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Wed Oct 01 2014 Mikhail Efremov <sem@altlinux.org> 0.32-alt1
- Add patches from Debian.
- Add init scripts.
- Fix libcgmanager linking.
- Initial build.
