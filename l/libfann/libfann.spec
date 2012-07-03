# $Id: fann.spec 3926 2006-01-10 22:04:21Z dries $
# Authority: dries
%define pk_name fann

Name: libfann
Version: 2.0.0
Release: alt1
Summary: Fast artificial neural network library
License: LGPL
Group: System/Libraries 
URL: http://fann.sourceforge.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: http://dl.sf.net/fann/%pk_name-%version.tar.bz2
BuildRequires: gcc, make, gcc-c++

%description
Fann is a fast artificial neural network library. More information and
a lot of documentation is available at http://fann.sourceforge.net/

%prep
%setup -n %pk_name-%version

%build
export LIBS='-lm'
%configure
%make

%install
%makeinstall
rm -f %buildroot/%_libdir/lib*fann.a

%package devel
Summary: Files for development with FANN
Group: Development/Other
Requires: libfann = %version-%release

%description devel
Development headers of FANN (Fast artificial neural network library)

%files
%doc AUTHORS COPYING INSTALL NEWS README README TODO
%_libdir/libfloatfann.so.*
%_libdir/libdoublefann.so.*
%_libdir/libfixedfann.so.*
%_libdir/libfann.so.*
%_libdir/pkgconfig/fann.pc

%files devel
%_libdir/libfloatfann.so
%_libdir/libdoublefann.so
%_libdir/libfixedfann.so
%_libdir/libfann.so
%_includedir/compat_time.h
%_includedir/doublefann.h
%_includedir/fann*.h
%_includedir/fixedfann.h
%_includedir/floatfann.h

%changelog
* Wed May 05 2010 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build to Sisyphus.
