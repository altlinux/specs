# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: freexl
Version: 1.0.0d
Release: alt2
Summary: Library to extract data from within an Excel spreadsheet
Group: System/Libraries
License: MPLv1.1 or GPLv2+ or LGPLv2+
Url: http://www.gaia-gis.it/FreeXL
Source0: http://www.gaia-gis.it/FreeXL/%name-%version.tar.gz
BuildRequires: doxygen
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source44: import.info
Patch33: freexl-1.0.0d-alt-linkage.patch

%description
FreeXL is a library to extract valid data
from within an Excel spreadsheet (.xls)

Design goals:
    * simple and lightweight
    * stable, robust and efficient
    * easily and universally portable
    * completely ignore any GUI-related oddity

%package devel
Summary: Development Libraries for FreeXL
Group: Development/C
Requires: %name%{?_isa} = %version-%release

%description devel
The %%{name}-devel package contains libraries and header files for
developing applications that use %%{name}.

%prep
%setup
%patch33 -p1

%build
autoreconf -fisv
%configure --enable-gcov=no --disable-static
make %{?_smp_mflags}

# Mailed the author on Dec 5th 2011
# Preserve date of header file
sed -i 's/^INSTALL_HEADER = \$(INSTALL_DATA)/& -p/' headers/Makefile.in

# Generate HTML documentation and clean unused installdox script
doxygen
rm -f html/installdox

%check
make check

# Clean up
pushd examples
  make clean
popd

%install
make install DESTDIR=%buildroot

# Delete undesired libtool archives
rm -f %buildroot%_libdir/lib%name.la

%files
%doc COPYING AUTHORS README
%_libdir/lib%name.so.*

%files devel
%doc examples html
%_includedir/freexl.h
%_libdir/lib%name.so
%_libdir/pkgconfig/freexl.pc

%changelog
* Tue Jan 29 2013 Ilya Mashkin <oddity@altlinux.ru> 1.0.0d-alt2
- build for Sisyphus

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0d-alt1_2
- initial fc import

