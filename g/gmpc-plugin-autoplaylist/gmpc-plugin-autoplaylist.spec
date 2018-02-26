%define func autoplaylist

Name:		gmpc-plugin-%func 
Version:	0.15.5.0
Release:	alt2

%define builddeps libgtk+2-devel libglade-devel libxml2-devel libmpd-devel >= 0.14.99 gmpc-devel >= 0.15.4.99

BuildRequires(pre): rpm-build-gmpc
%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/lib%func.so
%dir %gmpc_plugin_datadir/apl
%gmpc_plugin_datadir/apl/apl.glade

%exclude %gmpc_plugin_libdir/*.la

%changelog
* Sat Mar 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.15.5.0-alt2
- Moved the part common to all GMPC plugin specfiles to rpm-build-gmpc.
- Updated builreqs.
- Moved to git/gear.
- Rebuilt with GMPC/libmpd 0.18.0

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.5.0-alt1.1
-  plugin install path fix.

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.5.0-alt1
-  initial build for ALTLinux.


