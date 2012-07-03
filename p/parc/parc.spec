# vim: set ft=spec: -*- rpm-spec -*-
# $Id: parc,v 1.3 2006/01/12 18:24:03 raorn Exp $

Name: parc
Version: 00.05.01
Release: alt1

Summary: Palm database archiver
Group: File tools
License: MPL
Url: http://www.djw.org/product/palm/par/

Source: %url/prc.tgz

%description
The %name utility creates and manipulates PalmOS database (.pdb)
and resource (.prc) files. %name is designed to be a Swiss army
knife for managing these files. It's a command line tool, and
not for the faint of heart, but it's very handy and replaces a
bunch of little utilities that you might otherwise use.

%prep
%setup -q -n prc
%__subst 's,\<par\>,parc,g' par.man
%__subst 's,\<PAR\>,PARC,g' par.man
# !!!ACHTUNG!!!
%__subst 's,\<par\>,parc,g' par.c

%build
%make_build CFLAGS="%optflags"

%install
%__install -m755 -p -D par %buildroot%_bindir/%name
%__install -m644 -p -D par.man %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Thu Jan 12 2006 Sir Raorn <raorn@altlinux.ru> 00.05.01-alt1
- Built for Sisyphus


