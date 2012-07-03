Name: fusion-icon
Version: 0.1.0
Release: alt5

Summary: Compiz Fusion panel applet
License: %gpl2plus
Group: Graphical desktop/Other

URL: http://www.compiz.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

BuildRequires: python-devel

Requires: simple-ccsm %name-ui = %version-%release

%description
The Compiz Fusion Icon is a simple panel applet for starting and
controlling Compiz Fusion. Upon launch, it will attempt to start Compiz
Fusion automatically. You may need to select a window decorator, if one
does not appear.

%package -n python-module-%name-gtk
Requires: %name = %version-%release
Group: Graphical desktop/Other
Summary: GTK UI for fusion-icon
Provides: %name-ui = %version-%release

%description -n python-module-%name-gtk
This package provides the gtk UI for fusion-icon.

%package -n python-module-%name-qt4
Requires: %name = %version-%release
Group: Graphical desktop/Other
Summary: QT UI for fusion-icon
Provides: %name-ui = %version-%release
Provides: python-module-%name-qt
Obsoletes: python-module-%name-qt

%description -n python-module-%name-qt4
This package provides the qt UI for fusion-icon.

%prep
%setup
%patch -p1

%build
%make

%install
%makeinstall_std

%files
%_bindir/fusion-icon
%_desktopdir/*.desktop
%dir %python_sitelibdir/FusionIcon/
%python_sitelibdir/FusionIcon/*py*
%python_sitelibdir/fusion_icon-*.egg-info
%_iconsdir/hicolor/*/apps/fusion-icon.png
%_iconsdir/hicolor/scalable/apps/fusion-icon.svg
%_datadir/locale/*/*/%name.mo
/usr/lib/%name

%files -n python-module-%name-gtk
%python_sitelibdir/FusionIcon/interface_gtk/

%files -n python-module-%name-qt4
%python_sitelibdir/FusionIcon/interface_qt4/

%changelog
* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.0-alt5
- restore compiz in Sisyphus

* Wed Jun 22 2011 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt4.M60P.3
- Update Russian localization (tnx cas@).
- check-compiz-support.sh: Add localization support.
- Add check-compiz-support.sh to the package itself.

* Tue Jun 14 2011 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt4.M60P.2
- Replace ccsm with simple-ccsm.

* Fri Jun 10 2011 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt4.M60P.1
- Check hardware status before compiz start.

* Thu May 12 2011 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt4
- Don't use localized options names for log print.
- Whitespaces cleanup.

* Thu Apr 14 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.0-alt3
- Fix Russian translation

* Thu Apr 07 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.0-alt2
- Add localization support
- Add Russian translation
- Rename package python-module-fusion-icon-qt to
python-module-fusion-icon-qt4

* Mon Apr 04 2011 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- fusion-icon-runpatch.patch from Fedora.
- Fix for xfwm4-4.8.
- Localize .desktop file into Russian (by Andrey Cherepanov).
- Initial build (based on fedora spec).
