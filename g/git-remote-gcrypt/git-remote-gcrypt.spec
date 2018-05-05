Name: git-remote-gcrypt
Version: 1.0.3
Release: alt2

Summary: A git remote helper for GPG-encrypted remotes
License: GPLv2+
Group: Development/Tools

Url: https://github.com/spwhitton/git-remote-gcrypt.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Pavel Nakonechnyi <zorg@altlinux.org>

Provides: git-remote-gcrypt

BuildArch: noarch
BuildRequires: python-module-docutils-compat

%description
This lets git store git repositories in encrypted form.
It supports storing repositories on rsync or sftp servers.
It can also store the encrypted git repository inside a remote git
repository. All the regular git commands like git push and git pull
can be used to operate on such an encrypted repository.

The aim is to provide confidential, authenticated git storage and
collaboration using typical untrusted file hosts or services.

%prep
%setup
%patch -p1

%install
install -d %buildroot%_bindir
install -m 755 git-remote-gcrypt %buildroot%_bindir
rst2man README.rst | gzip -9 > git-remote-gcrypt.1.gz
install -d %buildroot%_man1dir
install -m 644 git-remote-gcrypt.1.gz %buildroot%_man1dir

%files
%_bindir/git-remote-gcrypt
%_man1dir/git-remote-gcrypt*

%changelog
* Sat May 05 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.0.3-alt2
- fix temporary directory creation

* Sat Apr 21 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.0.3-alt1
- updated to 1.0.3 upstream version

* Sat Sep 16 2017 Pavel Nakonechnyi <zorg@altlinux.org> 1.0.2-alt1
- updated to 1.0.2 upstream version
- minor changes, but important updates in documentation

* Wed Dec 28 2016 Pavel Nakonechnyi <zorg@altlinux.org> 1.0.0-alt1
- initial build, based on tag 1.0.0 of https://github.com/spwhitton/git-remote-gcrypt.git repo
- store temp files under system's $TMPDIR
