Group: Development/C
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 60ea749837362c226e8501718f505ab138e5c19d
%global date 20171225

%global with_check 1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    libb2
Summary: C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp
Version: 0.98
Release: alt1_2.%{date}git%{shortcommit}
License: CC0
URL:     https://blake2.net/
Source0: https://github.com/BLAKE2/libb2/archive/%{commit}/libb2-%{commit}.tar.gz

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
%setup -q -n libb2-%{commit}


# Force default Fedora cflags
sed -e 's|CFLAGS=-O3|CFLAGS="%{optflags}"|g' -i configure.ac
autoreconf -ivf

%build
# Default Fedora cflags prevents SSE checking
unset $CFLAGS
%configure --disable-silent-rules --enable-static=no --enable-native=no
%make_build LDFLAGS="%{__global_ldflags}"

%if 0%{with_check}
%check
make check
%endif

%install
%makeinstall_std
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la



%files
%doc --no-dereference LICENSE
%{_libdir}/libb2.so.*

%files devel
%{_libdir}/libb2.so
%{_includedir}/blake2.h

%changelog
* Fri Jan 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1_2.20171225git60ea749
- new version

