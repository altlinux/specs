%define pypi_name dogtail

Name: dogtail
Version: 2.1.0
Release: alt1

Summary: GUI test tool and automation framework

License: GPL-2.0
Group: Development/Other
Url: https://gitlab.com/dogtail/dogtail

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

# gir-python.req ignores gi.require_version(): dogtail needs Gtk/Gdk 3.0
# (utils.py, rawinput.py), unversioned typelib(Gtk) is also provided by GTK4
Requires: typelib(Gtk) = 3.0
Requires: typelib(Gdk) = 3.0

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-setuptools_scm

# optional distro-specific package backends in dogtail.distro
%add_python3_req_skip apt_pkg conaryclient portage
# pytest fixture for dogtail.hermetic, used only from within pytest
%add_python3_req_skip pytest

%description
GUI test tool and automation framework that uses assistive technologies
(AT-SPI) to communicate with desktop applications. Works in both X11 and
Wayland sessions (the latter via gnome-ponytail-daemon).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# upstream ships its unit tests as a top-level "tests" package
rm -rv %buildroot%python3_sitelibdir/tests/
find examples -type f -exec chmod 0644 {} \;

%files
%doc README.md NEWS CHANGES FAQ.md HERMETIC.md examples/
%_bindir/dogtail-create-config
%_bindir/dogtail-get-config
%_bindir/dogtail-headless
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Oct 07 2026 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0
- build with pyproject from the PyPI tarball, drop obsolete py2-to-py3 patch
- upstream dropped sniff, dogtail-run-headless* and pyatspi (uses Atspi via gi)
- new dogtail-headless, dogtail-create-config, dogtail-get-config scripts
- generate typelib requires with rpm-build-gir
- require typelib(Gtk) = 3.0 and typelib(Gdk) = 3.0 (not detected by gir-python.req)

* Mon Oct 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.11-alt2
- python2 -> python3

* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.11-alt1
- new version 0.9.11 (with rpmrb script)

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- new version 0.9.10 (with rpmrb script)

* Sat Jan 30 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt1
- new version 0.9.9 (with rpmrb script)

* Sat Nov 08 2014 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

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

