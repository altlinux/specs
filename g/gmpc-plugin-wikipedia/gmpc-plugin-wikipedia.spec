%define func wikipedia

Name:		gmpc-plugin-%func 
Version:	0.18.0
Release:	alt3

%define builddeps libgtk+2-devel >= 2.8 libxml2-devel libmpd-devel >= 0.14.99 gmpc-devel >= 0.15.4.102 libwebkit-devel

BuildRequires(pre): rpm-build-gmpc

%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/wikiplugin.so

%exclude %gmpc_plugin_libdir/*.la

%changelog
* Sun Oct 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt3
- Rebuild with new libwebkitgtk.

* Wed Apr 15 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt2
- Rebuild with new libwebkit.

* Sat Mar 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt1
- Initial Sisyphus release.

