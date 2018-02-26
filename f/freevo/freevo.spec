# FIXME: use special user for freevo daemons
# FIXME: fix fonts/encoding for russian texts
# FIXME: disable freevo service (it is for embedded)
# FIXME: init scripts (correct condrestart)

Name: freevo
Version: 1.8.3
Release: alt1.3.1

Summary: Freevo

License: GPL
Group: Graphics
Url: http://freevo.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://dl.sf.net/%name/%name-%version.tar.bz2
Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2
Source1: %name-boot_config
Source2: %name.init
Source3: %name-record.init
Source4: %name-web.init
Source5: %name.desktop

Patch: %name-1.7.7-vpodcast.patch

BuildArch: noarch

##########################################################################
%define _contribdir %_datadir/freevo/contrib

%setup_python_module %name

Requires: python-module-numpy

# fix bug #11959
Requires: python-module-elementtree python-module-twisted

%add_python_req_skip audio image video misc animation childapp config directory event gui fxditem menu item osd playlist plugin plugins pygphoto pyosd rc skin tv util view_favorites commdetectcore encodingcore rssperiodic


# manually removed: pybliographic 
# Automatically added by buildreq on Sat May 26 2007 (-bi)
BuildRequires: kbd python-module-BeautifulSoup python-module-elementtree
BuildRequires: python-module-imaging python-module-kaa-imlib2
BuildRequires: python-module-kaa-metadata libnumpy-devel python-module-pygame
BuildRequires: python-module-PyXML python-module-setuptools
BuildRequires: python-module-twisted-web rpm-build-mono

BuildPreReq: python-module-imaging-devel rpm-build-compat >= 1.2

%description
Freevo is a Linux application that turns a PC with a TV capture card
and/or TV-out into a standalone multimedia jukebox/VCR. It builds on
other applications such as xine, mplayer, tvtime and mencoder to play
and record video and audio.

See http://gentoo-wiki.com/Freevo

%package boot
Summary: Files to enable a standalone Freevo system (started from initscript)
Group: Graphics
Requires: %name

%description boot
Freevo is a Linux application that turns a PC with a TV capture card
and/or TV-out into a standalone multimedia jukebox/VCR. It builds on
other applications such as mplayer and mencoder to play and record
video and audio.

Note: This installs the initscripts necessary for a standalone Freevo system.

%prep
%setup -q
#patch -p1

%build
find . -name CVS | xargs rm -rf
find . -name ".cvsignore" |xargs rm -f
find . -name "*.pyc" |xargs rm -f
find . -name "*.pyo" |xargs rm -f
find . -name "*.py" |xargs chmod 644

%python_build

%install
%python_install

mkdir -p %buildroot%_sysconfdir/freevo
# The following is needed to let RPM know that the files should be backed up
touch %buildroot%_sysconfdir/freevo/freevo.conf
install -m 644 local_conf.py.example %buildroot%_sysconfdir/freevo/local_conf.py

# boot scripts
mkdir -p %buildroot{%_initrddir,%_bindir}
install -m 644 -D %SOURCE1 %buildroot%_sysconfdir/freevo/boot_config
install -m 755 %SOURCE2 %buildroot%_initrddir/freevo
install -m 755 %SOURCE3 %buildroot%_initrddir/freevo_record
install -m 755 %SOURCE4 %buildroot%_initrddir/freevo_web

install -D -m 755 %SOURCE5 %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_logdir/freevo
mkdir -p %buildroot%_cachedir/freevo
mkdir -p %buildroot%_cachedir/freevo/{thumbnails,audio}
mkdir -p %buildroot%_cachedir/xmltv/logos
chmod 777 %buildroot%_cachedir/{freevo,freevo/thumbnails,freevo/audio,xmltv,xmltv/logos}
chmod 777 %buildroot%_logdir/freevo

mkdir -p %buildroot%_contribdir/lirc
cp -av contrib/lirc %buildroot%_contribdir

#find_lang %name
rm -f %buildroot%_datadir/locale/*/LC_MESSAGES/freevo.po
rm -f %buildroot%_datadir/locale/*/LC_MESSAGES/freevo.mo

%files
# -f %name.lang
%_docdir/%name-%version
%_bindir/freevo
%dir %_sysconfdir/freevo/
%config %_sysconfdir/freevo/freevo.conf
%config %_sysconfdir/freevo/local_conf.py
%attr(775,root,audio) %_logdir/freevo
%attr(775,root,audio) %dir %_cachedir/freevo
%attr(775,root,audio) %dir %_cachedir/freevo/audio
%attr(775,root,audio) %dir %_cachedir/freevo/thumbnails
%attr(775,root,audio) %dir %_cachedir/xmltv
%attr(775,root,audio) %dir %_cachedir/xmltv/logos
%_datadir/%name/
%python_sitelibdir/%modulename/
%_desktopdir/%name.desktop

%files boot
%config %_sysconfdir/freevo/boot_config
%_initrddir/freevo
%_initrddir/freevo_web
%_initrddir/freevo_record

%post boot
#post_service freevo
%post_service freevo_record
%post_service freevo_web

%preun boot
#preun_service freevo
%preun_service freevo_record
%preun_service freevo_web

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.3-alt1.3.1
- Rebuild with Python-2.7

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt1.3
- Rebuilt with reformed NumPy (see http://www.altlinux.org/Python/Refactoring)

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt1.2
- Rebuilt without python-module-Numeric

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt1.1
- Rebuilt with python 2.6

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.3-alt1
- new version 1.8.3 (with rpmrb script)

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Thu May 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- new version 1.7.7 (with rpmrb script)

* Mon Jan 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt2
- fix post/preun service registering
- fix files intersection
- do not pack localize files (due bug #11960)

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- new version 1.7.5 (with rpmrb script)

* Thu Sep 20 2007 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- new version 1.7.3 (with rpmrb script)

* Sun Jun 03 2007 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script)
- add requires python-module-elementtree python-module-twisted (fix bug #11959)

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- new version 1.7.1 (with rpmrb script)

* Tue Dec 26 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt0.1
- new version 1.6.1 (with rpmrb script)
- add python-module-Numeric requires (fix bug #10518)

* Wed Nov 22 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt0.1
- new version 1.6.0 (with rpmrb script)

* Fri Nov 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt0.1
- new version

* Fri Nov 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt0.2
- new version

* Mon Jul 19 2004 TC Wan <tcwan@cs.usm.my>
- Built 1.5.0 final

* Fri Jul  2 2004 TC Wan <tcwan@cs.usm.my>
- Added docs subdir for package cleanup, fixed contrib dir build warnings

* Tue Jun 29 2004 TC Wan <tcwan@cs.usm.my>
- Added python-numeric dependency, backup freevo.conf
  just before creating new default copy

* Fri Jun 18 2004 TC Wan <tcwan@cs.usm.my>
- Updated for 1.5

* Fri Dec 19 2003 TC Wan <tcwan@cs.usm.my>
- Updated for 1.4.1

* Sat Nov 22 2003 TC Wan <tcwan@cs.usm.my>
- Updated for 1.4 final

* Tue Nov 11 2003 TC Wan <tcwan@cs.usm.my>
- Updated for 1.4-rc4

* Tue Nov  4 2003 TC Wan <tcwan@cs.usm.my>
- Updated for 1.4-rc3 (name change)

* Sat Oct 25 2003 TC Wan <tcwan@cs.usm.my>
- Updated for 1.4-rc2

* Wed Oct  8 2003 TC Wan <tcwan@cs.usm.my>
- Fixed boot scripts for RH 9, disabled freevo_dep since it's obsolete (?)

* Fri Sep 26 2003 TC Wan <tcwan@cs.usm.my>
- Removed testfiles from build since it's no longer part of the package
  Cleaned up conditional flags

* Thu Sep 18 2003 TC Wan <tcwan@cs.usm.my>
- Added supporting directories and files to package

* Fri Sep  5 2003 TC Wan <tcwan@cs.usm.my>
- Initial SPEC file for python site-packages installation
