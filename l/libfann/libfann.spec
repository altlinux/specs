# $Id: fann.spec 3926 2006-01-10 22:04:21Z dries $
# Authority: dries
%define pk_name fann

Name:    libfann
Version: 2.2.0
Release: alt1
Summary: Fast artificial neural network library
License: LGPL
Group:   System/Libraries 
URL:     http://fann.sourceforge.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  http://dl.sf.net/fann/%pk_name-%version.tar.bz2

Patch1:  portable-handling-for-va_list.patch
Patch2:  fann-2.2.0-pkgconfig.patch
Patch3:  libfann-link-with-libm.patch

BuildRequires: cmake gcc-c++

%description
Fann is a fast artificial neural network library. More information and
a lot of documentation is available at http://fann.sourceforge.net/

%prep
%setup -n %pk_name-%version
%patch1 -p2
%patch2 -p1
%patch3 -p2

%build
%cmake -DPKGCONFIG_INSTALL_DIR=/%_lib/pkgconfig
cd BUILD
%make

%install
cd BUILD
%makeinstall_std
rm -f %buildroot/%_libdir/lib*fann.a

%package devel
Summary: Files for development with FANN
Group: Development/Other
Requires: libfann = %version-%release

%description devel
Development headers of FANN (Fast artificial neural network library)

%files
%doc README.txt
%_libdir/lib*.so.*
%_pkgconfigdir/fann.pc

%files devel
%_libdir/lib*.so
%_includedir/*.h

%changelog
* Wed Jan 23 2013 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version 2.2.0
- Clean spec file

* Wed May 05 2010 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build to Sisyphus.
