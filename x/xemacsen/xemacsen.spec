#==========================================
# subset of xemacs-related macros for bootstrap
%define _xemacs_confdir %_sysconfdir/xemacs
%define _xemacs_sitestartdir %_xemacs_confdir/site-start.d

%define _xemacs_infodir %_infodir/xemacs

%define _xemacs_package_root %_datadir/xemacs
%define _xemacs_pkgdir %_xemacs_package_root/xemacs-packages
%define _xemacs_muledir %_xemacs_package_root/mule-packages
%define _xemacs_sitedir %_xemacs_package_root/site-packages
#==========================================

Name: xemacsen
Version: 0.5
Release: alt2

Summary: Common directories and start scripts for XEmacsen
License: GPL
Group: Editors
BuildArch: noarch

Source: %name-%version-%release.tar

%package -n xemacs-common
Summary: Common set of XEmacs packages
Group: Editors
Serial: 1
PreReq: ctags
PreReq: xemacs-minimal
PreReq: xemacs-cc-mode
PreReq: xemacs-dired
PreReq: xemacs-edebug
PreReq: xemacs-ediff
PreReq: xemacs-edit-utils
PreReq: xemacs-efs
PreReq: xemacs-emerge
PreReq: xemacs-eterm
PreReq: xemacs-gnus
PreReq: xemacs-ispell
PreReq: xemacs-mailcrypt
PreReq: xemacs-mail-lib
PreReq: xemacs-pcl-cvs
PreReq: xemacs-prog-modes
PreReq: xemacs-ps-print
PreReq: xemacs-sh-script
PreReq: xemacs-speedbar
PreReq: xemacs-text-modes
PreReq: xemacs-vc
PreReq: xemacs-w3

%package -n xemacs-mule-common
Summary: Common set of MULE-featured XEmacs packages
Group: Editors
Serial: 1
PreReq: xemacs-common = %serial:%version-%release
PreReq: xemacs-latin-unity
PreReq: xemacs-leim 

%description
The common site start scripts for XEmacsen contain the default 
configuration for XEmacsen suggetsted by ALT. Administrators can
add some scripts of their own to customize XEmacsen even more.
This package also contains some common, non version- and arch-specific
directories in XEmacsen hierarchy.

%description -n xemacs-common
This virtual package provides common set of the XEmacs packages

%description -n xemacs-mule-common
This virtual package provides common set of the MULE-featured
XEmacs packages

%prep
%setup

%install
sed -i 's|@VERSION@|%version|; s|@RELEASE@|%release|' %name-macros
mkdir -p \
    %buildroot%_xemacs_confdir \
    %buildroot%_xemacs_sitestartdir \
    %buildroot%_xemacs_pkgdir/{etc,lisp,lib-src} \
    %buildroot%_xemacs_muledir/{etc,lisp,lib-src} \
    %buildroot%_xemacs_sitedir/{etc,lisp,lib-src} \
    %buildroot%_xemacs_infodir

install -pm0644 site-start.el %buildroot%_xemacs_confdir
install -pm0644 [01][01]*.el %buildroot%_xemacs_sitestartdir
install -pm0644 -D %name-macros %buildroot%_rpmmacrosdir/xemacs
install -pm0644 -D package-index %buildroot%_xemacs_package_root/package-index
install -pm0644 xemacsen.el %buildroot%_xemacs_package_root
touch %buildroot%_xemacs_infodir/dir

%files
%_rpmmacrosdir/xemacs
%dir %_xemacs_confdir
%dir %_xemacs_sitestartdir
%dir %_xemacs_infodir
%dir %_xemacs_package_root
%dir %_xemacs_pkgdir
%dir %_xemacs_pkgdir/etc
%dir %_xemacs_pkgdir/lisp
%dir %_xemacs_pkgdir/lib-src
%dir %_xemacs_muledir
%dir %_xemacs_muledir/etc
%dir %_xemacs_muledir/lisp
%dir %_xemacs_muledir/lib-src
%dir %_xemacs_sitedir
%dir %_xemacs_sitedir/etc
%dir %_xemacs_sitedir/lisp
%dir %_xemacs_sitedir/lib-src
%_xemacs_package_root/package-index
%_xemacs_package_root/xemacsen.el
%config(noreplace) %_xemacs_confdir/site-start.el
%config(noreplace) %_xemacs_sitestartdir/*.el
%ghost %_xemacs_infodir/dir

%files -n xemacs-common
%files -n xemacs-mule-common

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt2
- mask ede req in package index for a while

* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt1
- obsolete install-info calls removed
- xemacs-related rpm macros relocated to %%_rpmmacrosdir
- package index updated 2009-02-04

* Mon Oct  2 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- removed xselection hack from site-start
- added locale-based language environent guessing code
- mule-ucs package considered useless
- rpm macros updated for beta xemacsen handling

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt10
- package index updated 2006-05-08

* Sun Jan 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt9
- package index updated 2006-01-04

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt8
- package index updated 2005-12-08

* Mon Nov 21 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt7
- builreq for ordinary xemacs package sync'd with apt's opinion

* Sat Nov 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt6
- adopted for stricter rpm macro policy

* Sat Aug  6 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt5
- package index updated 2005-07-10

* Fri May  6 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt4
- package index updated 2005-05-01

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt3
- extra requires to rmail, mh-e and vm suppressed

* Sun Mar 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt2
- some site-packages related macros fixed

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- package index updated 2005-03-05

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt0.1
- package index updated 2005-01-17

* Thu Jan  6 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt2
- rpm macrofile redo

* Tue Dec 21 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- updated alternatives format
- few rpm macros added

* Tue Jun  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt13
- package index updated 2004-05-14
- removed obsolete xterm-keys hack
 
* Sat Feb  7 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt12
- added CTEXT selection handling hack by SJT
- package index updated 2004-01-30

* Sat Oct  4 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt11
- package-index updated 2003-10-01

* Sat Jul  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.1-alt10
- package-index updated 2003-06-28

* Sat Jun 14 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.1-alt9
- switched to new alternatives
- keys in xterm adopted for ALT's defaults

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.1-alt8
- package-index updated 2003-04-10

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.1-alt7
- removed obsolete install-info workaround
- package-index updated 20030125

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt6
- package-index updated 20021101

* Sat Nov 23 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt5
- switch-buffers modifications by Alexey Morozov <morozov@novosoft.ru>

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt4
- package index updated 20021014

* Sat Sep 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt3
- package index added

* Mon Sep  9 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt2
- added macros for byte-compilation

* Sat Sep  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt1
- first build for %distribution distribution
