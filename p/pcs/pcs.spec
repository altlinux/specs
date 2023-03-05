%define _unpackaged_files_terminate_build 1
%define pyagentx_version 0.4.pcs.2

Name: 	       pcs
Epoch:         1
Version:       0.11.5
Release:       alt1
Summary:       Pacemaker/Corosync configuration system
License:       GPL-2.0 and Apache-2.0 and MIT
Group:         System/Servers
Url:           https://github.com/ClusterLabs/pcs
Vcs:           https://github.com/ClusterLabs/pcs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       pyagentx-v%pyagentx_version.tar.gz
Source2:       pcsd
Source3:       known-hosts
Patch:         compat.patch

%add_python3_req_skip pyagentx
Requires:      python3-module-pcs = %version
Requires:      python3-module-snmp = %version
Obsoletes:     pcs-pcsd < %EVR
Provides:      pcs-pcsd = %EVR

Requires: gem-rack
Requires: gem-sinatra
Requires: gem-rack-protection
Requires: gem-thin
Requires: gem-rake-compiler-dock
Requires: gem-open4
Requires: gem-backports
Requires: gem-ethon
Requires: gem-rspec

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-ruby
BuildRequires: corosync fontconfig fonts-ttf-liberation
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-lxml
BuildRequires: python3-module-pip
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-pycurl
BuildRequires: python3-module-pyparsing
BuildRequires: python3-module-dacite
BuildRequires: python3-module-tornado >= 6.0.0
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-distro
BuildRequires: python3-module-wheel
BuildRequires: gem-backports
BuildRequires: ruby-daemons
BuildRequires: gem-ethon
BuildRequires: gem-eventmachine
BuildRequires: ruby-open4
BuildRequires: gem-rack
BuildRequires: gem-rack-protection
BuildRequires: gem-rack-test
BuildRequires: gem-sinatra
BuildRequires: gem-tilt
BuildRequires: gem-thin
BuildRequires: gem-rexml
BuildRequires: gem-webrick
BuildRequires: gem-childprocess
BuildRequires: gem-nio4r
BuildRequires: gem-puma
BuildRequires: libpacemaker-devel
BuildRequires: libsystemd-devel
BuildRequires: wget
BuildRequires: service
BuildRequires: nss-utils

%description
Pacemaker/Corosync configuration system with remote access
Pacemaker/Corosync gui/cli configuration system and daemon

%package       -n python3-module-pcs
Summary:       Python module for pacemaker/corosync gui/cli configuration system and daemon
Group:         Development/Python3
BuildArch:     noarch
Requires:      %name = %version
Requires:      pacemaker >= 2.0.3-alt2

%description   -n python3-module-pcs
Python module for pacemaker/corosync gui/cli configuration system and daemon

%package       -n python3-module-snmp
Group:         Development/Python3
Summary:       Pacemaker cluster SNMP agent
License:       GPL-2.0 or BSD-2-Clause
Requires:      %name = %EVR
Requires:      pacemaker >= 2.0.3-alt2
Requires:      net-snmp
Obsoletes:     pcs-snmp < %EVR
Provides:      pcs-snmp = %EVR

%description   -n python3-module-snmp
SNMP agent that provides information about pacemaker cluster to the master
agent (snmpd).

%prep
%setup
%patch -p1
cp %SOURCE1 rpm
mkdir -p pcs_bundled/src
echo %version > .tarball-version
echo %version > .version

%build
%autoreconf
export PATH=/sbin:$PATH
%configure \
    --with-distro=fedora \
    --enable-local-build \
    --enable-use-local-cache-only \
    --enable-individual-bundling \
    --localstatedir=%_var \
    PYTHON=%__python3 \
    SYSTEMCTL="/bin/systemctl"
%make_build

%install
%makeinstall_std \
     BUILD_GEMS=false \
     SYSTEMCTL_OVERRIDE=true \
     DEST_SYSTEMD_SYSTEM=%buildroot%systemd_unitdir \
     bashcompletiondir=%_sysconfdir/bash_completion.d

install -Dm 0755 %SOURCE2 %buildroot%_initdir/pcsd
install -Dm 0644 %SOURCE3 %buildroot%_localstatedir/pcsd/known-hosts

# Set correct python3 executable in shebang
subst 's|#!.*python$|#!%__python3|' %buildroot%_libdir/pcs/pcs_bundled/packages/pyagentx/*.py

# Remove wrong placed documentation
rm -f %buildroot%_defaultdocdir/pcs/*.md

%check
%ruby_test

%post
%post_service pcsd

%preun
%preun_service pcsd

%post -n python3-module-snmp
%post_service pcs_snmp_agent

%preun -n python3-module-snmp
%preun_service pcs_snmp_agent

%files
%doc CHANGELOG.md COPYING README.md
%_sbindir/pcs
%_man8dir/*.*
%exclude %_man8dir/pcs_snmp_agent.*
%_sysconfdir/bash_completion.d/pcs
%_sbindir/pcsd
%_initdir/pcsd
%_libdir/pcsd
%dir %_libdir/pcs
%dir %_libdir/pcs/pcs_bundled
%dir %_libdir/pcs/pcs_bundled/packages/
%_libdir/pcs/pcs_internal
%_libdir/pcs/data
%config(noreplace) %_sysconfdir/pam.d/pcsd
%config(noreplace) %_sysconfdir/sysconfig/pcsd
%config(noreplace) %_logrotatedir/pcsd
%dir %_logdir/pcsd
%dir %_localstatedir/pcsd
%systemd_unitdir/pcsd.service
%systemd_unitdir/pcsd-ruby.service
%_localstatedir/pcsd/known-hosts

%files -n python3-module-pcs
%python3_sitelibdir_noarch/*

%files -n python3-module-snmp
%config(noreplace) %_sysconfdir/sysconfig/pcs_snmp_agent
%_libdir/pcs/pcs_snmp_agent
%_libdir/pcs/pcs_bundled/packages/pyagentx*
%systemd_unitdir/pcs_snmp_agent.service
%_datadir/snmp/mibs/PCMK-PCS*-MIB.txt
%_man8dir/pcs_snmp_agent.*

%changelog
* Fri Mar 03 2023 Andrey Cherepanov <cas@altlinux.org> 1:0.11.5-alt1
- New version.

* Thu Nov 24 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.11.4-alt1
- New version.

* Fri Jun 24 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.11.3-alt1
- New version.

* Wed May 18 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.11.2-alt3
- Used pacemaker development package for real pacemaker pathes (ALT #40854).

* Tue Apr 05 2022 Alexander Danilov <admsasha@altlinux.org> 1:0.11.2-alt2
- FTBFS: fixed build

* Sat Feb 05 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.11.2-alt1
- New version.

* Fri Dec 03 2021 Egor Ignatov <egori@altlinux.org> 1:0.11.1-alt3
- package ocf-1.0.rng and ocf-1.1.rng

* Thu Dec 02 2021 Egor Ignatov <egori@altlinux.org> 1:0.11.1-alt2
- Explicitly set SYSTEMCTL for configure script (pcs systemd driver
  didn't work because systemctl_binary in settings.py was not set).

* Wed Dec 01 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.11.1-alt1
- New version.

* Fri Nov 26 2021 Egor Ignatov <egori@altlinux.org> 1:0.10.11-alt2
- Add missing dependencies

* Fri Oct 08 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.10.11-alt1
- New version.
- Do not use ruby macros.

* Fri Aug 20 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.10.10-alt1
- New version.
- Leave only python module in python3-module-pcs.
- Mark config files.

* Tue Aug 10 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.10.9-alt1
- New version.

* Tue May 18 2021 Pavel Vasenkov <pav@altlinux.org> 1:0.10.8-alt2
- Disable python2 requirement

* Tue Feb 02 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.10.8-alt1
- New version.

* Fri Oct 02 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.10.7-alt1
- New version.

* Fri Jun 12 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.10.6-alt1
- New version.
- Tranasform old ALT-specific to replace regexp.
- Fix License and Group tags.

* Fri Apr 03 2020 Pavel Skrylev <majioa@altlinux.org> 1:0.10.5-alt2
- + proper patch to fix config
- + pcsd init script
- + joint pcs and ruby-pcsd

* Wed Mar 18 2020 Pavel Skrylev <majioa@altlinux.org> 1:0.10.5-alt1
- ^ 0.10.4 -> 0.10.5 (closes #36898)
- fixed ! pcsd start (closes #37837)
- fixed ! license according to SPDX and licenses in some files

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1:0.10.4-alt1
- updated (^) 0.10.3 -> 0.10.4
- fixed (!) spec
- fixed (!) lost provides, and requires

* Mon Sep 09 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.10.3-alt1.1
- fixed (!) spec according to changelog rules

* Sun Aug 25 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.10.3-alt1
- used (>) Ruby Policy 2.0
- updated (^) 0.10.2 -> 0.10.3
- fixed (!) names of subpackages according to the language they were written in

* Mon Aug 12 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.10.2-alt1
- New version.
- Remove obsolete initscript.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.166-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.165-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.165-alt1
- New version.

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
