Name: keyringer
Version: 0.5.3
Release: alt1

Summary: Encrypted and distributed secret sharing software

Group: File tools
License: GPLv2
Url: https://keyringer.pw/

BuildArch: noarch

# Source-git: git://git.fluxo.info/keyringer.git
Source: %name-%version.tar

%description
Keyringer: encrypted and distributed secret sharing software.

Keyringer lets you manage and share secrets using GnuPG and Git
with custom commands to encrypt, decrypt, recrypt, create key pairs, etc.

%prep
%setup
%__subst "s@/lib/@/share/@g" Makefile keyringer
# hack to skip qdbus requires
%__subst "s@qdbus @a= qdbus @g" lib/keyringer/actions/xclip

%build

%install
%makeinstall_std PREFIX=%prefix

%files
%_bindir/%name
%_docdir/*
%_man1dir/*
%_datadir/%name/
%_datadir/bash-completion/completions/%name
%_datadir/zsh/vendor-completions/_keyringer

%changelog
* Tue Dec 25 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.3-alt1
- new version 0.5.3 (with rpmrb script)

* Thu Mar 01 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- build new version

* Wed Aug 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt1
- initial build for ALT Linux Sisyphus
