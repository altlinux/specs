# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define fedora 15
Name:           libscs
Version:        1.4.1
Release:        alt3_5.2
Summary:        Software Carry-Save Multiple-Precision Library

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.ens-lyon.fr/LIP/Arenaire/Ware/SCSLib/
Source0:        http://www.ens-lyon.fr/LIP/Arenaire/Ware/SCSLib/scslib-%{version}.tar.gz
Patch0:         scslib-1.4.1-shared.patch

BuildRequires:  autoconf automake libtool
%if 0%{?fedora} > 0 || 0%{?rhel} > 5
BuildRequires:  libmpfr-devel libgmp-devel libgmp_cxx-devel
%endif
Source44: import.info

%description
The Software Carry-Save (SCS) Library is a fast and lightweight
multiple-precision library.

SCSLib has the following features:

- Multiple-precision
SCSLib is a fixed-precision library, where precision is selected at
compile-time. Out-of-the-box, the library ensures 210 bits of precision
(quad-double).

- Floating-point format
The SCS format is a floating-point format where exponents are machine integers
(usually 32-bit numbers), which ensures a huge exponent range.

- Supported operations
SCSLib currently offers addition/subtraction, multiplication, and an
experimental division, plus all the useful conversion functions.

- IEEE-754 compatibility
The range of SCS numbers includes the range of IEEE double-precision numbers,
including denormals and exceptional cases. Conversions between SCS format and 
IEEE-754 doubles, as well as arithmetic operations, follow the IEEE rules
concerning the exceptional cases. SCS doesn't ensure correct rounding, but
provides conversions to doubles in the four IEEE-754 rounding modes.

- Performance
SCSLib is designed to be fast. With 210 bits, it outperforms MPF for most
operations on most architectures.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
%if 0%{?fedora} > 0 || 0%{?rhel} > 5
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n scslib-%{version}
%patch0 -p1 -b .shared


%build
# autoreconf required because the patch modifies autoconf files
autoreconf --install --force
%configure --disable-static \
%if 0%{?fedora} > 0 || 0%{?rhel} > 5
	--enable-mpfr --enable-gmp
%endif

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc COPYING AUTHORS
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%doc DocsDev/html/*
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt3_5.2
- fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt2_5.2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt2_4.2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_4.2
- initial import by fcimport

