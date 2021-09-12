%global _unpackaged_files_terminate_build 1

Name:		fscrypt
Version:	0.3.0.0.5.e479779
Release:	alt2
Summary:	A high-level tool for the management of Linux kernel filesystem encryption

Group:		System/Kernel and hardware
License:	Apache-2.0
URL:		https://github.com/google/fscrypt

Source:     %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: libpam0-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm e2fsprogs expect keyutils}}

# cgo can't handle LTO till golang 1.17
# https://github.com/golang/go/commit/24e9707cbfa6b1ed6abdd4b11f9ddaf3aac5ad88
%define optflags_lto %nil

%description
Fscrypt is a high-level tool for the management of Linux filesystem
encryption (https://www.kernel.org/doc/html/latest/filesystems/fscrypt.html).
Fscrypt manages metadata, key generation, key wrapping, PAM integration, and
provides a uniform interface for creating and modifying encrypted directories.

%prep
%setup -q

%build
%make_build \
    CFLAGS="%optflags" \
    GO_FLAGS="-mod=vendor" \
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
mkdir -p /usr/src/bin
ln -sf /usr/bin/time /usr/src/bin/sudo
vm-run --kvm=cond --sbin --udevd \
	make test-setup test test-teardown

%files
%_bindir/%name
/%_lib/security/*.so
%_datadir/bash-completion/completions/%name
%_sysconfdir/pam.d/%name
%doc *.md

%changelog
* Sun Sep 12 2021 Andrew Savchenko <bircoph@altlinux.org> 0.3.0.0.5.e479779-alt2
- Fix build after LTO enforement: disable LTO for now due to golang < 1.17 bug.

* Fri May 14 2021 Vitaly Chikunov <vt@altlinux.org> 0.3.0.0.5.e479779-alt1
- Run tests in %%check.

* Fri May 07 2021 Andrew Savchenko <bircoph@altlinux.org> 0.3.0.0.4.677ae75-alt1
- Initial version
