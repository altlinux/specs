%define pkg_name edb
%define pre %nil
Version: 1.29
Release: alt1
Name: emacs-%pkg_name
License: GPL
Group: Editors
Url: http://www.glug.org/people/ttn/software/edb/
Summary: EDB is a database program for GNU Emacs
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>
Source: ftp://theory.lcs.mit.edu/pub/emacs/edb/%pkg_name-%version%pre.tar.gz
Patch: edb-1.29-alt-add-info-direntry.patch

BuildArch: noarch
# Automatically added by buildreq on Tue Jun 17 2003
BuildRequires: emacs-common texinfo
Requires: emacs-common 

%description
EDB is a database program for GNU Emacs.  It permits you to
manipulate structured (or not-so-structured) data within Emacs and
provides many of the usual database features.

%prep
%setup -n %pkg_name-%version%pre
%patch

%build
%configure
#make_build
make
make check


%install
%makeinstall edb-elc-dir=%buildroot/%_emacslispdir/%pkg_name install

%files
%doc AUTHORS BUGS COPYING HACKING NEWS README* TODO
%_emacslispdir/*
%_infodir/*

%changelog
* Tue Aug 25 2009 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- new version

* Sun Jan 22 2006 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- downgrade to version 1.25 (emacs21 compatible)

* Thu Jan 12 2006 Igor Vlasenko <viy@altlinux.ru> 1.26-alt0
- updated url; now maintained by Emacs Maintainers Team
- fixing spec; 
- fixed info post/pre;
- new version
- BuildArch: noarch

* Wed Nov 12 2003 Ott Alex <ott@altlinux.ru> 1.21-alt2
- Fixing spec

* Mon Oct 13 2003 Ott Alex <ott@altlinux.ru> 1.21-alt1
- first build for altlinux

