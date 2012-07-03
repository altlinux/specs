%define _libexecdir %_prefix/libexec

Name: podsleuth
Version: 0.6.5
Release: alt1

Summary: Extract metadata from Apple iPods
License: %mit
Group: System/Libraries
Url: http://banshee-project.org/PodSleuth

Source: http://banshee-project.org/files/%name/%name-%version.tar.bz2
Patch: podsleuth-0.6.3-alt-fix-pkgconfig.patch

BuildRequires: mono-devel mono-mcs
BuildRequires: libhal-devel hal
BuildRequires: ndesk-dbus-devel
BuildRequires: libsgutils-devel
BuildRequires: /proc
BuildPreReq: rpm-build-mono rpm-build-licenses

%description
PodSleuth is a tool to discover detailed model information about an
Apple (TM) iPod (TM). Its primary role is to be run as a callout by
HAL (http://freedesktop.org/wiki/Software_2fhal) because root access
is needed to scan the device for required information. When the model
information is discovered, it is merged into HAL as properties for
other applications to use.

%package devel
Summary: ipod-sharp development files
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%prep
%setup -q
%patch -p1

%build
%__aclocal -I m4
%__autoconf
%__automake

%configure \
	--with-hal-callouts-dir=%_libexecdir/hal \
	--with-update-dir=%_var/cache/%name
%make

%install
mkdir -p %buildroot%_var/cache/%name
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING ChangeLog README NEWS
%_bindir/%name
%_libexecdir/hal/*
%_prefix/lib/%name
%_datadir/hal/fdi/policy/20thirdparty/20-podsleuth.fdi
%dir %_var/cache/%name

%files devel
%_pkgconfigdir/*

%changelog
* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Thu Aug 20 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.4-alt2
- rebuild with new libsgutils (sg3_utils-1.27-alt1)

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.4-alt1
- 0.6.4
- move pkgconfig files from main to devel package

* Wed Nov 12 2008 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt2
- for build on x86_64

* Sat Oct 25 2008 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALTLinux

