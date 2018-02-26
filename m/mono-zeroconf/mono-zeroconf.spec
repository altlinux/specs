%define origname mono-zeroconf

Name: mono-zeroconf
Version: 0.9.0
Release: alt1

Summary: Cross platform Zero Configuration Networking library 
License: %mit
Group: Development/Other
Url: http://mono-project.com/Mono_Zeroconf

Source: http://download.banshee-project.org/mono-zeroconf/%name-%version.tar.bz2
Patch1: %name-0.8.0-alt-fix-path.patch

BuildRequires: mono-devel mono-mcs
BuildRequires: /proc
BuildPreReq: rpm-build-mono rpm-build-licenses

%description
Mono.Zeroconf is a cross platform Zero Configuration Networking library for
Mono and .NET. It provides a unified API for performing the most common
zeroconf operations on a variety of platforms and subsystems: all the
operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.

This package was built with support for Avahi only.

%package devel
Summary: Development files %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%package doc
Summary: Development documentation for %name
Group: Documentation
Provides: %name-monodoc = %version-%release
Obsoletes: %name-monodoc 
BuildPreReq: monodoc-devel
Requires: monodoc
BuildArch: noarch

%description doc
This package contains the API documentation for %name in
Monodoc format.

%prep
%setup -q
%patch1 -p1
subst "s|^assemblydir *= \$(libdir)/mono-zeroconf|assemblydir = \$(prefix)/lib/mono-zeroconf|" \
	src/*/Makefile.{in,am}

%build
%configure --disable-mdnsresponder --disable-static
%make

%install
%make_install DESTDIR=%buildroot install

%files
%doc README COPYING
%_bindir/*
%_monogacdir/*
%_monodir/%name
%_prefix/lib/%name

%files devel
%_pkgconfigdir/*

%files doc
%_monodocdir/*

%changelog
* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0
- move pkgconfig files from main to devel package
- drop patch2 (fixed upstream)

* Tue Apr 07 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt5
- fix build with mono-2.2 (patch2)

* Thu Nov 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt4
- rebuild with new macros _monodocdir
- remove post scripts
- rename package %name-monodoc to %name-doc

* Sat Nov 08 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt3
- fix install path dll for x86_64

* Wed Oct 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt2
- fix for x86_64

* Sat Oct 25 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- initial build for ALTLinux

