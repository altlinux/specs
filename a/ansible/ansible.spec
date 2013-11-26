Name: ansible
Summary: SSH-based configuration management, deployment, and task execution system
Version: 1.4.0
Release: alt1

Group: System/Libraries
License: GPLv3
Source0: http://ansibleworks.com/releases/%name-%version.tar
Patch0:%name-%version-alt.patch
Url: http://ansibleworks.com

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%prep
%setup
%patch0 -p1

%build
%python_build

%install
%python_install
mkdir -p %buildroot%_sysconfdir/%name/
cp examples/hosts %buildroot%_sysconfdir/%name/
cp examples/ansible.cfg %buildroot%_sysconfdir/%name/
mkdir -p %buildroot/%_man1dir
cp -v docs/man/man1/*.1 %buildroot/%_man1dir/
mkdir -p %buildroot/%_datadir/%name
cp -va library/* %buildroot/%_datadir/%name/

%files
%_bindir/%{name}*
%config(noreplace) %_sysconfdir/%name
%_datadir/%name
%_man1dir/%{name}*
%python_sitelibdir/%{name}*
%doc examples/playbooks examples/scripts
%doc README.md CONTRIBUTING.md CHANGELOG.md RELEASES.txt

%changelog
* Tue Nov 26 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Nov 11 2013 Terechkov Evgenii <evg@altlinux.org> 1.3.4-alt1
- 1.3.4

* Tue Oct  8 2013 Terechkov Evgenii <evg@altlinux.org> 1.3.3-alt1
- 1.3.3

* Sun Sep 29 2013 Terechkov Evgenii <evg@altlinux.org> 1.3.2-alt1
- 1.3.2
