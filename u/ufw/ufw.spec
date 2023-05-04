Name: ufw
Version: 0.35
Release: alt1
Summary: Uncomplicated Firewall
Group: System/Configuration/Networking

License: GPLv3
Url: https://launchpad.net/%name
Source0: https://launchpad.net/%name/%version/%version/+download/ufw-%version.tar.gz
# systemd service file
Source1: ufw.service
# Install translations to the systemwide standard location for %%find_lang
Patch0: ufw-0.35-trans-dir.patch
# Separate libexec_dir from state_dir because the state files must go into /var,
# whereas the scripts don't belong there (we install them to /usr/libexec
# instead). Upstream used to install everything into /lib/ufw, a hack to make
# separate /var work on Ubuntu, but /lib/ufw is /usr/lib/ufw in Fedora and that
# must not contain writable state data according to Fedora packaging guidelines.
# Now, upstream essentially uses state_dir only for libexec-type stuff, and has
# moved user.rules and user6.rules back to /etc, we move them back to /var/lib.
Patch1: ufw-0.35-libexec-dir.patch
# Default to enabled, let systemd handle whether ufw is actually enabled
Patch2: ufw-0.34~rc-default-enabled.patch
# Allow SSH connections by default
Patch3: ufw-0.34~rc-default-allow-ssh.patch
# Define multicast protocols (mDNS, UPnP) as a normal protocol profile
# Use a managed rule instead of a "before" rule for default-allowing mDNS
# Do not allow UPnP by default at all, document in ufw.8 how it can be allowed
# Update the README file and the ufw.8 manpage according to the above changes
Patch4: ufw-0.34~rc-multicast.patch
# Add protocol profiles for KDE Connect (#1257699) and Icecream (#1262009)
Patch5: ufw-0.34~rc-additional-profiles.patch
# Fix check-requirements for Python 3.5, add 3.6, remove unsupported 3.2/3.3
Patch6: ufw-0.35-python36.patch
# Change permissions of the *.rules files from 0640 to 0644
# Change permissions of the before.init and after.init hooks from 0640 to 0755
Patch7: ufw-0.35-permissions.patch
# Don't prepend /usr/bin/env to sys.executable, which is always an absolute path
Patch8: ufw-0.35-no-pointless-env.patch

BuildArch: noarch
Requires: conntrack-tools

# Automatically added by buildreq on Thu May 04 2023
# optimized out: libgpg-error python3 python3-base python3-dev python3-module-pkg_resources sh4
BuildRequires: iptables python3-module-setuptools

%description
The Uncomplicated Firewall(ufw) is a front-end for netfilter, which
aims to make it easier for people unfamiliar with firewall concepts.
Ufw provides a framework for managing netfilter as well as
manipulating the firewall.

%prep
%setup
%patch0 -p1 -b .trans-dir
%patch1 -p1 -b .libexec-dir
%patch2 -p1 -b .default-enabled
%patch3 -p1 -b .default-allow-ssh
%patch4 -p1 -b .multicast
rm -f profiles/*.multicast
%patch5 -p1 -b .additional-profiles
rm -f profiles/*.additional-profiles
%patch6 -p1 -b .python36
%patch7 -p1 -b .permissions
%patch8 -p1 -b .no-pointless-env

%build
%python3_build

%install
%python3_install
install -D -p -m 644 %SOURCE1 %buildroot%_unitdir/ufw.service
%find_lang %name

%files -f %name.lang
%doc ChangeLog README TODO AUTHORS
%_sbindir/ufw
%_prefix/libexec/ufw/
%python3_sitelibdir/*
%_datadir/ufw/
%_unitdir/ufw.service
# config files under /etc, directly user-editable, should survive updates
%dir %_sysconfdir/ufw/
%config(noreplace) %_sysconfdir/ufw/after.init
%config(noreplace) %_sysconfdir/ufw/after.rules
%config(noreplace) %_sysconfdir/ufw/after6.rules
%config(noreplace) %_sysconfdir/ufw/before.init
%config(noreplace) %_sysconfdir/ufw/before.rules
%config(noreplace) %_sysconfdir/ufw/before6.rules
%config(noreplace) %_sysconfdir/ufw/sysctl.conf
%config(noreplace) %_sysconfdir/ufw/ufw.conf
%dir %_sysconfdir/ufw/applications.d/
%config(noreplace) %_sysconfdir/ufw/applications.d/ufw-*
%config(noreplace) %_sysconfdir/ufw/applications.d/fedora-*
%config(noreplace) %_sysconfdir/default/ufw
# state files under /var, not directly user-editable, but should survive updates
%dir %_sharedstatedir/ufw/
%config(noreplace) %_sharedstatedir/ufw/user.rules
%config(noreplace) %_sharedstatedir/ufw/user6.rules
%_mandir/man8/ufw-framework.8*
%_mandir/man8/ufw.8*

%changelog
* Thu May 04 2023 Fr. Br. George <george@altlinux.org> 0.35-alt1
- Initial build for ALT from Fedora
