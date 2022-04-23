Name: git-remote-gcrypt
Version: 1.4
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
BuildRequires: python3-module-docutils

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
rst2man README.rst > git-remote-gcrypt.1
install -d %buildroot%_man1dir
install -m 644 git-remote-gcrypt.1 %buildroot%_man1dir

%files
%_bindir/git-remote-gcrypt
%_man1dir/git-remote-gcrypt.1*

%changelog
* Sat Apr 23 2022 Pavel Nakonechnyi <zorg@altlinux.org> 1.4-alt1
- updated to 1.4 upstream version (minor fixes, rsync-related changes)
- require python3-module-docutils build dep explicitly

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- NMU: use rst2man.py from python3-module-docutils

* Sun Dec 16 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.2-alt1
- updated to 1.2 upstream version

* Fri Aug 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.3-alt3
- NMU: updated build dependencies and man page compression.

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
