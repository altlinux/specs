Name: nagios-plugins-check_glusterfs
Version: 1.0
Release: alt2

Summary: Nagios(R) plug-in for checking glusterfs volume status

License: GPL
Group: Monitoring
Url: http://exchange.nagios.org/directory/Plugins/System-Metrics/File-System/GlusterFS-checks/details

Packager: Danil Mikhailov <danil@altlinux.org>

Source: %name-%version.tar

BuildArchitectures: noarch

%description
nagios-plugins-check_glusterfs checks GlusterFS health on the server. Tests include:
- daemons running
- number of bricks online
- disk space
- healing status

# nagios uses /usr/lib for plugins in any arch
%define pluginsdir %_prefix/lib/nagios/plugins

%prep
%setup


%install
mkdir -p %buildroot%pluginsdir/
install -m755 check_glusterfs %buildroot%pluginsdir/
mkdir -p -m700 %buildroot/etc/sudoers.d
install -m400 nagios_glusterfs %buildroot/etc/sudoers.d/


%files
/etc/sudoers.d/nagios_glusterfs
%pluginsdir/check_glusterfs
%doc README

%changelog
* Fri Feb 13 2015 Danil Mikhailov <danil@altlinux.org> 1.0-alt2
- Remove glusterfsd check

* Thu Feb 12 2015 Danil Mikhailov <danil@altlinux.org> 1.0-alt1
- The initial plugin build 
