# SPEC file for kpcli package

Name: kpcli
Version: 2.4
Release: alt1

Summary: command line interface to work with KeePass database files

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
BuildRequires: perl-File-KeePass perl-Term-ShellUI perl-Clone

%description
kpcli is a KeePass Command Line Interface (CLI) / interactive shell.

This program provides a way to access and manage KeePass 1.x and 2.x
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
* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.4-alt1
- New version

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.3-alt1
- New version

* Sat Jun 29 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.2-alt1
- New version

* Wed Jun 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.1-alt1
- New version

* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.7-alt1
- New version

* Tue Nov 27 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.6-alt1
- New version

* Sun Aug 26 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.4-alt1
- New version

* Sun May 29 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux Sisyphus

