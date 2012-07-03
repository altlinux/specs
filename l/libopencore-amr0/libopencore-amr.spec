%set_verify_elf_method textrel=relaxed

%define libname libopencore-amr
%define soversion 0

Name: %libname%soversion
Version: 0.1.2
Release: alt2
Summary: OpenCore implementation of AMR speech codec.

Packager: Konstantin Pavlov <thresh@altlinux.org>
Group: System/Libraries
License: GPLv3

BuildRequires: gcc-c++

Url: http://sourceforge.net/projects/opencore-amr

Source: %libname-%version.tar.bz2

%description
Adaptive Multi Rate speech codec - shared library.
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec.
The implementation is derived from the OpenCORE framework, part of
the Google Android project.

%package -n %{libname}wb%soversion
Summary: OpenCore implementation of AMR speech codec wideband version.
Group: System/Libraries
Provides: %{libname}wb = %version-%release

%description -n %{libname}wb%soversion
Adaptive Multi Rate speech codec - wideband version shared library.
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec.
The implementation is derived from the OpenCORE framework, part of
the Google Android project.

%package -n %{libname}nb%soversion
Summary: OpenCore implementation of AMR speech codec narrowband version.
Group: System/Libraries
Provides: %{libname}nb = %version-%release

%description -n %{libname}nb%soversion
Adaptive Multi Rate speech codec - narrowband version shared library.
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec.
The implementation is derived from the OpenCORE framework, part of
the Google Android project.

%package -n %{libname}wb-devel
Summary: Development files for %{libname}wb
Group: Development/C++
Requires: %{libname}wb = %version-%release

%description -n %{libname}wb-devel
Adaptive Multi Rate speech codec - wideband version development files.
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec.
The implementation is derived from the OpenCORE framework, part of
the Google Android project.

%package -n %{libname}nb-devel
Summary: Development files for %{libname}nb
Group: Development/C++
Requires: %{libname}nb = %version-%release

%description -n %{libname}nb-devel
Adaptive Multi Rate speech codec - narrowband version development files.
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec.
The implementation is derived from the OpenCORE framework, part of
the Google Android project.

%prep
%setup -q -n %libname-%version

%build
%autoreconf

%configure --disable-static

%make_build

%install
%make_install DESTDIR=%buildroot PREFIX=/usr LIBDIR=%_libdir install

%files -n %{libname}wb%soversion
%_libdir/%{libname}wb.so.%{soversion}*

%files -n %{libname}nb%soversion
%_libdir/%{libname}nb.so.%{soversion}*

%files -n %{libname}wb-devel
%_includedir/opencore-amrwb
%_libdir/%{libname}wb.so
%_pkgconfigdir/opencore-amrwb.pc

%files -n %{libname}nb-devel
%_includedir/opencore-amrnb
%_libdir/%{libname}nb.so
%_pkgconfigdir/opencore-amrnb.pc

%changelog
* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Rebuilt for soname set-versions

* Thu Oct 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.1.2-alt1
- 0.1.2 release.

* Mon Jun 01 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.1.1-alt1
- Initial build for ALT Linux.
