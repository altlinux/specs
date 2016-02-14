Name: ansible-shell
Summary: Interactive shell for ansible
Version: 0.0.6
Release: alt1

Group: System/Libraries
License: GPLv3
Source0: %name-%version.tar
Patch0: %name-%version-upstream.patch
Url: https://github.com/dominis/ansible-shell

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
Interactive shell for ansible built-in tab completion for all the modules.

%prep
%setup
%patch0 -p1

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%doc README.md

%changelog
* Sun Feb 14 2016 Terechkov Evgenii <evg@altlinux.org> 0.0.6-alt1
- Fix FTBFS/missed merge conflict
- 0.0.6-5-g590c182

* Wed Jul  8 2015 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt3.2
- Upstream fix for https://github.com/dominis/ansible-shell/issues/39

* Sun Jul  5 2015 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt3.1
- Fix for https://github.com/dominis/ansible-shell/issues/39

* Sun Jul  5 2015 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt3
- git-20150705

* Mon Dec  2 2013 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt2
- git-20131202

* Tue Oct  8 2013 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
