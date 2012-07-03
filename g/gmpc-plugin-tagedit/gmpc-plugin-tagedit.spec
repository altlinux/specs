%define func tagedit

Name:		gmpc-plugin-%func 
Version:	0.18.0
Release:	alt1

%define builddeps gob2 >= 2.0.10 glib2-devel >= 2.16 libgtk+2-devel >= 2.8 libxml2-devel libmpd-devel >= 0.15.98 gmpc-devel >= 0.16.2 libtag-devel

BuildRequires(pre): rpm-build-gmpc

%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/gmpctageditplugin.so

%exclude %gmpc_plugin_libdir/*.la

%changelog
* Sat Mar 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt1
- Initial Sisyphus release

