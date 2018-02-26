%define remoteversion 100

Name: gkermit
Version: 1.00
Release: alt1

Summary: Transfer files with the Kermit protocol

License: GPL
Group: Networking/File transfer
Url: http://www.columbia.edu/kermit/gkermit.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://kermit.columbia.edu/kermit/archives/gku%remoteversion.tar.bz2
Patch: gkermit-missing-errno-include.patch.bz2

%description
gkermit is a GPL'd implementation of the Kermit protocol, developed by
Columbia University.  Kermit is often used to transfer files over serial
connections as well as through networks.  This version is quite minimal;
support for non-Kermit protocols may be found in ckermit, which is not,
unfortunately, Free Software. See the gkermit webpage for more information.

gkermit is a command line, non-interactive client.

%prep
%setup
%patch0 -p1

%build
%make_build
bzip2 -f gkermit.nr

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
cp gkermit %buildroot%_bindir/
cp gkermit.nr.bz2 %buildroot%_man1dir/gkermit.1.bz2

%files
%doc ANNOUNCE COPYING README
%_bindir/gkermit
%_man1dir/*

%changelog
* Fri Jul 25 2008 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt1
- initial build for ALT Linux Sisyphus

* Sun May 06 2007 Lenny Cartier <lenny@mandriva.com> 1.00-5mdv2008.0
+ Revision: 23778
- Fix filelist
- Fix manpage name (Bug #16555)
- Import gkermit

* Thu Dec 05 2006 Lenny Cartier <lenny@mandriva.com> 1.00-3mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.00-2mdk
- rebuild

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.00-1mdk
- from Levi Ramsey <leviramsey@linux-mandrake.com> :
	- Initial Cooker contrib
	- Contents of tarball moved to gkermit-1.00/
- add errno-missing-include.patch
