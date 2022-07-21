%define _unpackaged_files_terminate_build 1

%def_disable static

Name: ykpers
Version: 1.20.0
Release: alt2

Summary: A library and command line tool used to personalize YubiKeys
License: BSD-2-Clause
Group: System/Configuration/Hardware
Url: https://github.com/Yubico/yubikey-personalization

Source: %name-%version.tar
Patch0: ykpers-1.20.0-alt-make-header-declarations-extern.patch
Patch1: ykpers-1.20.0-alt-fix-boolean-value-with-json-c.patch

BuildRequires: pkg-config
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libyubikey-devel
BuildRequires: libusb-devel
BuildRequires: libjson-c-devel
BuildRequires: asciidoc
BuildRequires: asciidoc-a2x
BuildRequires: xsltproc
BuildRequires: docbook-style-xsl

Requires: libykpers-1 = %EVR

%description
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

%package -n libykpers-1
Summary: A library used to personalize YubiKeys.
Group: Development/Other

%description -n libykpers-1
This package contains ykpers-1 library.

%package -n libykpers-1-devel
Summary: Development files for libykpers-1 library.
Group: Development/Other
Requires: libykpers-1 = %EVR

%description -n libykpers-1-devel
This package contains headers files for ykpers-1 library.

%prep
%setup
%patch0 -p 1
%patch1 -p 1

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_udevrulesdir/

install -p 69-yubikey.rules %buildroot%_udevrulesdir/
install -p 70-yubikey.rules %buildroot%_udevrulesdir/

cat << EOF >> %buildroot%_udevrulesdir/75-yubikey.rules
#udev rule for allowing HID access to Yubico devices for FIDO support.

KERNEL=="hidraw*", SUBSYSTEM=="hidraw", \
  MODE="0664", GROUP="plugdev", ATTRS{idVendor}=="1050"
EOF

%check
%make check

%files -n libykpers-1
%_libdir/*so*

%files -n libykpers-1-devel
%_includedir/ykpers-1/*
%_pkgconfigdir/*

%files -n %name
%doc AUTHORS BLURB COPYING NEWS README
%_bindir/*
%_man1dir/*
%attr(0644,root,root) %_udevrulesdir/*

%changelog
* Thu Jul 21 2022 Anton Zhukharev <ancieg@altlinux.org> 1.20.0-alt2
- add make check

* Thu Jun 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.20.0-alt1
- initial build for Sisyphus
