Name: jdupes
Version: 1.27.3
Release: alt1

Summary: A powerful duplicate file finder and an enhanced fork of 'fdupes'

License: %mit
Group: File tools
Url: https://github.com/jbruchon/jdupes

# Source-url: https://github.com/jbruchon/jdupes/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildRequires: libjodycode-devel

%description
jdupes is a program for identifying and taking actions upon duplicate
files.

A WORD OF WARNING: jdupes IS NOT a drop-in compatible replacement for
fdupes! Do not blindly replace fdupes with jdupes in scripts and expect
everything to work the same way. Option availability and meanings differ
between the two programs. For example, the -I switch in jdupes means
"isolate" and blocks intra-argument matching, while in fdupes it means
"immediately delete files during scanning without prompting the user."

%prep
%setup

%build
%add_optflags -DENABLE_DEDUPE=1
%make_build CFLAGS_EXTRA="%optflags"

%install
%makeinstall_std PREFIX=%prefix MAN_BASE_DIR=%_mandir

%check
./jdupes testdir
./jdupes -r testdir

%files
%doc CHANGES.txt README.md
%_bindir/*
%_man1dir/*

%changelog
* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1.27.3-alt1
- new version 1.27.3 (with rpmrb script)

* Tue Aug 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1.26.1-alt1
- new version 1.26.1 (with rpmrb script)
- add BR: libjodycode-devel

* Tue Jun 27 2023 Ildar Mulyukov <ildar@altlinux.ru> 1.21.3-alt2
- ENABLE_DEDUPE

* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1.21.3-alt1
- new version 1.21.3 (with rpmrb script)

* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 1.21.1-alt1
- new version 1.21.1 (with rpmrb script)

* Sat Sep 10 2022 Vitaly Lipatov <lav@altlinux.ru> 1.21.0-alt1
- new version 1.21.0 (with rpmrb script)

* Mon Jan 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1.20.2-alt1
- new version 1.20.2 (with rpmrb script)

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1.20.0-alt1
- new version 1.20.0 (with rpmrb script)

* Sat Mar 30 2019 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- initial build for ALT Sisyphus


