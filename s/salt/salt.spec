Summary: Tool to manage your infrastructure
Name: salt
Version: 0.10.5
Release: alt1
Url: http://saltstack.org
Source0: %name-%version.tar
License: apache-2.0
Group: System/Configuration/Other

BuildRequires: python-module-setuptools perl-podlators python-module-nose libzeromq-devel python-module-zmq-devel python-module-Crypto python-module-msgpack python-module-yaml

BuildArch: noarch

%add_python_req_skip win32api win32event win32service win32serviceutil winerror

%description
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in the
world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds, or even thousands of individual
servers. It handles them quickly and through a simple yet manageable interface.

%package -n python-module-salt
Summary: Management component for salt, a parallel remote execution system
Group: Development/Python
Requires: python-module-yaml python-module-msgpack python-module-json

%description  -n python-module-salt
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in the
world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds, or even thousands of individual
servers. It handles them quickly and through a simple yet manageable interface.

%package master
Summary: Management component for salt, a parallel remote execution system
Group: System/Configuration/Other

%description master
The Salt master is the central server to which all minions connect.

%package minion
Summary: Client component for salt, a parallel remote execution system
Group: System/Configuration/Other

%description minion
Salt minion is queried and controlled from the master.

%prep
%setup

%build
%__python setup.py build

%install
%__python setup.py install --prefix=/usr --root=%buildroot

install -D -m 755 pkg/altlinux/salt-master.init %buildroot%_initdir/salt-master
install -D -m 755 pkg/altlinux/salt-syndic.init %buildroot%_initdir/salt-syndic
install -D -m 755 pkg/altlinux/salt-minion.init %buildroot%_initdir/salt-minion

mkdir -p %buildroot%_unitdir
install -p -m 0644 pkg/salt-master.service %buildroot%_unitdir/
install -p -m 0644 pkg/salt-syndic.service %buildroot%_unitdir/
install -p -m 0644 pkg/salt-minion.service %buildroot%_unitdir/

mkdir -p %buildroot%_sysconfdir/salt/
install -p -m 0640 conf/minion.template %buildroot%_sysconfdir/salt/minion
install -p -m 0640 conf/minion.template %buildroot%_sysconfdir/salt/minion.template
install -p -m 0640 conf/master.template %buildroot%_sysconfdir/salt/master
install -p -m 0640 conf/master.template %buildroot%_sysconfdir/salt/master.template

mkdir -p %buildroot%_sysconfdir/sysconfig
echo "ARG=''" >  %buildroot%_sysconfdir/sysconfig/salt-master
echo "ARG=''" >  %buildroot%_sysconfdir/sysconfig/salt-syndic
echo "ARG=''" >  %buildroot%_sysconfdir/sysconfig/salt-minion

install -D -m 0644 pkg/salt_bash_completion %buildroot%_sysconfdir/bash_completion.d/salt

install -D -m 0644 pkg/master.logrotate %buildroot%_sysconfdir/logrotate.d/salt-master
install -D -m 0644 pkg/minion.logrotate %buildroot%_sysconfdir/logrotate.d/salt-minion

#check

%post master
%post_service salt-master
%post_service salt-syndic

%preun master
%preun_service salt-master
%preun_service salt-syndic

%post minion
%post_service salt-minion

%preun minion
%preun_service salt-minion


%files -n python-module-salt
%doc AUTHORS README* LICENSE HACKING.rst
%python_sitelibdir/*
%_man7dir/salt.7.*

%files master
%config(noreplace) %_sysconfdir/salt/master
%config %_sysconfdir/salt/master.template
%config %_sysconfdir/bash_completion.d/*
%config(noreplace) %_sysconfdir/logrotate.d/salt-master

%config(noreplace) %_sysconfdir/sysconfig/salt-master
%config(noreplace) %_sysconfdir/sysconfig/salt-syndic

%_initdir/salt-master
%_initdir/salt-syndic

%_unitdir/salt-master.service
%_unitdir/salt-syndic.service

%_bindir/salt
%_bindir/salt-master
%_bindir/salt-syndic
%_bindir/salt-cp
%_bindir/salt-key
%_bindir/salt-run

%_man1dir/salt-master.1.*
%_man1dir/salt.1.*
%_man1dir/salt-cp.1.*
%_man1dir/salt-key.1.*
%_man1dir/salt-run.1.*
%_man1dir/salt-syndic.1.*


%files minion
%config(noreplace) %_sysconfdir/salt/minion
%config %_sysconfdir/salt/minion.template
%config(noreplace) %_sysconfdir/logrotate.d/salt-minion

%config(noreplace) %_sysconfdir/sysconfig/salt-minion

%_initdir/salt-minion
%_unitdir/salt-minion.service

%_bindir/salt-minion
%_bindir/salt-call

%_man1dir/salt-call.1.*
%_man1dir/salt-minion.1.*

%changelog
* Thu Dec 06 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.10.5-alt1
- Build for ALT
