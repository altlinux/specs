%define oname webkit-sharp
%def_disable docs

Summary: WebKit bindings for Mono
Name: lib%oname
Version: 0.3
Release: alt4
License: MIT
Group: Development/Other
Url: http://www.mono-project.com/
Packager: Mono Maintainers Team <mono@packages.altlinux.org>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libwebkitgtk2-devel
BuildRequires: libgtk-sharp2-devel
BuildRequires: mono-devel mono-mcs
BuildRequires: /proc

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE, and used
primarily in Apple's Safari browser. It is made to be embedded in other
applications, such as mail readers, or web browsers.

This package provides Mono bindings for WebKit libraries.

%if_enabled docs
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
%endif

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version

%description devel
This package contains the development files needed to build with %name.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS
%_monogacdir/*
%_monodir/%oname

%files devel
%_pkgconfigdir/*

%if_enabled docs
%files doc
%_monodocdir/*
%endif

%changelog
* Wed Oct 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt4
- rebuild with mono-2.10

* Tue Nov 23 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt3
- rebuild with mono-2.8

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt2
- rebuild with libwebkitgtk2

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- 0.3

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt5
- update buildreq

* Fri Apr 17 2009 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt4
- rebuild and fix for webkit-1.1.4(libwebkit-1.0.so.2.2.0)
- enable build docs

* Thu Nov 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt3
- disabled build doc(need fix error)
- remove post scripts
- rename package %name-monodoc to %name-doc

* Wed Oct 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt2
- fix for x86_64

* Thu Aug 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- initial build for ALTLinux

