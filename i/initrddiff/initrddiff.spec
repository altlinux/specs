Name: initrddiff
Version: 0.01
Release: alt2

Summary: Print diff between two initrd images
License: GPLv3+
Group: System/Configuration/Boot and Init
URL: http://git.altlinux.org/people/evg/packages/initrddiff.git

BuildArch: noarch

Packager: Evgenii Terechkov <evg@altlinux.org>

Source0: %name-%version.tar

%description
Print diff between two initrd images
%prep
%setup

%install
mkdir -p %buildroot/sbin
install -p -m755 %name %buildroot/sbin/

%files
/sbin/%name

%changelog
* Sun Mar  4 2012 Terechkov Evgenii <evg@altlinux.org> 0.01-alt2
- Major rewrite from legion@

* Sat Mar  3 2012 Terechkov Evgenii <evg@altlinux.org> 0.01-alt1
- Initial build for ALT Linux Sisyphus
