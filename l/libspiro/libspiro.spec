# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global major   1
%define libname libspiro%{major}
%define devname libspiro-devel

Name:           libspiro
Version:        20221101
Release:        alt1_1
Summary:        Library to simplify the drawing of beautiful curves

Group:          System/Libraries
License:        GPLv2+
URL:            https://libspiro.sourceforge.net/
# Let's use libspiro-dist tarball from upstream as it does not require autoreconf
Source0:        https://github.com/fontforge/libspiro/releases/download/%{version}/libspiro-dist-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
Source44: import.info

%description
This library will take an array of spiro control points and
convert them into a series of bA.zier splines which can then
be used in the myriad of ways the world has come to use bA.ziers.

%package        -n %libname
Summary:        Library to simplify the drawing of beautiful curves
Group:          System/Libraries

%description    -n %libname
This library will take an array of spiro control points and
convert them into a series of bA.zier splines which can then
be used in the myriad of ways the world has come to use bA.ziers.

%package        -n %devname
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       spiro-devel = %{version}-%{release}

%description    -n %devname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n libspiro-%{version}


%build
%configure --disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%check
make check

%files -n %libname
%doc COPYING README* ChangeLog AUTHORS
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %devname
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libspiro.pc
%{_mandir}/man3/libspiro.3*



%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 20221101-alt1_1
- update by mgaimport

* Fri Nov 05 2021 Igor Vlasenko <viy@altlinux.org> 20200505-alt1_1
- new version (closes: 41201)

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20071029-alt2.qa2
- NMU: rebuilt for debuginfo.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 20071029-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 20071029-alt2
- cleanup spec

* Tue Oct 30 2007 Vitaly Lipatov <lav@altlinux.ru> 20071029-alt1
- initial build for ALT Linux Sisyphus
