Name: 	  pcs
Version:  0.9.158
Release:  alt1
Epoch:    1

Summary:  Pacemaker/Corosync configuration system
License:  GPLv2
Group:    Other
Url: 	  https://github.com/ClusterLabs/pcs

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch
BuildArch: noarch

BuildRequires: rpm-build-python rpm-build-ruby ruby python-devel corosync python-module-setuptools fontconfig fonts-ttf-liberation
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

%prep
%setup
%patch -p1

%install
%makeinstall_std
mkdir -p %buildroot/%_logdir/pcsd
make install_pcsd DESTDIR=%buildroot BUILD_GEMS=false PCSD_PARENT_DIR=%ruby_sitelibdir
mkdir -p %buildroot/%_initdir
mv %buildroot/%_sysconfdir/init.d/pcsd %buildroot/%_initdir
install -Dm 0644 pcsd/pcsd.logrotate %buildroot%_logrotatedir/pcsd.logrotate
mkdir -p %buildroot/var/lib/pcsd

# Remove unnecessary stuff
rm -rf %buildroot/%ruby_sitelibdir/pcsd/*{.service,.logrotate,debian,orig}*

%post pcsd
%post_service pcsd

%preun pcsd
%preun_service pcsd

%files
%doc CHANGELOG.md COPYING README.md
%_sbindir/pcs
%python_sitelibdir_noarch/*
%_man8dir/*.*
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

%files pcsd-tests
%ruby_sitelibdir/pcsd/test/*

%changelog
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
