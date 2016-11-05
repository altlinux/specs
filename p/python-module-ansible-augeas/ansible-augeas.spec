%define _ansibledir %python_sitelibdir/ansible/modules

Name: python-module-ansible-augeas
Summary: Augeas module for ansible
Version: 0.0.1
Release: alt5

Group: System/Libraries
License: GPLv3+
Url: https://github.com/paluh/ansible-augeas.git
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch
Obsoletes: ansible-augeas < %EVR

# Ansible requires python 2.4+, so we require augeas module for python2:
Requires: python-module-augeas
# python bindings dont work without low-level library:
Requires: libaugeas
# module is useless without ansible:
Requires: ansible >= 1.8

%description
Augeas module which exposes simple API for `match`, `set` and `rm`
operations. You can execute commands one by one or in chunk.

%prep
%setup
# %%patch0 -p1

%build

%install
install -pD -m 644 augeas %buildroot%_ansibledir/files/augeas.py # modules have .py extension since ansible-1.8

%files
%_ansibledir/files/augeas.py
%doc README.md

%changelog
* Sat Nov  5 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt5
- Obsoletes etc.: For cleanliness, let's leave just it without Provides
  (as it was, but with %%EVR for future;
  https://www.altlinux.org/Girar_does_not_delete_obsoleted_pkgs )

* Thu Nov  3 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt4
- To delete old pkg, we need Provides: ansible-augeas

* Wed Jul 15 2015 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt3
- git-20150715

* Sun Nov 30 2014 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt2
- git-20141130

* Sun Nov  9 2014 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt1
- git-20141005
