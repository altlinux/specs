Name:     kubernetes-pause
Version:  3.9
Release:  alt1

Summary:  This executable can be used as a minimal init process inside a container
License:  Apache-2.0
Group:    Other
Url:      https://raw.githubusercontent.com/kubernetes/kubernetes/v1.26.3/build/pause/linux/pause.c

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
* Thu Mar 30 2023 Stepan Paksashvili <paksa@altlinux.org> 3.9-alt1
- 3.9

* Mon Dec 12 2022 Mikhail Gordeev <obirvalger@altlinux.org> 3.7-alt1
- Just update version to the appropriate for kubernetes 1.24.8

* Wed Nov 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 3.5-alt1
Initial build for Sisyphus
