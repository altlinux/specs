%define _unpackaged_files_terminate_build 1
%define _localstatedir %_var
%define _runtimedir /run
%ifarch %ix86
%def_without check
%else
%def_with check
%endif

%define modname tile

Name: apache2-mod_%modname
Version: 0.8.1
Release: alt1

Summary: A system to serve raster tiles
License: GPL-2.0-only
Group: System/Servers
URL: https://wiki.openstreetmap.org/wiki/Mod_tile
VCS: https://github.com/openstreetmap/mod_tile

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: %apache2_name-base > 2.2.22-alt15
Requires: %apache2_name-mmn = %apache2_mmn
Requires: %apache2_libapr_name >= %apache2_libapr_evr
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr

BuildRequires(pre): apache2-devel > 2.2.22-alt15
BuildRequires(pre): rpm-macros-systemd
BuildRequires: gcc-c++
BuildRequires: libicu-devel
BuildRequires: glib2-devel
BuildRequires: libiniparser-devel
BuildRequires: libmapnik-devel
BuildRequires: libcurl-devel
BuildRequires: libcairo-devel
BuildRequires: libmemcached-devel
%ifnarch %ix86
BuildRequires: librados-devel
%endif

%description
mod_tile is a system to serve raster tiles for example to use within
a slippy map.  It provides a dynamic combination of efficient caching
and on the fly rendering.  Due to its dynamic rendering, only a small
fraction of overall tiles need to be kept on disk, reducing the resources
required.  At the same time, its caching strategy allows for a high
performance serving and can support several thousand requests per second.

%package -n renderd
Summary: A daemon that renders map tiles using mapnik
Group: Engineering
Requires: %name = %EVR
Requires: mapnik-plugins

%description -n renderd
%summary.

%prep
%setup
%autopatch -p1

# fix basic config installed by make
sed etc/renderd/renderd.conf.in \
    -e 's|@RENDERD_RUN_DIR@|%_runtimedir/renderd|' \
    -e 's|@RENDERD_TILE_DIR@|%_localstatedir/cache/renderd/tiles|' \
    -e 's|@MAPNIK_FONTS_DIR@|%_datadir/fonts|' \
    -e 's|@MAPNIK_FONTS_DIR_RECURSE@|true|' \
    -e 's|@MAPNIK_PLUGINS_DIR@|%_libdir/mapnik/input|' \
    > etc/renderd/renderd.conf

%build
%autoreconf
%configure
%make_build \
    renderd_CXXFLAGS='$(MAPNIK_CFLAGS) -DMAPNIK_FONTS_DIR_RECURSE=1'

%install
%makeinstall_std install-mod_%modname

mkdir -p %buildroot%apache2_mods_available
sed etc/apache2/%modname.load.in \
    -e 's|@CMAKE_INSTALL_MODULESDIR@|%apache2_moduledir|' \
    > %buildroot%apache2_mods_available/%modname.load

# for %%ghost
mkdir -p %buildroot%apache2_mods_enabled
touch %buildroot%apache2_mods_enabled/%modname.load

# based on upstream/systemd branch
mkdir -p %buildroot%_tmpfilesdir
echo "d %_runtimedir/renderd 0755 root root -" \
    > %buildroot%_tmpfilesdir/renderd.conf

mkdir -p %buildroot%_unitdir
cat > %buildroot%_unitdir/renderd.service <<__EOF__
[Unit]
Description=Daemon that renders map tiles using mapnik
Documentation=man:renderd
After=network.target auditd.service

[Service]
RuntimeDirectory=%_runtimedir/renderd
RuntimeDirectoryMode=0755
ExecStart=%_bindir/renderd -f

[Install]
WantedBy=multi-user.target
__EOF__

%check
%make test

%files
%doc AUTHORS COPYING README.rst screenshot.jpg
%apache2_moduledir/mod_%modname.so
%config(noreplace) %apache2_mods_available/%modname.load
%ghost %apache2_mods_enabled/%modname.load

%files -n renderd
%_bindir/renderd
%_bindir/render_expired
%_bindir/render_list
%_bindir/render_old
%_bindir/render_speedtest
%_sysconfdir/renderd.conf
%_unitdir/renderd.service
%_tmpfilesdir/renderd.conf
%_man1dir/*.1.*
%_man5dir/*.5.*

%changelog
* Tue Sep 29 2026 Valery Zabrovsky <brow@altlinux.org> 0.8.1-alt1
- Initial build for ALT Sisyphus.
