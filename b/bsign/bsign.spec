Name: bsign
Version: 0.4.5
Release: alt3

Summary: Embed hash and signature in elf executables

License: GPL
Group: File tools
Url: https://launchpad.net/ubuntu/+source/bsign

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildPreReq: libstdc++-devel-static
BuildRequires: libatomic-devel-static

BuildRequires: gcc-c++

%description
This package embeds secure hashes (SHA1) and digital signatures (GNU
Privacy Guard) into files for verification and authentication.
Currently, target file types are all ELF format: executables, kernel
modules, shared and static link libraries. This program has
functionality similar to tripwire and integrit without the need to
maintain a database.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
mkdir %buildroot
%makeinstall

%files
%doc README NOTES TODO
%_bindir/%name
%_man1dir/*
%doc %_docdir/%name/

%changelog
* Wed Nov 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt3
- fix static build with GCC 16: add BuildRequires: libatomic-devel-static

* Thu Feb 21 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt2
- fix build

* Mon Feb 24 2014 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt1
- initial build for ALT Linux Sisyphus
