%def_enable docs

Summary: C# Bindings for libgphoto2
Name: libgphoto2-sharp
Version: 2.3.99.0
Release: alt4.svn10888
License: %lgpl2plus
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://gphoto.org/
Source: %name-%version.tar.bz2
Source2: %name.snk
Patch1: %name-2.3.99.0-fix-path.patch
Patch2: %name-alt-add-snk.patch
Patch3: %name-2.3.99.0-fix-dll.patch


BuildPreReq: libgphoto2-devel >= 2.3.1
BuildRequires: rpm-build-mono rpm-build-licenses
BuildRequires: /proc
BuildRequires: gcc-c++ mono-mcs mono-devel

%description
This RPM contains C# (.NET) bindings for the libgphoto2 camera access
library.

%package devel
Summary: Development files %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%if_enabled docs
%package doc
Summary: Documentation for libgphoto2-sharp API.
Group: Development/Other
BuildRequires: doxygen fonts-ttf-dejavu graphviz 
BuildPreReq: monodoc-devel
Requires: monodoc
BuildArch: noarch

%description doc
The libgphoto2-sharp-doc package documentation for libgphoto2-sharp API
%endif

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
cp %SOURCE2 src/

%build
%autoreconf
%configure --disable-static %{subst_enable docs} 
%make

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_monodir/%name/%name.*
gacutil -i src/%name.dll -f -package %name -root %buildroot/usr/lib

%files
%doc README AUTHORS COPYING ChangeLog NEWS
%_monodir/%name
%_monogacdir/*

%files devel
%_pkgconfigdir/*

%if_enabled docs
%files doc
%_docdir/%name
%endif

%changelog
* Fri Oct 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.3.99.0-alt4.svn10888
- update dll map patch

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 2.3.99.0-alt3.svn10888
- move pkgconfig files from main to devel package

* Mon Feb 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.3.99.0-alt2.svn10888
- add mono-devel to BuildRequires
- cleanup spec
- build doc package as noarch

* Thu Mar 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.3.99.0-alt1.svn10888
- svn version 2.3.99.0
- add doc package

* Thu Jan 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- Inital release for ALTLinux

