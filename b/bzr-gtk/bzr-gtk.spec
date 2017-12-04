Packager: Anatoly Kitaikin <cetus@altlinux.ru>
Name:           bzr-gtk
Version:        0.104.0
Release:        alt2.bzr20161127
Summary:        Bazaar plugin for GTK+ interfaces to most Bazaar operations

Group:          Development/Other
License:        GPLv2+
URL:            https://launchpad.net/bzr-gtk
Source0:        bzr-gtk-%version.tar
Patch0:         bzr-gtk-%version.patch
Patch1:         bzr-gtk-gi.require_version.patch

BuildRequires:  python-devel
BuildRequires:  bzr
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
Requires:       bzr >= 2.0
Requires:       libgtk+3-gir
Requires:       libgtksourceview3-gir

%description
bzr-gtk is a plugin for Bazaar that aims to provide GTK+ interfaces to most
Bazaar operations.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="%optflags" %__python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

#desktop-file-validate bazaar-properties.desktop
#desktop-file-validate bzr-handle-patch.desktop
#desktop-file-validate olive-gtk.desktop
%__python setup.py install --skip-build --root $RPM_BUILD_ROOT

# hack :(  
if test "%_libdir" != "/usr/lib" ; then
    install -d -m 0755 $RPM_BUILD_ROOT%python_sitelibdir
    mv $RPM_BUILD_ROOT/usr/lib/python*/site-packages/* $RPM_BUILD_ROOT/%python_sitelibdir/
fi

pkg-config --variable=pythondir nautilus-python || rm -f $RPM_BUILD_ROOT/%python_sitelibdir/bzrlib/plugins/gtk/nautilus-bzr.*

%find_lang olive-gtk

# This won't do anything until after we add bzr-dbus.
rm -rf $RPM_BUILD_ROOT/%_datadir/applications/bzr-notify.desktop

%files -f olive-gtk.lang
%doc COPYING README
%_bindir/*
%_datadir/applications/*
%_datadir/application-registry/bzr-gtk.applications
#_datadir/olive/
%_datadir/bzr-gtk/
%_datadir/pixmaps/*.png
%_datadir/icons/hicolor/scalable/emblems/
%_datadir/icons/hicolor/scalable/apps/
%python_sitelibdir/bzrlib/plugins/gtk/
%python_sitelibdir/*.egg-info

%changelog
* Mon Dec 04 2017 Anatoly Kitaykin <cetus@altlinux.org> 0.104.0-alt2.bzr20161127
- Upgrade to 2016-11-27 snapshot

* Mon Dec 04 2017 Anatoly Kitaykin <cetus@altlinux.org> 0.104.0-alt1
- Upgrade to 0.104.0

* Mon Dec 04 2017 Anatoly Kitaykin <cetus@altlinux.org> 0.103.0-alt1
- Upgrade to 0.103.0
- Remove bzr-gtk-disable-nautilus-pull.patch

* Mon Dec 04 2017 Anatoly Kitaykin <cetus@altlinux.org> 0.100.0-alt2
- Rebuild with remastered gear repo
- Convert upstream to checkout
- Spec cleanup

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.100.0-alt1.1
- Rebuild with Python-2.7

* Fri Oct 07 2011 Anatoly Kitaikin <cetus@altlinux.org> 0.100.0-alt1
- 0.100.0 release

* Wed Feb 17 2010 Igor Vlasenko <viy@altlinux.ru> 0.97.0-alt1
- new version

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95.0-alt1.1.1
- Rebuilt with python 2.6

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.95.0-alt1.1
- NMU (by repocop): the following fixes applied:

* Mon Oct 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.95.0-alt1
- first build
