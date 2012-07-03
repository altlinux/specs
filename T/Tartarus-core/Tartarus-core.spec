
Version: 0.8.3
Release: alt3.1.1

%define tname Tartarus

Summary: %tname Core components
Name: %tname-core
Source: %tname-%version.tar
License: %gpl2plus
Group: System/Configuration/Other
Url: http://www.tartarus.ru
Packager: Ivan A. Melnikov <iv@altlinux.org>

BuildRequires(pre): rpm-build-licenses, rpm-build-python

BuildRequires: python-devel gcc-c++ ice-devel-utils libice-devel

%description
Core components for %tname.

# {{{1 Utility

%package -n %tname-common
Summary: Common files for %tname
Group: System/Configuration/Other

%description -n %tname-common
Common files required by most of %tname modules.


%package -n %tname-srv1
Summary: %tname python service loader
Group: System/Servers
Provides: %tname = %version-%release
Requires: %tname-common = %version-%release
Requires: python-module-%tname = %version-%release
Requires: python-module-%tname-daemon = %version-%release

%description -n %tname-srv1
%tname python service loader

%package -n %tname-deploy-common
Summary: %tname common deployment utilities
Group: System/Configuration/Other
Requires: %tname = %version-%release
Requires: %tname-leave = %version-%release
Requires: %tname-common = %version-%release
Requires: %tname-slices = %version-%release
Requires: python-module-%tname = %version-%release
Requires: python-module-%tname-deploy = %version-%release
Requires: python-module-%tname-system = %version-%release
Requires: libnss-tartarus, krb5-kinit, pam_krb5

%description -n %tname-deploy-common
%tname-deploy-common common utilities and modules for Tartarus deployment

%package -n %tname-deploy-srv
Summary: %tname server deployment utility
Group: System/Configuration/Other
Requires: %tname-DNS = %version-%release
Requires: %tname-DHCP = %version-%release
Requires: %tname-Kadmin5 = %version-%release
Requires: %tname-SysDB = %version-%release
Requires: %tname-slices = %version-%release
Requires: %tname-deploy-common = %version-%release
Requires: python-module-dnet

%description -n %tname-deploy-srv
%tname-deploy-srv is a simple console utility which will help you to create
inital configuration for Tartarus server.


%package -n %tname-join
Summary: Tartarus client deployment
Group: System/Configuration/Other
Requires: %tname-dnsupdate >= 0.1.0
Requires: %tname-deploy-common = %version-%release
Requires: nscd

%description -n %tname-join
Tartarus client deployment.

%package -n %tname-leave
Summary: Tartarus client leave
Group: System/Configuration/Other
Requires: %tname-common = %version-%release
Requires: %tname-slices = %version-%release
Requires: python-module-%tname = %version-%release
Requires: python-module-%tname-deploy = %version-%release
Requires: python-module-%tname-system = %version-%release

%description -n %tname-leave
Tartarus client leave.


# {{{1 Internal modules

%package -n python-module-%tname
Summary: Core components of %tname for Python.
Group: Development/Python

%description -n python-module-%tname
Core components of %tname for Python.

This module is built for python %__python_version


%package -n python-module-%tname-daemon
Summary: Daemonization support for %tname.
Group: Development/Python
Requires: python-module-%tname = %version-%release

%description -n python-module-%tname-daemon
Daemonization support for %tname.

This module is built for python %__python_version


%package -n python-module-%tname-system
Summary: System tools for %tname.
Group: Development/Python
Requires: python-module-%tname = %version-%release
Requires: python-module-kadmin5

%description -n python-module-%tname-system
System tools for %tname.

This module is built for python %__python_version


%package -n python-module-%tname-db
Summary: Database support for %tname.
Group: Development/Python
Requires: python-module-%tname = %version-%release

%description -n python-module-%tname-db
Database support for %tname.

This module is built for python %__python_version


%package -n python-module-%tname-deploy
Summary: %tname deployment internals.
Group: Development/Python
Requires: python-module-%tname = %version-%release

%description -n python-module-%tname-deploy
%tname deployment internals.

This module is built for python %__python_version


# {{{1 Configurators

%package -n %tname-DNS
Summary: %tname DNS Configurator.
Group: System/Configuration/Other
Requires: python%__python_version(sqlite)
Requires: python-module-%tname = %version-%release
Requires: python-module-%tname-db = %version-%release
Requires: %tname = %version-%release
Requires: pdns-backend-sqlite3
Requires: %tname-DNS-client = %version-%release

%description -n %tname-DNS
%tname DNS Configurator.

This module is built for python %__python_version


%package -n %tname-DNS-client
Summary: %tname DNS adminitrative utility.
Group: System/Configuration/Other
Requires: %tname-DNS-slice = %version-%release
Requires: python-module-%tname = %version-%release

%description -n %tname-DNS-client
%tname DNS adminitrative utility.

This module is built for python %__python_version


%package -n %tname-Kadmin5
Summary: %tname Kadmin5 Configurator.
Group: System/Configuration/Other
Requires: python-module-%tname = %version-%release
Requires: python-module-kadmin5 >= 0.0.5
Requires: %tname = %version-%release
Requires: krb5-kdc

%description -n %tname-Kadmin5
%tname Kadmin5 Configurator.

This module is built for python %__python_version


%package -n %tname-Kerberos-client
Summary: %tname Kerberos adminitrative utility.
Group: System/Configuration/Other
Requires: %tname-Kerberos-slice = %version-%release
Requires: python-module-%tname = %version-%release

%description -n %tname-Kerberos-client
%tname Kerberos adminitrative utility.

This module is built for python %__python_version


%package -n %tname-SysDB
Summary: %tname SysDB service.
Group: System/Servers
Requires: python%__python_version(sqlite3)
Requires: python-module-%tname = %version-%release
Requires: python-module-%tname-db = %version-%release
Requires: %tname = %version-%release
Requires: %tname-SysDB-client = %version-%release

%description -n %tname-SysDB
%tname SysDB service.

This module is built for python %__python_version


%package -n %tname-SysDB-client
Summary: %tname SysDB adminitrative utility.
Group: System/Configuration/Other
Requires: %tname-SysDB-slice = %version-%release
Requires: %tname-Kerberos-slice = %version-%release
Requires: python-module-%tname = %version-%release

%description -n %tname-SysDB-client
%tname SysDB adminitrative utility.

This module is built for python %__python_version


%package -n %tname-DHCP
Summary: %tname DHCP service.
Group: System/Servers
Requires: dhcp-server
Requires: python-module-%tname = %version-%release
Requires: python-module-%tname-db = %version-%release
Requires: %tname = %version-%release
Requires: %tname-DHCP-client = %version-%release

%description -n %tname-DHCP
%tname DHCP service.

This module is built for python %__python_version


%package -n %tname-DHCP-client
Summary: %tname DHCP adminitrative utility.
Group: System/Configuration/Other
Requires: %tname-DHCP-slice = %version-%release
Requires: python-module-%tname = %version-%release

%description -n %tname-DHCP-client
%tname DHCP adminitrative utility.

This module is built for python %__python_version


%package -n %tname-Time
Summary: %tname Time service.
Group: System/Servers
Requires: python-module-%tname = %version-%release
Requires: %tname = %version-%release

%description -n %tname-Time
%tname Time service.

This module is built for python %__python_version


# {{{1 Slices

%package -n %tname-slices
Summary: Interface defenision files for %tname objects.
Group: Development/Other
Requires: %tname-SysDB-slice = %version-%release
Requires: %tname-Kerberos-slice = %version-%release
Requires: %tname-DNS-slice = %version-%release
Requires: %tname-DHCP-slice = %version-%release
Requires: %tname-Time-slice = %version-%release

%description -n %tname-slices
Interface defenision files for %tname core objects.


%package -n %tname-core-slice
Summary: Interface defenision files for %tname core objects.
Group: Development/Other

%description -n %tname-core-slice
Interface defenision files for %tname core objects.


%package -n %tname-Kerberos-slice
Summary: Interface defenision files for Kerberos %tname.
Group: Development/Other
Requires: %tname-core-slice = %version-%release

%description -n %tname-Kerberos-slice
Interface defenision files for %tname Kerberos objects.


%package -n %tname-DNS-slice
Summary: Interface defenision files for %tname DNS objects.
Group: Development/Other
Requires: %tname-core-slice = %version-%release

%description -n %tname-DNS-slice
Interface defenision files for %tname DNS objects.


%package -n %tname-SysDB-slice
Summary: Interface defenision files for %tname SysDB objects.
Group: Development/Other
Requires: %tname-core-slice = %version-%release

%description -n %tname-SysDB-slice
Interface defenision files for %tname SysDB objects.


%package -n %tname-DHCP-slice
Summary: Interface defenision files for %tname DHCP objects.
Group: Development/Other
Requires: %tname-core-slice = %version-%release

%description -n %tname-DHCP-slice
Interface defenision files for %tname DHCP objects.


%package -n %tname-Time-slice
Summary: Interface defenision files for %tname Time objects.
Group: Development/Other
Requires: %tname-core-slice = %version-%release

%description -n %tname-Time-slice
Interface defenision files for %tname Time objects.


# {{{1 Libraries

%package -n %tname-devel
Summary: Development files for build C++ %tname projects.
Group: Development/C++
Requires: libice-devel

%description -n %tname-devel
Development files for build C++ %tname projects.


# {{{1 prep

%prep
%define tconfdir %_sysconfdir/%tname
%define tmoduledir %_libdir/%tname/modules
%define tslicedir %_datadir/%tname/slice
%define ttemplatedir %_datadir/%tname/templates
%define tpythondir %python_sitelibdir/%tname
%define tincludedir %_includedir/%tname

%setup  -q -n %tname-%version

%build
# check version
if [ "%version" != "`./waf --package-version`" ]; then
    echo RPM and package versions are not equal
    exit 1
fi

./configure --libdir=%_libdir
./waf

# {{{1 install

%install
./waf install --destdir=%buildroot

# {{{1 triggers

%preun -n %tname-leave
if [ "$1" = "0" ]; then
    t-leave -f ||:
fi


# {{{1 files

%files -n %tname-common
%dir %tconfdir
%dir %tconfdir/modules
%dir %tconfdir/deploy
%dir %tconfdir/clients

%dir %tmoduledir
%dir %_datadir/%tname
%dir %tslicedir
# FIXME: this should have a better place
%ttemplatedir
# and this too
%config(noreplace) %_sysconfdir/pam.d/*


%files -n %tname-srv1
%_sbindir/t-modules
%_sbindir/*1
%tconfdir/%{tname}*.conf
%_initdir/*

%files -n %tname-deploy-srv
%_sbindir/*deploy-srv
%tconfdir/clients/deploy*

%files -n %tname-deploy-common
%_bindir/*diag
%_sbindir/*timeset

%files -n %tname-join
%_sbindir/*join*

%files -n %tname-leave
%_sbindir/*leave*

%files -n python-module-%tname
%dir %tpythondir
%tpythondir/__init__*
%tpythondir/iface*
%tpythondir/logging*
%tpythondir/modules*
%tpythondir/slices*
%tpythondir/client*

%files -n python-module-%tname-daemon
%tpythondir/auth*
%tpythondir/daemon*
%tpythondir/locator*

%files -n python-module-%tname-system
%tpythondir/system*

%files -n python-module-%tname-db
%tpythondir/db*

%files -n python-module-%tname-deploy
%tpythondir/deploy*

%files -n %tname-DNS
%tconfdir/*/DNS*
%tmoduledir/DNS

%files -n %tname-Kadmin5
%tconfdir/*/Kadmin5*
%tmoduledir/Kadmin5

%files -n %tname-SysDB
%tconfdir/*/SysDB*
%tmoduledir/SysDB

%files -n %tname-DHCP
%tconfdir/*/DHCP*
%tmoduledir/DHCP

%files -n %tname-Time
%tconfdir/*/Time*
%tmoduledir/Time

%files -n %tname-SysDB-client
%_bindir/t-passwd
%_bindir/t-user*
%_bindir/t-group*

%files -n %tname-DNS-client
%_bindir/t-dns

%files -n %tname-DHCP-client
%_sbindir/t-dhcp*
%_bindir/t-dhcp*

%files -n %tname-Kerberos-client
%_sbindir/t-krb*

%files -n %tname-slices

%files -n %tname-core-slice
%dir %tslicedir
%tslicedir/core

%files -n %tname-Kerberos-slice
%tslicedir/Kerberos

%files -n %tname-DNS-slice
%tslicedir/DNS

%files -n %tname-SysDB-slice
%tslicedir/SysDB

%files -n %tname-DHCP-slice
%tslicedir/DHCP

%files -n %tname-Time-slice
%tslicedir/Time


%files -n %tname-devel
%tincludedir
%_libdir/*.a
%_pkgconfigdir/*.pc


# {{{1 changelog

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.3-alt3.1.1
- Rebuild with Python-2.7

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt3.1
- Rebuilt with python 2.6

* Wed Aug 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.3-alt3
- Second bugfixes to 0.8.3
+ Fixed bug #149 with server deployment

* Tue May 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.3-alt2
- First bugfixes to 0.8.3
+ clean code from silly bugs

* Fri May 22 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.3-alt1
- Release of version 0.8.3
+ Add t-diag and t-timeset utilities.

* Tue May 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt20
- sixteenth build fixes for sisyphus prebuild of alpha4
+ Time: add getTime() method for unixtime.

* Tue May 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt19
- fifteenth build fixes for sisyphus prebuild of alpha4
+ Add Time service.
+ krbconf: CfgReader add ignore comments.

* Wed Apr 29 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt18
- fourteenth build fixes for sisyphus prebuild of alpha4
+ deploy: improve error handling.
+ t-grouplst. Bug 139. Corrected 
- fix uninstall staff to ignore errors of t-leave

* Wed Apr 29 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt17
- thirteenth build fixes for sisyphus prebuild of alpha4
+ t-leave: add force option for using in scripts.
- fix uninstall staff with using force option for t-leave
- fix upgrade staff with noreplace of PAM configs

* Tue Apr 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt16
- twelfth build fixes for sisyphus prebuild of alpha4
+ t-leave: was added a condition.
+ deploy DHCP: fixed dhcp load config problem with update to versions.
- add Tartarus-slices requires for all deployment staff

* Mon Apr 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt15
- eleventh build fixes for sisyphus prebuild of alpha4
+ SysDB: improved error handling in GroupManger::addUserToGroups.
+ SysDB: Fixed #132.
+ db: a couple of small improvements.
+ SysDB: fixed test names to run more tests in bad*.
+ Configure pam_krb5 when joining to store ccache in
  /tmp/krb5cc_<uid> file.
+ JOIN: Add pam::ccname_template tag in krb5.conf when joining.
+ DHCP: Check error in t-dhcp initialization process.
+ Add new t-krb-mkservice utility.
- fix Tartarus-join requires for slices

* Wed Apr 22 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt14
- tenth build fixes for sisyphus prebuild of alpha4
+ deploy client: fix domain check.

* Wed Apr 22 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt13
- nineth build fixes for sisyphus prebuild of alpha4
+ deploy: remove old utilities.
+ deploy client: fix domain check and set fqdn as hostname.
+ deploy client: fixed join and leave.
+ deploy client: comment dhcpreg.
+ deploy client: fixed krb5.conf initialization process.
- fix postun for Tartarus-leave to use t-leave

* Tue Apr 21 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt12
- eighth build fixes for sisyphus prebuild of alpha4
+ DNS: Fixed #135. End. Added a processing of parametres for commands
  and subcommands.
+ DNS: Fixed #135. Begin. Added a processing of parametres for
  commands and subcommands.
+ t-dns. bug 137. was added check on exist of config file.
+ were added help or --help.
+ were added helps to record.

* Tue Apr 21 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt11
- seventh build fixes for sisyphus prebuild of alpha4
+ deploy: add domain checks for server.

* Thu Apr 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt10
- sixth build fixes for sisyphus prebuild of alpha4
+ DHCP: Raise exception if host already exists on server
+ Remove old deploy and join code
+ New utility t-dhcpreg also has been added

* Thu Apr 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt9
- fifth build fixes for sisyphus prebuild of alpha4
+ DHCP: Add '\0' to begin of host identity

* Thu Apr 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt8
- fourth build fixes for sisyphus prebuild of alpha4
+ dhcpd.conf file do not contains client identifiers in host declaration
+ error when adding host with ethernet identity by t-dhcp
 
* Thu Apr 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt7
- third build fixes for sisyphus prebuild of alpha4
+ DHCP: Check contexts for options
+ DHCP: remove static range support, because I do not known how to
        implement that

* Wed Apr 01 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt6
- second build fixes for sisyphus prebuild of alpha4
+ DHCP: fix bug in IpListOption type
+ New Tartarus join utility: t-join

* Fri Mar 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt5
- build fixes for sisyphus prebuild of alpha4
+ DHCP: fix deploing of DHCP service
+ Also move DHCP/iptools -> Tartarus.system.ipaddr
+ Add t-modules utility
+ DHCP: bug fixing and code refactoring
+ DHCP: impove error handling and fix some bugs
+ DHCP: Some changes in t-dhcp and DHCP service
+ DHCP: Improve subnet utility
+ DHCP: Improve hosts support
+ DHCP: remove OldRange command
+ DHCP: new improved IP-ranges support
+ DHCP: new mutable enum module
+ DHCP: New module to manipulate IP addresses, ranges, networks

* Fri Mar 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt4
- fix building on x86_64 with new build system

* Fri Mar 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt3
- fix DNS bug (#134)
- add more diagnostics to Tartarus.auth.DefaultSrvLocator
- add missed requires for new clients package

* Fri Mar 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt2
- add simple service locator (#119)
- add DNS console utility (#125)
- add SysDB (users and groups) console utility (#129)
- add locator for service lookup (#119)
- fix '_' in user names (#131)

* Fri Feb 20 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.2-alt1
- add DHCP service with simple authentification and console client
- directory creation code added to constructor of database helper (#117)
- add waf build system (#113)

* Wed Feb 18 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.1-alt2
- build fixes for sisyphus prebuild of alpha3
+ Now proper services should start and stop in proper moments (#114)
+ core: minor pylint-driven code cleanup
+ SysDB: fixed broken test database dump
+ SysDB: improved diagnostics on user and group creation

* Fri Feb 06 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.1-alt1
- build alpha2 for sisyphus
+ add leave running to Tartarus-leave preun script
+ add force option to Tartarus-leave for uninstall scripts

* Fri Jan 30 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.2-alt3
- build fixes for sisyphus prebuild of alpha2
+ add SRV records for kadmin service
+ change join default admin username

* Thu Jan 29 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.2-alt2
- build for sisyphus prebuild of alpha2
+ fixed admin and user names, added kadmin and nscd starting

* Wed Jan 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.2-alt1
- build for sisyphus prebuild of alpha2
+ refuse to create system users
+ refactored SysDB database code

* Fri Jan 23 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.1-alt1
- build for sisyphus alpha1

