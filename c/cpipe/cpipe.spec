Name: cpipe
Version: 3.0.2
Release: alt1

Summary: Counting pipe
Group: Development/Tools
License: GPLv2+

Url: http://cpipe.berlios.de/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.berlios.de/%name/%name-%version.tar
Patch: cpipe-lib.patch

%description
Cpipe copies its standard input to its standard output while measuring
the time it takes to read an input buffer and write an output
buffer. Statistics of average throughput and the total amount of bytes
copied are printed to the standard error output.

%prep
%setup
%patch -p2

%build
# Use included filess
touch cmdline.c cmdline.h cpipe.1
%make_build CFLAGS='%optflags'

%install
%make_install install \
    BINDIR=%buildroot%_bindir \
    MANDIR=%buildroot%_man1dir
chmod 0644 %buildroot%_man1dir/%{name}*

%files
%doc CHANGES COPYING-2.0 README
%_bindir/%name
%_man1dir/*

%changelog
* Tue Mar 30 2010 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1
- new version 3.0.2 (with rpmrb script)

* Tue Mar 30 2010 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- initial build for ALT Linux Sisyphus

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  9 2008 Terje Rosten <terje.rosten@ntnu.no> - 3.0.1-3
- rebuild

* Wed Jan 23 2008 Terje Rosten <terje.rosten@ntnu.no> - 3.0.1-2
- rebuild

* Sun Jan  6 2008 Terje Rosten <terje.rosten@ntnu.no> - 3.0.1-1
- initial package
