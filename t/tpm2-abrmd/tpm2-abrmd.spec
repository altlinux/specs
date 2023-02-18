%define _unpackaged_files_terminate_build 1

Name: tpm2-abrmd
Version: 3.0.0
Release: alt1
Summary: A system daemon implementing TPM2 Access Broker and Resource Manager
Group: System/Servers
License: BSD
Url: https://github.com/tpm2-software/tpm2-abrmd
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-systemd
BuildRequires: autoconf-archive
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(tss2-mu)
BuildRequires: pkgconfig(tss2-sys) >= 2.4.0

BuildRequires: pkgconfig(cmocka)

%description
tpm2-abrmd is a system daemon implementing the TPM2 access broker (TAB) and
Resource Manager (RM) spec from the TCG.

%package devel
Summary: Headers, static libraries and package config files of tpm2-abrmd
Group: Development/C
Requires: %name = %EVR
# tpm2-abrmd-devel depends on tpm2-tss-devel for tss2-mu/sys libs
Requires: libtpm2-tss-devel >= 2.4.0

%description devel
This package contains headers, static libraries and package config files
required to build applications that use tpm2-abrmd.

%prep
%setup
%patch -p1
echo %version > VERSION

%build
%autoreconf
%configure --disable-static --disable-silent-rules \
           --with-systemdsystemunitdir=%_unitdir \
           --with-systemdpresetdir=%_presetdir \
           --with-dbuspolicydir=%_datadir/dbus-1/system.d/

%make_build

%install
%makeinstall_std
find %buildroot%_libdir -type f -name \*.la -delete
rm -f %buildroot%_presetdir/tpm2-abrmd.preset

%check
%make check

%post
%systemd_post tpm2-abrmd.service

%preun
%systemd_preun tpm2-abrmd.service

%postun
%systemd_postun tpm2-abrmd.service

%files
%doc LICENSE
%doc README.md CHANGELOG.md
%_libdir/libtss2-tcti-tabrmd.so.*
%_sbindir/tpm2-abrmd
%_datadir/dbus-1/system.d/tpm2-abrmd.conf
%_datadir/dbus-1/system-services/com.intel.tss2.Tabrmd.service
%_unitdir/tpm2-abrmd.service
%_mandir/man8/tpm2-abrmd.8*

%files devel
%_includedir/tss2/tss2-tcti-tabrmd.h
%_libdir/libtss2-tcti-tabrmd.so
%_libdir/pkgconfig/tss2-tcti-tabrmd.pc
%_mandir/man3/Tss2_Tcti_Tabrmd_Init.3*
%_mandir/man7/tss2-tcti-tabrmd.7*

%changelog
* Sat Feb 18 2023 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- new version 3.0.0

* Thu Mar 24 2022 Alexey Shabalin <shaba@altlinux.org> 2.4.1-alt1
- new version 2.4.1

* Sat Aug 28 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.0-alt1
- Initial build.

