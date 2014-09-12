%set_verify_elf_method textrel=relaxed

%define libname libopencore-amr
%define soversion 0

Name: %libname%soversion
Version: 0.1.3
Release: alt1.git20140714
Summary: OpenCore implementation of AMR speech codec.

Group: System/Libraries
License: ASLv2.0

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

%package -n %libname-examples
Summary: Examples for %libname
Group: Development/Documentation

%description -n %libname-examples
Adaptive Multi Rate speech codec - narrowband version development files.
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec.
The implementation is derived from the OpenCORE framework, part of
the Google Android project.

This package contains examples for %libname.


%prep
%setup -n %libname-%version

%build
%autoreconf

%configure --disable-static \
	--enable-examples

cp -fR test examples

%make_build V=1

%install
%makeinstall_std PREFIX=/usr LIBDIR=%_libdir

%files -n %{libname}wb%soversion
%doc ChangeLog README
%_libdir/%{libname}wb.so.%{soversion}*

%files -n %{libname}nb%soversion
%doc ChangeLog README
%_libdir/%{libname}nb.so.%{soversion}*

%files -n %{libname}wb-devel
%_includedir/opencore-amrwb
%_libdir/%{libname}wb.so
%_pkgconfigdir/opencore-amrwb.pc

%files -n %{libname}nb-devel
%_includedir/opencore-amrnb
%_libdir/%{libname}nb.so
%_pkgconfigdir/opencore-amrnb.pc

%files -n %libname-examples
%doc examples/*
%_bindir/*

%changelog
* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20140714
- Version 0.1.3

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.2-alt2.1.qa1
- NMU: rebuilt for updated dependencies.

* Sat Nov 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.1
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Rebuilt for soname set-versions

* Thu Oct 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.1.2-alt1
- 0.1.2 release.

* Mon Jun 01 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.1.1-alt1
- Initial build for ALT Linux.
