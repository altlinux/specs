Name: mirage
Version: 0.9.5.2
Release: alt1

Summary: A fast and simple PyGTK image viewer.
License: %gpl3plus
Group: Graphics
Url: http://mirageiv.sourceforge.net/

Source: http://downloads.sf.net/mirageiv/%name-%version.tar.bz2

# fc patchset
# Fix bug 559853, backtrace when clicking middle button in some case
# Must be sent to upstream
Patch: mirage-0.9.3-prevmouse-not-defined-with-click.patch
# Don't call gtk.gdk.threads_init() on GLib >= 2.41,
# workaround for bug 1123953
Patch1: mirage-0.9.5.2-glib241-init-workaround.patch

Requires: python-module-pygnome-gconf

BuildPreReq: rpm-build-licenses

# From setup.py
BuildPreReq: python-module-pygtk-devel >= 2.6.0
BuildPreReq: libX11-devel
BuildRequires: desktop-file-utils

%description
Mirage is a fast and simple GTK+ image viewer. Because it depends only on
PyGTK, Mirage is ideal for users who wish to keep their computers lean
while still having a clean image viewer.

Features:
- Supports png, jpg, svg, xpm, gif, bmp, tiff, and others
- Cycling through multiple images (with preloading)
- Slideshow and fullscreen modes
- Rotating, zooming, flipping, resizing, cropping
- Saving, deleting, renaming
- Custom actions
- Command-line access
- Configurable interface.

%prep
%setup
%patch -p1
%patch1 -p1

%build
env CFLAGS="%optflags" python setup.py build

%install
python setup.py install --root=%buildroot --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%python_sitelibdir/*.py*
%_desktopdir/%name.desktop

%changelog
* Tue Jun 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.9.5.2-alt1
- 0.9.5.2 (new url)

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt1.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.2
- Rebuilt with python 2.6

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for mirage

* Sun Feb 03 2008 Grigory Batalov <bga@altlinux.ru> 0.9.2-alt1.1
- Rebuilt with python-2.5.

* Tue Jan 29 2008 Alexey Rusakov <ktirf@altlinux.org> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)

* Fri Jan 11 2008 Alexey Rusakov <ktirf@altlinux.org> 0.9.1-alt1
- New version (0.9.1).
- Updated buildreqs.

* Thu Oct 18 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9-alt1
- New version (0.9).
- Updated the license to %gpl3plus.
- Updated the files list (.desktop file has been added); added %%post and
  %%postun scripts to update menus of legacy WMs.

* Thu Aug 30 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8.3-alt1
- new version (0.8.3)

* Sun Oct 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.8-alt1
- Initial Sisyphus package.

