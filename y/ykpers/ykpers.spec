%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
%add_optflags -ffat-lto-objects

%def_disable static

Name: ykpers
Version: 1.20.0
Release: alt3

Summary: A library and command line tool used to personalize YubiKeys
License: BSD-2-Clause
Group: System/Configuration/Hardware
Url: https://developers.yubico.com/yubikey-personalization/
Vcs: https://github.com/Yubico/yubikey-personalization

Source0: %name-%version.tar
Source1: 75-yubikey.rules
Patch0: ykpers-1.20.0-alt-make-header-declarations-extern.patch
Patch1: ykpers-1.20.0-alt-fix-boolean-value-with-json-c.patch

BuildRequires: libyubikey-devel
BuildRequires: libusb-devel
BuildRequires: libjson-c-devel
BuildRequires: libudev-devel
BuildRequires: asciidoc-a2x
BuildRequires: docbook-style-xsl

%description
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

%package -n libykpers-1
Summary: A library used to personalize YubiKeys
Group: Development/Other

%description -n libykpers-1
This package contains ykpers-1 library.

%package -n libykpers-1-devel
Summary: Development files for libykpers-1 library
Group: Development/Other

%description -n libykpers-1-devel
This package contains headers files for ykpers-1 library.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure \
    %{subst_enable static} \
    --with-udevrulesdir=%_udevrulesdir \
    %nil
%make_build

%install
%makeinstall_std

%__install -pD -m0644 %SOURCE1 %buildroot%_udevrulesdir/75-yubikey.rules

%check
%make check

%files
%doc AUTHORS COPYING NEWS README
%_bindir/yk*
%_man1dir/yk*.1.xz
%_udevrulesdir/*-yubikey.rules

%files -n libykpers-1
%_libdir/libykpers-1.so.*

%files -n libykpers-1-devel
%_libdir/libykpers-1.so
%_includedir/ykpers-1/
%_pkgconfigdir/ykpers-1.pc

%changelog
* Mon Oct 02 2023 Anton Zhukharev <ancieg@altlinux.org> 1.20.0-alt3
- Followed Shared Libs Policy draft.
- Stopped packaging BLURB file.
- Stopped packaging unused 70-yubikey.rules udev rules file.

* Thu Jul 21 2022 Anton Zhukharev <ancieg@altlinux.org> 1.20.0-alt2
- add make check

* Thu Jun 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.20.0-alt1
- initial build for Sisyphus
