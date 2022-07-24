%define _unpackaged_files_terminate_build 1

%def_disable static

Name: ykclient
Version: 2.15
Release: alt3

Summary: YubiCloud One-Time-Password Validation Client
License: BSD-2-Clause
Group: System/Configuration/Hardware
Url: https://github.com/Yubico/yubico-c-client

Source: %name-%version.tar

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libcurl-devel
BuildRequires: libtool
BuildRequires: help2man

Requires: libykclient = %EVR

%description
%summary

%package -n libykclient
Summary: Yubico C client library
Group: Development/Other

%description -n libykclient
A C library used to validate an Yubikey OTP against Yubico's servers.

%package -n libykclient-devel
Summary: Yubico C client library development files
Group: Development/Other
Requires: libykclient = %EVR

%description -n libykclient-devel
Development files for libykclient library.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%files -n libykclient
%_libdir/*so*

%files -n libykclient-devel
%_includedir/*

%changelog
* Sun Jul 24 2022 Anton Zhukharev <ancieg@altlinux.org> 2.15-alt3
- bump release to override autoimports package

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 2.15-alt1
- initial build for Sisyphus
