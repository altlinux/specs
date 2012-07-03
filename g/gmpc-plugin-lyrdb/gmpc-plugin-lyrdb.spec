%define func lyrdb

Name:		gmpc-plugin-%func 
Version:	0.0.1
Release:	alt1

%define builddeps glib2-devel >= 2.16 libgtk+2-devel >= 2.12 libxml2-devel libgio-devel libmpd-devel >= 0.15.98 gmpc-devel >= 0.16.2

BuildRequires(pre): rpm-build-gmpc

%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/%{func}plugin.so

%exclude %gmpc_plugin_libdir/*.la

%changelog
* Sat Mar 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.0.1-alt1
- Initial Sisyphus release

