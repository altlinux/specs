Name:    git-crypt
Version: 0.6.0.11.g1c905fa
Release: alt1

Summary: Transparent file encryption in git
Url:     https://github.com/AGWA/git-crypt
Group:   Development/Other
License: GPL3

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar

BuildRequires: libssl-devel gcc-c++ xsltproc docbook-style-xsl

%description
The %name enables transparent encryption and decryption of files in a git
repository.  Files which you choose to protect are encrypted when committed, and
decrypted when checked out. %name lets you freely share a repository containing
a mix of public and private content.  name gracefully degrades, so developers
without the secret key can still clone and commit to a repository with
encrypted files. This lets you store your secret material (such as keys or
passwords) in the same repository as your code, without requiring you to lock
down your entire repository.

%prep
%setup -q

%build
%make_build \
	PREFIX=%_prefix \
	ENABLE_MAN=yes

%install
%makeinstall_std \
	PREFIX=%_prefix \
	ENABLE_MAN=yes

%files
%_bindir/*
%_man1dir/*

%changelog
* Mon Jan 17 2022 Alexey Gladkov <legion@altlinux.ru> 0.6.0.11.g1c905fa-alt1
- Upstream snapshot.
- Build with OpenSSL.

* Sat Jun 09 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6.0-alt1.1
- Rebuilt against libtls17.

* Mon Mar 05 2018 Alexey Gladkov <legion@altlinux.ru> 0.6.0-alt1
- First build.
