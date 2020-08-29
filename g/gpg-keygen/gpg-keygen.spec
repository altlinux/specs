Name: gpg-keygen
Version: 20190611
Release: alt1

Summary: Generate a new GPG key pair exported in a file

License: MIT
Group: Text tools
# VCS: https://gist.github.com/8dc567ed4d7b4585111996242aa573a8.git
Url: https://gist.github.com/jirutka/8dc567ed4d7b4585111996242aa573a8

Requires: /usr/bin/gpg2

Source: %name-%version.tar

BuildArch: noarch

%description
Generate a new GPG key pair in a temporary GPG Home and export it to a file.
It can run completely unattended, without prompting for a passphrase.

%prep
%setup


%install
install -p -m0755 gpg-keygen -D -t %buildroot%_bindir

%files
%_bindir/*
%doc LICENSE

%package checkinstall
%global checkinstall_summary Run a test of %name immediately on installation
Summary: %checkinstall_summary
Group: Development/Other
Requires(pre): %name
Requires(pre): /usr/bin/gpg

%description checkinstall
%checkinstall_summary.

%files checkinstall

%pre checkinstall -p /usr/sbin/sh-safely
set -x
keyid="$(gpg-keygen --passphrase '' seckey.asc pubkey.asc)"
readonly keyid

pwd >test.txt
gpg --import seckey.asc
gpg --default-key "$keyid" --detach-sign test.txt

gpg --import pubkey.asc
gpg --verify test.txt.sig test.txt

%changelog
* Wed Jul 29 2020 Ivan Zakharyaschev <imz@altlinux.org> 20190611-alt1
- Initial build for ALT Linux Sisyphus (from a gist by Jakub Jirutka).
- Enable creation of an unprotected key (if -p or $GPG_PASSPHRASE is empty).
