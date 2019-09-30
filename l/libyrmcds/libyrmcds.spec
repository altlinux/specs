# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major     0
%define libname   libyrmcds%{major}
%define develname libyrmcds-devel

Summary:        A memcached client library written in C
Name:           libyrmcds
Version:        1.2.1
Release:        alt1_3
Group:          System/Libraries
License:        BSD-like
URL:            http://cybozu.github.io/libyrmcds/
Source0:        https://github.com/cybozu/libyrmcds/archive/v%{version}.tar.gz
Patch0:         libyrmcds-1.2.1-shared.diff
Patch1:         libyrmcds-1.2.1-system_lz4.diff
BuildRequires:  pkgconfig(liblz4)
Source44: import.info

%description
This package contains client memcached/yrmcds client programs and provides
access to all libyrmcds library functions therefore access to all server
functions.

%package -n     %{libname}
Summary:        Shared memcached client library
Group:          System/Libraries
Obsoletes:      %{_lib}libyrmcds0 < 1.2.1-2

%description -n %{libname}
A memcached client library for C/C++.

%package -n     %{develname}
Summary:        Development library for libyrmcds
Group:          Development/C
Requires:       pkgconfig(liblz4)
Requires:       %{libname} = %{version}-%{release}
Provides:       yrmcds-devel = %{version}-%{release}
Obsoletes:      %{_lib}libyrmcds-devel < 1.2.1-2

%description -n %{develname}
This package contains the header(.h) and library(.so) files required to build
applications using the libyrmcds library.

%prep

%setup -q
%patch0 -p1
%patch1 -p1


%build
%make_build CFLAGS="%{optflags} -fPIC" LDFLAGS=" -L."

%install
%makeinstall_std LIBDIR=%{_libdir} PREFIX=%{_prefix}

install -d %{buildroot}%{_bindir}
install -m0755 yc %{buildroot}%{_bindir}/
install -m0755 yc-cnt %{buildroot}%{_bindir}/

rm -f %{buildroot}%{_libdir}/*.*a

%files
%{_bindir}/yc
%{_bindir}/yc-cnt

%files -n %libname
%doc COPYING README* USAGE*
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %develname
%{_includedir}/*.h
%{_libdir}/*.so


%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3
- new version

