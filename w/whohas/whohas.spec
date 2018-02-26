Name: whohas
Version: 0.29
Release: alt1

Summary: Command line tool for query package lists

Group: File tools
License: GPLv2+
Url: http://www.philippwesche.org/200811/whohas/intro.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.philippwesche.org/200811/%name/%name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 07 2009 (-bi)
BuildRequires: perl-libwww perl-threads

%description
whohas is a command line tool that allows querying several package
lists at once - currently supported are Arch, Debian, Gentoo and
Slackware. whohas is written in Perl and was designed to help
package maintainers find ebuilds, pkgbuilds and similar package
definitions from other distributions to learn from.

%prep
%setup -q
chmod a-x Changelog intro.* html_assets/*

%install
install -Dp -m 0755 program/%name %buildroot%_bindir/%name
install -Dp -m 0644 usr/share/man/man1/%name.1 %buildroot%_man1dir/%name.1

%files
%doc Changelog intro.txt intro.html html_assets/
%_bindir/%name
%_man1dir/%name.*

%changelog
* Mon Jan 16 2012 Vitaly Lipatov <lav@altlinux.ru> 0.29-alt1
- new version 0.29 (with rpmrb script)

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.24-alt1
- new version 0.24 (with rpmrb script)

* Wed Oct 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.23-alt1
- initial build for ALT Linux Sisyphus

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 05 2009 Fabian Affolter <fabian@bernewireless.net> - 0.23-1
- Updated to new upstream version 0.23

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 30 2009 Fabian Affolter <fabian@bernewireless.net> - 0.22-2
- License is GPLv2+ not GPLv2
- Fixed requirements

* Sat Jan 30 2009 Fabian Affolter <fabian@bernewireless.net> - 0.22-1
- Initial package for Fedora
