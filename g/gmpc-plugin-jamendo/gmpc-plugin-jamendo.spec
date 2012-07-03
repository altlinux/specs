%define func jamendo

Name:		gmpc-plugin-%func 
Version:	0.18.0
Release:	alt1

%define builddeps gob2 >= 2.0.10 zlib-devel libgtk+2-devel libmpd-devel >= 0.15.98 gmpc-devel >= 0.17.1 libxml2-devel >= 2.6 libglade-devel libsqlite3-devel

BuildRequires(pre): rpm-build-gmpc

%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/%{func}plugin.so
%dir %gmpc_plugin_datadir/%func
%gmpc_plugin_datadir/%func/*.png

%exclude %gmpc_plugin_libdir/*.la

%changelog
* Sat Mar 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt1
- Initial Sisyphus release

