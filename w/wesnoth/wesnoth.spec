%define _unpackaged_files_terminate_build 1
#----------------------------------------------------------------------
# remove after fix
%add_findreq_skiplist /usr/share/wesnoth/data/tools/wmlunits

%define wessuffix %nil
#define wessuffix 16

%def_enable server
%if "%wessuffix" == ""
%def_enable tools
%def_enable python3module
%else
# tools use <import wesnoth. ...> and <from wesnoth import ...>
# so to use renamed tools we need to properly fix python imports
%def_disable tools
%def_disable python3module
%endif

%define _wesnothd_user     _wesnothd
%define _wesnothd_group    _wesnothd
%define _wesnothd_home     %_runtimedir/wesnothd%wessuffix

Name: wesnoth%wessuffix
Version: 1.16.7
Release: alt1
Group: Games/Strategy
Summary: 2D fantasy turn-based strategy
Summary(ru_RU.UTF-8): двухмерная пошаговая стратегия в стиле фэнтези
License: %gpl2plus
Url: http://www.wesnoth.org
VCS: git+https://github.com/wesnoth/wesnoth.git
Source0: wesnoth-%version.tar
Patch1: wesnoth-1.13.8-sdl2.02-alt-hack.patch

Requires: %name-data = %EVR

BuildRequires(pre): rpm-build-licenses

BuildRequires: gcc-c++
BuildRequires: scons
BuildRequires: libICE-devel libSDL2-devel libSDL2_image-devel libSDL2_mixer-devel libSDL2_net-devel libSDL2_ttf-devel libfreetype-devel libfribidi-devel libpango-devel libpng-devel xorg-cf-files liblua5-devel libpng-devel libdbus-devel libpixman-devel libXdmcp-devel libreadline-devel libvorbis-devel openssl-devel
BuildRequires: boost-devel boost-devel-headers boost-asio-devel boost-context-devel boost-coroutine-devel boost-filesystem-devel boost-locale-devel boost-program_options-devel
# docs
BuildRequires: asciidoc fribidi po4a xsltproc
# use BR to trigger systemd files or edit BoolVariable('systemd'...) in SConstruct
BuildRequires: /bin/systemctl

# used in spec
BuildRequires: ImageMagick-tools desktop-file-utils
# font symlinks
BuildRequires: fonts-ttf-dejavu fonts-ttf-google-lato

%if_disabled tools
Obsoletes: %name-tools < 1.13
%endif
%if_enabled python3module
BuildRequires: python3-devel rpm-build-python3
BuildRequires(pre): rpm-build-python3
Requires: python3-module-%name = %EVR
%else
AutoReq: yes,nopython,nopython3
%endif
Obsoletes: python-module-%name < 1.13

%description
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.

%description -l ru_RU.UTF-8
'Битва за Вэснот' это пошаговая стратегия в стите фэнтези.
Сражайся за контроль над деревнями, используя различные войска,
которые имеют свои преимущества и недостатки на разных типах
территорий и против разных типов атак. Войска получают опыт и повышают
уровни, переносимые на следующий сценарий в кампании.
Создай Героя и возглавь свою армию. Различные расы с различными
способностями, оружием и заклинаниями.


%package data
Group: Games/Strategy
Summary: Data files to Battle for Wesnoth
BuildArch: noarch
Conflicts: %name < 1.6.5-alt1
Conflicts: %name-editor < 1.13.0
Obsoletes: %name-editor < 1.13.0
%if_disabled python3module
AutoReq: yes,nopython,nopython3
%endif

%description data
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains data files to Battle for Wesnoth.


%package doc
Group: Documentation
Summary: Manual to Battle for Wesnoth
Provides: %name-manual = %version-%release
BuildArch: noarch

%description doc
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains manual to Battle for Wesnoth.


%if_enabled tools
%package tools
Group: Games/Strategy
Summary: Battle for Wesnoth tools
BuildArch: noarch
Requires: python3-module-%name = %EVR
# for utils/woptipng.py
Requires: optipng

%description tools
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains Battle for Wesnoth tools.
%endif


%if_enabled server
%package server
Group: Games/Strategy
Summary: %name server for multiplayer games
Summary(ru_RU.UTF-8): %name сервер для многопользовательских игр

%description server
Battle for Wesnoth multiplayer network daemon.

%description server -l ru_RU.UTF-8
Сервер для многопользовательских игр 'Битва за Вэснот'.
%endif

%if_enabled python3module
%package -n python3-module-%name
%py3_provides %name
Group: Development/Python3
Summary: Python3 interface to Battle for Wesnoth
BuildArch: noarch

%description -n python3-module-%name
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains python3 interface to Battle for Wesnoth.
%endif

%prep
%setup -n wesnoth-%version
%patch1 -p1

%build
%define _optlevel 3
# note for 1.10.5 - outdated.
# evil, evil... configure does not work, cmake does not build translations,
# note for 1.10.7 - upstream really moved to scons.
# scons now works. cmake is outdated and does not build campaignd.
scons all \
      	  prefix=%{_prefix} \
          bindir=%{_bindir} \
          libdir=%{_libdir} \
	  fifodir=%_wesnothd_home \
	  datadirname=%name \
	  docdir=%_docdir/%name \
          extra_flags_release="%optflags" \
          python_site_packages_dir=%{python3_sitelibdir_noarch}/%{name} \
          %{?_smp_mflags}

# ignore: it just renames datadirname/translations to datadirname/locale
#          localedirname=locale \

bzip2 --keep --best --force changelog*

%install

# scons install
scons install install-pytools destdir=$RPM_BUILD_ROOT

%if "%name" != "wesnoth"
for i in wesnoth wesnoth_addon_manager wmlindent wmllint wmlscope \
 ; do
    [ -e %buildroot%_bindir/$i ] && mv %buildroot%_bindir/$i %buildroot%_bindir/${i}%wessuffix
done
mv %buildroot%_desktopdir/org.wesnoth.Wesnoth{,%wessuffix}.desktop
mv %buildroot%_datadir/metainfo/org.wesnoth.Wesnoth{,%wessuffix}.appdata.xml
mv %buildroot%_iconsdir/HighContrast/scalable/apps/{wesnoth,%name}-icon.svg

find %buildroot%_mandir -name wesnoth.6 -execdir mv {} wesnoth%wessuffix.6 \;
find %buildroot%_mandir -name wesnothd.6 -execdir mv {} wesnothd%wessuffix.6 \;
sed -i -e 's,Exec=wesnoth,Exec=wesnoth%wessuffix,;s,^\(Name.*\),\1 (Ver. %version),' %buildroot%_desktopdir/org.wesnoth.Wesnoth%{wessuffix}.desktop
%endif #wessuffix

# move to sbin
install -d -m 0755 %buildroot%_sbindir
[ -e %buildroot%_bindir/wesnothd ] && mv %buildroot{%_bindir/wesnothd,%_sbindir/wesnothd%wessuffix}
[ -e %buildroot%_bindir/campaignd ] && mv %buildroot{%_bindir/campaignd,%_sbindir/campaignd%wessuffix}

mkdir -p %buildroot%_docdir/%name-%version/manual
mv %buildroot%_docdir/%name/* %buildroot%_docdir/%name-%version/manual/
install -m 0644 README.md copyright changelog.* %buildroot%_docdir/%name-%version/

mkdir -p packaging/icons/hicolor/48x48/apps/
for s in 48; do convert -depth 8 -resize ${s}x$s packaging/icons/hicolor/{64x64,${s}x${s}}/apps/wesnoth-icon.png
done
# remove wesnoth-icon
rm -rf %buildroot%_iconsdir/hicolor/
for s in 16 32 48 64 128 256; do
    install -D -m 0644 packaging/icons/hicolor/${s}x${s}/apps/wesnoth-icon.png \
    %buildroot%_iconsdir/hicolor/${s}x$s/apps/%{name}-icon.png
done

sed -i 's/wesnoth-icon/%{name}-icon/' %buildroot%_desktopdir/org.wesnoth.Wesnoth%wessuffix.desktop

mkdir -p %buildroot%_sysconfdir/sysconfig/
cat > %buildroot%_sysconfdir/sysconfig/wesnoth%wessuffix <<'EOF'
#
# wesnothd(6) options. Pick a custom port here if needed, for example.
#
WESNOTHD_OPTIONS=""
EOF

rm -rf %buildroot/usr/lib/{systemd,tmpfiles.d}

mkdir -p %buildroot%_tmpfilesdir/
cat > %buildroot%_tmpfilesdir/wesnothd%wessuffix.conf <<'EOF'
d %_wesnothd_home 0700 %_wesnothd_user %_wesnothd_group -
EOF
install -D -m 644 ./packaging/systemd/wesnothd.conf %buildroot%_tmpfilesdir/wesnothd%{wessuffix}.conf
##### backport specific ###############
mkdir -p %buildroot%_unitdir/
cat > %buildroot%_unitdir/wesnothd%wessuffix.service <<'EOF'
[Unit]
Description=Wesnoth multiplayer game server
After=network.target

[Service]
EnvironmentFile=-/etc/sysconfig/wesnoth%wessuffix
Type=forking
User=%_wesnothd_user
ExecStartPre=/bin/mkdir -p /var/run/wesnothd%wessuffix/
ExecStartPre=/bin/chown -R %_wesnothd_user.%_wesnothd_group /var/run/wesnothd%wessuffix/
ExecStart=/usr/sbin/wesnothd%wessuffix --daemon $WESNOTHD_OPTIONS

[Install]
WantedBy=multi-user.target
EOF
##### backport specific ###############


%find_lang --with-man wesnoth%wessuffix
%find_lang --with-man wesnothd%wessuffix
%if "%name" != "wesnoth"
%find_lang wesnoth
%find_lang wesnothd
cat wesnoth.lang >> %name.lang
cat wesnothd.lang >> wesnothd%{wessuffix}.lang
rm -f wesnoth.lang wesnothd.lang
%endif

for d in %buildroot%_datadir/%name/translations/*; do
    l=$(basename "$d")
    c=${l:0:2}
    echo "%%lang($c) %%dir %_datadir/%name/translations/$l" >> %name.lang
    echo "%%lang($c) %%dir %_datadir/%name/translations/$l/LC_MESSAGES" >> %name.lang
    [ -f $d/LC_MESSAGES/wesnoth.mo ] && echo "%%lang($c) %_datadir/%name/translations/$l/LC_MESSAGES/wesnoth.mo" >> %name.lang
    for i in ai anl aoi did dm editor ei httt l lib low multiplayer nr sof sotbe tb test thot trow tsg tutorial units utbs dw help manpages manual sota wc; do
	[ -f $d/LC_MESSAGES/wesnoth-$i.mo ] && echo "%%lang($c) %_datadir/%name/translations/$l/LC_MESSAGES/wesnoth-$i.mo" >> %name.lang
    done
done
for f in %buildroot%_datadir/%name/data/languages/*_*.cfg; do
    l=$(basename "$f")
    echo "%%lang(${l:0:2}) %_datadir/%name/data/languages/$l" >> %name.lang
done
#    /usr/share/wesnoth/data/languages/racv.cfg
echo "%%lang(racv) %_datadir/%name/data/languages/racv.cfg" >> %name.lang
#    /usr/share/wesnoth/data/languages/en@shaw.cfg
echo "%%lang(en) %_datadir/%name/data/languages/en@shaw.cfg" >> %name.lang


for f in \
    dejavu/DejaVuSans-Bold.ttf dejavu/DejaVuSansMono-Bold.ttf dejavu/DejaVuSansMono.ttf dejavu/DejaVuSans-Oblique.ttf dejavu/DejaVuSans.ttf \
    lato/Lato-BlackItalic.ttf lato/Lato-Black.ttf lato/Lato-BoldItalic.ttf lato/Lato-Bold.ttf lato/Lato-HeavyItalic.ttf lato/Lato-Heavy.ttf lato/Lato-Italic.ttf lato/Lato-LightItalic.ttf lato/Lato-Light.ttf lato/Lato-MediumItalic.ttf lato/Lato-Medium.ttf lato/Lato-Regular.ttf lato/Lato-SemiboldItalic.ttf lato/Lato-Semibold.ttf lato/Lato-ThinItalic.ttf lato/Lato-Thin.ttf \
	 ; do
    rm %buildroot%_datadir/wesnoth/fonts/$(basename $f)
    ln -s /usr/share/fonts/ttf/$f %buildroot%_datadir/wesnoth/fonts/$(basename $f)
done

%if_disabled tools
rm -rf %buildroot%_bindir/wesnoth_addon_manager%wessuffix \
   %buildroot%_bindir/wmlindent%wessuffix \
   %buildroot%_bindir/wmllint%wessuffix \
   %buildroot%_bindir/wmlscope%wessuffix
%endif

# not enough python modules installed
# NEW unmet dependencies detected:
#wesnoth-tools#1.16.0-alt1:sisyphus+289107.100.1.1@1636225396  python3(pywmlx) < 0
#wesnoth-tools#1.16.0-alt1:sisyphus+289107.100.1.1@1636225396  python3(wesnoth.trackplacer3) < 0
rm -rf %buildroot{/usr/lib/python/site-packages/,%python3_sitelibdir_noarch}
%if_enabled python3module
mkdir -p %buildroot/%python3_sitelibdir_noarch
mv %buildroot%_datadir/%name/data/tools/wesnoth %buildroot%_datadir/%name/data/tools/pywmlx \
   %buildroot%python3_sitelibdir_noarch/
%endif

%if_enabled server
%pre server
/usr/sbin/groupadd -r -f %_wesnothd_group ||:
/usr/sbin/useradd -g %_wesnothd_group -c 'Wesnoth server' \
        -d %_wesnothd_home -s /dev/null -r %_wesnothd_user >/dev/null 2>&1 ||:

%preun server
%preun_service wesnothd%wessuffix

%post server
%post_service wesnothd%wessuffix
%endif

%files
%_bindir/%name

%files data -f %name.lang
%_desktopdir/org.wesnoth.Wesnoth%wessuffix.desktop
%_datadir/metainfo/org.wesnoth.Wesnoth%wessuffix.appdata.xml
%_iconsdir/hicolor/*/apps/%{name}-icon.png
%_iconsdir/HighContrast/*/apps/%{name}-icon.*
%dir %_docdir/%name-%version
%doc %_docdir/%name-%version/README.md
%doc %_docdir/%name-%version/copyright
%doc %_docdir/%name-%version/changelog.*
%dir %_datadir/%name
%_datadir/%name/fonts
%_datadir/%name/images
%_datadir/%name/sounds
%dir %_datadir/%name/translations
%dir %_datadir/%name/data
%_datadir/%name/data/COPYING.txt
%_datadir/%name/data/ai/
%_datadir/%name/data/campaigns
%_datadir/%name/data/core
%_datadir/%name/data/gui/
%_datadir/%name/data/hardwired
%_datadir/%name/data/modifications
%_datadir/%name/data/multiplayer
%_datadir/%name/data/schema
%_datadir/%name/data/themes
%_datadir/%name/data/lua
%_datadir/%name/data/test
%_datadir/%name/data/*.cfg
%dir %_datadir/%name/data/languages
%_man6dir/%name.6*
%if_disabled tools
%_datadir/%name/data/tools
%endif

%files doc
%dir %_docdir/%name-%version
/%_docdir/%name-%version/manual

%if_enabled tools
%files tools
%_bindir/wesnoth_addon_manager%wessuffix
%_bindir/wml*
%dir %_datadir/%name
%dir %_datadir/%name/data
%_datadir/%name/data/tools
%endif

%if_enabled python3module
%files -n python3-module-%name
%python3_sitelibdir_noarch/wesnoth
%python3_sitelibdir_noarch/pywmlx
%endif

%if_enabled server
%files server -f wesnothd%{wessuffix}.lang
%_sbindir/wesnothd%wessuffix
%_sbindir/campaignd%wessuffix
%_unitdir/wesnothd%wessuffix.service
%_tmpfilesdir/wesnothd%{wessuffix}.conf
%config(noreplace) %_sysconfdir/sysconfig/wesnoth%wessuffix
%_man6dir/wesnothd%{wessuffix}.6*
%endif

%changelog
* Mon Jan 16 2023 Igor Vlasenko <viy@altlinux.org> 1.16.7-alt1
- new version

* Thu Sep 29 2022 Igor Vlasenko <viy@altlinux.org> 1.16.6-alt1
- new version

* Wed Sep 14 2022 Ivan A. Melnikov <iv@altlinux.org> 1.16.3-alt2
- NMU: fix build with recent boost

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 1.16.3-alt1
- new version

* Tue May 10 2022 Igor Vlasenko <viy@altlinux.org> 1.16.2-alt1
- new version

* Sat Jan 08 2022 Igor Vlasenko <viy@altlinux.org> 1.16.1-alt1
- new version

* Sun Nov 07 2021 Igor Vlasenko <viy@altlinux.org> 1.16.0-alt1
- new version

* Fri Nov 05 2021 Igor Vlasenko <viy@altlinux.org> 1.16.0-alt0.1
- pre-release of new branch 1.16.

* Wed Nov 03 2021 Igor Vlasenko <viy@altlinux.org> 1.14.17-alt1
- new version

* Thu May 13 2021 Igor Vlasenko <viy@altlinux.org> 1.14.16-alt1
- new version

* Sun Jan 17 2021 Igor Vlasenko <viy@altlinux.ru> 1.14.15-alt1
- new version

* Tue Aug 11 2020 Igor Vlasenko <viy@altlinux.ru> 1.14.13-alt1
- new version

* Thu Apr 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.14.11-alt1
- new version

* Wed Dec 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.14.5-alt3
- Rebuilt with boost-1.71.0.

* Tue Feb 12 2019 Igor Vlasenko <viy@altlinux.ru> 1.14.5-alt2
- added gcc8 patch

* Mon Feb 11 2019 Igor Vlasenko <viy@altlinux.ru> 1.14.5-alt1
- 1.14.5

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.14.3-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jun 13 2018 Igor Vlasenko <viy@altlinux.ru> 1.14.3-alt0.M80P.1
- backport

* Wed Jun 13 2018 Igor Vlasenko <viy@altlinux.ru> 1.14.3-alt1
- 1.14.3

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.14.2-alt0.M80P.1
- backport

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 1.14.0-alt1
- 1.14 release (closes: #34875)

* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.13.10-alt1
- 1.14 Beta 2

* Thu Oct 05 2017 Igor Vlasenko <viy@altlinux.ru> 1.13.8-alt1
- 1.14 Beta 1

* Tue Oct 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.6-alt0.M80P.1
- backport

* Tue Oct 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.6-alt1
- 1.20.6 stable release

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.5-alt1
- 1.20.5 stable release

* Fri Aug 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.12.4-alt1
- 1.20.4 stable release

* Tue Feb 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1
- 1.20.1 stable release

* Fri Jan 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1
- 1.20 release

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.11.15-alt1.1
- rebuild with boost 1.57.0;
- fix includes for Boost.Optional.

* Tue May 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.11.15-alt1
- 1.12 beta 5

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.11.13-alt2
- bugfix release

* Fri May 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.11.13-alt1
- 1.12 beta 3

* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.10.7-alt1
- new version
- use scons for build
- native systemd support
- wesnothd is now run under _wesnothd pseudo user.

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.10.5-alt1
- update to 1.10.5
- linked sazanami fonts
- added missing optional BR: libpixman-devel libXdmcp-devel
- fixed localization packaging (closes: 28689)
- note: #28689 was introduced in 1.10.2-alt1.1 by using cmake.
  tried to fix it using scons, but due to lack of schema_validator,
  used -DGETTEXT_FOUND=ON cmake hack

* Sat Dec 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt1.1
- Rebuilt with Boost 1.52.0

* Thu Apr 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.2-alt1
- 1.10.2

* Thu Mar 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Mon Jan 30 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Fri Jan 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.4-alt1
- 1.9.4 (1.10-rc1)

* Tue Aug 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.6-alt2
- rebuild with boost-1.47

* Tue May 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.6-alt1
- 1.8.6

* Wed Mar 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.5-alt3
- build repaired

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.5-alt2
- rebuild with boost-1.45

* Tue Sep 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.5-alt1
- 1.8.5

* Fri Aug 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Fri Jul 09 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Mon Jun 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Fri May 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Sat Apr 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.0-alt1
- 1.8.0 (ALT #23272)

* Tue Mar 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt3
- Enable fullscreen by default to hide (ALT #23150)
- Add condstop to wesnothd.init

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt2.1
- Rebuilt with python 2.6

* Thu Oct 08 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt2
- add conflict with old package to data subpackage

* Thu Sep 24 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Sun Dec 28 2008 Led <led@altlinux.ru> 1.4.7-alt1.2
- add subpackage ais

* Sat Dec 27 2008 Led <led@altlinux.ru> 1.4.7-alt1.1
- cleaned up spec

* Fri Dec 19 2008 Ilya Mashkin <oddity@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Mon Oct 27 2008 Ilya Mashkin <oddity@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 1.4.0-alt2
- rebuild
- update requires

* Mon Mar 17 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.4.0-alt1
- new stable release

* Thu Feb 28 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.16-alt2
- boost depend added

* Wed Feb 20 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.16-alt1
- new development version

* Fri Nov 30 2007 Gleb Stiblo <ulfr@altlinux.ru> 1.3.11-alt1
- new development version

* Wed Sep 26 2007 Gleb Stiblo <ulfr@altlinux.ru> 1.3.7-alt1
- new version

* Mon Jun 04 2007 Gleb Stiblo <ulfr@altlinux.ru> 1.3.3-alt1
- new version

* Fri Jan 19 2007 Gleb Stiblo <ulfr@altlinux.ru> 1.2.1-alt1
- new version
- 10449 fix

* Fri Dec 15 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.13-alt1
- new version

* Tue Oct 10 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.11-alt1
- new version

* Tue Oct 03 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.10-alt1
- new version
- use fribidi

* Thu Jun 29 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.7-alt1
- new version

* Tue May 23 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.1.2-alt1
- new version

* Fri Dec 09 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0.2-alt1
- new version

* Wed Oct 26 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0.1-alt1
- new verison

* Mon Oct 10 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0-alt3
- added .spec

* Fri Oct 07 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0-alt2
- temporary removed soundwrapper
- long title fixed

* Tue Oct 04 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.0-alt1
- 1.0 release

* Mon Aug 22 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.5-alt1
- new upstream version

* Tue Jul 26 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.4-alt1
- new upstream version

* Tue Jul 12 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.3-alt1
- user interface improvements
- updated translations and documentation
- campaigns and units fixing and balancing
- some new unit and terrains graphics

* Thu Jun 09 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.2-alt1
- lots of improvements in the user interface.
- several bugs in campaigns have already been fixed and
  lots of new death animations.
- the Drakes get reinforcements, with their new level 3 units.
- there are also a great number of changes regarding
  multiplayer balancement and most multiplayer maps have
  been replaced by new ones.

* Wed May 04 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.1-alt1
- New upstream version
- Many bugs have been fixed

* Wed Apr 13 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.9.0-alt1
- new release
- init script for server

* Tue Mar 01 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.8.11-alt1
- new bugfix release

* Tue Feb 08 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.8.10-alt1
- new release

* Wed Jan 26 2005 Gleb Stiblo <ulfr@altlinux.ru> 0.8.9-alt1
- new version

* Mon Oct 18 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.8-alt2
- menu group fixed

* Tue Jul 06 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.8-alt1
- new version

* Mon May 03 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.7-alt2
- glibc 2.3 build

* Wed Mar 24 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.7-alt1
- Ver 0.7
- New maps, new units, new music. A lot of fixes and improvements

* Fri Jan 30 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.6.1-alt1
- ver 0.6.1.

* Thu Jan 29 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.4.8-alt1
- ALT adaptations.

