%global _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name:		fscrypt
Version:	0.3.4
Release:	alt1
Summary:	A high-level tool for the management of Linux kernel filesystem encryption

Group:		System/Kernel and hardware
License:	Apache-2.0
URL:		https://github.com/google/fscrypt

Source:     %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: libpam0-devel
# older cgo versions can't handle LTO
BuildRequires: golang >= 1.17
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm e2fsprogs expect keyutils}}

%description
Fscrypt is a high-level tool for the management of Linux filesystem
encryption (https://www.kernel.org/doc/html/latest/filesystems/fscrypt.html).
Fscrypt manages metadata, key generation, key wrapping, PAM integration, and
provides a uniform interface for creating and modifying encrypted directories.

%prep
%setup

# Delete -trimpath from GO_FLAGS or else we'll miss .go sources from
# debuginfo.
sed -i '/-trimpath/d' Makefile

%build
%make_build \
    CFLAGS="%optflags" \
    GO_FLAGS="-mod=vendor -buildmode=pie -x" \
    GO_LINK_FLAGS="" \
    TAG_VERSION="v%version-%release"

%install
%makeinstall_std \
    PREFIX="/usr" \
    PAM_MODULE_DIR="/%_lib/security"
rm -r %buildroot/%_datadir/pam-configs
install -Dm0644 .gear/%name.pam %buildroot%_sysconfdir/pam.d/%name

%check
sed -i 's/go test /\0 -mod=vendor /' Makefile
vm-run --kvm=cond --sbin --user --udevd \
	make test-setup test test-teardown

%files
%_bindir/%name
/%_lib/security/*.so
%_datadir/bash-completion/completions/%name
%_sysconfdir/pam.d/%name
%doc *.md

%changelog
* Mon Jun 05 2023 Vitaly Chikunov <vt@altlinux.org> 0.3.4-alt1
- Update to v0.3.4 (2023-01-30). (Fixes: CVE-2022-25326, CVE-2022-25327,
  CVE-2022-25328).

* Fri Nov 11 2022 Vitaly Chikunov <vt@altlinux.org> 0.3.1.0.2.360467d-alt2
- Unimportant update to simplify %%check.

* Wed Dec 01 2021 Andrew Savchenko <bircoph@altlinux.org> 0.3.1.0.2.360467d-alt1
- Version bump.
- Enable LTO with fixed cgo in golang >= 1.17.

* Sun Sep 12 2021 Andrew Savchenko <bircoph@altlinux.org> 0.3.0.0.5.e479779-alt2
- Fix build after LTO enforement: disable LTO for now due to golang < 1.17 bug.

* Fri May 14 2021 Vitaly Chikunov <vt@altlinux.org> 0.3.0.0.5.e479779-alt1
- Run tests in %%check.

* Fri May 07 2021 Andrew Savchenko <bircoph@altlinux.org> 0.3.0.0.4.677ae75-alt1
- Initial version
