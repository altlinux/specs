# SPEC file for kpcli package

Name: kpcli
Version: 3.8.1
Release: alt2

Summary: command line interface to work with KeePass database files

License: %perl_license
Group: Networking/Other
URL: http://sourceforge.net/projects/kpcli/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Jan 15 2023
# optimized out: libgpg-error perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-parent perl-podlators python-modules python2-base python3-base sh4
BuildRequires: perl-Pod-Usage perl-podlators perl-devel perl-diagnostics

BuildRequires: perl-Crypt-Rijndael perl-Sort-Naturally perl-Term-ReadKey
BuildRequires: perl-File-KeePass perl-Term-ShellUI perl-Clone perl-Time-Piece
BuildRequires: perl-Module-Loaded

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
%doc README.md

%_bindir/%name
%_man1dir/%{name}*

%changelog
* Sun Jun 02 2024 Nikolay A. Fetisov <naf@altlinux.org> 3.8.1-alt2
- Update BuildRequires

* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 3.8.1-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.6-alt1
- New version

* Sun May 17 2020 Nikolay A. Fetisov <naf@altlinux.org> 3.4-alt1
- New version

* Sat Aug 17 2019 Nikolay A. Fetisov <naf@altlinux.org> 3.3-alt1
- New version

* Sat Dec 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.2-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 3.1-alt1
- New version

* Tue Aug 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0-alt1
- New version

* Sun Jun 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.8-alt1
- New version

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.7-alt1
- New version

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

