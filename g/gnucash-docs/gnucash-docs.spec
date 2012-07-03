Name: gnucash-docs
Version: 2.2.0
Release: alt1.qa1

Summary: Documentation for the Gnucash

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL
Group: Office
Url: http://www.gnucash.org

BuildArch: noarch

Requires: yelp

Requires(post): scrollkeeper
Requires(postun): scrollkeeper

Source: http://www.gnucash.org/pub/gnucash/sources/stable/%name-%version.tar.bz2

# Automatically added by buildreq on Thu Dec 28 2006
BuildRequires: scrollkeeper xsltproc

%description
GnuCash is a personal finance manager. A check-book like
register GUI allows you to enter and track bank accounts,
stocks, income and even currency trades. The interface is
designed to be simple and easy to use, but is backed with
double-entry accounting principles to ensure balanced books.
This is the documentation module for GnuCash.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS COPYING-DOCS ChangeLog NEWS README HACKING
%_datadir/gnome/help/gnucash/
%_datadir/omf/gnucash-docs/

%changelog
* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-scrollkeeper-update for gnucash-docs
  * postclean-05-filetriggers for spec file

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version 2.0.5 (with rpmrb script)
- add yelp to requires

* Sat Dec 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt0.1
- new version, rewrote spec

* Sun Dec  4 2005 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt2
- update buildreq

* Thu Dec 16 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- first separate package with gnucash documentation
