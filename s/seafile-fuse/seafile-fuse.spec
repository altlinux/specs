Name: seafile-fuse
Version: 2.0.28
Release: alt1

Summary: SeaDrive daemon with FUSE interface

Group: Networking/File transfer
License: GPLv2 with permissions for OpenSSL
Url: https://github.com/haiwen/seafile-fuse

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/haiwen/seadrive-fuse/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
#BuildRequires: vala
BuildRequires: libuuid-devel

# see configure.ac
BuildRequires: pkgconfig(sqlite3) >= 3.0.0
BuildRequires: pkgconfig(openssl) >= 0.98

BuildRequires: pkgconfig(libevent) >= 2.0
BuildRequires: pkgconfig(glib-2.0) >= 2.16.0
BuildRequires: pkgconfig(gobject-2.0) >= 2.16.0
BuildRequires: pkgconfig(libsearpc) >= 1.0
BuildRequires: pkgconfig(jansson) >= 2.2.1
BuildRequires: pkgconfig(libcurl) >= 7.17
BuildRequires: pkgconfig(fuse) >= 2.7.3
BuildRequires: pkgconfig(zlib) >= 1.2.0
BuildRequires: pkgconfig(libwebsockets) >= 4.0.20

# FIXME: python3(seadrive.rpcclient)
%add_python3_req_skip rpcclient

%description
SeaDrive daemon with FUSE interface.

%package -n python3-module-seafile-fuse
Summary: Seafile fuse python3 module
Group: Networking/File transfer
Requires: %name = %EVR

%description -n python3-module-seafile-fuse
The python3 module with Seafile fuse.


%prep
%setup

%build
%autoreconf
%configure --disable-static --enable-ws
%make_build || %make

%install
%makeinstall_std

%files
%_bindir/seadrive

%files -n python3-module-seafile-fuse
%python3_sitelibdir/seadrive/


%changelog
* Mon Mar 04 2024 Vitaly Lipatov <lav@altlinux.ru> 2.0.28-alt1
- initial build for ALT Sisyphus
