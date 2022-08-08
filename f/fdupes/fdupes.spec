Name: fdupes
Version: 2.1.2
Epoch: 1
Release: alt1

Summary: Identifies duplicate files within given directories

License: MIT
Group: File tools
Url: https://github.com/adrianlopezroche/fdupes

# Source-url: https://github.com/adrianlopezroche/fdupes/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: libncursesw-devel libpcre2-devel

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
./fdupes testdir
./fdupes -r testdir

%files
%doc CHANGES CONTRIBUTORS README
%_bindir/*
%_man1dir/*
%_man7dir/*

%changelog
* Mon Aug 08 2022 Vitaly Lipatov <lav@altlinux.ru> 1:2.1.2-alt1
- new version 2.1.2 (with rpmrb script)
- switch to autoconf/automake
- change Url

* Sat Mar 30 2019 Vitaly Lipatov <lav@altlinux.ru> 1:1.6.1-alt1
- new version 1.6.1 (with rpmrb script)

* Sun Aug 16 2015 Vitaly Lipatov <lav@altlinux.ru> 1.51-alt1
- new version 1.51 (with rpmrb script)
- add check section, do not pack tests

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.40-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Oct 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.40-alt2
- fixed manpage name (#17404)

* Sun Aug 26 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.40-alt1
- initial build for Sisyphus


