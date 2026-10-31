%define _unpackaged_files_terminate_build 1
%define kflavour yogabook

Name: apt-repo-yogabook-kernel
Version: 0.0.1
Release: alt1

Summary: %kflavour kernel migration package

License: MIT
Group: System/Configuration/Other
Url: https://alt-lakostis.gitlab.io/kernel-image-%kflavour
Vcs: https://github.com/jekhor/yogabook-linux

Source0: kernel-%kflavour.list

# tablet is x86_64 only
ExclusiveArch: x86_64
Requires: update-kernel apt-https ca-certificates

%description
This is an apt repo configuration to ease switch to %kflavour kernel for
Lenovo Yoga Book tablets (YB1-X91L/F, YB1-X90L/F).

WARNING! %kflavour kernel is not supported by ALTLinux/Basealt, use this kernel
at own risk!

%prep

%build

%install
install -pDm644 %SOURCE0 %buildroot%_sysconfdir/apt/sources.list.d/kernel-%kflavour.list

%post
printf '%s\n' "Please manually run 'update-kernel -f -t %kflavour' to activate kernel"

%postun
if [ -f /boot/initrd-%kflavour.img ]; then
    printf '%s\n' "%kflavour kernel found, please run 'remove-old-kernels -f -t %kflavour' to remove it"
fi

%files
%_sysconfdir/apt/sources.list.d/kernel-%kflavour.list

%changelog
* Thu Oct 29 2026 L.A. Kostis <lakostis@altlinux.ru> 0.0.1-alt1
- Initial build for ALTLinux.

