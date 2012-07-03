%define func extraplaylist

Name:		gmpc-plugin-%func 
Version:	0.18.0
Release:	alt1

%define builddeps libgtk+2-devel libglade-devel libxml2-devel libmpd-devel >= 0.15.98 gmpc-devel >= 0.15.98

BuildRequires(pre): rpm-build-gmpc
%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/lib%{func}.so

%exclude %gmpc_plugin_libdir/*.la

%changelog
* Sat Mar 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt1
- New version (0.18.0).
- Moved the part common to all GMPC plugin specfiles to rpm-build-gmpc.
- Updated builreqs.
- Moved to git/gear.

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.5.0-alt1.1
-  plugin install path fix.

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.5.0-alt1
-  initial build for ALTLinux.


