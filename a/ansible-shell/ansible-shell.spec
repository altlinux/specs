Name: ansible-shell
Summary: Interactive shell for ansible
Version: 0.0.1
Release: alt2

Group: System/Libraries
License: Distributable
Source0: %name-%version.tar
Url: https://github.com/dominis/ansible-shell

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
Interactive shell for ansible built-in tab completion for all the modules.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%doc README.md

%changelog
* Mon Dec  2 2013 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt2
- git-20131202

* Tue Oct  8 2013 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
