%define func mdcover2

Name:		gmpc-plugin-%func 
Version:	0.15.4
Release:	alt1

%define builddeps glib2-devel >= 2.10 libgtk+2-devel >= 2.8 libxml2-devel libmpd-devel >= 0.14.99 gmpc-devel >= 0.15.4.100

BuildRequires(pre): rpm-build-gmpc

%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/gmpc%{func}plugin.so

%exclude %gmpc_plugin_libdir/*.la

%changelog
* Sat Mar 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.15.4-alt1
- Initial Sisyphus release

