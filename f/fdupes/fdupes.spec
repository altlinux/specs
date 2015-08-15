Name: fdupes
Version: 1.51
Release: alt1

Summary: Identifies duplicate files within given directories

License: %mit
Group: File tools
Url: http://netdial.caribe.net/~adrian2/fdupes.html

Packager: Artem Zolochevskiy <azol@altlinux.ru>

# Source-url: https://github.com/adrianlopezroche/fdupes/archive/fdupes-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories.

%prep
%setup

%build
%make_build

%install
%makeinstall PREFIX=%buildroot%prefix MAN_BASE_DIR=%buildroot%_mandir install

%check
./fdupes testdir
./fdupes -r testdir

%files
%doc CHANGES CONTRIBUTORS README TODO
%_bindir/*
%_man1dir/*

%changelog
* Sun Aug 16 2015 Vitaly Lipatov <lav@altlinux.ru> 1.51-alt1
- new version 1.51 (with rpmrb script)
- add check section, do not pack tests

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.40-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Oct 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.40-alt2
- fixed manpage name (#17404)

* Sun Aug 26 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.40-alt1
- initial build for Sisyphus


