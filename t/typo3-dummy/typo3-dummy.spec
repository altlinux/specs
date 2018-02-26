%define origname dummy
%define beta %nil

Name: typo3-%origname
Version: 4.5.16
Release: alt1

Summary: Dummy site for TYPO3
License: GPL
Group: Networking/Other

Url: http://www.typo3.org
Source: %origname-%version%beta.tar.gz
Source100: typo3-dummy.watch
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

AutoReqProv: no

# Speed-up build process
%define _verify_elf_method skip
%define _strip_method none

%define installdir %_datadir/%name-%version

%description
This package provides an initial skeleton for custom TYPO3 site
deployment -- you should copy the read-only template as a root
directory of a new website.

Dummy also contains an empty database with only a single admin
user configured (user: "admin", password: "password").
Obviously, change those before too long (or too late).

%prep
%setup -n %origname-%version%beta

%install
mkdir -p %buildroot%installdir
# no need to copy the engine
mv [^IR_]* %buildroot%installdir/
mv _.htaccess %buildroot%installdir/.htaccess ||:

# TODO:
# - proper deployer (cp, chown, chmod)
# - activate mod_rewrite or comment out in default .htaccess
# - control apache-php5 public; [mem 32M]; service httpd reload
# - TYPO3_CONF_VARS[GFX][TTFdpi]=96
# - [GFX][gdlib_2] = 1
# - [GFX][im_path_lzw] = /usr/bin/
# - [GFX][im_version_5] = im6
# - [GFX][im_v5effects] = 1
# - [SYS][compat_version] = 4.1 -- since it's a dummy
#   (not sure, see Upgrade Wizard)
# - [SYS][curlUse] = 1
# - [SYS][binPath] = /usr/bin,/bin [?]
# - [SYS][t3lib_cs_convMethod] = iconv
# - [t3lib_cs_utils] = iconv [PHP 5.0 only!]
# - [SYS][UTF8filesystem] = 1
# - [BE][forceCharset] = utf-8
# - http://bugs.mysql.com/bug.php?id=6604 [sys_refindex]

%files
%installdir/
%doc *.txt

%changelog
* Tue May 22 2012 Michael Shigorin <mike@altlinux.org> 4.5.16-alt1
- 4.5.16

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 4.5.15-alt2
- added watch file (4.5.x series)

* Tue Apr 17 2012 Michael Shigorin <mike@altlinux.org> 4.5.15-alt1
- 4.5.15
- fixed .htaccess installation

* Wed Mar 28 2012 Michael Shigorin <mike@altlinux.org> 4.5.14-alt1
- 4.5.14

* Tue Mar 13 2012 Michael Shigorin <mike@altlinux.org> 4.5.13-alt1
- 4.5.13

* Tue Mar 06 2012 Michael Shigorin <mike@altlinux.org> 4.5.12-alt1
- 4.5.12

* Tue Jan 24 2012 Michael Shigorin <mike@altlinux.org> 4.5.11-alt1
- 4.5.11

* Tue Dec 20 2011 Michael Shigorin <mike@altlinux.org> 4.5.10-alt1
- 4.5.10

* Fri Dec 16 2011 Michael Shigorin <mike@altlinux.org> 4.5.9-alt1
- 4.5.9

* Fri Nov 25 2011 Michael Shigorin <mike@altlinux.org> 4.5.8-alt1
- 4.5.8

* Wed Sep 14 2011 Michael Shigorin <mike@altlinux.org> 4.5.6-alt1
- 4.5.6

* Tue Aug 16 2011 Michael Shigorin <mike@altlinux.org> 4.5.5-alt1
- 4.5.5

* Fri Aug 05 2011 Michael Shigorin <mike@altlinux.org> 4.5.4-alt1
- 4.5.4
  + no more _.htaccess in upstream tarball

* Sat Feb 26 2011 Michael Shigorin <mike@altlinux.org> 4.5.2-alt1
- 4.5.2

* Wed Feb 23 2011 Michael Shigorin <mike@altlinux.org> 4.5.1-alt1
- 4.5.1

* Wed Jan 26 2011 Michael Shigorin <mike@altlinux.org> 4.5.0-alt1
- 4.5.0

* Tue Dec 28 2010 Michael Shigorin <mike@altlinux.org> 4.3.10-alt1
- 4.3.10

* Thu Dec 16 2010 Michael Shigorin <mike@altlinux.org> 4.3.9-alt1
- 4.3.9

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 4.3.8-alt1
- 4.3.8

* Wed Oct 06 2010 Michael Shigorin <mike@altlinux.org> 4.3.7-alt1
- 4.3.7

* Tue Sep 28 2010 Michael Shigorin <mike@altlinux.org> 4.3.6-alt1
- 4.3.6

* Fri Aug 06 2010 Michael Shigorin <mike@altlinux.org> 4.3.5-alt1
- 4.3.5

* Sun Aug 01 2010 Michael Shigorin <mike@altlinux.org> 4.3.4-alt1
- 4.3.4

* Tue Feb 23 2010 Michael Shigorin <mike@altlinux.org> 4.3.2-alt1
- 4.3.2

* Thu Jan 14 2010 Michael Shigorin <mike@altlinux.org> 4.3.1-alt1
- 4.3.1

* Mon Nov 30 2009 Michael Shigorin <mike@altlinux.org> 4.3.0-alt1
- 4.3.0

* Sun Oct 25 2009 Michael Shigorin <mike@altlinux.org> 4.2.10-alt1
- 4.2.10

* Mon Sep 28 2009 Michael Shigorin <mike@altlinux.org> 4.2.9-alt1
- 4.2.9

* Sat Jul 04 2009 Michael Shigorin <mike@altlinux.org> 4.2.8-alt1
- 4.2.8
  + 4.2.7 src release contained a glitch so was effectively skipped

* Tue Feb 10 2009 Michael Shigorin <mike@altlinux.org> 4.2.6-alt1
- 4.2.6

* Tue Jan 20 2009 Michael Shigorin <mike@altlinux.org> 4.2.4-alt1
- 4.2.4

* Thu Nov 13 2008 Michael Shigorin <mike@altlinux.org> 4.2.3-alt1
- 4.2.3

* Sat Oct 18 2008 Michael Shigorin <mike@altlinux.org> 4.2.2-alt1
- 4.2.2

* Wed Jun 11 2008 Michael Shigorin <mike@altlinux.org> 4.2.1-alt1
- 4.2.1

* Wed Apr 23 2008 Michael Shigorin <mike@altlinux.org> 4.2.0-alt1
- 4.2.0

* Mon Apr 21 2008 Michael Shigorin <mike@altlinux.org> 4.2.0-alt0.2
- 4.2.0RC2

* Tue Mar 04 2008 Michael Shigorin <mike@altlinux.org> 4.1.6-alt1
- 4.1.6

* Mon Dec 31 2007 Michael Shigorin <mike@altlinux.org> 4.1.5-alt1
- 4.1.5

* Tue Jul 17 2007 Michael Shigorin <mike@altlinux.org> 4.1.2-alt1
- 4.1.2

* Tue Jun 05 2007 Michael Shigorin <mike@altlinux.org> 4.1.1-alt1
- built for ALT Linux
