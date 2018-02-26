%define func lastfmradio

Name:		gmpc-plugin-%func 
Version:	0.17.98
Release:	alt1

%define builddeps gob2 >= 2.0.10 glib2-devel >= 2.16 libgtk+2-devel >= 2.8 libxml2-devel libmpd-devel >= 0.15.98 gmpc-devel >= 0.17.1

BuildRequires(pre): rpm-build-gmpc

%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/%{func}plugin.so
%dir %gmpc_plugin_datadir/lfr
%gmpc_plugin_datadir/lfr/*.png
%gmpc_plugin_datadir/lfr/*.svg

%exclude %gmpc_plugin_libdir/*.la

%changelog
* Sat Mar 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.17.98-alt1
- Initial Sisyphus release

