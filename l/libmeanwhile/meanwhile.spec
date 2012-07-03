%define oname meanwhile
%def_disable static
%def_disable debug
%def_disable mailme
%def_enable doxygen

Name: lib%oname
Summary: Lotus Sametime Community Client library
License: LGPLv2+
Group: Networking/Instant messaging
Version: 1.1.0
Release: alt2
Source: http://dl.sf.net/%oname/%oname-1.0.2.tar.gz
Patch0: meanwhile-1.1.0.patch
Patch1: meanwhile-crash.patch
Patch2: meanwhile-fix-glib-headers.patch

Url: http://meanwhile.sourceforge.net

# Automatically added by buildreq on Mon Dec 01 2008
BuildRequires: gcc-c++ glib2-devel

%{?_enable_doxygen:BuildPreReq: doxygen}

%description
The heart of the Meanwhile Project is the Meanwhile library, providing the
basic Lotus Sametime session functionality along with the core services;
Presence Awareness, Instant Messaging, Multi-user Conferencing, Preferences
Storage, Identity Resolution, and File Transfer. This extensible client
interface allows additional services to be added to a session at runtime,
allowing for simple integration of future service handlers such as the user
directory and whiteboard and screen-sharing.

%package devel
Summary: Header files, libraries and development documentation for %oname
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %oname,
you will need to install %name-devel.

%package doc
Summary: Documentation for the Meanwhile library
Group: Documentation
License: GFDL
BuildArch: noarch

%description doc
Documentation for the Meanwhile library

%prep
%setup -q -n %oname-1.0.2
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{?_enable_debug:--enable-debug} \
	%{subst_enable mailme} \
	%{subst_enable doxygen}

%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS ChangeLog README TODO
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%_defaultdocdir/%oname-doc-%version

%changelog
* Sat Mar 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt2
- fixed build against glib2 >= 2.31 (fc patch)

* Fri Nov 12 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon Dec 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- initial build for ALTLinux

