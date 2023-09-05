%define _unpackaged_files_terminate_build 1
%def_without selinux
%def_with gnutls
%def_with openssl
%def_without cuse
%define _localstatedir %_var
%def_disable check

Name: swtpm
Version: 0.8.1
Release: alt1

Summary: TPM Emulator
License: BSD
Group: System/Configuration/Other
Url: https://github.com/stefanberger/swtpm
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%{?_with_selinux:BuildRequires: selinux-policy-devel}
%{?_with_openssl:BuildRequires: libssl-devel pkgconfig(libcrypto)}
BuildRequires: pkgconfig(libtasn1)
BuildRequires: pkgconfig(libtpms) >= 0.6.0
BuildRequires: trousers >= 0.3.9
%{?_with_cuse:BuildRequires: pkgconfig(fuse)}
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gthread-2.0)
%{?_with_gnutls:BuildRequires: pkgconfig(gnutls) /usr/bin/certtool}
BuildRequires: /usr/bin/ss
BuildRequires: expect socat gawk coreutils
BuildRequires: socat
BuildRequires: softhsm
BuildRequires: libseccomp-devel
BuildRequires: tpm2-pkcs11 tpm2-pkcs11-tools tpm2-tools tpm2-abrmd
BuildRequires: /usr/bin/pod2man
%{!?_disable_check:BuildRequires: /proc /dev/pts}

Requires: lib%name = %EVR
Requires: libtpms >= 0.6.0

%description
TPM emulator built on libtpms providing TPM functionality for QEMU VMs

%package -n lib%name
Summary: Private libraries for swtpm TPM emulators
Group: System/Libraries
License: BSD

%description -n lib%name
A private library with callback functions for libtpms based swtpm TPM emulator

%package -n lib%name-devel
Summary: Include files for the TPM emulator's CUSE interface for usage by clients
License: BSD
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Include files for the TPM emulator's CUSE interface.

%package tools
Summary: Tools for the TPM emulator
Group: System/Configuration/Other
License: BSD
Requires: %name = %EVR
Requires: trousers >= 0.3.9 gnutls-utils
# For tss user and group
Requires(pre): libtpm2-tss-common

%description tools
Tools for the TPM emulator from the swtpm package

%package tools-pkcs11
Summary: Tools for creating a local CA based on a pkcs11 device
Group: System/Configuration/Other
License: BSD
Requires: %name-tools = %EVR
Requires: tpm2-pkcs11 tpm2-pkcs11-tools tpm2-tools tpm2-abrmd
Requires: expect

%description tools-pkcs11
Tools for creating a local CA based on a pkcs11 device

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    %{subst_with selinux} \
    %{subst_with openssl} \
    %{subst_with gnutls} \
    %{subst_with cuse} \
    --disable-static

%make_build

%install
%makeinstall_std
rm -f $RPM_BUILD_ROOT%_libdir/%name/*.{a,la}

%check
%make check

%if_with selinux
%post
for pp in /usr/share/selinux/packages/swtpm.pp \
          /usr/share/selinux/packages/swtpm_svirt.pp; do
  %selinux_modules_install -s %selinuxtype ${pp}
done

%postun
if [ $1 -eq  0 ]; then
  for p in swtpm swtpm_svirt; do
    %selinux_modules_uninstall -s %selinuxtype $p
  done
fi
%endif

%files
%doc README LICENSE
%_bindir/swtpm
%_man8dir/swtpm.8*
%if_with selinux
%_datadir/selinux/packages/swtpm.pp
%_datadir/selinux/packages/swtpm_svirt.pp
%endif

%files -n lib%name
%dir %_libdir/%name
%_libdir/%name/*.so.*

%files -n lib%name-devel
%_libdir/%name/*.so
%_includedir/*
%_man3dir/*

%files tools
%doc README
%_bindir/*
%exclude %_bindir/swtpm
%_man5dir/*
%_man8dir/*
%exclude %_man8dir/swtpm.8*
%exclude %_man8dir/swtpm-create-tpmca.8*
%config(noreplace) %_sysconfdir/swtpm_setup.conf
%config(noreplace) %_sysconfdir/swtpm-localca.options
%config(noreplace) %_sysconfdir/swtpm-localca.conf
%dir %_datadir/swtpm
%_datadir/swtpm/swtpm-localca
%_datadir/swtpm/swtpm-create-user-config-files
%attr( 770, root, tss) %_localstatedir/lib/swtpm-localca

%files tools-pkcs11
%_man8dir/swtpm-create-tpmca.8*
%_datadir/swtpm/swtpm-create-tpmca

%changelog
* Tue Sep 05 2023 Alexey Shabalin <shaba@altlinux.org> 0.8.1-alt1
- New version 0.8.1.

* Sat May 27 2023 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- new version 0.8.0

* Thu Mar 24 2022 Alexey Shabalin <shaba@altlinux.org> 0.7.2-alt1
- new version 0.7.2 (Fixes: CVE-2022-23645)

* Thu Dec 02 2021 Alexey Shabalin <shaba@altlinux.org> 0.7.0-alt1
- new version 0.7.0

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.1-alt1
- new version 0.6.1

* Fri Aug 27 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.0-alt1
- Initial build.

