%define _mkve_confdir %_sysconfdir/alterator/mkve

Name: alterator-mkve
Version: 0.26
Release: alt1
Packager: Anton Protopopov <aspsk@altlinux.org>
BuildArch: noarch
Source0: %name-%version.tar
Source1: config
Summary: Alterator module for creating/destroing virtual environments
License: GPL
Group: System/Configuration/Other

Requires: gettext
Requires: alterator >= 3.3-alt8
Requires: mkve
Requires: alterator-net-iptables
Requires: alterator-sh-functions
Requires: alterator-fbi >= 5.9-alt3

BuildPreReq: alterator-fbi >= 0.15-alt2
BuildRequires: alterator >= 3.3-alt8

%description
Alterator module for creating/destroing virtual environments

%prep
%setup -q

%build

%install
%makeinstall
%__mkdir_p %buildroot%_mkve_confdir
install %SOURCE1 %buildroot%_mkve_confdir
%find_lang %name

%post
if [ -f "/etc/libvirt/qemu/networks/default.xml" ]; then
    %__rm -f /etc/libvirt/qemu/networks/default.xml
    %__rm -f /etc/libvirt/qemu/networks/autostart/default.xml
    service libvirtd restart
fi

%files -f %name.lang
%_datadir/alterator/applications/*
%_datadir/alterator/help/*/*
%_datadir/alterator/ui/*
%_datadir/alterator/type/*
%_libexecdir/alterator/backend3/*
%_mkve_confdir

%changelog
* Mon Oct 12 2009 Anton Protopopov <aspsk@altlinux.org> 0.26-alt1
- "There can be only none" (in five parts)
- Ask user when destroing a machine
- (m.)adopt -> (fem.)adopt
- Bugfixes (ALT #21882)

* Thu Sep 24 2009 Anton Protopopov <aspsk@altlinux.org> 0.25-alt1
- Work with root password in openvz more gracefully (ALT 21676)
- mkve/openvz: pack into accordion
- Always show hardware interfaces
- Update po

* Tue Sep 22 2009 Anton Protopopov <aspsk@altlinux.org> 0.24-alt1
- Fix parsing output of iptables_helper
- Remove js from *.html files

* Mon Sep 21 2009 Anton Protopopov <aspsk@altlinux.org> 0.23-alt1
- Failcnt field is missing in bc table (ALT 21632)
- Add "Reset status" button to openvz/ubc page
- Update po

* Fri Sep 18 2009 Anton Protopopov <aspsk@altlinux.org> 0.22-alt1
- Implement mkve/pack usability (ALT 20902)

* Mon Aug 31 2009 Anton Protopopov <aspsk@altlinux.org> 0.21-alt1
- Some localization issues

* Mon Aug 24 2009 Anton Protopopov <aspsk@altlinux.org> 0.20-alt1
- (optionally) set CTID when creating an OpenVZ machine (ALT 21025)
- ui/mkve/*: Move to "wf=none" from "wf=form"

* Thu Aug 06 2009 Anton Protopopov <aspsk@altlinux.org> 0.19-alt1
- Display held and maxheld fields in openvz UBC page (ALT 20728)
- Display `used' field in openvz Quota page
- Show information about VNC display

* Wed Jun 17 2009 Anton Protopopov <aspsk@altlinux.org> 0.18-alt1
- update help/ru_RU
- make update-po

* Mon Jun 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.17-alt1
- new interface: mkve/adopt
- Check for architecture when creating an openvz machine
- Bugs (ALT #20390)

* Mon Jun 08 2009 Anton Protopopov <aspsk@altlinux.org> 0.16-alt1
- Add some checks (ALT #20116)
- make update-po

* Fri Jun 05 2009 Anton Protopopov <aspsk@altlinux.org> 0.15-alt1
- actually include mkve-machine-name.scm
- Some fixes in help
- make update-po

* Tue Jun 02 2009 Anton Protopopov <aspsk@altlinux.org> 0.14-alt1
- mkve-create: add action_type callback
- mkve-create: work with config
- remove dead code

* Tue Jun 02 2009 Anton Protopopov <aspsk@altlinux.org> 0.13-alt1
- mkve-create: search for partitions (ALT #20265)
- mkve-create: don't include config if it doesn't exist

* Wed May 27 2009 Anton Protopopov <aspsk@altlinux.org> 0.12-alt1
- Take bundles from usb block devices too
- Fix #20146, #20047
- Fix #20119 (you can't use whitespaces in name)
- Fix #20118 (read quotas from config)
- Add config file /etc/altlinux/mkve
- A lot of small fixes

* Mon May 18 2009 Anton Protopopov <aspsk@altlinux.org> 0.11-alt1
- Fix #19851

* Fri Apr 24 2009 Anton Protopopov <aspsk@altlinux.org> 0.1-alt1
- mkve: add "ip" field to main page, return "not found" if ip was not found
- mkve-kvm: use default arp.dat iff arp.dat.$bridge is absent

* Tue Apr 21 2009 Anton Protopopov <aspsk@altlinux.org> 0.1-alt0.6
- Update kvm interface
- mkve-kvm: our future presentation
- Remove dead interfaces
- Remove default libvirt network on install
- Set bridge when creating a machine

* Fri Apr 03 2009 Anton Protopopov <aspsk@altlinux.org> 0.1-alt0.5
- Set kvm password
- Fix bug with empty bundles list
- Move to system desktop directory
- qemu -> kvm
- Fix creating of machines in new interface
- mkve-create: take info from `info'
- Rewrite create interface
- Show available CD as possible source
- Fix to create QEMU containers
- Use wf=none
- Use standard directory and more local reads
- Add russian translation
- Add some help info
- mkve: use buttons instead of actions list

* Fri Mar 13 2009 Anton Protopopov <aspsk@altlinux.org> 0.1-alt0.4
- Fix #19168
- Fix dependence: meaned -net-iptables instead of -net-common
- display hypervisor-specific div when creating a machine
- Use a list of links into hypervisor-specific page instead of
  "Alterator" button on main page
- mkve: report an actual error message
- Use ajax
- move templates from templates/ to ui/
- add license field to create/ page
- totally rewrite openvz/ interface
- add setting password into openvz/ page
- redirect to "configure" page after creating
- don't clear password field if it was set successfully
- Remove debug and dead code
- Optimization
  * run mkve less frequently
  * call backend from ajax less frequently
- Many interface fixes
- Many little bug fixes

* Fri Dec 26 2008 Anton Protopopov <aspsk@altlinux.org> 0.1-alt0.3
- Rewrite main interface
- Add conflict on alterator-ovz
- Add 'general options' to openvz configure
- Remove support for Device Access Management
- Move create part to mkve/create
- Hide machine info when no machines available
- Fix security hole: password appeared on command line
- Choose root password when creating new machine
- Rewrite 'capabilities'
- Add 'Autostart' button to main page
- Redirect to container
- Add support for setting capabilities via vzctl
- Use fake /proc/bc/$(veid)/resources (for shutted down machines)
- Add support for setting and resetting quotas in openvz machines
- Add support for setting and resetting ubc in openvz machines
- Add redirection to config pages
- Rewrite mkve wrapper
- Add description and default values to global variables
- Move 'ovz' -> 'openvz'
- Add new workflow
- Rename *ve-machines* -> *mkve*
- Remove ve-networks
- Update package to confirm new mkve(1)

* Thu Sep 04 2008 Anton Protopopov <aspsk@altlinux.org> 0.1-alt0.2
- Rename package: *-ve-machines -> *-mkve
- Rewrite web-interface
- Info textarea in ve-machines and ve-networks
- Add support for creating new networks
- Now view of configure.html depends on hypervisor type

* Wed Jul 02 2008 Anton Protopopov <aspsk@altlinux.org> 0.1-alt0.1
- Initial build
