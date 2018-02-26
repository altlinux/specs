%def_disable static

Name: libEMF
Version: 1.0.4
Release: alt1.qa1

Summary: A library for generating Enhanced Metafiles
License: LGPLv2+ and GPLv2+
Group: System/Libraries

Url: http://libemf.sourceforge.net
Source: http://downloads.sourceforge.net/pstoedit/%name-%version.tar.gz
Patch: %name-amd64.patch
Patch1: %name-axp.patch
Patch3: %name-s390.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Dec 13 2009
BuildRequires: gcc-c++

Summary(pl): Biblioteka do generowania plików w formacie Enhanced Metafile

%description
libEMF is a library for generating Enhanced Metafiles on systems which
don't natively support the ECMA-234 Graphics Device Interface
(GDI). The library is intended to be used as a driver for other
graphics programs such as Grace or gnuplot. Therefore, it implements a
very limited subset of the GDI.

%description -l pl
libEMF to biblioteka do generowania plików w formacie Enhanced
Metafile na systemach nie obsługujących natywnie systemu graficznego
ECMA-234 GDI. Biblioteka ma służyć jako sterownik dla innych programów
graficznych, takich jak Grace czy gnuplot. Z tego powodu ma
zaimplementowany bardzo ograniczony podzbiór GDI.

%package utils
Summary: libEMF utilities
Group: File tools

%description utils
libEMF utilities

%package devel
Summary: libEMF header files
Summary(pl): Pliki nagłówkowe libEMF
Group: Development/C++
Requires: %name = %version-%release
Requires: libstdc++-devel

%description devel
libEMF header files.

%description devel -l pl
Pliki nagłówkowe libEMF.

%if_enabled static
%package devel
Summary: libEMF static files
Group: Development/C++
Requires: %name = %version-%release
Requires: libstdc++-devel

%description devel-static
libEMF static files.
%endif

%prep
%setup
%patch0 -p1 -b .amd64
%patch1 -p1 -b .axp
%patch3 -p1 -b .s390

%build
%autoreconf
%configure %{subst_enable static} --enable-editing
%make_build

%install
export CPPROG="cp -p"
%makeinstall_std

%check
make check

%files
%doc AUTHORS ChangeLog COPYING COPYING.LIB NEWS README
%_libdir/lib*.so.*

%files utils
%_bindir/*

%files devel
%doc doc/html
%_libdir/lib*.so
%_includedir/%name/

%if_enabled static
%files devel-static
%_libdir/lib*.a
%endif

%changelog
* Sat Nov 27 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1.0.4-alt1
- built for ALT Linux
  + spec adapted from Fedora
    - where it got adapted from PLD
- heavy spec cleanup
- refined subpackages (added utils and optional devel-static)
