%def_without nautilus

Name: tortoisehg
Version: 4.8.2
Release: alt1

Summary: Mercurial GUI command line tool thg

License: GPLv2
# - few files are however under the more permissive GPLv2+
Group: Development/Other
Url: https://tortoisehg.bitbucket.io

Source: %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

Requires: python-module-iniparse mercurial
# gconf needed at util/shlib.py for browse_url(url).
Requires: python-module-pygnome-gconf
Requires: python-module-PyQt5 python-module-qscintilla2-qt5 python-module-Pygments
Requires: python-module-pygobject

BuildRequires: python-devel gettext python-module-sphinx python-module-PyQt5
BuildRequires: python-module-enum34 desktop-file-utils libappstream-glib

BuildArch: noarch

%add_python_req_skip _winreg comtypes pythoncom

%description
This package contains the thg command line tool, which provides a graphical
user interface to the Mercurial distributed revision control system.

%if_with nautilus
%package nautilus
Summary: Mercurial GUI plug-in to the Nautilus file manager
Group: Development/Other
Requires: %name = %EVR, python-module-nautilus

%description nautilus
This package contains the TortoiseHg Gnome/Nautilus extension, which makes the
Mercurial distributed revision control system available in the file manager
with a graphical interface.

Note that the nautilus extension has been deprecated upstream.
%endif

%prep
%setup

cat > tortoisehg/util/config.py << EOT
bin_path     = "%_bindir"
license_path = "%_defaultdocdir/COPYING.txt"
locale_path  = "%_datadir/locale"
icon_path    = "%_datadir/pixmaps/tortoisehg/icons"
nofork       = True
EOT

%build
%python_build

(cd doc && make html)
rm doc/build/html/.buildinfo

%install
%python_install
rm %buildroot%python_sitelibdir/hgext3rd/__init__.*

mkdir -p %buildroot%_sysconfdir/mercurial/hgrc.d
install -pm0644 contrib/mergetools.rc %buildroot%_sysconfdir/mercurial/hgrc.d/thgmergetools.rc

ln -s tortoisehg/icons/scalable/apps/thg.svg %buildroot%_datadir/pixmaps/thg_logo.svg
desktop-file-install --dir=%buildroot%_datadir/applications contrib/thg.desktop

%find_lang %name

%files -f %name.lang
%doc doc/build/html/ COPYING.txt
%config(noreplace) %_sysconfdir/mercurial/hgrc.d/thgmergetools.rc
%_bindir/thg
%python_sitelibdir/hgext3rd/thg.py*
%python_sitelibdir/tortoisehg/
%python_sitelibdir/tortoisehg-*.egg-info
%_datadir/pixmaps/tortoisehg/
%_datadir/pixmaps/thg_logo.svg
%_datadir/applications/thg.desktop

%if_with nautilus
%files nautilus
%_datadir/nautilus-python/extensions/nautilus-thg.py*
%endif

%changelog
* Tue Jan 29 2019 Grigory Ustinov <grenka@altlinux.org> 4.8.2-alt1
- Build new version.

* Wed Dec 12 2018 Grigory Ustinov <grenka@altlinux.org> 4.8.1-alt1
- Build new version.
- Build without nautilus plugin, because it doesn't work.

* Sat Nov 17 2018 Grigory Ustinov <grenka@altlinux.org> 4.8-alt1
- Build new version.

* Thu Nov 08 2018 Grigory Ustinov <grenka@altlinux.org> 4.7.2-alt1
- Initial build for Sisyphus.
