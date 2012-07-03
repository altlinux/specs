Name: whatmask
Version: 1.2
Release: alt2

Summary: Whatmask - Convert between different netmask types and display helpful network information
License: GPL
Group: Networking/Other
Source: http://downloads.laffeycomputer.com/current_builds/%name/%name-%version.tar.gz
URL: http://www.laffeycomputer.com/wm.html

Packager: Igor Zubkov <icesik@altlinux.org>

%description
Whatmask is a small C program that will help you with network settings.

It can analyze CIDR, netmask, netmask (hex), and wildcard bit notations to 
give useful information about the network block in question.

%prep
%setup -q
%configure

%build
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%_bindir/whatmask
%_man1dir/whatmask.*

%changelog
* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 1.2-alt2
- add Packager tag

* Wed Jan 18 2006 Igor Zubkov <icesik@altlinux.ru> 1.2-alt1
- Initial build for Sisyphus

* Wed Dec 10 2003 Joe Laffey <software@laffeycomputer.com>
- Upgraded to version 1.2 with incorporated manpage.

* Sat Nov 30 2002 Tim Jackson <tim@timj.co.uk>
- Adjusted packaging; can build as non-root and does not overwrite
  system files whilst building

* Thu Sep 13 2001 Joe Laffey <software@laffeycomputer.com>
- Upgraded to version 1.1.

* Thu Jul 05 2001 Joe Laffey <software@laffeycomputer.com>
- Initial RPM packaging
