%global provider        github.com
%global project         opencontainers
%global repo            runc

%global provider_prefix %{provider}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          b2567b37d7b75eb4cf325b77297b140ea686ce8f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:           docker-runc
Version:        1.0.0
Release:        alt2.git%shortcommit
Summary:        CLI for running Open Containers (Docker version)
Group:          Development/Other
License:        Apache 2.0
URL:            https://github.com/opencontainers/runc
ExclusiveArch:  x86_64

Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libseccomp-devel

Conflicts: docker-io <= 17.03.0

%description
Docker version of runc utility. The runc command can be used to start containers
which are packaged in accordance with the Open Container Initiative's
specifications, and to manage containers running under runc.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"

%golang_prepare
# TODO: Looks ugly. Definetly should be fixed.
rm -fr "$BUILDDIR/src/$IMPORT_PATH/vendor"
cp -alv -- vendor/* "$BUILDDIR/src"
make

%install
mkdir -p -- %buildroot/%_bindir
install -p -m 755 runc %buildroot/%_bindir/%name

%files
%doc MAINTAINERS_GUIDE.md PRINCIPLES.md README.md CONTRIBUTING.md
%_bindir/*

%changelog
* Fri Dec 29 2017 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt2.gitb2567b3
- new version for docker-ce 17.12.0

* Fri Nov 24 2017 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1.git0351df1
- Switch to new upstream (opencontainers/runc)
- new version for docker-ce 17.11.0

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1.git9c2d8d1
- Initial build for Alt Linux.
