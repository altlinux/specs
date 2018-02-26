%define func mdcover

Name: gmpc-plugin-%func 
Version: 0.18.0
Release: alt1

%define builddeps glib2-devel >= 2.10 libgtk+2-devel >= 2.8 libxml2-devel libmpd-devel >= 0.15.98 gmpc-devel >= 0.15.98

BuildRequires(pre): rpm-build-gmpc
%include %gmpc_plugin_incspec

%files
%gmpc_plugin_libdir/*.so

%exclude %gmpc_plugin_libdir/*.la

%changelog
* Sun Mar 15 2009 Alexey Rusakov <ktirf@altlinux.org> 0.18.0-alt1
- New version
- Moved a common part of all GMPC plugin specs to rpm-build-gmpc.
- Updated buildreqs.
- Moved to git/gear.

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.5.0-alt1.1
-  plugin install path fix.

* Thu Mar 20 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.15.5.0-alt1
-  initial build for ALTLinux.


