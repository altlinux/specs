%global commit 949e6facb77383876aeff8a6944dde66b3089574
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name:		docker-init
Version:	0.13.0
Release:	alt1.git%abbrev
Summary:	A tiny but valid init for containers

Group:		Development/Other
License:	%mit
URL:		https://github.com/krallin/tini

Source0: %name-%version.tar
ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-licenses
BuildRequires: cmake
BuildRequires: glibc-devel-static

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
cp -a -- tini-static    %buildroot/%_bindir/docker-init

%files

%_bindir/docker-init

%changelog
* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.org> 0.13.0-alt1.git949e6fac
- Initial build for ALTLinux.
