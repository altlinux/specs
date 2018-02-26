%define func discogs

Name:		gmpc-plugin-%func 
Version:	0.1.0.20090127
Release:	alt1

%define builddeps libgtk+2-devel >= 2.8 libxml2-devel libmpd-devel >= 0.15.98 gmpc-devel >= 0.16.2

BuildRequires(pre): rpm-build-gmpc

%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/%{func}plugin.so

%exclude %gmpc_plugin_libdir/%{func}plugin.la

%changelog
* Sat Mar 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.1.0.20090127-alt1
- Initial Sisyphus release.

