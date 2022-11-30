%def_without nautilus

Name: tortoisehg
Version: 6.3.1
Release: alt1

Summary: Mercurial GUI command line tool thg

License: GPLv2
# - few files are however under the more permissive GPLv2+
Group: Development/Other
Url: https://tortoisehg.bitbucket.io

Source: %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

Requires: python3-module-iniparse mercurial
Requires: python3-module-PyQt5 python3-module-qscintilla2-qt5 python3-module-Pygments
Requires: python3-module-pygobject

BuildRequires(pre): rpm-build-python3
BuildRequires: mercurial
BuildRequires: gettext python3-module-sphinx python3-module-PyQt5
BuildRequires: desktop-file-utils libappstream-glib

BuildArch: noarch

%add_python3_req_skip _winreg pythoncom comtypes comtypes.automation comtypes.client

%description
This package contains the thg command line tool, which provides a graphical
user interface to the Mercurial distributed revision control system.

%if_with nautilus
%package nautilus
Summary: Mercurial GUI plug-in to the Nautilus file manager
Group: Development/Other
Requires: %name = %EVR, python3-module-nautilus

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
%python3_build

%make SPHINXBUILD="sphinx-build-3" -C doc html

%install
%python3_install
rm %buildroot%python3_sitelibdir/hgext3rd/__init__.*

mkdir -p %buildroot%_sysconfdir/mercurial/hgrc.d
install -pm0644 contrib/mergetools.rc %buildroot%_sysconfdir/mercurial/hgrc.d/thgmergetools.rc

desktop-file-install --dir=%buildroot%_datadir/applications contrib/thg.desktop

rm -f %buildroot/%_datadir/doc/tortoisehg/COPYING.txt

%if_without nautilus
rm -rf %buildroot%_datadir/nautilus-python/extensions/nautilus-thg.py*
%endif

%find_lang %name

%files -f %name.lang
%doc doc/build/html/ COPYING.txt
%config(noreplace) %_sysconfdir/mercurial/hgrc.d/thgmergetools.rc
%_bindir/thg
%python3_sitelibdir/hgext3rd
%python3_sitelibdir/tortoisehg
%python3_sitelibdir/tortoisehg-*.egg-info
%_datadir/pixmaps/tortoisehg
%_datadir/pixmaps/thg_logo.svg
%_datadir/applications/thg.desktop

%if_with nautilus
%files nautilus
%_datadir/nautilus-python/extensions/nautilus-thg.py*
%endif

%changelog
* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 6.3.1-alt1
- Build new version.

* Mon Jul 25 2022 Grigory Ustinov <grenka@altlinux.org> 6.2-alt1
- Build new version.

* Tue Jan 11 2022 Grigory Ustinov <grenka@altlinux.org> 6.0-alt1
- Build new version.

* Mon Sep 13 2021 Grigory Ustinov <grenka@altlinux.org> 5.9.1-alt1
- Build new version.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 5.8-alt1
- Build new version.

* Fri Mar 19 2021 Grigory Ustinov <grenka@altlinux.org> 5.7.1-alt1
- Build new version.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 5.6-alt1
- Build new version.

* Thu Nov 05 2020 Grigory Ustinov <grenka@altlinux.org> 5.5.2-alt1
- Build new version.

* Thu Oct 01 2020 Grigory Ustinov <grenka@altlinux.org> 5.5.1-alt1
- Add watch file.
- Transfer on python3.
- Automatically updated to 5.5.1.

* Tue Jul 23 2019 Grigory Ustinov <grenka@altlinux.org> 5.0.2-alt1
- Build new version.

* Mon May 13 2019 Grigory Ustinov <grenka@altlinux.org> 4.9.1-alt2
- Update russian localization.

* Fri Apr 26 2019 Grigory Ustinov <grenka@altlinux.org> 4.9.1-alt1
- Build new version.

* Mon Mar 04 2019 Grigory Ustinov <grenka@altlinux.org> 4.9-alt1
- Build new version.

* Tue Jan 29 2019 Grigory Ustinov <grenka@altlinux.org> 4.8.2-alt1
- Build new version.

* Wed Dec 12 2018 Grigory Ustinov <grenka@altlinux.org> 4.8.1-alt1
- Build new version.
- Build without nautilus plugin, because it doesn't work.

* Sat Nov 17 2018 Grigory Ustinov <grenka@altlinux.org> 4.8-alt1
- Build new version.

* Thu Nov 08 2018 Grigory Ustinov <grenka@altlinux.org> 4.7.2-alt1
- Initial build for Sisyphus.
