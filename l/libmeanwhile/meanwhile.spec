%define oname meanwhile
%def_disable static
%def_disable debug
%def_disable mailme
%def_enable doxygen
%def_enable check

Name: lib%oname
Version: 1.1.1
Release: alt1

Summary: Lotus Sametime Community Client library
Group: Networking/Instant messaging
License: LGPLv3+
Url: https://github.com/obriencj/%oname

Source: %oname-%version.tar.gz

BuildRequires: gcc-c++ glib2-devel

%{?_enable_doxygen:BuildRequires: doxygen}

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
%setup -n %oname-%version

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{?_enable_debug:--enable-debug} \
	%{subst_enable mailme} \
	%{subst_enable doxygen}

%make_build

%install
%makeinstall_std

%check
%make check

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
* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1 (new %%url)

* Sat Mar 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt2
- fixed build against glib2 >= 2.31 (fc patch)

* Fri Nov 12 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon Dec 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- initial build for ALTLinux

