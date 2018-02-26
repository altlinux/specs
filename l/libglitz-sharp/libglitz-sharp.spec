%define realname glitz-sharp
%define ver_major 0.0

Summary: C# Glitz binding
Name: lib%{realname}
Version: %ver_major.0
Release: alt3.git20070113
License: MIT
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.ndesk.org/
Source: %realname-%ver_major.tar.bz2
Source1: NDesk.Glitz.dll.config
Source2: NDesk.Glitz.pkgconfig
Patch1: %name-unsafe.patch

BuildRequires: libgtk-sharp2-devel mono-mcs mono-devel libglitz-devel

BuildRequires: rpm-build-mono
BuildRequires: /proc

%description
glitz-sharp is a .NET Glitz binding

%package devel
Summary: Development files %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%prep
%setup -n %realname-%ver_major -q
%patch1 -p1

%build
%make CSFLAGS=" -debug -unsafe"

%install
mkdir -p %buildroot%_monodir/NDesk.Glitz
gacutil -i src/NDesk.Glitz.dll -f -package NDesk.Glitz -root %buildroot/usr/lib

mkdir -p %buildroot%_pkgconfigdir
install -m 644 %SOURCE2 %buildroot%_pkgconfigdir/glitz-sharp.pc

%files
%doc COPYING
%_monodir/NDesk.Glitz
%_monogacdir/*

%files devel
%_pkgconfigdir/*

%changelog
* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.0.0-alt3.git20070113
- move pkgconfig files from main to devel package

* Mon Feb 16 2009 Alexey Shabalin <shaba@altlinux.ru> 0.0.0-alt2.git20070113
- add mono-devel to BuildRequires
- cleanup spec

* Mon Jan 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.0.0-alt1.git20070113
- Inital release for ALTLinux
