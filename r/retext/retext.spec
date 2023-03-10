%def_without tests
%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name:    retext
Version: 7.2.3
Release: alt2
License: GPL-3.0+
Summary: Text editor for Markdown and reStructuredText
Summary(de): Texteditor für Markdown und reStructuredText
Group:   Editors
URL:     https://github.com/retext-project/retext

Source0: %name-%version.tar
Source1: %name.1

AutoProv:yes,nopython3

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): python3-devel
BuildRequires(pre): rpm-macros-qt5
BuildRequires: python3-module-setuptools
BuildRequires: /dev/pts
BuildRequires: python3-module-markups
BuildRequires: python3-module-docutils
BuildRequires: python3-module-enchant
BuildRequires: python3-module-markdown
BuildRequires: libpng-devel
BuildRequires: librsvg-devel
BuildRequires: librsvg-utils
BuildRequires: ImageMagick-tools
BuildRequires: qt5-tools-devel

%if_with tests
BuildRequires:  libappstream-glib
%endif

%py3_requires docutils enchant markdown mdx_math chardet pygments
%add_python3_req_skip FakeVim
%if_enabled qtwebengine
%add_python3_req_skip PyQt5.QtWebKit PyQt5.QtWebKitWidgets
%else
%add_python3_req_skip PyQt5.QtWebEngineCore PyQt5.QtWebEngineWidgets
%endif

%description
ReText is a simple but powerful text editor for Markdown and
reStructuredText.

%description -l de
ReText ist ein einfacher, aber leistungsfähiger Texteditor
für Markdown und reStructuredText.

%prep
%setup

%build
export PATH=%_qt5_bindir:$PATH
%python3_build_debug

%install
%python3_install
if [ "%python3_sitelibdir" != "%python3_sitelibdir_noarch" ] ; then
    mkdir -p %buildroot/%python3_sitelibdir
    mv %buildroot/%python3_sitelibdir_noarch/* %buildroot/%python3_sitelibdir/
fi

install -Dm 0644 %SOURCE1 %buildroot/%_man1dir/%name.1

# Generate resized icons
pushd icons
mkdir -p %buildroot/%_datadir/icons/hicolor/{16x16,22x22,24x24,32x32,48x48,64x64,72x72,96x96,128x128,scalable}/apps
for s in 16x16 22x22 24x24 32x32 48x48 64x64 72x72 96x96 128x128
do
    convert ./retext.png -resize $s %buildroot/%_datadir/icons/hicolor/$s/apps/retext.png
done
install -p -m 0644 retext.svg %buildroot/%_datadir/icons/hicolor/scalable/apps
popd

%find_lang retext --with-man

%check
%if_with tests
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/*.appdata.xml ||:
python3 setup.py test
%endif

%files -f retext.lang
%doc changelog.md configuration.md README.md LICENSE_GPL
%_bindir/%name
%_datadir/metainfo/*.appdata.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/%name/
%_man1dir/*.1*
%python3_sitelibdir/ReText/
%python3_sitelibdir/*egg-info

%changelog
* Fri Mar 10 2023 Andrey Cherepanov <cas@altlinux.org> 7.2.3-alt2
- Removed wrong requirement python3(sip).

* Fri Feb 04 2022 Andrey Cherepanov <cas@altlinux.org> 7.2.3-alt1
- New version.

* Thu Feb 03 2022 Sergey V Turchin <zerg@altlinux.org> 7.2.2-alt3
- build with qtwebkit instead of qtwebengine on e2k and ppc64le

* Wed Feb 02 2022 Sergey V Turchin <zerg@altlinux.org> 7.2.2-alt2
- Exclude e2k and ppc64le.

* Thu Oct 14 2021 Andrey Cherepanov <cas@altlinux.org> 7.2.2-alt1
- New version.

* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 7.2.1-alt2
- drop BR: python-module-PyQt5-devel
- skip WebKit requires (ALT bug 40361)
- disable python provides

* Mon Mar 08 2021 Andrey Cherepanov <cas@altlinux.org> 7.2.1-alt1
- New version.

* Tue Feb 09 2021 Andrey Cherepanov <cas@altlinux.org> 7.2.0-alt1
- New version.

* Fri Sep 25 2020 Andrey Cherepanov <cas@altlinux.org> 7.1.0-alt3
- Complete Russian translation (thanks Maria Shikunova).
- Remove desktop file duplicate.
- Move appdata file to %_datadir/metainfo directory.
- Fix build localization files.
- Add runtime module requirements.

* Tue Sep 15 2020 Andrey Cherepanov <cas@altlinux.org> 7.1.0-alt2
- Requires python3-module-Pygments.

* Sat Apr 04 2020 Andrey Cherepanov <cas@altlinux.org> 7.1.0-alt1
- New version.

* Mon Sep 24 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.4-alt1
- New version.

* Mon Jul 09 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt1
- New version.

* Wed May 16 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.1-alt1
- New version

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 10 2016 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- new version 6.0.2

* Wed Jul 13 2016 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- new version 6.0.1

* Tue May 17 2016 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 21 2016 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- Initial build in Sisyphus (based on Fedora spec)

