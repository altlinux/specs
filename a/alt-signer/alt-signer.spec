Name: alt-signer
Version: 1.1
Release: alt1

Summary: A service for remote kernel module signing
License: GPL-2.0-or-later
Group: System/Servers

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
This package contains constrained shells and helper scripts for operating a
pesign keyring with dedicated service accounts.  The keyring shell provisions
and rotates NSS certificates in /var/lib/alt-signer, while the signer shell
streams payloads through pesign.

%prep
%setup

%build
%meson
%meson_build -v

%install
%meson_install

%define _unpackaged_files_terminate_build 1
%set_verify_elf_method strict

%pre
%_sbindir/groupadd -r -f alt-signer
%_sbindir/useradd -r -g alt-signer -G pesign -d /var/empty -s %_libexecdir/alt-signer/alt-signer-sh -c "alt-signer user" -n alt-signer ||:
%_sbindir/groupadd -r -f alt-signer-keyring
%_sbindir/useradd -r -g alt-signer-keyring -d /var/lib/alt-signer -s %_libexecdir/alt-signer/alt-signer-keyring-sh -c "alt-signer keyring" -n alt-signer-keyring ||:

%files
%doc docs/ADMIN.md
%_sbindir/alt-signer-keyring-init
%_libexecdir/alt-signer
%dir %attr(750,alt-signer-keyring,pesign) %_sharedstatedir/alt-signer
%dir %attr(755,root,root) /etc/alt-signer
%config(noreplace) %attr(644,root,root) /etc/alt-signer/config
%config(noreplace) %attr(640,root,alt-signer) /etc/openssh/authorized_keys/alt-signer
%config(noreplace) %attr(640,root,alt-signer-keyring) /etc/openssh/authorized_keys/alt-signer-keyring

%changelog
* Tue Apr 21 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1-alt1
- Changed the keygen script to:
  + Generate RSA4096 keys;
  + Added O= and OU= fields to the default cert subject prefix.

* Thu Jan 22 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt1
- Initial build.
