Name: git-remote-gcrypt
Version: 1.0.0
Release: alt1

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
* Wed Dec 28 2016 Pavel Nakonechnyi <zorg@altlinux.org> 1.0.0-alt1
- initial build, based on tag 1.0.0 of https://github.com/spwhitton/git-remote-gcrypt.git repo
- store temp files under system's $TMPDIR
