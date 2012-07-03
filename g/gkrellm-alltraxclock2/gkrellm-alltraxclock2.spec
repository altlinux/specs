%define plugin alltraxclock2

Name: gkrellm-%plugin
Version: 0.2
Release: alt1
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: GKrellM analog clock plugin
Summary(ru_RU.KOI8-R): Часы со стрелками для GKrellM
License: GPL
Group: Monitoring
Url: http://perso.wanadoo.fr/alltrax/alltraxclock.html

Source: http://perso.wanadoo.fr/alltrax/alltraxclock2_0.2-1.tar.bz2
Patch0: http://lrn.ru/~bga/gkrellm/alltraxclock2-0.2-alt-i18n.patch.gz
Patch1: http://lrn.ru/~bga/gkrellm/alltraxclock2-0.2-alt-ru_po.patch.gz

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Thu Jun 19 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
A plugin for GKrellM, which displays a nice analog clock
with the theme colors.
%description -l ru_RU.KOI8-R
Плагин для GKrellM, отображающий время на часах со стрелками
соответственно оформлению GkrellM.

%prep
%setup -q -n %{plugin}_%version
%patch0 -p1
%patch1 -p1

%build
%make_build enable_nls=1
# CFLAGS="$RPM_OPT_FLAGS" LOCALEDIR=%_datadir/locale

%install
#%__mkdir_p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang alltraxclock

%files -f alltraxclock.lang
%doc debian/changelog debian/changelog.old
%_libdir/gkrellm2/plugins/alltraxclock.so

%changelog
* Thu Jun 19 2003 Grigory Batalov <bga@altlinux.ru> 0.2-alt1
- 0.2
- I18n and ru.po patches
