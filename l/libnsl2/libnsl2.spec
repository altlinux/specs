# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       libnsl2
Version:    1.1.0
Release:    alt1_1
Summary:    Public client interface library for NIS(YP) and NIS+

License:    BSD and LGPLv2+
Group:      System/Libraries
URL:        https://github.com/thkukuk/libnsl


Source0:    https://github.com/thkukuk/libnsl/archive/libnsl-%{version}.tar.gz#/libnsl-libnsl-%{version}.tar.gz

Patch0: libnsl2-1.0.5-include_stdint.patch

BuildRequires: autoconf, automake gettext-tools libasprintf-devel, libtool, libtirpc-devel
Source44: import.info

%description
This package contains the libnsl library. This library contains
the public client interface for NIS(YP) and NIS+.
This code was formerly part of glibc, but is now standalone to
be able to link against TI-RPC for IPv6 support.

%package devel
Summary: Development files for libnsl
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description devel
Development files for libnsl2


%prep
%setup -q -n libnsl-libnsl-%{version}

%patch0 -p1 -b .include_stdint

%build

export CFLAGS="%{optflags}"

autoreconf -fiv

%configure\
    --libdir=%{_libdir}/nsl\
    --includedir=%{_includedir}/nsl\

%make_build


%install

%makeinstall_std

rm %{buildroot}/%{_libdir}/nsl/libnsl.a
rm %{buildroot}/%{_libdir}/nsl/libnsl.la
mv %{buildroot}/%{_libdir}/nsl/pkgconfig %{buildroot}/%{_libdir}

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/nsl" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%files
%dir %{_libdir}/nsl
%{_libdir}/nsl/libnsl.so.2
%{_libdir}/nsl/libnsl.so.2.0.0
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/*

%doc COPYING


%files devel
%{_libdir}/nsl/libnsl.so
%{_includedir}/nsl/
%{_libdir}/pkgconfig/libnsl.pc

%changelog
* Fri Nov 24 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- new version

