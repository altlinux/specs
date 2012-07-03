Name: dogtail
Version: 0.7.0
Release: alt2.1

Summary: GUI test tool and automation framework

License: GPL
Group: Development/Other
Url: https://fedorahosted.org/dogtail/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://people.redhat.com/zcerza/dogtail/releases/dogtail-%version.tar

BuildArch: noarch
# Automatically added by buildreq on Sat May 21 2011
# optimized out: python-base python-devel python-modules python-modules-compiler
BuildRequires: python-module-paste python-module-peak

BuildRequires: desktop-file-utils

%py_requires gconf

Requires: xinit

# Hack for build
%add_python_req_skip Accessibility

%description
GUI test tool and automation framework that uses assistive technologies to
communicate with desktop applications.

Before using enable accessibility via
$ gconftool-2 -s -t boolean /desktop/gnome/interface/accessibility true

%prep
%setup

%build
%python_build

%install
%python_install
rm -rf %buildroot%_docdir/dogtail/
find examples -type f -exec chmod 0644 \{\} \;
%__subst "s|\.svg||g" %buildroot%_desktopdir/*

%files
%doc README examples/
%_bindir/*
%python_sitelibdir/%name/
%python_sitelibdir/%name-*.egg-info
%_desktopdir/*
%_datadir/%name/
%_liconsdir/*
%_iconsdir/hicolor/scalable/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt2.1
- Rebuild with Python-2.7

* Sat May 21 2011 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt2
- resend due broken desktop file permissions
- update buildreqs

* Sun Aug 01 2010 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3.2
- Rebuilt with python 2.6

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.1-alt3.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for dogtail
  * postclean-05-filetriggers for spec file

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.6.1-alt3.1
- Rebuilt with python-2.5.

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt3
- enable update/clean menus

* Sun Sep 09 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt2
- fix desktop file

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Fri Oct 27 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.1
- initial build for ALT Linux Sisyphus

* Wed Sep 13 2006 Zack Cerza <zcerza@redhat.com> - 0.6.0-1
- New upstream release.
- Add Requires for xorg-x11-xinit.
- Add Requires for gnome-python2-gconf.
- Bump pyspi Requires.

* Tue Aug 01 2006 Zack Cerza <zcerza@redhat.com> - 0.5.2-1
- New upstream release.
- Update Requires from Xvfb to xorg-x11-server-Xvfb.
- Bump pyspi Requires.
- Remove ImageMagick Requires.
- Escape post-macro in changelog-macro.

* Mon Apr 17 2006 Zack Cerza <zcerza@redhat.com> - 0.5.1-3
- Fix the URL field.

* Tue Mar 21 2006 Zack Cerza <zcerza@redhat.com> - 0.5.1-2
- Fix URL and Source0 fields.
- Fix desktop-file-utils magic; use desktop-file-install.

* Fri Feb 24 2006 Zack Cerza <zcerza@redhat.com> - 0.5.1-1
- Remove BuildRequires on at-spi-devel. Added one on python.
- Use macros instead of absolute paths.
- Touch _datadir/icons/hicolor/ before running gtk-update-icon-cache.
- Require and use desktop-file-utils.
- postun = post.
- Shorten BuildArchitectures to BuildArch. The former worked, but even vim's
  hilighting hated it.
- Put each *Requires on a separate line.
- Remove __os_install_post definition.
- Use Fedora Extras BuildRoot.
- Instead of _libdir, which kills the build if it's _libdir64, use a
  python macro to define python_sitelib and use that.
- Remove the executable bit on the examples in install scriptlet.
- Remove call to /bin/rm in post scriptlet.
- Use dist in Release.

* Fri Feb 17 2006 Zack Cerza <zcerza@redhat.com> - 0.5.0-2
- It looks like xorg-x11-Xvfb changed names. Require 'Xvfb' instead.
- Remove Requires on python-elementtree, since RHEL4 didn't have it. The
  functionality it provides is probably never used anyway, and will most likely
  be removed in the future.
- Don't run gtk-update-icon-cache if it doesn't exist.

* Fri Feb  3 2006 Zack Cerza <zcerza@redhat.com> - 0.5.0-1
- New upstream release.
- Added missing BuildRequires on at-spi-devel.
- Added Requires on pyspi >= 0.5.3.
- Added Requires on rpm-python, pygtk2, ImageMagick, xorg-x11-Xvfb,
  python-elementtree.
- Moved documentation (including examples) to the correct place.
- Make sure %_docdir/dogtail is removed.
- Added 'gtk-update-icon-cache' to %%post.

* Mon Oct 24 2005 Zack Cerza <zcerza@redhat.com> - 0.4.3-1
- New upstream release.

* Sat Oct  8 2005 Jeremy Katz <katzj@redhat.com> - 0.4.2-1
- Initial build.

