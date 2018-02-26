# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-prog-modes.spec,v 1.7 2006/02/04 18:02:41 eugene Exp $

%define pkg_name prog-modes

Version: 0.2
Release: alt4
Name: emacs-%pkg_name
License: GPL
Group: Editors
Summary: Various programming packages for Emacs
Summary(ru_RU.UTF-8): Дополнительные пакеты Emacs для работы с исходными текстами программ
Requires: emacs-common

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %name.tar.gz
Source1: emacs-mode-php-site-start.el
Source3: emacs-mode-eiffel-site-start.el
Source4: emacs-mode-postscript-site-start.el
Source5: emacs-mode-rexx-site-start.el
Source6: emacs-mode-rpm-site-start.el
Source8: emacs-mode-vrml-site-start.el
Source9: emacs-mode-xbase-site-start.el

BuildArch: noarch

BuildPreReq: emacs-devel >= 0.0.1-alt2

# Automatically added by buildreq on Thu Oct 13 2005
BuildRequires: emacs-cedet emacs-common emacs-elib emacs-leim fontconfig freetype2 xorg-x11-locales

%description
Various programming packages for Emacs, including packages for editing
programms on C, Scheme, Fortran and others.

%description -l ru_RU.UTF-8
Дополнительные пакеты Emacs для работы с исходными текстами программ на
языках С, Fortran, Scheme и других, а также различные вспомогательные
режимы для редактирования файлов Autoconf/Automake, отладки и многого
другого.

%prep
%setup -q -n %name

%install
mkdir -p %buildroot%_emacslispdir/
install -m 644 *.el* %buildroot%_emacslispdir/
# %__mkdir_p %buildroot%_emacs_etc_dir/%pkg_name/
# %__install -m 755 *.sh %buildroot%_emacs_etc_dir/%pkg_name/
# %__install -m 644 c_synopsis_list %buildroot%_emacs_etc_dir/%pkg_name/
install -pD -m0644 %SOURCE1 %buildroot%_emacs_sitestart_dir/php.el
install -pD -m0644 %SOURCE3 %buildroot%_emacs_sitestart_dir/eiffel.el
install -pD -m0644 %SOURCE4 %buildroot%_emacs_sitestart_dir/postscript.el
install -pD -m0644 %SOURCE5 %buildroot%_emacs_sitestart_dir/rexx.el
install -pD -m0644 %SOURCE6 %buildroot%_emacs_sitestart_dir/rpm.el
install -pD -m0644 %SOURCE8 %buildroot%_emacs_sitestart_dir/vrml.el
install -pD -m0644 %SOURCE9 %buildroot%_emacs_sitestart_dir/xbase.el
%byte_recompile_lispdir

%files
%doc emacs-prog-modes-list.txt
%_emacslispdir/*.el*
# %_emacs_etc_dir/%pkg_name/
%config(noreplace) %_emacs_sitestart_dir/*


%changelog
* Thu May 01 2008 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt4
- Removed c-mode-addons.el, c_synopsis_list and support scripts (#15474)

* Tue Apr 08 2008 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt3
- Updated autoconf-mode, clearcase, compile-, compile+, constants,
  dbfrobs, mode-compile, php-mode, quack
- Removed verilog-mode

* Sat Feb 04 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt2
- Build with emacs-devel
- Updated oct (and renamed from ect)
- Updated c-includes, fm, ftnchek
- Removed antlr-mode, cperl-mode, delphi, flymake
- Fixed autoloads for rpm-spec-mode and postscript

* Wed Oct 12 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt1
- Updated clearcase, constants, eiffel, flymake, javascript-mode,
  mode-compile, php-mode, quack, rpm-spec-mode, verilog-mode
- Added c-eldoc, compile-, compile+, sql-indent
- Removed eshell-bash, http-mode, p4, pydoc, teco
- Fixed build requires

* Wed Jul 14 2004 AEN <aen@altlinux.ru> 0.1-alt13
- NMU: rebuild in Master 2.4 environment 

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 0.1-alt12
- Added flymake package
- Added codemetric package
- Added different minor modes for work with CVS

* Tue Jan 27 2004 Ott Alex <ott@altlinux.ru> 0.1-alt11
- Fixing startup scripts

* Mon Jan 26 2004 Ott Alex <ott@altlinux.ru> 0.1-alt10
- Fixing startup scripts

* Tue Dec 16 2003 Ott Alex <ott@altlinux.ru> 0.1-alt9
- Remove ruby-mode, that conflicts with emacs-ruby-mode package

* Sat Dec 13 2003 Ott Alex <ott@altlinux.ru> 0.1-alt8
- New version of php-mode 
- Move antlr-mode from emacs-common

* Sun Nov 30 2003 Ott Alex <ott@altlinux.ru> 0.1-alt7
- add php-mode from emacs-common to package
- adding more site-start scripts

* Tue Oct 28 2003 Ott Alex <ott@altlinux.ru> 0.1-alt6
- Move pov-im file to emacs-pov-mode

* Sun Oct 26 2003 Ott Alex <ott@altlinux.ru> 0.1-alt5
- Adding new packages

* Tue Sep 23 2003 Ott Alex <ott@altlinux.ru> 0.1-alt4
- New snapshot

* Fri Jan 17 2003 Ott Alex <ott@altlinux.ru> 0.1-alt3
- Fixing spec-file

* Mon Jan 13 2003 Ott Alex <ott@altlinux.ru> 0.1-alt2
- New release of files

* Tue Dec 24 2002 Ott Alex <ott@altlinux.ru> 0.1-alt1
- Initial build
