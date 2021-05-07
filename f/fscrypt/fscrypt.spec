%global _unpackaged_files_terminate_build 1

Name:		fscrypt
Version:	0.3.0.0.4.677ae75
Release:	alt1
Summary:	A high-level tool for the management of Linux kernel filesystem encryption

Group:		System/Kernel and hardware
License:	Apache-2.0
URL:		https://github.com/google/fscrypt

Source:     %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: libpam0-devel

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

%files
%_bindir/%name
/%_lib/security/*.so
%_datadir/bash-completion/completions/%name
%_sysconfdir/pam.d/%name
%doc *.md

%changelog
* Fri May 07 2021 Andrew Savchenko <bircoph@altlinux.org> 0.3.0.0.4.677ae75-alt1
- Initial version
