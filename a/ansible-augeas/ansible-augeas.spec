%define _ansibledir %_datadir/ansible

Name: ansible-augeas
Summary: Augeas module for ansible
Version: 0.0.1
Release: alt1

Group: System/Libraries
License: GPLv3+
Url: https://github.com/paluh/ansible-augeas.git
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

# Ansible requires python 2.4+, so we require augeas module for python2:
Requires: python-module-augeas
# python bindings dont work without low-level library:
Requires: libaugeas
# module is useless without ansible:
Requires: ansible >= 1.1

%description
Augeas module which exposes simple API for `match`, `set` and `rm`
operations. You can execute commands one by one or in chunk.

%prep
%setup
# %%patch0 -p1

%build

%install
install -pD -m 644 augeas %buildroot%_ansibledir/files/augeas

%files
%_ansibledir/files/augeas
%doc README.md

%changelog
* Sun Nov  9 2014 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt1
- git-20141005
