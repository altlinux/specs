# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-muse-mode.spec,v 1.1 2006/05/27 12:58:42 eugene Exp $

%define modename muse
%define base_rel alt1

Version: 3.20
%ifdef beta_ver
Release: %base_rel.%beta_ver.1
%else
Release: %base_rel.1
%endif
Name: emacs-%modename-mode
License: GPL
Group: Editors
Url: http://www.mwolson.org/projects/MuseMode.html
Summary: Publishing environment for Emacs
Requires: emacs-common emacs-misc-modes

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

%ifdef beta_ver
Source: http://www.mwolson.org/static/dist/%modename/%modename-%version%beta_ver.tar.gz
%else
Source: http://www.mwolson.org/static/dist/%modename/%modename-%version.tar.gz
%endif
Source1: %name.el

BuildArch: noarch

BuildPreReq: emacs-misc-modes >= 0.2-alt3
BuildPreReq: emacs-devel

# Automatically added by buildreq on Sat May 27 2006
BuildRequires: fontconfig
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Emacs Muse is an authoring and publishing environment for Emacs. It
simplifies the process of writings documents and publishing them to various
output formats. Muse uses a very simple Wiki-like format as input.

Muse consists of two main parts: an enhanced text-mode for authoring
documents and navigating within Muse projects, and a set of publishing
styles for generating different kinds of output.

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%prep
%ifdef beta_ver
%setup -q -n %modename-%version%beta_ver
%else
%setup -q -n %modename-%version
%endif

%build
%__make PREFIX=%prefix

%install
mkdir -p %buildroot%_emacslispdir/%modename
install -m 644 lisp/*.el* %buildroot%_emacslispdir/%modename

mkdir -p %buildroot%_infodir
install -m 644 texi/*.info* %buildroot%_infodir/

mkdir -p %buildroot%_emacs_sitestart_dir
install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/%modename.el

# gzip ChangeLog*

%files
%doc AUTHORS NEWS README
%_infodir/*
%dir %_emacslispdir/%modename
%_emacslispdir/%modename/*.elc
%_emacslispdir/%modename/%modename-autoloads.el
%config(noreplace) %_emacs_sitestart_dir/*

%files el
%_emacslispdir/%modename/*.el
%exclude %_emacslispdir/%modename/%modename-autoloads.el


%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 3.20-alt1.1
- NMU: added BR: texinfo

* Fri Apr 05 2013 Eugene Vlasov <eugvv@altlinux.ru> 3.20-alt1
- New version
- Removed build requires on emacs-w3
- Removed obsoletes macros

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop at altlinux.org> 3.02.93-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for emacs-muse-mode
  * postclean-05-filetriggers for spec file

* Mon Jan 01 2007 Eugene Vlasov <eugvv@altlinux.ru> 3.02.93-alt1
- New version
- Packed NEWS instead of Changelog

* Sat May 27 2006 Eugene Vlasov <eugvv@altlinux.ru> 3.02.6-alt0.1.b
- Initial build for Sisyphus

