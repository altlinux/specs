Name: dvipng
Version: 1.14
Release: alt1

Summary: Makes PNG graphics from DVI files
License: LGPLv3+
Group: Editors

URL: http://sourceforge.net/projects/dvipng/
Source: http://download.sourceforge.net/dvipng/dvipng-%version.tar.gz

# Automatically added by buildreq on Fri Dec 17 2010
BuildRequires: libfreetype-devel libgd2-devel libkpathsea-devel libpng-devel t1lib-devel texlive-generic-recommended texlive-latex-base

%description
This program makes PNG graphics from DVI files as obtained from TeX and its
relatives. It can be used as companion to emacs-preview-latex package.

%prep
%setup

%build
%configure --enable-selfauto-set
%make_build
make dvipng.info

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%_infodir/*.info.*
%exclude %_infodir/dir

%changelog
* Fri Dec 17 2010 Victor Forsiuk <force@altlinux.org> 1.14-alt1
- 1.14

* Fri Mar 19 2010 Victor Forsiuk <force@altlinux.org> 1.13-alt1
- 1.13

* Tue Jul 07 2009 Victor Forsyuk <force@altlinux.org> 1.12-alt2
- Rebuild in texlive environment (closes: ALT#20089).

* Tue Mar 24 2009 Victor Forsyuk <force@altlinux.org> 1.12-alt1
- 1.12

* Tue Jun 10 2008 Victor Forsyuk <force@altlinux.org> 1.11-alt2
- Fix info files installation.

* Wed May 21 2008 Victor Forsyuk <force@altlinux.org> 1.11-alt1
- 1.11

* Thu May 15 2008 Victor Forsyuk <force@altlinux.org> 1.10-alt1
- 1.10

* Wed Nov 22 2006 Victor Forsyuk <force@altlinux.org> 1.9-alt1
- 1.9

* Thu Apr 13 2006 Victor Forsyuk <force@altlinux.ru> 1.8-alt1
- 1.8
- Refresh build requirements.

* Thu Nov 17 2005 Victor Forsyuk <force@altlinux.ru> 1.7-alt2
- Build to fix bugs in previous erroneous NMU (1.7-alt1 that
  appeared in Sisyphus repo was not my build).

* Tue Nov 15 2005 Victor Forsyuk <force@altlinux.ru> 1.7-alt1
- 1.7

* Mon Jul 11 2005 Victor Forsyuk <force@altlinux.ru> 1.6-alt1
- 1.6

* Tue Apr 05 2005 Victor Forsyuk <force@altlinux.ru> 1.5-alt1
- Fix URL.
- Refresh build requirements.
- Install man pages.

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 1.0-alt1
- Initial build for ALTLinux
