Group: Development/C
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global with_check 1

Name:    libb2
Summary: C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp
Version: 0.98.1
Release: alt1_1
License: CC0
URL:     https://blake2.net/
Source0: https://github.com/BLAKE2/libb2/archive/v%{version}/libb2-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: automake
BuildRequires: libtool
Source44: import.info

%description
C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp.

BLAKE2 is a cryptographic hash function faster than MD5, SHA-1, SHA-2,
and SHA-3, yet is at least as secure as the latest standard SHA-3.

%package        devel
Group: Development/C
Summary:        Development files for the Blake2 library
Requires:       %{name} = %{version}-%{release}

%description    devel
%{summary}.

%prep
%setup -q -n libb2-%{version}


# Force default Fedora cflags
sed -e 's|CFLAGS=-O3|CFLAGS="%{optflags}"|g' -i configure.ac
autoreconf -ivf

%build
%configure --disable-silent-rules --enable-static=no --enable-native=no
%make_build

%if 0%{with_check}
%check
make check
%endif

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la



%files
%doc --no-dereference COPYING
%{_libdir}/libb2.so.1
%{_libdir}/libb2.so.1.*

%files devel
%{_libdir}/libb2.so
%{_libdir}/pkgconfig/libb2.pc
%{_includedir}/blake2.h

%changelog
* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.98.1-alt1_1
- update to new release by fcimport

* Fri Jan 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1_2.20171225git60ea749
- new version

