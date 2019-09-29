BuildRequires: chrpath
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/clang-format /usr/bin/cppcheck gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major		4
%define libname		libczmq%{major}
%define develname	libczmq-devel

Name:           czmq
Version:        4.2.0
Release:        alt1_1
Summary:        High-level C binding for 0MQ (ZeroMQ)
Group:          Development/Other
License:        MPLv2.0
URL:            http://czmq.zeromq.org/
Source0:        https://github.com/zeromq/czmq/releases/download/v%{version}/czmq-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libuuid-devel
BuildRequires:  libzeromq-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(systemd)
# --with-docs
BuildRequires:  perl
BuildRequires:  asciidoc asciidoc-a2x
BuildRequires:  xmlto
Source44: import.info

%description
CZMQ has the following goals:
  i) To wrap the A'MQ core API in semantics that are natural and lead to
     shorter, more readable applications.
 ii) To hide the differences between versions of A'MQ.
iii) To provide a space for development of more sophisticated API semantics.

%package -n	%{libname}
Summary:        High-level C binding for 0MQ (ZeroMQ)
Group:		System/Libraries

%description -n %{libname}
CZMQ has the following goals:
  i) To wrap the A'MQ core API in semantics that are natural and lead to
     shorter, more readable applications.
 ii) To hide the differences between versions of A'MQ.
iii) To provide a space for development of more sophisticated API semantics.

%package -n %{develname}
Summary:        Development files for the czmq package
Requires:       %{libname} = %{version}-%{release}
Group:		Development/C
Provides:       %{name}-devel
Provides:       lib%{name}-devel

%description -n %{develname}
This package contains files needed to develop applications using czmq.


%prep
%setup -q



%build
%configure \
    --disable-static \
    --with-docs
%make_build


%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done

%check
make check

%files -n %{libname}
%doc AUTHORS NEWS
%doc --no-dereference LICENSE
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%doc CONTRIBUTING.md README.md
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*
%{_datadir}/zproject/


%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_1
- new version

