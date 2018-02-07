%global commit 0effd37412ba5ae7e00af0db1f36f5dbc1671df9
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name:		tini
Version:	0.16.1
Release:	alt1
Summary:	A tiny but valid init for containers

Group:		Development/Other
License:	%mit
URL:		https://github.com/krallin/tini

Source0: %name-%version.tar
ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-licenses
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

%build
cmake .
make tini-static

%install
mkdir -p -- %buildroot/%_bindir
cp -a -- tini-static    %buildroot/%_bindir/tini

%files

%_bindir/tini

%changelog
* Wed Feb 7 2018 Vladimir Didenko <cow@altlinux.org> 0.16.1-alt1
- Rename from docker-init to tini
- New version

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.org> 0.13.0-alt1.git949e6fac
- Initial build for ALTLinux.
