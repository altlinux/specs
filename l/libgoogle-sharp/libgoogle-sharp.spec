%define realname google-sharp
%def_enable doc

Summary: Google-sharp is a .NET library.
Name: lib%{realname}
Version: 0.1.0
Release: alt4.svn20070520
License: X11/MIT
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.mono-project.com/
Source: %realname-%version.tar.bz2
Patch1: google-sharp-0.1.0-alt-monodoc.patch

BuildRequires: mono-mcs mono-devel
BuildRequires: rpm-build-mono
BuildRequires: /proc

%description
Google-sharp is a .NET library that lets you log in to Google services and use
them programatically. Currently only Picasaweb is supported.

When connected to a picasaweb account, you can create albums and browse,
download or upload pictures.

%package devel
Summary: Google-sharp  development files
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the Google-sharp project.

%package doc
Summary: Development documentation for %name
Group: Documentation
Provides: %name-monodoc = %version-%release
Obsoletes: %name-monodoc
BuildPreReq: monodoc-devel
Requires: monodoc
BuildArch: noarch

%description doc
This package contains the API documentation for the %name in
Monodoc format.

%prep
%setup -n %realname-%version -q
%patch1 -p1

%build
%__aclocal
%__automake -a
%__autoconf
%configure --disable-static
%make

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_monodir/Mono.Google/Mono.Google.*
gacutil -package Mono.Google -root %buildroot/usr/lib -i src/Mono.Google.dll

%files
%doc README AUTHORS COPYING ChangeLog
%_monodir/Mono.Google
%_monogacdir/*

%files devel
%_pkgconfigdir/*

%if_enabled doc
%files doc
%_monodocdir/*
%endif

%changelog
* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt4.svn20070520
- move pkgconfig files from main to devel package

* Mon Feb 16 2009 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt3.svn20070520
- add mono-devel to BuildRequires

* Mon Dec 01 2008 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt2.svn20070520
- rebuild with new macros _monodocdir

* Mon Jan 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1.svn20070520
- Inital release for ALTLinux

