####### wesnoth >= 1.13  ##############
BuildRequires: boost-devel-headers
#######################################
####### wesnoth >= 1.12  ##############
BuildRequires: libvorbis-devel
#######################################

%define _unpackaged_files_terminate_build 1
%def_with build_using_scons
%def_with install_using_scons
%def_without install_using_manual
%def_without install_using_cmake
# remnants of configure, drop them later
%def_enable nls
%def_enable rpath
%def_disable debug
%def_disable tests
%def_disable static
%def_enable optipng
%def_enable game
%def_enable server
%def_disable editor
%def_disable python3
%def_disable python
%def_disable tools
%def_enable bandwidth_monitor
%def_enable sdltest
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%define _pseudouser_user     _wesnothd
%define _pseudouser_group    _wesnothd
%define _pseudouser_home     %_var/run/wesnothd

%define wessuffix %nil
#define wesdesktopsuffix %nil

Name: wesnoth%wessuffix
Version: 1.13.10
Release: alt1
Group: Games/Strategy
Summary: 2D fantasy turn-based strategy
Summary(ru_RU.UTF-8): двухмерная пошаговая стратегия в стиле фэнтези
License: %gpl2plus
Url: http://www.%name.org
Source0: wesnoth-%version.tar
Patch0: wesnoth-1.13.8-sdl2.02.patch
Patch1: wesnoth-1.13.8-sdl2.02-alt-hack.patch

Requires: %name-data = %version-%release

BuildRequires(pre): rpm-build-licenses

BuildRequires: ImageMagick-tools asciidoc boost-devel desktop-file-utils fribidi gcc-c++ hd2u imake libICE-devel libSDL2-devel libSDL2_image-devel libSDL2_mixer-devel libSDL2_net-devel libSDL2_ttf-devel libfreetype-devel libfribidi-devel libpango-devel libpng-devel po4a subversion xorg-cf-files xsltproc liblua5-devel libpng-devel cmake boost-program_options-devel boost-filesystem-devel boost-locale-devel libdbus-devel boost-asio-devel libpixman-devel libXdmcp-devel libreadline-devel openssl-devel
%if_with build_using_scons
BuildRequires: scons
%endif

BuildRequires: fonts-ttf-dejavu fonts-ttf-sazanami-gothic fonts-ttf-wqy-zenhei
%{?_enable_optipng:BuildRequires: optipng}

%if_disabled tools
Obsoletes: %name-tools < 1.13
%endif
%if_enabled python
%if_enabled python3
BuildRequires: python3-devel rpm-build-python3
BuildRequires(pre): rpm-build-python3
Requires: python3-module-%name = %version-%release
Obsoletes: python-module-%name < 1.13
%else
BuildRequires: python-devel
Requires: python-module-%name = %version-%release
Conflicts: %name-tools < 1.11.7
%endif
%else
Obsoletes: python-module-%name < 1.13
AutoReq: yes,nopython,nopython3
%endif

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
%if_disabled python
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


%if_enabled editor
%package editor
Group: Games/Strategy
Summary: Battle for Wesnoth map editor
BuildArch: noarch
#
%description editor
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains Battle for Wesnoth map editor.
%endif


%if_enabled tools
%package tools
Group: Games/Strategy
Summary: Battle for Wesnoth tools
%if_enabled python
%if_enabled python3
Requires: python3-module-%name = %version-%release
%else
Requires: python-module-%name = %version-%release
%endif
%endif

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

%if_enabled python
%if_enabled python3
%package -n python3-module-%name
%py3_provides %name
%else
%package -n python-module-%name
%py_provides %name
%endif
Group: Development/Python
Summary: Python interface to Battle for Wesnoth
BuildArch: noarch

%if_enabled python3
%description -n python3-module-%name
%else
%description -n python-module-%name
%endif
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which have
advantages and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.
Build a Hero, and lead your army. Different races, with distinctive
abilities, weapons and spells.
This package contains python interface to Battle for Wesnoth.
%endif

%prep
%setup -n wesnoth-%version
%patch -p1
%patch1 -p1

%build
%define _optlevel 3
# note for 1.10.5 - outdated.
# evil, evil... configure does not work, cmake does not build translations,
# note for 1.10.7 - upstream really moved to scons.
# scons now works. cmake is outdated and does not build campaignd.
%if_with build_using_scons
scons all \
      	  prefix=%{_prefix} \
          bindir=%{_bindir} \
          libdir=%{_libdir} \
	  fifodir=%_runtimedir/wesnothd%wessuffix \
	  datadirname=%name \
	  docdir=%_docdir/%name \
          extra_flags_release="%optflags" \
%if_enabled python
%if_enabled python3
          python_site_packages_dir=%{python3_sitelibdir_noarch}/%{name} \
%else
          python_site_packages_dir=%{python_sitelibdir_noarch}/%{name} \
%endif
%endif
          %{?_smp_mflags}

# TODO
#	localedirname=locale \

#	  version_suffix=%wessuffix \

	  # let it be default - translations - for now, for cmake install compatibility
	  #localedirname=locale \
%else
export PYTHON_PREFIX=/usr
%if_enabled python3
export PYTHON_VERSION=%__python3_version
%else
export PYTHON_VERSION=%__python_version
%endif
#%%configure \
#    --disable-option-checking \
#    --with-gnu-ld \
#    %{subst_enable nls} \
#    %{subst_enable rpath} \
#    %{subst_enable debug} \
#    %{subst_enable tests} \
#    %{subst_enable static} \
#    %{subst_enable python} \
#    %{subst_enable optipng} \
#    %{subst_enable game} \
#    %{subst_enable server} \
#    %{subst_enable editor} \
#    %{subst_enable tools} \
#    %{subst_enable_to display_revision display-revision} \
#    %{subst_enable sdltest} \

cmake . \
	-DCMAKE_INSTALL_PREFIX=%buildroot%_prefix \
	-DCMAKE_C_FLAGS="%optflags" \
	-DCMAKE_CXX_FLAGS="%optflags" \
	-DDATAROOTDIR=%_datadir \
	-DDATADIRNAME=%name \
	-DDOCDIR=%_docdir/%name \
	-DFIFO_DIR=%_runtimedir/wesnothd%wessuffix \
	-DBINDIR=%_bindir \
	-DENABLE_TOOLS=ON \
	-DENABLE_NLS=ON \
 	-DGETTEXT_FOUND=ON \
 	-DENABLE_STRICT_COMPILATION=OFF \
	-DCMAKE_INSTALL_PREFIX=%buildroot

#-DSERVER_UID=%name \

%make_build VERBOSE=1
%endif # scons

for s in 96 72 48 36 32 24 22 16; do
    convert -depth 8 -resize ${s}x$s icons/wesnoth-{icon,$s}.png
#    convert -depth 8 -resize ${s}x$s icons/{map-editor-icon-Mac,wesnoth_editor-$s}.png
done
bzip2 --keep --best --force changelog

%install

%if_with install_using_cmake
# cmake install
%make_install \
    DESTDIR=%buildroot \
    docdir=%_docdir/%name-%version \
    appentrydir=%_desktopdir \
    install
%else

%if_with install_using_scons
# scons install
scons install install-pytools destdir=$RPM_BUILD_ROOT
rm %buildroot%{_datadir}/icons/wesnoth-icon.png
rm %buildroot%_desktopdir/wesnoth.desktop
rm -rf %buildroot/usr/lib/python/site-packages/%name
rm -rf %buildroot%{python3_sitelibdir_noarch}/%{name}
%endif

%if_with install_using_manual
# manual install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sbindir
for i in cutter exploder wesnoth; do
        cp -p $i %buildroot%_bindir/
done
cp wesnothd %buildroot%_sbindir/
cp campaignd %buildroot%_sbindir/
mkdir -p %buildroot%{_datadir}/wesnoth
for i in data fonts icons images sounds translations l10n-track; do
        cp -pr $i %buildroot%{_datadir}/wesnoth/
done
%endif

%ifdef wesdesktopsuffix
# cutter exploder
for i in wesnoth wesnoth_addon_manager \
 wmlindent wmllint wmlscope \
 ; do
	 mv %buildroot%_bindir/$i %buildroot%_bindir/${i}%wessuffix
done
cp icons/wesnoth{,%wessuffix}.desktop
find %buildroot%_mandir -name wesnoth.6 -execdir mv {} wesnoth%wessuffix.6 \;
find %buildroot%_mandir -name wesnothd.6 -execdir mv {} wesnothd%wessuffix.6 \;
sed -i -e 's,Exec=wesnoth,Exec=wesnoth%wessuffix,;s,^\(Name.*\),\1 (%wesdesktopsuffix),' icons/wesnoth*%{wessuffix}.desktop
%endif

#if with install_using_manual || with install_using_scons
# emulate cmake install
desktop-file-install --dir %buildroot%_desktopdir \
                     --mode="0644" \
                     --remove-key="Version" \
                     icons/wesnoth%wessuffix.desktop
mkdir -p %buildroot%{_datadir}/pixmaps
cp icons/wesnoth-icon.png %buildroot%{_datadir}/pixmaps
mkdir -p %buildroot%_docdir/
cp -a doc/manual %buildroot%_docdir/%name
%endif

install -d -m 0755 %buildroot%_sbindir
[ -e %buildroot%_bindir/wesnothd ] && mv %buildroot{%_bindir/wesnothd,%_sbindir/wesnothd%wessuffix}
[ -e %buildroot%_bindir/campaignd ] && mv %buildroot{%_bindir/campaignd,%_sbindir/campaignd%wessuffix}

%if_enabled tests
mv %buildroot%_bindir/{,%name-}test
%endif

%if_enabled python
%if_enabled python3
mkdir -p %buildroot/%python3_sitelibdir_noarch
mv %buildroot%_datadir/%name/data/tools/wesnoth %buildroot%python3_sitelibdir_noarch
#mv %buildroot%_datadir/%name/data/tools/addon_manager %buildroot%python3_sitelibdir_noarch
#mv %buildroot%_datadir/%name/data/tools/unit_tree %buildroot%python3_sitelibdir_noarch
find %buildroot%python3_sitelibdir_noarch \( -name wmldata.py -or -name wmlparser.py -or -name wmlparser2.py \) -delete
echo python2 rm -f \
   %buildroot%_datadir/%name/data/tools/expand-terrain-macros.py \
   %buildroot%_datadir/%name/data/tools/journeylifter \
   %buildroot%_datadir/%name/data/tools/rmtrans/rmtrans.py \
   %buildroot%_datadir/%name/data/tools/scoutDefault.py \
   %buildroot%_datadir/%name/data/tools/wmlflip \
   %buildroot%_datadir/%name/data/tools/wmlvalidator \
   %buildroot%_datadir/%name/data/tools/unit_tree/overview.py
%else
mkdir -p %buildroot/%python_sitelibdir_noarch
mv %buildroot%_datadir/%name/data/tools/wesnoth %buildroot%python_sitelibdir_noarch
#mv %buildroot%_datadir/%name/data/tools/addon_manager %buildroot%python_sitelibdir_noarch
#mv %buildroot%_datadir/%name/data/tools/unit_tree %buildroot%python_sitelibdir_noarch
# python2 only
#rm -f \
#%buildroot/%python_sitelibdir_noarch/wmlparser3.py \
#%buildroot/%python_sitelibdir_noarch/wmltools3.py \
#%buildroot/%python_sitelibdir_noarch/wesnoth/campaignserver_client.py \
#%buildroot/%python_sitelibdir_noarch/wesnoth/wmltools3.py \
#%buildroot/%python_sitelibdir_noarch/wesnoth/wmliterator3.py
%endif
%endif

#pushd data
#pushd tools
#for i in wesnoth_addon_manager wml*; do
#    cp $i %buildroot/%_bindir/
#done
#popd
#popd

mkdir -p %buildroot%_docdir/%name-%version/manual
mv %buildroot%_docdir/%name/* %buildroot%_docdir/%name-%version/manual/
install -m 0644 README.md copyright changelog.* %buildroot%_docdir/%name-%version/
install -d -m 0755 %buildroot%_iconsdir/hicolor/64x64/apps
mv %buildroot{%_pixmapsdir/wesnoth-icon,%_iconsdir/hicolor/64x64/apps/%name}.png
#install -D -m 0644 {icons/wesnoth-icon-Mac,%buildroot%_iconsdir/hicolor/128x128/apps/%name}.png
%if_enabled editor
for s in 48 32 16; do
    install -D -m 0644 utils/umc_dev/org.wesnoth/icons/wesnoth_editor-icon_$s.png %buildroot%_iconsdir/hicolor/${s}x$s/apps/wesnoth_editor%{wessuffix}.png
done
%endif
for s in 32 16; do
    install -D -m 0644 utils/umc_dev/org.wesnoth/icons/wesnoth-icon_$s.png %buildroot%_iconsdir/hicolor/${s}x$s/apps/%name.png
done
install -D -m 0644 icons/wesnoth-48.png %buildroot%_iconsdir/hicolor/48x48/apps/wesnoth%{wessuffix}.png
#install -D -m 0644 utils/umc_dev/org.wesnoth/icons/wesnoth-icon.png %buildroot%_iconsdir/hicolor/64x64/apps/wesnoth%{wessuffix}.png

mkdir -p %buildroot%_initdir/ %buildroot%_sysconfdir/sysconfig/
cat > %buildroot%_sysconfdir/sysconfig/wesnoth%wessuffix <<'EOF'
#
# wesnothd(6) options. Pick a custom port here if needed, for example.
#
WESNOTHD_OPTIONS=""
EOF
cat > %buildroot%_initdir/wesnothd%wessuffix <<'EOF'
#! /bin/sh
#
# wesnothd%wessuffix	Wesnoth server
#
# chkconfig:	345 98 02
#
# description:	This is a 'Battle for Wesnoth' daemon 
#
#		Modified for ALTLinux
#		by Gleb Stiblo <errandir@gmail.com>
#

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Do not load RH compatibility interface.
WITHOUT_RC_COMPAT=1

# Source function library
. /etc/rc.d/init.d/functions

DAEMON=/usr/sbin/wesnothd%wessuffix
NAME=wesnothd
USER=%_pseudouser_user
LOCKFILE=/var/lock/subsys/wesnothd%wessuffix
PIDFILE=/var/run/wesnothd%wessuffix.pid
SOCKETDIR=/var/run/wesnothd%wessuffix
RETVAL=0

test -x $DAEMON || exit 0

WESNOTHD_OPTIONS=
# Include wesnoth defaults if available
SourceIfNotEmpty /etc/sysconfig/wesnoth%wessuffix || exit 1


start()
{
	# for /var/run on tmpfs
	/bin/mkdir -p $SOCKETDIR/
	/bin/chown -R $USER.$USER $SOCKETDIR/
	start_daemon --make-pidfile $PIDFILE --pidfile $PIDFILE --name $NAME --user $USER -- $DAEMON $WESNOTHD_OPTIONS
	RETVAL=$?
	return $RETVAL
}

stop()
{
	stop_daemon --pidfile $PIDFILE --name $NAME -- $DAEMON 

	RETVAL=$?
	return $RETVAL
}

restart()
{
	stop
	sleep 1
	start
}

# See how we were called.
case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart)
	restart
	;;
  reload)
	;;
  condstop)
	if [ -e "$LOCKFILE" ]; then
	    stop
	fi
	;;
  condrestart)
	if [ -e "$LOCKFILE" ]; then
	    restart
	fi
	;;
  condreload)
	;;
  status)
	status --pidfile "$PIDFILE" -- $DAEMON
	RETVAL=$?
	;;
  *)
	msg_usage "${0##*/} {start|stop|restart|reload|condstop|condrestart|condreload|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

##### backport specific ###############
mkdir -p %buildroot%_unitdir/
cat > %buildroot%_unitdir/wesnothd%wessuffix.service <<'EOF'
[Unit]
Description=Wesnoth Multiplayer Server Daemon
After=network.target

[Service]
EnvironmentFile=-/etc/sysconfig/wesnoth%wessuffix
User=%_pseudouser_user
ExecStartPre=/bin/mkdir -p /var/run/wesnothd%wessuffix/
ExecStartPre=/bin/chown -R %_pseudouser_user.%_pseudouser_group /var/run/wesnothd%wessuffix/
ExecStart=/usr/sbin/wesnothd%wessuffix $WESNOTHD_OPTIONS

[Install]
WantedBy=multi-user.target
EOF
##### backport specific ###############


%ifdef wesdesktopsuffix
%find_lang --with-man wesnoth%wessuffix
%find_lang --with-man wesnothd%wessuffix
%find_lang wesnoth
%find_lang wesnothd
cat wesnoth.lang >> %name.lang
cat wesnothd.lang >> wesnothd%{wessuffix}.lang
rm -f wesnoth.lang wesnothd.lang
%else
%find_lang --with-man wesnoth
%find_lang --with-man wesnothd
%endif

for d in %buildroot%_datadir/%name/translations/*; do
    l=$(basename "$d")
    c=${l:0:2}
    echo "%%lang($c) %%dir %_datadir/%name/translations/$l" >> %name.lang
    echo "%%lang($c) %%dir %_datadir/%name/translations/$l/LC_MESSAGES" >> %name.lang
    [ -f $d/LC_MESSAGES/wesnoth.mo ] && echo "%%lang($c) %_datadir/%name/translations/$l/LC_MESSAGES/wesnoth.mo" >> %name.lang
    for i in ai anl aoi did dm editor ei httt l lib low multiplayer nr sof sotbe tb test thot trow tsg tutorial units utbs dw help manpages manual sota; do
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

rm -rf %buildroot%_datadir/%name/icons
rm -f %buildroot%_datadir/%name/fonts/DejaVuSans.ttf
ln -s %_datadir/fonts/ttf/dejavu/DejaVuSans.ttf %buildroot%_datadir/%name/fonts/
# sazanami-fonts-gothic
ln -s %_datadir/fonts/ttf/sazanami/gothic/sazanami-gothic.ttf %buildroot%_datadir/%name/fonts/sazanami-gothic.ttf
# wqy-zenhei-fonts
ln -s %_datadir/fonts/ttf/wqy-zenhei/wqy-zenhei.ttc %buildroot%_datadir/%name/fonts/wqy-zenhei.ttc


sed -i 's/wesnoth-icon/wesnoth%wessuffix/' %buildroot%_desktopdir/%name.desktop

%if_disabled tools
rm -rf %buildroot%_bindir/wesnoth_addon_manager \
   %buildroot%_bindir/wmlindent \
   %buildroot%_bindir/wmllint \
   %buildroot%_bindir/wmlscope
%endif

%if_enabled server
%pre server
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'Wesnoth server' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%preun server
%preun_service wesnothd%wessuffix

%post server
%post_service wesnothd%wessuffix
%endif

%files
%_bindir/%name

%files data -f %name.lang
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
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
%_datadir/%name/data/multiplayer
%_datadir/%name/data/shaders
%_datadir/%name/data/themes
%_datadir/%name/data/lua
%_datadir/%name/data/test
%_datadir/%name/data/*.cfg
%dir %_datadir/%name/data/languages
%_datadir/%name/l10n-track
%_man6dir/%name.6*
%if_disabled tools
%dir %_datadir/%name
%dir %_datadir/%name/data
%_datadir/%name/data/tools
%endif

%files doc
%dir %_docdir/%name-%version
/%_docdir/%name-%version/manual

%if_enabled editor
%files editor
%_desktopdir/wesnoth_editor%{wessuffix}.desktop
%_iconsdir/hicolor/*/apps/wesnoth_editor%{wessuffix}.png
%endif

%if_enabled tools
%files tools
#%_bindir/cutter%wessuffix
#%_bindir/exploder%wessuffix
%if_with build_using_scons
%else
%_bindir/schema_generator%wessuffix
%_bindir/schema_validator%wessuffix
%endif
%_bindir/wesnoth_addon_manager%wessuffix
%dir %_datadir/%name
%dir %_datadir/%name/data
%_datadir/%name/data/tools
%{?_enable_tests:%_bindir/%name-test}
%if_enabled python
%_bindir/wml*
%else
%exclude %_bindir/wml*
%endif
%endif

%if_enabled server
%files server -f wesnothd%{wessuffix}.lang
%_sbindir/wesnothd%wessuffix
%_sbindir/campaignd%wessuffix
%_initdir/wesnothd%wessuffix
##### backport specific ###############
%_unitdir/wesnothd%wessuffix.service
##### backport specific ###############
%config(noreplace) %_sysconfdir/sysconfig/wesnoth%wessuffix
%_man6dir/wesnothd%{wessuffix}.6*
%endif

%if_enabled python
%if_enabled python3
%files -n python3-module-%name
%python3_sitelibdir_noarch/wesnoth
#python3_sitelibdir_noarch/addon_manager
#python3_sitelibdir_noarch/unit_tree
%else
%files -n python-module-%name
%python_sitelibdir_noarch/wesnoth
#python_sitelibdir_noarch/addon_manager
#python_sitelibdir_noarch/unit_tree
%endif
%endif

%changelog
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

