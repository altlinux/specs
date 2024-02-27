%define lib_name libUseful

Name:    Alaya
Version: 4.5.0.1.gitc003169
Release: alt1

Summary: Webdav enabled webserver mostly focused on file storage

License: GPL-3.0
Group:   System/Servers
Url:     https://github.com/ColumPaget/Alaya

Packager: Sergey Gvozdetskiy <serjigva@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-webserver-common
BuildRequires: LibreSSL-devel libcrypto3
BuildRequires: libcap-devel
BuildRequires: libpam0-devel
BuildRequires: zlib-devel

%description
Alaya is a chrooting webserver with basic webdav extensions.
It can serve both http and https and is intended to provide a simple means for
people to share directories with webdav. Although it chroots it supports
running CGI programs outside of the chroot via a trusted-path method.
Alaya aims at ease of use, so all options can be configured via command-line
args, though a config file is also supported.

# Development stuff library pkg
%package -n %lib_name-devel
Summary: %lib_name development libraries and headers
Group:   Development/C

%description -n %lib_name-devel
%lib_name provides a range of functions that simplify common programming tasks
in 'C', particularly networking and communications. It hides the complexities
of sockets, openssl, zlib, pseudoterminals, http, etc and provides commonly
needed functionality like resizeable strings, linked lists and maps.

%prep
%setup

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%autoreconf
%configure \
%ifarch x86_64
  --enable-simd \
%endif
  --enable-ssl \
  --enable-ipv6 \
  --enable-largefiles \
  --enable-pam

%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_libdir/%lib_name,%_includedir/%lib_name}
mkdir -p %buildroot%_defaultdocdir/%lib_name-%version

cp --preserve=all %lib_name/%{lib_name}*so %buildroot%_libdir/%lib_name
cp --preserve=all %lib_name/*.h %buildroot%_includedir/%lib_name
cp --preserve=all %lib_name/*.md %buildroot%_defaultdocdir/%lib_name-%version

%files
%doc *.md LICENCE
%_sbindir/alaya
%config(noreplace) %_sysconfdir/alaya.conf

%files -n %lib_name-devel
%_defaultdocdir/%lib_name-%version
%_includedir/%lib_name
%_libdir/%lib_name

%changelog
* Thu Feb 01 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 4.5.0.1.gitc003169-alt1
- Build new version from git ref c003169 for Sisyphus

* Mon Dec 25 2023 Sergey Gvozdetskiy <serjigva@altlinux.org> 4.5-alt1
- initial build for Sisyphus
