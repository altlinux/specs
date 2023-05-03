%global commit de40ad007797e0dcd8b7126f27bb87401d224240
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name:		tini
Version:	0.19.0
Release:	alt2
Summary:	A tiny but valid init for containers

Group:		Development/Other
License:	%mit
URL:		https://github.com/krallin/tini

Source0: %name-%version.tar
Patch: tini-0.19.0-alt-fortify-source.patch
ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-licenses rpm-build-golang
BuildRequires: cmake
BuildRequires: glibc-devel-static

Provides: docker-init = %version-%release
Obsoletes: docker-init <= 0.13.0

%description
Tini is the simplest init you could think of.

All Tini does is spawn a single child (Tini is meant to be run in a container),
and wait for it to exit all the while reaping zombies and performing signal
forwarding.

%prep
%setup -q
%autopatch -p1

%build
cmake .
make tini-static

%install
mkdir -p -- %buildroot%_bindir
cp -a -- tini-static    %buildroot%_bindir/tini

%files

%_bindir/tini

%changelog
* Wed May 3 2023 Vladimir Didenko <cow@altlinux.org> 0.19.0-alt2
- Fix build with FORTIFY_SOURCE=3

* Fri May 29 2020 Vladimir Didenko <cow@altlinux.org> 0.19.0-alt1
- New version

* Mon May 14 2018 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt2
- define ExclusiveArch as %%go_arches

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.org> 0.18.0-alt1
- New version

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.org> 0.17.0-alt1
- New version

* Wed Feb 7 2018 Vladimir Didenko <cow@altlinux.org> 0.16.1-alt1
- Rename from docker-init to tini
- New version

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.org> 0.13.0-alt1.git949e6fac
- Initial build for ALTLinux.
