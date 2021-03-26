Name: fatsort
Version: 1.6.3.622
Release: alt1
Summary: A command-line utilitiy that sorts directory structures of FAT12, FAT16 and FAT32 file systems
License: %pubdomain
Group: File tools

Packager: Anton Shevtsov <x09@altlinux.org>

Url: http://%name.sourceforge.net/
Source: https://sourceforge.net/projects/%name/files/%name-%version.tar.xz

BuildRequires(pre): rpm-build-licenses
BuildRequires: help2man

%description
FATSort is a small utilitiy for Linux that sorts directory structures of
FAT12, FAT16 and FAT32 file systems. It is written in C and can be run from
the command line.

%prep
%setup

%build
%make_build CFLAGS+='%optflags'

%install
%makeinstall_std SBINDIR=%_sbindir MANDIR=%_man1dir

%files
%_sbindir/%name
%_man1dir/%name.1.*

%changelog
* Fri Mar 26 2021 Slava Aseev <ptrnine@altlinux.org> 1.6.3.622-alt1
- Update to 1.6.3.622

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.2.439-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.2.439-alt2
- NMU: remove %ubt from release

* Wed Jan 17 2018 Anton Shevtsov <x09@altlinux.org> 1.4.2.439-alt1%ubt
- Initial build for ALT 
