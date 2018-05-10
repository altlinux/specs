Name:     semaphore
Version:  2.4.1
Release:  alt1

Summary:  Open Source alternative to Ansible Tower
License:  MIT
Group:    Other
Url:      https://github.com/ansible-semaphore/semaphore

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source0:  %name-%version.tar
Source1:  semaphore-bin-alt

ExclusiveArch: x86_64

%description
%summary

%prep
%setup

%install
install -D %SOURCE1 -T %buildroot%_bindir/%name

%files
%_bindir/%name
%doc README.ALT
%doc *.md

%changelog
* Thu May 10 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
