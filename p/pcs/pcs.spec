Name: 	  pcs
Version:  0.99.156
Release:  alt4

Summary:  Pacemaker/Corosync configuration system
License:  GPLv2
Group:    Other
Url: 	  https://github.com/ClusterLabs/pcs

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-python rpm-build-ruby ruby python-devel corosync python-module-setuptools fontconfig fonts-ttf-liberation
Requires: pacemaker

%filter_from_requires /^ruby(\(auth\|bootstrap\|cfgsync\|cluster\|cluster_entity\|config\|corosyncconf\|fenceagent\|pcs\|pcsd\|pcsd_file\|permissions\|remote\|resource\|session\|settings\|ssl\|wizard\|pcsd_test_utils\|test_auth\|test_cfgsync\|test_cluster\|test_cluster_entity\|test_config\|test_corosyncconf\|test_pcs\|test_permissions\|test_session\))/d

%description
Pacemaker/Corosync configuration system with remote access

%package pcsd
Summary:  Pacemaker/Corosync cli and gui for configuration system
Requires: pcs
Group: Other
BuildArch: noarch

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

%install
%makeinstall_std
mkdir -p %buildroot/%_logdir/pcsd
make install_pcsd DESTDIR=%buildroot BUILD_GEMS=false PCSD_PARENT_DIR=%ruby_sitelibdir
mkdir -p %buildroot/%_initdir
mv %buildroot/%_sysconfdir/init.d/pcsd %buildroot/%_initdir
mkdir -p %buildroot/lib/systemd/system
cp %buildroot/%ruby_sitelibdir/pcsd/pcsd.service %buildroot/lib/systemd/system
mkdir -p %buildroot/%_sbindir
cp %buildroot/%ruby_sitelibdir/pcsd/pcsd.bin %buildroot%_sbindir/pcsd
mkdir -p %buildroot/var/lib/pcsd

%post pcsd
%post_service pcsd

%preun pcsd
%preun_service pcsd

%files
%doc CHANGELOG.md COPYING README.md
%_sbindir/*
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
/lib/systemd/system/*
%dir /var/lib/pcsd
%_sbindir/pcsd

%files pcsd-tests
%ruby_sitelibdir/pcsd/test/*

%changelog
* Wed Jun 14 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt4
- Packaged pcsd (ALT #33522) (thanks cas@)

* Wed Apr 05 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt3
- changed default placement of pacemaker files

* Tue Apr 04 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt2
- added dependency to pacemaker

* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt1
- Initial release
