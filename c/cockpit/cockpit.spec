%define _unpackaged_files_terminate_build 1

%define _localstatedir %_var
%define _libexecdir    /usr/libexec
%define cockpit_user   _cockpit-ws
%define cockpit_group  _cockpit-ws
%define cockpit_wsinstance_user  _cockpit-wsinstance

%def_with doc

%def_with optional
%define with_pcp 1
%define with_packagekit 1

%if_without optional
# force disable
%define with_pcp 0
%define with_packagekit 0
%endif

%if %with_pcp
%def_with pcp
%else
%def_without pcp
%endif

%if %with_packagekit
%def_with packagekit
%else
%def_without packagekit
%endif

%def_with check

###############################################################################

Name: cockpit
Version: 280.1
Release: alt1

Summary: Web Console for Linux servers
License: LGPLv2+
Group: System/Base
VCS: https://github.com/cockpit-project/cockpit.git
Url: https://cockpit-project.org/
Source0: %name-%version.tar
Source1: cockpit.alt.pam
Source2: vendor_nodejs.tar
Patch: %name-%version-alt.patch

BuildRequires: node
BuildRequires: libgnutls-devel
BuildRequires: libjson-glib-devel
BuildRequires: libsystemd-devel
BuildRequires: libpolkit-devel
BuildRequires: libkrb5-devel
BuildRequires: libpam0-devel

BuildRequires: libssh-devel >= 0.8.5
BuildRequires: xsltproc

%if_with doc
BuildRequires: xmlto
%endif

%if_with pcp
BuildRequires: libpcopilot-devel
%endif

%if_with check
BuildRequires: glib-networking
BuildRequires: polkit
BuildRequires: openssh-common
BuildRequires: openssh-clients
BuildRequires: dbus
BuildRequires: /proc
BuildRequires: /dev/pts
%endif

# e.g. cockpit-client is written in Python
BuildRequires: rpm-build-python3

Requires: cockpit-bridge
Requires: cockpit-ws
Requires: cockpit-system
# Optional components
Requires: cockpit-networkmanager
Requires: cockpit-storaged
%if_with packagekit
Requires: cockpit-packagekit
%endif
%if_with pcp
Requires: cockpit-pcp
%endif

%description
The Cockpit Web Console enables users to administer GNU/Linux servers using a
web browser.

It offers network configuration, log inspection, diagnostic reports, SELinux
troubleshooting, interactive command-line sessions, and more.

###############################################################################

%package bridge
Summary: Cockpit bridge server-side component
Group: System/Base
Requires: glib-networking

%description bridge
The Cockpit bridge component installed server side and runs commands on the
system on behalf of the web based user interface.

###############################################################################

%package ssh
Summary: Cockpit ssh server-side component
Group: System/Base

%description ssh
The Cockpit ssh component installed server side and runs commands on the
system on behalf of the web based user interface.

###############################################################################

%package doc
Summary: Cockpit deployment and developer guide
Group: Documentation
BuildArch: noarch

%description doc
The Cockpit Deployment and Developer Guide shows sysadmins how to
deploy Cockpit on their machines as well as helps developers who want to
embed or extend Cockpit.

###############################################################################

%package system
Summary: Cockpit admin interface package for configuring and troubleshooting a system
Group: System/Base
BuildArch: noarch
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: cockpit-systemd
Requires: cockpit-tuned
Requires: cockpit-users
Requires: cockpit-metrics
%description system
This package contains the Cockpit shell and system configuration interfaces.

###############################################################################

%package metrics
Summary: Cockpit admin interface package for metrics
Group: System/Base
BuildArch: noarch

%description metrics
This package contains the Cockpit metrics configuration interfaces.

###############################################################################

%package shell
Summary: Cockpit admin interface package for configuring shell
Group: System/Base
BuildArch: noarch
Conflicts: cockpit-dashboard
Obsoletes: cockpit-dashboard < 247

%description shell
This package contains the Cockpit shell configuration interfaces.

###############################################################################

%package systemd
Summary: Cockpit admin interface package for configuring systemd
Group: System/Base
BuildArch: noarch
Conflicts: cockpit-realmd
Obsoletes: cockpit-realmd < 247

%description systemd
This package contains the Cockpit systemd configuration interfaces.

###############################################################################

%package tuned
Summary: Cockpit admin interface package for configuring tuned
Group: System/Base
BuildArch: noarch
Requires: tuned

%description tuned
This package contains the Cockpit tuned configuration interfaces.

###############################################################################

%package users
Summary: Cockpit admin interface package for configuring users
Group: System/Base
BuildArch: noarch

# /usr/bin/pwqcheck
Requires: passwdqc-utils

%description users
This package contains the Cockpit users configuration interfaces.

###############################################################################

%package ws
Summary: Cockpit Web Service
Group: System/Base
Requires: glib-networking
Requires: glib2 >= 2.37.4
# drop requirement on symlink, which is created at runtime
# by cockpit.socket service
%filter_from_requires /^\/run\/cockpit\/motd$/d

%description ws
The Cockpit Web Service listens on the network, and authenticates users.

If sssd-dbus is installed, you can enable client certificate/smart card
authentication via SSSD/FreeIPA.

###############################################################################

%package kdump
Summary: Cockpit user interface for kernel crash dumping
Group: System/Base
BuildArch: noarch
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: kexec-tools

%description kdump
The Cockpit component for configuring kernel crash dumping.

###############################################################################

%package sosreport
Summary: Cockpit user interface for diagnostic reports
Group: System/Base
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: sos
BuildArch: noarch

%description sosreport
The Cockpit component for creating diagnostic reports with the
sosreport tool.

###############################################################################

%package networkmanager
Summary: Cockpit user interface for networking, using NetworkManager
Group: System/Base
BuildArch: noarch
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: NetworkManager

%description networkmanager
The Cockpit component for managing networking. This package uses
NetworkManager.

###############################################################################

%if_with optional

%package storaged
Summary: Cockpit user interface for storage, using udisks
Group: System/Base
BuildArch: noarch
Requires: cockpit-shell
Requires: udisks2
Requires: udisks2-module-lvm2
# not packaged in ALT
# Requires: udisks2-iscsi >= 2.6
Requires: multipath-tools
Requires: python3(dbus)

%description storaged
The Cockpit component for managing storage.  This package uses udisks.

###############################################################################

%package tests
Summary: Tests for Cockpit
Group: System/Base
Requires: cockpit-bridge
Requires: cockpit-system
Requires: openssh-clients

%description tests
This package contains tests and files used while testing Cockpit.
These files are not required for running Cockpit.

###############################################################################

%if_with pcp
%package pcp
Summary: Cockpit PCP integration
Group: System/Base
Requires: cockpit-bridge
Requires: pcp

%description pcp
Cockpit support for reading PCP metrics and loading PCP archives.
%endif

###############################################################################

%if_with packagekit
%package packagekit
Summary: Cockpit user interface for packages
Group: System/Base
BuildArch: noarch
Requires: cockpit-bridge
Requires: packagekit

%description packagekit
The Cockpit components for installing OS updates and Cockpit add-ons,
via PackageKit.
%endif


%endif
###############################################################################

%prep
%setup -a2
%patch -p1

echo 'm4_define(VERSION_NUMBER, [%version])' > version.m4

[ -e package-lock.json ] || touch package-lock.json

# systemd tmpfiles in ALTLinux are packaged into /lib/tmpfiles.d
grep -q 'tempconfdir = $(prefix)/lib/tmpfiles.d' src/systemd/Makefile.am || exit 1
sed -i '/tempconfdir = $(prefix)\/lib\/tmpfiles.d/{s@$(prefix)/lib/tmpfiles.d@%_tmpfilesdir@}' \
src/systemd/Makefile.am

# ALT uses /etc/openssh directory, not /etc/ssh one
grep -qr '/ssh/ssh_known_hosts' || exit 1
grep -rl '/ssh/ssh_known_hosts' | \
xargs sed -i 's/\/ssh\/ssh_known_hosts/\/openssh\/ssh_known_hosts/g'

# /usr/bin -> /bin
grep -qr '/usr/bin/true' || exit 1
grep -rl '/usr/bin/true' | xargs sed -i 's/\/usr\/bin\/true/\/bin\/true/g'

grep -qr '/usr/bin/false' || exit 1
grep -rl '/usr/bin/false' | xargs sed -i 's/\/usr\/bin\/false/\/bin\/false/g'

%if_with pcp
# pcp name in ALTLinux is pcopilot due to name conflicts
grep -rl -- '\(-lpcp\|#include <pcp/\)' | xargs \
    sed -i \
        -e 's/-lpcp/-lpcopilot/g' \
        -e 's/#include <pcp\//#include <pcopilot\//g'
sed -i \
    -e 's/AC_CHECK_LIB(pcp/AC_CHECK_LIB(pcopilot/g' \
    -e 's/pcp\//pcopilot\//g' \
    configure.ac
%endif

%build
%autoreconf

%configure \
    --disable-silent-rules \
    %{?_without_pcp:--disable-pcp } \
    %{?_without_doc:--disable-doc } \
    --with-cockpit-user=%cockpit_user \
    --with-cockpit-ws-instance-user=%cockpit_wsinstance_user \
    --with-pamdir=%_pam_modules_dir \
    %nil

# run eslint even in production mode to catch any breakages caused by ALT's
# changes and new upstream's code
export ESLINT=1
%make_build all

%check
%make_build VERBOSE=1 check

%install
%makeinstall_std
%make install-tests DESTDIR=%buildroot
mkdir -p %buildroot%_sysconfdir/pam.d
install -p -m 644 %SOURCE1 %buildroot%_sysconfdir/pam.d/cockpit

%if_without packagekit
rm -r %buildroot/%_datadir/cockpit/packagekit
rm -r %buildroot/%_datadir/cockpit/apps
%endif

%if_without pcp
rm -r %buildroot%_datadir/cockpit/pcp/
%endif

%find_lang cockpit

# remove selinux stuff
rm -r %buildroot/%_datadir/cockpit/selinux
rm %buildroot%_datadir/metainfo/org.cockpit-project.cockpit-selinux.metainfo.xml

%if_without optional
for pkg in playground storaged; do
    rm -r %buildroot/%_datadir/cockpit/$pkg
done
rm %buildroot%_pam_modules_dir/mock-pam-conv-mod.so
rm %buildroot%_datadir/metainfo/org.cockpit-project.cockpit-storaged.metainfo.xml
%endif

# remove not default brandings, as they have broken symlinks
pushd %buildroot/%_datadir/cockpit/branding
ls -1 | (. /etc/os-release; grep -v "default\|$ID") | xargs rm -vr
popd

# ghost files
mkdir -p %buildroot%_sysconfdir/cockpit
touch %buildroot%_sysconfdir/cockpit/disallowed-users

###############################################################################

%files
%doc AUTHORS COPYING README.md
%_datadir/metainfo/cockpit.appdata.xml
%_datadir/pixmaps/cockpit.png
%doc %_man1dir/cockpit.1.*

%files bridge
%doc %_man1dir/cockpit-bridge.1.*
%_sysconfdir/cockpit/machines.d/
%dir %_datadir/cockpit
%_datadir/cockpit/base1/
%_datadir/polkit-1/actions/org.cockpit-project.cockpit-bridge.policy
%_bindir/cockpit-bridge
%_libexecdir/cockpit-askpass

%files ssh
%_datadir/cockpit/ssh/
%_libexecdir/cockpit-ssh

%files doc
%_docdir/cockpit

%files system

%files metrics
%_datadir/cockpit/metrics/

%files shell
%_datadir/cockpit/shell/

%files systemd
%_datadir/cockpit/systemd/

%files tuned
%_datadir/cockpit/tuned/

%files users
%_datadir/cockpit/users/

%files ws -f cockpit.lang
%doc %_man1dir/cockpit-desktop.1.*
%doc %_man5dir/cockpit.conf.5.*
%doc %_man8dir/cockpit-ws.8.*
%doc %_man8dir/cockpit-tls.8.*
%doc %_man8dir/pam_ssh_add.8.*
%config(noreplace) %_sysconfdir/cockpit/ws-certs.d/
%config(noreplace) %_sysconfdir/pam.d/cockpit

# managed by post script
%ghost %_sysconfdir/issue.d/cockpit.issue
%ghost %_sysconfdir/motd.d/cockpit
%ghost %attr(0644, root, root) %_sysconfdir/cockpit/disallowed-users

%_datadir/cockpit/motd/update-motd
%_datadir/cockpit/motd/inactive.motd
%_unitdir/cockpit.service
%_unitdir/cockpit-motd.service
%_unitdir/cockpit.socket
%_unitdir/cockpit-wsinstance-http.socket
%_unitdir/cockpit-wsinstance-http.service
%_unitdir/cockpit-wsinstance-https-factory.socket
%_unitdir/cockpit-wsinstance-https-factory@.service
%_unitdir/cockpit-wsinstance-https@.socket
%_unitdir/cockpit-wsinstance-https@.service
%_unitdir/system-cockpithttps.slice
%_tmpfilesdir/cockpit-tempfiles.conf
%_pam_modules_dir/pam_ssh_add.so
%_pam_modules_dir/pam_cockpit_cert.so
%_libexecdir/cockpit-ws
%_libexecdir/cockpit-wsinstance-factory
%_libexecdir/cockpit-tls
%_libexecdir/cockpit-client
%_libexecdir/cockpit-client.ui
%_libexecdir/cockpit-desktop
%_libexecdir/cockpit-certificate-helper
%_libexecdir/cockpit-certificate-ensure
%attr(4710, root, %cockpit_wsinstance_user) %_libexecdir/cockpit-session
%_datadir/cockpit/static/
%_datadir/cockpit/branding/

%pre ws
%_sbindir/groupadd -r -f %cockpit_group >/dev/null 2>&1 ||:
%_sbindir/useradd -r -g %cockpit_group -d %_sharedstatedir/cockpit -s \
/dev/null -c "User for cockpit web service" %cockpit_user >/dev/null 2>&1 ||:

%_sbindir/groupadd -r -f %cockpit_wsinstance_user >/dev/null 2>&1 ||:
%_sbindir/useradd -r -g %cockpit_wsinstance_user -d %_sharedstatedir/cockpit -s \
/dev/null -c "User for cockpit-ws instances" %cockpit_wsinstance_user >/dev/null 2>&1 ||:

%post ws
if [ "$1" -eq 1 ]; then
    # in ALT nothing provides these dirs yet
    mkdir -p %_sysconfdir{motd.d,issue.d}

    ln -s ../../run/cockpit/motd %_sysconfdir/motd.d/cockpit
    ln -s ../../run/cockpit/motd %_sysconfdir/issue.d/cockpit.issue

    printf '# List of users which are not allowed to login to Cockpit\nroot\n' > %_sysconfdir/cockpit/disallowed-users
    chmod 644 %_sysconfdir/cockpit/disallowed-users
fi
systemd-tmpfiles --create cockpit-tempfiles.conf >/dev/null 2>&1 ||:
%post_service cockpit.socket
%post_service cockpit.service

%preun ws
%preun_service cockpit.socket
%preun_service cockpit.service

%files kdump
%_datadir/cockpit/kdump/
%_datadir/metainfo/org.cockpit-project.cockpit-kdump.metainfo.xml

%files sosreport
%_datadir/cockpit/sosreport/
%_datadir/metainfo/org.cockpit-project.cockpit-sosreport.metainfo.xml
%_datadir/pixmaps/cockpit-sosreport.png

%files networkmanager
%_datadir/cockpit/networkmanager/

%if_with optional

%files storaged
%_datadir/cockpit/storaged/
%_datadir/metainfo/org.cockpit-project.cockpit-storaged.metainfo.xml

%files tests
%_datadir/cockpit/playground/
%_pam_modules_dir/mock-pam-conv-mod.so

%if_with pcp
%files pcp
%_libexecdir/cockpit-pcp
%_sharedstatedir/pcp/config/pmlogconf/tools/cockpit
%_datadir/cockpit/pcp/

%post pcp
%post_service pcp
%endif

%if_with packagekit
%files packagekit
%_datadir/cockpit/apps/
%_datadir/cockpit/packagekit/
%endif

%endif # build optional extension packages

%changelog
* Tue Nov 29 2022 Stanislav Levin <slev@altlinux.org> 280.1-alt1
- 280 -> 280.1.

* Mon Nov 21 2022 Stanislav Levin <slev@altlinux.org> 280-alt1
- 253 -> 280.

* Mon Sep 20 2021 Stanislav Levin <slev@altlinux.org> 253-alt1
- 247 -> 253.

* Mon Jun 28 2021 Stanislav Levin <slev@altlinux.org> 247-alt1
- 209 -> 247.

* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 209-alt1.1
- NMU: applied logoved fixes

* Tue Dec 17 2019 Stanislav Levin <slev@altlinux.org> 209-alt1
- 208 -> 209.
- Built with Performance Co-Pilot framework.

* Fri Nov 29 2019 Stanislav Levin <slev@altlinux.org> 208-alt1
- 202 -> 208.

* Thu Sep 05 2019 Stanislav Levin <slev@altlinux.org> 202-alt1
- 194 -> 202.

* Thu Jul 18 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 194-alt2
- Enabled docker and kubernetes subpackages on ppc64le.

* Mon May 27 2019 Stanislav Levin <slev@altlinux.org> 194-alt1
- 192 -> 194.

* Thu Apr 18 2019 Stanislav Levin <slev@altlinux.org> 192-alt1
- 191 -> 192.

* Tue Apr 16 2019 Stanislav Levin <slev@altlinux.org> 191-alt1
- 189 -> 191.
- Fixed FTBFS.

* Tue Mar 12 2019 Stanislav Levin <slev@altlinux.org> 189-alt1
- 187 -> 189.

* Thu Feb 07 2019 Stanislav Levin <slev@altlinux.org> 187-alt1
- 185 -> 187.
- Increased build timeout.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 185-alt1
- 180 -> 185.

* Wed Oct 17 2018 Stanislav Levin <slev@altlinux.org> 180-alt1
- Initial build.

