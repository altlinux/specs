Name: lbdb
Version: 0.38
Release: alt1

Summary: The Little Brother's Database
License: GPLv2+
Group: Databases

Url: http://www.spinnaker.de/lbdb
Source: http://www.spinnaker.de/debian/lbdb_%version.tar.gz
Patch: lbdb-sample.lbdbrc.patch
Patch1: lbdb-muttalias.patch
Patch2: lbdb-0.38-evolution.patch

# Automatically added by buildreq on Fri May 21 2010
BuildRequires: abook finger gnupg perl-ldap perl-p5-Palm

# ... not detectable by buildreq:
BuildRequires: evolution
# We prefer not to depend on mawk...
BuildConflicts: mawk
BuildRequires: perl-Pod-Parser

%description
Lbdbq is the client program for the little brother's database. It will
attempt to invoke various modules to gather information about persons
matching something. E.g., it may look at a list of addresses from which
you have received mail, it may look at YP maps, or it may try to finger
something@<various hosts>.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1

%build
%configure --libdir=%_libdir/lbdb --with-evolution-addressbook-export=auto
%make_build

%install
%makeinstall libdir=%buildroot/%_libdir/lbdb

%files
%doc README sample.lbdbrc
%config(noreplace) %_sysconfdir/*
%_bindir/*
%_libdir/lbdb/
%_man1dir/*

%changelog
* Sun Jun 26 2011 Victor Forsiuk <force@altlinux.org> 0.38-alt1
- 0.38

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.37-alt1.1
- rebuilt with perl 5.12

* Fri May 21 2010 Victor Forsiuk <force@altlinux.org> 0.37-alt1
- 0.37

* Tue Jun 17 2008 Victor Forsyuk <force@altlinux.org> 0.36-alt1
- 0.36

* Fri Jun 01 2007 Victor Forsyuk <force@altlinux.org> 0.35.1-alt1
- 0.35.1

* Tue Feb 06 2007 Victor Forsyuk <force@altlinux.org> 0.34-alt2
- Rebuild to work with evolution 2.8.x.

* Wed Dec 13 2006 Victor Forsyuk <force@altlinux.org> 0.34-alt1
- 0.34

* Tue Oct 24 2006 Victor Forsyuk <force@altlinux.org> 0.33-alt1
- 0.33

* Thu Sep 07 2006 Victor Forsyuk <force@altlinux.ru> 0.32-alt1
- 0.32

* Tue Apr 11 2006 Victor Forsyuk <force@altlinux.ru> 0.31.1-alt1
- 0.31.1
- Fix evolution addressbook export to work with evolution 2.6.x.

* Mon Oct 31 2005 Victor Forsyuk <force@altlinux.ru> 0.31-alt1
- 0.31
- Change mawk to gawk.
- Add build with abook and evolution.

* Wed Oct 19 2005 Michael Shigorin <mike@altlinux.org> 0.30-alt2
- one-byter to fix #5619 (rather cosmetic :)

* Mon May 02 2005 Michael Shigorin <mike@altlinux.ru> 0.30-alt1
- 0.30
- patch2 (palm) disabled -- doesn't apply, got no update

* Thu Sep 25 2003 Michael Shigorin <mike@altlinux.ru> 0.27-alt4
- updated build requires
- for 0.28: recode patch port pending

* Mon Jul 07 2003 Michael Shigorin <mike@altlinux.ru> 0.27-alt3
- updated package requires (perl shift)
- removed COPYING from %%doc (license stated in package header)

* Wed May 14 2003 Michael Shigorin <mike@altlinux.ru> 0.27-alt2
- added missing system-wide configuration files (thanks abr@)
- added cyrillic recoding, based on JPilot preferences
  (done by Andrey Brindeew <abr@altlinux.ru>)

* Sat Mar 22 2003 Michael Shigorin <mike@altlinux.ru> 0.27-alt1
- 0.27

* Mon Oct 14 2002 Michael Shigorin <mike@altlinux.ru> 0.26-alt1.1
- built with gcc3.2
- updated dependencies

* Tue Feb 12 2002 Michael Shigorin <mike@altlinux.ru> 0.26-alt1
- new version
- uk_UA description added
  (thanks to Volodymyr M. Lisivka <lvm@mystery.lviv.net>)

* Tue Jan 29 2002 Michael Shigorin <mike@altlinux.ru> 0.25.2-alt2
- alt2
- spec cleanup (clashed with filesystem package)
- files moved from default %prefix/lib to %_libdir/%name

* Sun Oct 21 2001 Michael Shigorin <mike@altlinux.ru> 0.25.2-alt1
- alt1
- spec cleanup
- no more build logs in package
- sample ~/.lbdbrc

* Sat Dec 30 2000 Rob Payne <rnspayne@adelphia.net>
- Changed to fit version 0.22
- Change installation process to include RPM_BUILD_ROOT
- Removed auto-generated files list that did not take into account RPM
  4's automatic compression of the man pages *after* the
  auto-generation was running.
- Removed the empty post, postun, preun scripts.

* Mon Apr 10 2000 Horms <horms@vergenet.net>
- created for version 0.18.5
