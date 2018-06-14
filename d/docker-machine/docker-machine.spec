%global import_path github.com/docker/machine
%global commit b48dc28d9139c93d166f07d8b3a049b59bceef9c

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: docker-machine
Version: 0.15.0
Release: alt1%ubt
Summary: Docker Machine is a tool that lets you install Docker Engine on virtual hosts

Group: Development/Other
License: ASL 2.0
Url: https://%import_path
ExclusiveArch: %go_arches
Source: %name-%version.tar
BuildRequires(pre): rpm-build-golang rpm-build-ubt

%description
Machine lets you create Docker hosts on your computer, on cloud providers, and
inside your own data center. It creates servers, installs Docker on them, then
configures the Docker client to talk to them.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./cmd/docker-machine

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install

# cleanup
rm -rf -- %buildroot/%_datadir

%files
%doc README.md
%_bindir/%name

%changelog
* Thu Jun 14 2018 Alexey Shabalin <shaba@altlinux.ru> 0.15.0-alt1%ubt
- First build for ALTLinux.

