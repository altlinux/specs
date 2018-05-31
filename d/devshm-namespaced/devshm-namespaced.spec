Name: devshm-namespaced
Version: 1.0
Release: alt1

Summary: PAM namespace config
License: GPLv3
Group: System/Configuration/Other

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=devshm-namespaced.git
Source: %name-%version.tar

BuildArch: noarch

%description
This PAM namespace config makes access to /dev/shm/ possible
with enabled mandatory access control.

%prep
%setup

%build

%install
mkdir -p %buildroot/etc/security/namespace.d/
cp namespace.conf %buildroot/etc/security/namespace.d/

%files
/etc/security/namespace.d/namespace.conf

%changelog
* Thu May 31 2018 Alexey Appolonov <alexey@altlinux.org> 1.0-alt1
- Initial release.
