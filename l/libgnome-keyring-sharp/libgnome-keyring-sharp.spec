%define realname gnome-keyring-sharp
%def_enable dbus
%def_enable doc

Summary: Gnome-keyring-sharp is a fully managed implementation of libgnome-keyring.
Name: lib%{realname}
Version: 1.0.1
Release: alt5.svn20081014
License: X11/MIT
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.mono-project.com/

Source: %realname-%version.tar.bz2
Patch1: gnome-keyring-sharp-1.0.1-alt-monodoc.patch

BuildRequires: mono-mcs mono-devel ndesk-dbus-devel
BuildRequires: rpm-build-mono
BuildRequires: /proc

%description
When the gnome-keyring-daemon is running, you can use this to retrive/store
confidential information such as passwords, notes or network services user
information.

%package devel
Summary: Gnome-keyring-sharp development files
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the Gnome-keyring-sharp.


%package doc
Summary: Development documentation for gnome-keyring-sharp API.
Group: Documentation
Provides: %name-monodoc = %version-%release
Obsoletes: %name-monodoc
BuildPreReq: monodoc-devel
Requires: monodoc
BuildArch: noarch

%description doc
This package contains the API documentation for the gnome-keyring-sharp in
Monodoc format.

%prep
%setup -n %realname-%version -q
%patch1 -p1

%build
%__aclocal
%__automake -a
%__autoconf
%configure --disable-static %{subst_enable dbus}
%make

%install
%make_install install DESTDIR=%buildroot

%files
%doc README AUTHORS COPYING ChangeLog
%_monogacdir/*
%_monodir/%realname-1.0

%files devel
%_pkgconfigdir/*


%if_enabled doc
%files doc
%_monodocdir/*
%endif


%changelog
* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt5.svn20081014
- move pkgconfig files from main to devel package

* Mon Feb 16 2009 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt4.svn20081014
- add mono-devel to BuildRequires

* Mon Dec 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt3.svn20081014
- rebuild with new macros _monodocdir

* Wed Oct 22 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt2.svn20081014
- update to svn r116731
- build docs as noarch

* Mon Jan 21 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2.svn20071017
- fix monodoc path for x86_64 (patch1)

* Mon Jan 14 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1.svn20071017
- Inital release for ALTLinux

