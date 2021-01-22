%define _unpackaged_files_terminate_build 1

%global provider        github
%global provider_tld    com
%global project         docker
%global repo            cli

%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit      2291f610ae73533e6e0749d4ef1e360149b1e46b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       docker-cli
Version:    20.10.2
Release: alt1
Summary: Docker CLI
License: Apache-2.0
Group: System/Configuration/Other

Url: https://github.com/docker/cli
ExclusiveArch: %go_arches
Conflicts: docker

Source0: %name-%version.tar
Patch1: docker-cli-20.10.2-alt-fix-man-page-gen.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.3 libseccomp-devel
BuildRequires: go-md2man
Conflicts: docker-ce < 20.10.0-alt1.rc2

# do not extract debuginfo
%define __find_debuginfo_files %nil

# do not run debugedit for them
%add_debuginfo_skiplist /usr/bin/docker

%description
CLI for Docker Engine

%prep
%setup
%patch1 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"

%golang_prepare
rm -fr "$BUILDDIR/src/$IMPORT_PATH/vendor"
cp -alv -- vendor/* "$BUILDDIR/src"

DISABLE_WARN_OUTSIDE_CONTAINER=1 make VERSION=%{version} GITCOMMIT=%{shortcommit}
DISABLE_WARN_OUTSIDE_CONTAINER=1 make manpages

%install
# install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 build/docker %{buildroot}%{_bindir}/docker

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/man1/*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5
install -p -m 644 man/man5/*.5 %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man8
install -p -m 644 man/man8/*.8 %{buildroot}%{_mandir}/man8

# install bash completion
install -Dp -m 644 contrib/completion/bash/docker %{buildroot}%{_datadir}/bash-completion/completions/docker

# install zsh completion
install -Dp -m 644 contrib/completion/zsh/_docker %{buildroot}%{_datadir}/zsh/site-functions/_docker

# install fish completion
install -Dp -m 644 contrib/completion/fish/docker.fish %{buildroot}%{_datadir}/fish/completions/docker.fish

%files
%doc AUTHORS LICENSE
%doc MAINTAINERS NOTICE
%doc CONTRIBUTING.md README.md
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_bindir}/docker
%{_datadir}/bash-completion/completions/docker
%{_datadir}/zsh/site-functions/_docker
%{_datadir}/fish/completions/docker.fish

%changelog
* Fri Jan 22 2021 Vladimir Didenko <cow@altlinux.org> 20.10.2-alt1
- new release

* Wed Dec 9 2020 Vladimir Didenko <cow@altlinux.org> 20.10.0-alt2
- 20.10.0 release

* Fri Dec 4 2020 Vladimir Didenko <cow@altlinux.org> 20.10.0-alt1.rc2
- Initial build for Sisyphus
