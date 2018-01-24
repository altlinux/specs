Name: eric6
Summary: Python IDE
Version: 18.01
Release: alt1%ubt

License: GPLv3+
Group: Development/Python
Url: http://eric-ide.python-projects.org
Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch

Source: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-%version.tar.gz
Source1: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-cs-%version.tar.gz
Source2: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-de-%version.tar.gz
Source3: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-en-%version.tar.gz
Source4: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-es-%version.tar.gz
Source5: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-fr-%version.tar.gz
Source6: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-it-%version.tar.gz
Source7: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-pt-%version.tar.gz
Source8: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-ru-%version.tar.gz
Source9: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-tr-%version.tar.gz
Source10: http://downloads.sourceforge.net/sourceforge/eric-ide/%name-i18n-zh_CN-%version.tar.gz

Source30: eric-32.png
Source31: eric-48.png
Source32: eric-64.png

# sane defaults: disable version check, qt4/qt5 configuration
Patch1: eric6-17.11-defaults.patch

BuildRequires(pre): rpm-build-python3 rpm-build-ubt
BuildRequires: desktop-file-utils
BuildRequires: python3-devel
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-qscintilla2-qt5
BuildRequires: libappstream-glib
%py3_requires PyQt5.Qsci
%py_requires json

# ???
%add_python3_req_skip __builtin__ mod_python

%description
eric6 is a full featured Python IDE.

%prep
%setup -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -n eric6-%version

%patch1 -p1

%build
# Empty build

%install
python3 install.py \
  -i %buildroot/ \
  -b %_bindir \
  -d %python3_sitelibdir

# icons
install -m644 -p -D %SOURCE30 %buildroot%_iconsdir/hicolor/32x32/apps/eric.png
install -m644 -p -D %SOURCE31 %buildroot%_iconsdir/hicolor/48x48/apps/eric.png
install -m644 -p -D %SOURCE32 %buildroot%_iconsdir/hicolor/64x64/apps/eric.png

%find_lang %name --with-qt --all-name

# use legacy appdata dir instead of metainfo
if [ -d %buildroot%_datadir/metainfo ]; then
mkdir -p %buildroot%_datadir/appdata/
mv %buildroot%_datadir/metainfo/*.xml \
%buildroot%_datadir/appdata/
fi

## unpackaged files
# deprecated icons
rm -rfv %buildroot%_pixmapsdir/eric*
rm -fv  %buildroot%python3_sitelibdir/eric6/LICENSE.GPL3

%check
appstream-util validate-relax --nonet %buildroot%_datadir/appdata/eric6.appdata.xml
desktop-file-validate %buildroot%_desktopdir/eric6.desktop
desktop-file-validate %buildroot%_desktopdir/eric6_browser.desktop
desktop-file-validate %buildroot%_desktopdir/eric6_webbrowser.desktop

%files -f %name.lang
%doc eric/README* THANKS LICENSE.GPL3
%_bindir/eric6*
%python3_sitelibdir/eric6config.py*
%python3_sitelibdir/__pycache__/*
%dir %python3_sitelibdir/eric6/
%python3_sitelibdir/eric6/*.py*
%python3_sitelibdir/eric6/__pycache__/
%python3_sitelibdir/eric6/icons/
%python3_sitelibdir/eric6/pixmaps/
%python3_sitelibdir/eric6/[A-Z]*/
%python3_sitelibdir/eric6/*.e4k
%dir %python3_sitelibdir/eric6/i18n/
%python3_sitelibdir/eric6plugins/
%_datadir/appdata/eric6.appdata.xml
%_desktopdir/eric6.desktop
%_desktopdir/eric6_browser.desktop
%_desktopdir/eric6_webbrowser.desktop
%_iconsdir/hicolor/*/apps/eric.*
%_datadir/qt5/qsci/api/python/*
%_datadir/qt5/qsci/api/qss/*
%_datadir/qt5/qsci/api/ruby/*

%changelog
* Wed Jan 24 2018 Anton Midyukov <antohami@altlinux.org> 18.01-alt1%ubt
- New version 18.01
- Added missing requires python(json)

* Mon Jan 15 2018 Anton Midyukov <antohami@altlinux.org> 17.11-alt2%ubt
- Added missing requires python3(PyQt5.Qsci)

* Mon Nov 13 2017 Anton Midyukov <antohami@altlinux.org> 17.11-alt1%ubt
- Initial build for ALT Sisyphus (Closes: 33933).
