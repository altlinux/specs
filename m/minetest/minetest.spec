%def_with l10n
%define _hardened_build 1
%global gitname celeron55
%define irrlichtmt_version 1.9.0mt13

Name: minetest
Version: 5.9.0
Release: alt3
Summary: Multiplayer infinite-world block sandbox with survival mode
License: LGPL-2.0+ and CC-BY-SA-3.0
Group: Games/Other
URL: https://www.minetest.net

# VCS (executable): https://github.com/minetest/minetest.git
# VCS (data files): https://github.com/minetest/minetest_game.git

# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.desktop
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.service
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.rsyslog
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.logrotate
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.README
Source0: %name-%version.tar.gz
Source2: %{name}.service
Source3: %{name}.rsyslog
Source4: %{name}.logrotate
Source5: %{name}.README
#Source6: %{name}_game-5.7.0.tar.gz
Source7: http://www.gnu.org/licenses/lgpl-2.1.txt
# Now using its own Minetest-specific fork of irrlicht.
#Source8:	https://github.com/minetest/irrlicht/archive/%{irrlichtmt_version}/irrlicht-%{irrlichtmt_version}.tar.gz

Patch0:   includes.patch
Patch1:   metainfo.patch

#ExcludeArch: aarch64
BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
#BuildRequires: libirrlicht-devel
BuildRequires: bzip2-devel jthread-devel libsqlite3-devel
BuildRequires: libpng-devel libjpeg-devel libXxf86vm-devel libGL-devel libX11-devel libXcm-devel libXi-devel libXv-devel libXext-devel libGLU-devel
BuildRequires: libopenal-devel libvorbis-devel libzstd-devel doxygen  libgraphviz-devel libgmp-devel libpq-devel
#libdotconf-devel graphviz
BuildRequires: libfreetype-devel
BuildRequires: systemd
BuildRequires: gettext-tools
BuildRequires: libcurl-devel
BuildRequires: libuuid-devel
BuildRequires: libbrotli-devel
%ifnarch %e2k
BuildRequires: libluajit-devel
%else
BuildRequires: libluajit-e2k-devel
%endif

BuildRequires: libncurses-devel
BuildRequires: libleveldb-devel libhiredis-devel
BuildRequires: spatialindex-devel jsoncpp-devel libpcre-devel

Requires: %name-server = %version-%release
Requires: icon-theme-hicolor

# Extra deps for irrlichtMT:
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xxf86vm)



%description 
Game of mining, crafting and building in the infinite world of cubic
blocks with optional hostile creatures, features both single and the
network multiplayer mode.

%package server
Summary: Minetest multiplayer server
Group: Games/Other

Requires(pre): shadow-utils

%description server
Minetest multiplayer server. This package does not require X Window
System.

%prep
#%setup -q -n %gitname-%name
%setup -q
# -a 1 -a 2
%patch0 -p1
%patch1 -p1

#pushd games
#tar xf %%SOURCE6
#mv %{name}_game-%version %{name}_game
#popd

cp %SOURCE7 doc/

#tar xf %%SOURCE8
#mv irrlicht-%{irrlichtmt_version} lib/irrlichtmt

# purge bundled jsoncpp and lua, and gmp
rm -rf lib/jsoncpp lib/lua lib/gmp

find . -name .gitignore -print -delete
find . -name .travis.yml -print -delete
find . -name .luacheckrc -print -delete

%build
%ifarch aarch64
%define _lto_cflags %{nil}
%endif

%cmake_insource -GNinja\
%if_with l10n
    -DENABLE_GETTEXT=TRUE \
%endif
    -DENABLE_CURL=TRUE           \
    -DENABLE_LEVELDB=TRUE        \
    -DENABLE_LUAJIT=TRUE         \
    -DENABLE_GETTEXT=TRUE        \
    -DENABLE_SOUND=TRUE          \
    -DENABLE_SYSTEM_JSONCPP=TRUE \
    -DENABLE_SYSTEM_GMP=TRUE     \
    -DENABLE_FREETYPE=TRUE       \
    -DENABLE_REDIS=TRUE          \
    -DENABLE_POSTGRESQL=TRUE     \
    -DPostgreSQL_TYPE_INCLUDE_DIR=%{_includedir}/pgsql \
    -DBUILD_SERVER=TRUE          \
    -DJSON_INCLUDE_DIR=/usr/include/json \
    -DJTHREAD_INCLUDE_DIR=%_builddir/%name/src/jthread
    #-DJTHREAD_INCLUDE_DIR=%_builddir/%gitname-%name/src/jthread
%ninja_build

%install
%ninja_install

mkdir -p %{buildroot}%{_datadir}/minetest/irr/media
cp -r irr/media/Shaders %{buildroot}%{_datadir}/minetest/irr/media

# Systemd unit file
mkdir -p %buildroot%_unitdir
cp -p %SOURCE2 %buildroot%_unitdir

# /etc/rsyslog.d/minetest.conf
mkdir -p %buildroot%_sysconfdir/rsyslog.d
cp -p %SOURCE3 %buildroot%_sysconfdir/rsyslog.d/%{name}.conf

# /etc/logrotate.d/minetest
mkdir -p %buildroot/%{_sysconfdir}/logrotate.d
cp -p %SOURCE4 %buildroot/%{_sysconfdir}/logrotate.d/%{name}-server

# /var/lib/minetest directory for server data files
mkdir -p %buildroot%{_sharedstatedir}/%{name} 

# /etc/minetest.conf
mkdir -p %buildroot%{_sysconfdir}
cp -p minetest.conf.example %buildroot%{_sysconfdir}/%{name}.conf

cp -p %SOURCE5 README

%if_with l10n
%find_lang %name
%else
touch %name.lang
%endif

%pre server
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d /var/lib/%{name} -s /sbin/nologin \
    -c "Minetest multiplayer server" %{name}
exit 0

%post server
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun server
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable %{name}.service > /dev/null 2>&1 || :
    /bin/systemctl stop %{name}.service > /dev/null 2>&1 || :
fi

%postun server
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%files -f %{name}.lang
%doc README.md doc/lgpl-2.1.txt README
%doc %_docdir/%name
%_bindir/%name
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/128x128/apps/%name.png
%_man6dir/minetest.*
%_datadir/metainfo/*.metainfo.xml

%files server
%doc README.md doc/lgpl-2.1.txt doc/world_format.md doc/protocol.txt README
%_bindir/%{name}server
%_unitdir/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%config(noreplace) %{_sysconfdir}/rsyslog.d/%{name}.conf
%attr(0755,minetest,minetest) %dir %{_sharedstatedir}/%{name}
%_man6dir/minetestserver.6*

%changelog
* Wed Aug 28 2024 Ilya Mashkin <oddity@altlinux.ru> 5.9.0-alt3
- Copy irr/Shaders

* Thu Aug 22 2024 Ilya Mashkin <oddity@altlinux.ru> 5.9.0-alt2
- Add more BR

* Tue Aug 13 2024 Ilya Mashkin <oddity@altlinux.ru> 5.9.0-alt1
- 5.9.0

* Tue Dec 05 2023 Ilya Mashkin <oddity@altlinux.ru> 5.8.0-alt2
- Do not package minetest_game

* Tue Dec 05 2023 Ilya Mashkin <oddity@altlinux.ru> 5.8.0-alt1
- 5.8.0
- Minetest Game no longer comes preinstalled

* Mon Jun 05 2023 Ilya Mashkin <oddity@altlinux.ru> 5.7.0-alt1
- 5.7.0

* Mon Sep 26 2022 Ilya Mashkin <oddity@altlinux.ru> 5.6.1-alt1
- 5.6.1

* Sat Aug 06 2022 Ilya Mashkin <oddity@altlinux.ru> 5.6.0-alt1
- 5.6.0

* Sun May 22 2022 Ilya Mashkin <oddity@altlinux.ru> 5.5.1-alt2
- add missed game data (Closes: #42822)

* Tue May 17 2022 Ilya Mashkin <oddity@altlinux.ru> 5.5.1-alt1
- 5.5.1

* Mon May 16 2022 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt3
- Remove duplicated desktop file (ALT #42759).

* Tue Feb 08 2022 Ilya Mashkin <oddity@altlinux.ru> 5.5.0-alt2
- fix build on e2k

* Wed Feb 02 2022 Ilya Mashkin <oddity@altlinux.ru> 5.5.0-alt1
- 5.5.0
- Now using its own fork of irrlicht

* Tue Dec 28 2021 Ilya Mashkin <oddity@altlinux.ru> 5.4.1-alt2
- Add patch to fix build with gcc11
- ExcludeArch: aarch64

* Mon Apr 19 2021 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- New version.

* Tue Apr 06 2021 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt2
- Add missing devel packages (ALT #39398).
- Fix License tag.

* Mon Mar 08 2021 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1
- New version.

* Mon Aug 03 2020 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version.

* Thu Apr 09 2020 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Tue Jan 28 2020 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.

* Thu Apr 18 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.17.1-alt1
- New version.

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.16-alt1
- New version

* Fri Dec 30 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.15-alt1
- New version

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.14-alt1.1
- rebuild with irrlicht

* Mon Jun 06 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.14-alt1
- New version

* Sun Aug 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.4.13-alt1
- New version
- minetestserver is absent. Use minetest --server

* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 0.4.12-alt1
- New version

* Mon Dec 29 2014 Andrey Cherepanov <cas@altlinux.org> 0.4.11-alt1
- New version

* Tue Jul 08 2014 Andrey Cherepanov <cas@altlinux.org> 0.4.10-alt1
- New version
- Add appdata to package
- Support localization disabled by default

* Sun Jan 05 2014 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1
- New version

* Wed Nov 27 2013 Andrey Cherepanov <cas@altlinux.org> 0.4.8-alt1
- New version

* Mon Jul 29 2013 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1
- Initial build in Sisyphus (thanks Fedora maintainers)

