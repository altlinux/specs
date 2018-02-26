Name: flam3
Version: 2.7.18
Release: alt2

Summary: Cosmic Recursive Fractal Flames
License: GPL
Group: Graphics
Url: http://flam3.com/

Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name-%version.tar.gz

# Automatically added by buildreq on Wed Apr 11 2007
BuildRequires: libjpeg-devel libpng-devel libxml2-devel

%description
Flam3 renders fractal flames and manipulates their genomes.

%package devel
Summary: Development environment for building applications with %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Files required to compile software that uses %name

%package palettes
Summary: The %name palettes xml file
Group: Graphics
BuildArch: noarch

%description palettes
The %name palettes xml file

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libraries for %name

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/*
%doc README.txt COPYING
%_mandir/*/*

%files -n %name-palettes
%_datadir/%name

%files -n %name-devel
%_includedir/*
%_pkgconfigdir/%name.pc

%files -n %name-devel-static
%_libdir/lib%name.a

%changelog
* Thu Jan 28 2010 Alexandra Panyukova <mex3@altlinux.org> 2.7.18-alt2
- palettes subpackage made noarch (repocop) (Closes: 20867)

* Wed Jul 22 2009 Alexandra Panyukova <mex3@altlinux.ru> 2.7.18-alt1
- new version

* Fri Apr 11 2008 Alexandra Panyukova <mex3@altlinux.ru> 2.7.11-alt1
- new version

* Fri Jan 5 2008 Alexandra Panyukova <mex3@altlinux.ru> 2.7.7-alt1
- 2.7.7
- added %name-devel package
- added %name-devel-static package
- added %name-palettes package

* Wed Apr 11 2007 Alexandra Panyukova <mex3@altlinux.ru> 2.7.2-alt1
- Initial build
