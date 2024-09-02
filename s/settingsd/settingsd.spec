%def_without rtorrentd
%def_without pam

Name: settingsd
Version: 1.0
Release: alt2

Summary: Settingsd - extensible service to control the operating system via D-Bus

Group: System/Servers
License: LGPLv2
URL: https://github.com/Etersoft/settingsd

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/Etersoft/settingsd.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev

%add_python3_path %_datadir/%name/plugins/

Requires: python3-module-dbus
#, python3-module-pyinotify
# FIXME:
# Requires: chkconfig, service, SysVinit
Requires: pm-utils, lsb-release, hwclock

%description
Extensible service to control the operating system via D-Bus.


%package fmod-disks-smart
Summary: Settingsd functional plugin for view SMART information of disks
Group: Monitoring
Requires: smartmontools
Requires: %name = %EVR
%description fmod-disks-smart
%summary


%package fmod-ntp-config
Summary: Settingsd functional plugin for NTP configuration
Group: System/Configuration/Other
Requires: ntpdate
Requires: %name = %EVR
%description fmod-ntp-config
%summary


%package fmod-dnsmasq-config
Summary: Settingsd functional plugin for dnsmasq configuration
Group: System/Configuration/Networking
Requires: dnsmasq
Requires: %name = %EVR
%description fmod-dnsmasq-config
%summary


%package fmod-rtorrentd-config
Summary: Settingsd functional plugin for rtorrentd configuration
Group: System/Configuration/Networking
Requires: rtorrentd
Requires: %name = %EVR
%description fmod-rtorrentd-config
%summary


%package fmod-nss-roles
Summary: Settingsd functional plugin for NSS roles configuration
Group: System/Libraries
Requires: libnss-role
Requires: %name = %EVR
%description fmod-nss-roles
%summary

%package fmod-pam
Summary: Settingsd functional plugin for PAM authentication
Group: System/Libraries
Requires: %name = %EVR
%description fmod-pam
%summary


%prep
%setup
%__subst 's|/lib/systemd/system|%_unitdir|g' setup.py

# due missed gudev
rm -fv configs/settingsd/disks_smart.conf
rm -fv plugins/functions/fmod_disks_smart.py

%build
%python3_build

%install
%python3_install
# FIXME: Hack to drop out buildroot
%__subst 's|%buildroot||g' %buildroot%python3_sitelibdir/%name/const.py

%files
%_bindir/settingsd-server.py
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/main.conf
%config(noreplace) %_sysconfdir/%name/ssl.conf
%_initddir/%name
%_unitdir/%name.service
%_sysconfdir/dbus-1/system.d/*.conf
%dir %_datadir/%name/plugins/*/
%dir %_datadir/%name/data/*/
%_datadir/%name/plugins/functions/__pycache__/
%_datadir/%name/plugins/functions/fmod_common_info.py*
%_datadir/%name/plugins/functions/fmod_date_time.py*
%_datadir/%name/plugins/functions/fmod_example.py*
%_datadir/%name/plugins/functions/fmod_local_users.py*
%_datadir/%name/plugins/functions/fmod_local_groups.py*
%_datadir/%name/plugins/functions/fmod_machine.py*
%_datadir/%name/plugins/functions/fmod_network.py*
%_datadir/%name/plugins/functions/fmod_package_updates.py*
%_datadir/%name/plugins/functions/fmod_settingsd.py*
%_datadir/%name/plugins/functions/fmod_statistics.py*
%_datadir/%name/plugins/functions/fmod_system_services.py*
%_datadir/%name/plugins/functions/fmod_ssl.py*
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info


# due missed python gudev
#files fmod-disks-smart
#config(noreplace) %_sysconfdir/%name/disks_smart.conf
#_datadir/%name/plugins/functions/fmod_disks_smart.py*


%files fmod-ntp-config
%config(noreplace) %_sysconfdir/%name/ntp_config.conf
%_datadir/%name/plugins/functions/fmod_ntp_config.py*


%files fmod-dnsmasq-config
%config(noreplace) %_sysconfdir/%name/dnsmasq_config.conf
%_datadir/%name/plugins/functions/fmod_dnsmasq_config.py*

%if_with rtorrentd
%files fmod-rtorrentd-config
%config(noreplace) %_sysconfdir/%name/rtorrentd_config.conf
%_datadir/%name/plugins/functions/fmod_rtorrentd_config.py*
%endif

%files fmod-nss-roles
%config(noreplace) %_sysconfdir/%name/nss_roles.conf
%_datadir/%name/plugins/functions/fmod_nss_roles.py*

%if_with pam
%files pam
#config(noreplace) %_sysconfdir/%name/pam.conf
%_datadir/%name/plugins/functions/fmod_pam_authentication.py*
%endif

%changelog
* Sun Sep 01 2024 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix unitdir path

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- build version 1.0

* Mon Jan 28 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- build with python3
- add fmod-pam

* Fri Feb 04 2011 Devaev Maxim <mdevaev@etersoft.ru> 0.3-alt4
- d-Bus policy for fmod_nss_roles

* Fri Feb 04 2011 Devaev Maxim <mdevaev@etersoft.ru> 0.3-alt3
- functionality level = 132

* Fri Feb 04 2011 Devaev Maxim <mdevaev@etersoft.ru> 0.3-alt2
- added fmod_local_users to spec
- added methods for get GID variables from login.defs
- added methods for get UID variables from login.defs
- config options refactoring
- correct processing of missing files
- dBus policy for fmod_local_users
- fixed error on close() in PLainEditor
- fixed signal servicesChanged()
- fix variable path in PlainEditor on save()
- module for control at local users
- module for nss roles control (from Tartarus)
- new func level = 121
- new validators collection for standards UNIX entities
- none value in PlainEditor.setValue() works same as []
- plugin for control of UNIX groups, his D-Bus policy and configuration
- realName() method for some objects
- refactoring, fixed groupsChanged() signal
- refactoring of dbus namespaces in fmod_system_services
- refactoring, policy update for fmod_system_service
- removed word "UNIX" from log message
- setGid() for fmod_local_groups
- spec update for fmod_nss_roles
- code refactoring

* Thu Jan 27 2011 Devaev Maxim <mdevaev@etersoft.ru> 0.3-alt1
- added library for editing config files and universal class for plain configs
- closing editor in fmod_date_time
- fmod_date_time uses PlainEditor
- fmod_dnsmasq_config uses PlainEditor
- fmod_ntp_config uses PlainEditor
- log exceptions at file creating in PlainConfig
- logging in PlainEditor
- refactoring, fmod_rtorrentd_config uses PlainEditor
- splitted opening of config for read and write

* Wed Jan 19 2011 Devaev Maxim <mdevaev@etersoft.ru> 0.2-alt1
- dbus_tools and tools now a tools packages
- fixed installer, new version is 0.2
- message if resieved keyboard interrupt
- new validators in plugins
- refactoring
- splitted validators library
- using new version validators and tools

* Mon Jan 17 2011 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt14
- added module for rtorrentd configuration
- added package for module fmod_rtorrent_config
- checks for incorrect values in fmod_rtorrentd_config
- dBus policy for fmod_rtorrentd_config
- d-Bus policy update
- fixed build error, subpackage names
- functionality level = 83
- functional level = 87
- merge branch 'master' of git.eter:/people/mdevaev/packages/settingsd
- renamed dnsmasq.conf to dnsmasq_config.conf
- support of get/set raw data to config RTORRENT_CONFIG
- support option RTORRENT_CONFIG
- syntax error fix

* Fri Dec 17 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt13
- added loading default configs for date/time
- added loading default configs for dnsmasq
- added loading default configs for ntpd

* Wed Dec 08 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt12
- fixed broken dependency on smartmontools

* Wed Dec 08 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt11
- added folders for plugins data
- fixed build errors
- package is divided into the main program and plugins

* Tue Dec 07 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt10
- added validator for IPv4 address
- changed functionality level
- check for on-digit mask range
- closing file does not emmit exception
- fixed small bug in IPv4 address validator, added validator for IPv4 netmask validator, validator for hardware MAC address
- new parsers for ntp_config
- plugin for dnsmasq configuration
- some calls of execProcess in plugins no longer cause exceptions
- updated D-Bus policy

* Thu Nov 25 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt9
- added package requirement at hwclock

* Thu Nov 25 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt8
- added DBus policy for fmod_date_time, refactoring
- added module for date/time configuration
- current functionality level = 62
- fixed regexp for ntp servers, code for checks /etc/ntp.conf
- output version status at option -v
- refactoring

* Tue Nov 16 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt7
- added requirements for this verison

* Mon Nov 15 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt6
- added exception on process fail to fmod_system_services at first services loading
- added module for check SMART status
- added signal for disk changed to disks_smart
- additional version constants: functionality level and development status
- add simple SMART support checking
- add tools module with execProcess()
- aPI for determine settingsd version and functionality level
- dBus policy for fmod_disks_smart
- dynamic add and remove system services by inotify events on /etc/rc.d/init.d
- enable GObject threads
- fixed bug with getting dict of sharedObjects
- installation info and dynamic classifiers from settingsd/const.py
- merge branch 'master' of git.eter:/people/mdevaev/packages/settingsd
- moved raising SubprocessFailure to tools module
- new {submod} macros for logger
- refactoring all function modules for using tools
- removed unused modules
- systemServices in shared
- using constructor instead initService(), first run not emits signals

* Wed Nov 10 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt5
- changed return value type of meminfo API from float to int
- dBus policy for fmod_ntp_config
- fixed bug with access to object_path
- most verbosity server messages at loading and closing services
- nTP configuration module
- style fix
- using closed variables instead private in classes, fixed small bugs in logger
- validator for string list

* Tue Oct 26 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt4
- Fixed build errors

* Tue Oct 26 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt3
- Fixed init script including into package

* Mon Oct 25 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt2
- Fixed build errors
- Added startup init srcipt

* Mon Oct 25 2010 Devaev Maxim <mdevaev@etersoft.ru> 0.1-alt1
- Initial build

