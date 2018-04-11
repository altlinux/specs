%define pyagentx_version 0.4.pcs.1

Name: 	  pcs
Version:  0.9.164
Release:  alt1
Epoch:    1

Summary:  Pacemaker/Corosync configuration system
License:  GPLv2
Group:    Other
Url: 	  https://github.com/ClusterLabs/pcs

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar
Source1:  pyagentx-v%pyagentx_version.tar.gz
Patch:    %name-%version-%release.patch
BuildArch: noarch

%add_python_req_skip pyagentx

BuildRequires: rpm-build-python rpm-build-ruby ruby python-devel corosync python-module-setuptools fontconfig fonts-ttf-liberation
#BuildRequires: python3-devel python3-module-setuptools
Requires: pacemaker

%filter_from_requires /^ruby(\(auth\|bootstrap\|cfgsync\|cluster\|cluster_entity\|config\|corosyncconf\|fenceagent\|pcs\|pcsd\|pcsd_file\|permissions\|remote\|resource\|session\|settings\|ssl\|wizard\|pcsd_test_utils\|test_auth\|test_cfgsync\|test_cluster\|test_cluster_entity\|test_config\|test_corosyncconf\|test_pcs\|test_permissions\|test_session\|pcsd_action_command\|pcsd_exchange_format\|pcsd_remove_file\))/d

%description
Pacemaker/Corosync configuration system with remote access

%package pcsd
Summary:  Pacemaker/Corosync cli and gui for configuration system
Requires: pcs
Group: Other
BuildArch: noarch
Requires: corosync
Requires: openssl
Requires: ruby-rack-handler-webrick < 2.0.0

%description pcsd
Pacemaker/Corosync gui/cli configuration system and daemon

%package pcsd-tests
Summary: tests for Pacemaker/Corosync cli and gui
Requires: pcs-pcsd
Group: Other
BuildArch: noarch

%description pcsd-tests
Tests for Pacemaker/Corosync gui/cli configuration system and daemon

%package snmp
Group: Other
Summary: Pacemaker cluster SNMP agent
License: GPLv2, BSD 2-clause
Requires: %name = %EVR
Requires: pacemaker
Requires: net-snmp

%description snmp
SNMP agent that provides information about pacemaker cluster to the master
agent (snmpd).

%prep
%setup
%patch -p1
mkdir -p pcs/bundled/tmp
tar xf %SOURCE1 -C pcs/bundled/tmp
make -C pcs/snmp PYAGENTX_DIR=../bundled/tmp/pyagentx-%pyagentx_version build_bundled_libs

%install
mkdir -p %buildroot%_libexecdir/pcs
mkdir -p %buildroot%_logdir/pcsd
%makeinstall_std PYAGENTX_INSTALLED=true
mkdir -p %buildroot%_libexecdir/pcs/bundled/packages
cp -a pcs/bundled/packages/* %buildroot%_libexecdir/pcs/bundled/packages
make install_pcsd DESTDIR=%buildroot BUILD_GEMS=false PCSD_PARENT_DIR=%ruby_sitelibdir
mkdir -p %buildroot/%_initdir
mv %buildroot/%_sysconfdir/init.d/pcsd %buildroot/%_initdir
install -Dm 0644 pcsd/pcsd.logrotate %buildroot%_logrotatedir/pcsd.logrotate
mkdir -p %buildroot/var/lib/pcsd
mkdir -p %buildroot/lib/systemd/system
install -Dm 0644 pcsd/pcsd.service %buildroot/lib/systemd/system/pcsd.service
install -Dm 0644 pcs/snmp/pcs_snmp_agent.service %buildroot/lib/systemd/system/pcs_snmp_agent.service

mkdir -p %buildroot/usr/sbin/
install -Dm 0755 pcsd/pcsd.service-runner %buildroot%_sbindir/pcsd
chmod 750 %buildroot/usr/sbin/pcsd

# Remove unnecessary stuff
rm -rf %buildroot/%ruby_sitelibdir/pcsd/*{.service,.logrotate,debian,orig}*

%post pcsd
%post_service pcsd

%preun pcsd
%preun_service pcsd

%post snmp
%post_service pcs_snmp_agent

%preun snmp
%preun_service pcs_snmp_agent

%files
%doc CHANGELOG.md COPYING README.md
%_sbindir/pcs
%python_sitelibdir_noarch/*
%_man8dir/*.*
%exclude %_man8dir/pcs_snmp_agent.*
%_sysconfdir/bash_completion.d/pcs

%files pcsd
%exclude %ruby_sitelibdir/pcsd/test/*
%ruby_sitelibdir/pcsd/*
%_initdir/pcsd
%_sysconfdir/logrotate.d/pcsd
%_sysconfdir/pam.d/pcsd
%_sysconfdir/sysconfig/pcsd
%dir %_logdir/pcsd
%dir /var/lib/pcsd
%_logrotatedir/pcsd.logrotate
/lib/systemd/system/pcsd.service
/usr/sbin/pcsd

%files pcsd-tests
%ruby_sitelibdir/pcsd/test/*

%files snmp
%config(noreplace) %_sysconfdir/sysconfig/pcs_snmp_agent
%_libexecdir/pcs/pcs_snmp_agent
%_libexecdir/pcs/bundled/packages/pyagentx*
/lib/systemd/system/pcs_snmp_agent.service
%_datadir/snmp/mibs/PCMK-PCS*-MIB.txt
%_man8dir/pcs_snmp_agent.*

%changelog
* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.164-alt1
- New version.

* Wed Mar 14 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.163-alt1
- New version.

* Fri Nov 03 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.161-alt1
- New version

* Sun Oct 15 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.160-alt1
- New version

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt3
- Completely remove requirement rack as gem
- pcs-pcsd requires openssl

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt2
- Comment out rack as gem load to prevent daemon fail

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Jul 14 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt1
- New version

* Thu Jun 29 2017 Denis Medvedev <nbr@altlinux.org> 1:0.9.158-alt3
- Added systemd unit (ALT #33590).

* Fri Jun 23 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.158-alt2
- Fix pathes to pcsd and pacemaker data (ALT #33580)

* Tue Jun 20 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.158-alt1
- New version
- Build from upstream tag
- Use initscript and daemon executable from upstream (ALT #33562)
- pcs-pcsd requires ruby-rack-handler-webrick (ALT #33561)

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.99.156-alt5
- pcs-pcsd requires corosync and ruby-rack-handler-webrick
- fix initscript

* Wed Jun 14 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt4
- Packaged pcsd (ALT #33522) (thanks cas@)

* Wed Apr 05 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt3
- changed default placement of pacemaker files

* Tue Apr 04 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt2
- added dependency to pacemaker

* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt1
- Initial release
