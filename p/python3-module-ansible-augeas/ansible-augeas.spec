%define _ansibledir %python3_sitelibdir/ansible/modules

%define oname ansible-augeas

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Augeas module for ansible
License: GPLv3+
Group: System/Libraries
Url: https://github.com/paluh/ansible-augeas.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

Obsoletes: ansible-augeas < %EVR

# Ansible requires python 2.4+, so we require augeas module for python2:
Requires: python3-module-augeas

# python bindings dont work without low-level library:
Requires: libaugeas

# module is useless without ansible:
Requires: ansible >= 1.8


%description
Augeas module which exposes simple API for `match`, `set` and `rm`
operations. You can execute commands one by one or in chunk.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build

%install
install -pD -m 644 library/augeas.py %buildroot%_ansibledir/files/augeas.py

%files
%doc README.md
%_ansibledir/files/augeas.py
%python3_sitelibdir/*


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1
- Version updated to 1.0.0
- porting on python3.

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
