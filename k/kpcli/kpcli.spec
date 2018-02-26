# SPEC file for kpcli package

Name: kpcli
Version: 1.0
Release: alt1

Summary: command line interface to work with KeePass 1.x database files

License: %perl_license
Group: Networking/Other
URL: http://sourceforge.net/projects/kpcli/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun May 29 2011
# optimized out: perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators
BuildRequires: perl-Pod-Parser

BuildRequires: perl-Crypt-Rijndael perl-Sort-Naturally perl-Term-ReadKey
BuildRequires: perl-File-KeePass perl-Term-ShellUI

%description
kpcli is a KeePass Command Line Interface (CLI) / interactive shell.

This program provides a way to access and manage KeePass 1.x
database from a Unix-like command line.

%prep
%setup

%build
/usr/bin/pod2man %name.pl %name.1

%install
mkdir -p -- %buildroot/%_bindir
install -m 0755 -- %name.pl %buildroot/%_bindir/%name

mkdir -p -- %buildroot/%_man1dir
install -m 0644 -- %name.1 %buildroot/%_man1dir/

%files
%doc README

%_bindir/%name
%_man1dir/%{name}*

%changelog
* Sun May 29 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux Sisyphus

