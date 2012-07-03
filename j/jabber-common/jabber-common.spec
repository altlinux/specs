%define _jabber_server_dir %_datadir/jabber/server
%define _jabber_component_dir %_datadir/jabber/component
%define _jabber_config %_sbindir/jabber-config 

Name: jabber-common
Version: 0.3
Release: alt1
Group: System/Servers
Summary: Common configuration facility for all Jabber servers and components
License: GPLv3
Packager: Mikhail Yakshin <greycat@altlinux.org>

BuildArch: noarch

Source1: jabber-config
Source2: jabber.macros
Requires: rpm-macros-jabber = %version

%description
Common configuration facility for all Jabber servers and components,
"jabber-config".

jabber-config is a minimalistic solution for automatic deployment and
zero manual configuration for Jabber servers and components.

%package -n rpm-macros-jabber
Summary: Set of RPM macros for packaging Jabber servers and components
Group: Development/Other
# helps old apt to resolve file conflict at dist-upgrade (thanks to Stanislav Ievlev)
Conflicts: jabber-common <= 0.2-alt2

%description -n rpm-macros-jabber
Set of RPM macros for packaging Jabber servers and components for ALT Linux.
Install this package if you want to create RPM packages for a Jabber server
or component that will use jabber-config infrastructure for automatic
deployment.

%prep

%build

%install
mkdir -p %buildroot{%_jabber_server_dir,%_jabber_component_dir,%_rpmmacrosdir,%_sbindir}
install -m755 %SOURCE1 %buildroot%_sbindir
cp %SOURCE2 %buildroot%_rpmmacrosdir/jabber

%files
%dir %_datadir/jabber
%dir %_jabber_server_dir
%dir %_jabber_component_dir
%_sbindir/*

%files -n rpm-macros-jabber
%_rpmmacrosdir/*

%changelog
* Thu Jan 15 2009 Mikhail Yakshin <greycat@altlinux.org> 0.3-alt1
- Fixed RPM macros packaging, according to ALT policy: now they are in a
  separate subpackage.
- Proper --help, --version, --verbose option support.
- Lots of error checking and warning reporting for maximum script
  calling safety.
- Fixed bug #14369.

* Thu Apr 05 2007 Mikhail Yakshin <greycat@altlinux.ru> 0.2-alt2
- Fixed stupid typo.

* Wed Mar 28 2007 Mikhail Yakshin <greycat@altlinux.ru> 0.2-alt1
- jabberd2 support: added server policy '--single' to bind every
  component on a single port.
- jabber components are required to implement '--set-port',
  '--set-host', '--set-password' now.

* Tue Mar 13 2007 Mikhail Yakshin <greycat@altlinux.ru> 0.1-alt1
- Initial build.

