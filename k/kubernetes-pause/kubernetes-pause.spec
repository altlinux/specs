Name:     kubernetes-pause
Version:  3.7
Release:  alt1

Summary:  This executable can be used as a minimal init process inside a container
License:  Apache-2.0
Group:    Other
Url:      https://raw.githubusercontent.com/kubernetes/kubernetes/v1.22.8/build/pause/linux/pause.c

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires: glibc-devel-static

%description
%summary.

%prep
%setup

%build
gcc %optflags -static -DVERSION=%version pause.c -o pause

%install
install -m0755 -D pause %buildroot/%_bindir/kubernetes-pause

%files
%_bindir/*

%changelog
* Mon Dec 12 2022 Mikhail Gordeev <obirvalger@altlinux.org> 3.7-alt1
- Just update version to the appropriate for kubernetes 1.24.8

* Wed Nov 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 3.5-alt1
Initial build for Sisyphus
