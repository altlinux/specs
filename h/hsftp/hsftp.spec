Name: hsftp
Version: 1.15
Release: alt1

Summary: FTP-type client using SSH to transfer files
License: GPL
Group: Networking/File transfer

Url: http://la-samhna.de/hsftp
Source0: %name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

Requires: openssh-clients

# Automatically added by buildreq on Tue Dec 06 2005
BuildRequires: groff-base libncurses-devel libtinfo-devel

%description
hsftp is an FTP emulator that provides the look and feel of an FTP session,
but uses ssh to transport commands and data.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

# TODO:
# - control(8) support (root privileges are needed 
#   to avoid swapping out if using/caching password;
#   considered harmful though, 1.11 had a hole)

%files
%doc readme license hsftp.lsm
%_bindir/*
%_man1dir/*

%changelog
* Tue Dec 06 2005 Michael Shigorin <mike@altlinux.org> 1.15-alt1
- built for ALT Linux

* Thu Jan 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.15-1mdk
- 1.15

* Wed Dec 10 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.13-1mdk
- 1.13

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.11-5mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.11-4mdk
- rebuild

* Tue Jul 31 2001  Lenny Cartier <lenny@mandrakesoft.com> 1.11-3mdk
- rebuild

* Thu Jan 11 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.11-2mdk
- rebuild

* Mon Nov 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.11-1mdk
- updated to 1.11

* Mon Nov 13 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.10-1mdk
- updated to 1.10

* Thu Oct 19 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.9-2mdk
- requires openssh-clients

* Wed Oct 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.9-1mdk
- used srpm from rufus t firefly <rufus.t.firefly@linux-mandrake.com> :
	v1.9
	added prefix
	changed group
	stripped binaries and bzip'd man pages
- macros
- clean spec

* Thu May 04 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com> 1.7-1mdk
  - v1.7

* Tue May 02 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com> 1.6-1mdk
  - v1.6

* Tue Apr 18 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com> 1.5-1mdk
  - v1.5 (updated from freshmeat)
  - moved to .tar.bz2 archive

* Thu Mar 30 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com> 1.4-1mdk
  - new spec file
