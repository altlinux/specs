%def_disable package_dirs

Name:	 	xbrowser-plugins-common
Version:	3.1
Release:	alt1

Group:		System/Base
Summary: 	Netscape Gecko Plug-in API common files
License:	GPL

Provides: browser-plugins-npapi = %version-%release
#Obsoletes: browser-plugins-npapi-devel < %version-%release

Source: nil

%description
This package contains directories for storage of plug-ins 
for NPAPI(Netscape Gecko Plug-in API) compatible browsers.

%package -n rpm-build-browser-plugins
Summary: 	Netscape Gecko Plug-in API common packaging files 
Group: 		Development/Other
%if_enabled package_dirs
Requires: %name = %version-%release
%endif
Provides: rpm-macros-browser-plugins = %version-%release
Obsoletes: rpm-macros-browser-plugins < %version-%release
Provides: browser-plugins-npapi-devel = %version-%release
#Obsoletes: browser-plugins-npapi-devel < %version-%release
%description -n rpm-build-browser-plugins
This package contains rpm macroses to package NPAPI plugins.

%prep
%setup -Tc


%build


%install
mkdir -p %buildroot/%_libdir/browser-plugins
mkdir -p %buildroot/%_libdir/browser-plugins-npapi
mkdir -p %buildroot/%_libdir/mozilla/plugins
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
mkdir -p %buildroot/%_rpmlibdir

cat >%buildroot/%_sysconfdir/rpm/macros.d/browser-plugins <<__EOF__
%%__xbpc_browser_plugins_api_name_internal %{?browser_plugins_api:%browser_plugins_api}%{!?browser_plugins_api:npapi}
%%browser_plugins_path_old  %%_libdir/browser-plugins-%%__xbpc_browser_plugins_api_name_internal
%%browser_plugins_path      %%_libdir/browser-plugins
__EOF__

cat >%buildroot/%_rpmlibdir/browser-plugins.req.list <<__EOF__
/usr/lib/browser-plugins   %name
/usr/lib64/browser-plugins %name
__EOF__


%if_enabled package_dirs
%files
%dir %_libdir/mozilla
%dir %_libdir/mozilla/plugins
%dir %_libdir/browser-plugins
%dir %_libdir/browser-plugins-npapi
%endif

%files -n rpm-build-browser-plugins
%_sysconfdir/rpm/macros.d/browser-plugins
%if_enabled package_dirs
%_rpmlibdir/browser-plugins.req.list
%endif


%changelog
* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 3.1-alt1
- don't package directories

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 3.0-alt1
- add browser-plugins.req.list

* Thu Oct 01 2009 Sergey V Turchin <zerg@altlinux.org> 2.4-alt1
- add %_libdir/mozilla; thanks shrek@alt

* Tue Sep 29 2009 Sergey V Turchin <zerg@altlinux.org> 2.3-alt1
- add %%browser_plugins_path_old

* Tue Sep 29 2009 Sergey V Turchin <zerg@altlinux.org> 2.2-alt1
- small rename package

* Mon Sep 28 2009 Sergey V Turchin <zerg@altlinux.org> 2.1-alt1
- simplify macroses

* Mon Sep 28 2009 Sergey V Turchin <zerg@altlinux.org> 2.0-alt1
- initial release
