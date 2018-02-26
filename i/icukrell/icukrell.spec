Name: icukrell
Version: 2.0.0
Release: alt2_pre0.1

Summary: GKrellM gnomeICU status plugin
License: GPL
Group: Monitoring
Url: http://icukrell.sourceforge.net/
Source: http://umn.dl.sourceforge.net/sourceforge/icukrell/%{name}-%version-pre0.1.tar.gz

Patch0: icukrell-2.0.0-pre0.1-alt-i18n.patch.gz
Patch1: icukrell-2.0.0-pre0.1-alt-ru.patch.gz
Patch2: icukrell-2.0.0-pre0.1-alt-install.patch.gz

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Sun Mar 30 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
IcuKrell is a gKrellm (http://www.gkrellm.net) plugin which display status and 
control gnomeICU (http://gnomeicu.sourceforge.net)

%prep
%setup -q -n %name-%version-pre0.1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 DESTDIR=%buildroot PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %name

%files -f %name.lang
%doc ChangeLog INSTALL README TODO
%_libdir/gkrellm2/plugins/%name.so


%changelog
* Sun Mar 30 2003 Alex Murygin <murygin@altlinux.ru> 2.0.0-alt2_pre0.1
- Added russian translation
- Added i18n support

* Sun Mar 16 2003 Alex Murygin <murygin@altlinux.ru> 2.0.0-alt1_pre0.1
- First build for Sisyphus.

