%global import_path github.com/sourcegraph/zoekt
%global _unpackaged_files_terminate_build 1

Name:    zoekt
Version: 0.0.0
Release: alt1.gitf6ff44

Summary: Fast trigram based code search
License: Apache-2.0
Group:   Other
URL:     https://github.com/sourcegraph/zoekt
Vcs:     https://github.com/sourcegraph/zoekt

Source0: %name-%version.tar
Source1: config.json
Source2: config.json.example
Source3: %name-webserver.service
Source4: %name-indexserver.service
Source5: %name-dynamic-indexserver.service
Source6: %name-sourcegraph-indexserver.service

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.26
BuildRequires: git-core
BuildRequires: /proc

Requires: git-core

%description
Zoekt supports fast substring and regexp matching on source code,
with a rich query language that includes boolean operators (and, or, not).
It can search individual repositories, and search across many repositories
in a large codebase. Zoekt ranks search results using a combination of
code-related signals like whether the match is on a symbol.
Because of its general design based on trigram indexing and syntactic parsing,
it works well for a variety of programming languages.

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath -mod=vendor"
export LDFLAGS="-X github.com/sourcegraph/zoekt.Version=%version"

%golang_prepare
%golang_build cmd/%name
%golang_build cmd/%name-archive-index
%golang_build cmd/%name-dynamic-indexserver
%golang_build cmd/%name-git-clone
%golang_build cmd/%name-git-index
%golang_build cmd/%name-index
%golang_build cmd/%name-indexserver
%golang_build cmd/%name-local-sync
%golang_build cmd/%name-merge-index
%golang_build cmd/%name-mirror-bitbucket-server
%golang_build cmd/%name-mirror-gerrit
%golang_build cmd/%name-mirror-gitea
%golang_build cmd/%name-mirror-github
%golang_build cmd/%name-mirror-gitiles
%golang_build cmd/%name-mirror-gitlab
%golang_build cmd/%name-repo-index
%golang_build cmd/%name-sourcegraph-indexserver
%golang_build cmd/%name-test
%golang_build cmd/%name-webserver

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install

mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name

install -Dm 0644 %{SOURCE1} -t %buildroot%_sysconfdir/%name
install -Dm 0644 %{SOURCE2} -t %buildroot%_sysconfdir/%name
touch %buildroot%_sysconfdir/%name/token.txt
install -Dm 0644 %{SOURCE3} %buildroot%_unitdir/%name-webserver.service
install -Dm 0644 %{SOURCE4} %buildroot%_unitdir/%name-indexserver.service
install -Dm 0644 %{SOURCE5} %buildroot%_unitdir/%name-dynamic-indexserver.service
install -Dm 0644 %{SOURCE6} %buildroot%_unitdir/%name-sourcegraph-indexserver.service

rm -rf -- %buildroot%_datadir

%pre
groupadd -r -f _%name 2>/dev/null ||:
useradd -r -g _%name -c 'Zoekt daemon' \
        -s /dev/null  -d %_localstatedir/%name _%name 2>/dev/null ||:

%post
%post_systemd %name-webserver.service
%post_systemd %name-indexserver.service
%post_systemd %name-dynamic-indexserver.service
%post_systemd %name-sourcegraph-indexserver.service

%preun
%preun_systemd %name-webserver.service
%preun_systemd %name-indexserver.service
%preun_systemd %name-dynamic-indexserver.service
%preun_systemd %name-sourcegraph-indexserver.service

%check
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath -mod=vendor"

%ifarch %ix86
%gotest -skip \
	'^(TestMatchSize|TestGatherBranchesMany|TestSearchStats|TestNegativeMatchesOnlyShortcut)$' ./...
%else
%gotest ./...
%endif

%files
%doc *.md
%_bindir/%name
%_bindir/%name-archive-index
%_bindir/%name-dynamic-indexserver
%_bindir/%name-git-clone
%_bindir/%name-git-index
%_bindir/%name-index
%_bindir/%name-indexserver
%_bindir/%name-local-sync
%_bindir/%name-merge-index
%_bindir/%name-mirror-bitbucket-server
%_bindir/%name-mirror-gerrit
%_bindir/%name-mirror-gitea
%_bindir/%name-mirror-github
%_bindir/%name-mirror-gitiles
%_bindir/%name-mirror-gitlab
%_bindir/%name-repo-index
%_bindir/%name-sourcegraph-indexserver
%_bindir/%name-test
%_bindir/%name-webserver
%dir %attr(0770,root,_%name) %_logdir/%name
%dir %attr(0750,root,_%name) %_sysconfdir/%name
%dir %attr(0750,_%name,_%name) %_localstatedir/%name
%_unitdir/%name-webserver.service
%_unitdir/%name-indexserver.service
%_unitdir/%name-dynamic-indexserver.service
%_unitdir/%name-sourcegraph-indexserver.service
%config(noreplace) %attr(0640,root,_%name) %_sysconfdir/%name/config.json
%config(noreplace) %attr(0640,root,_%name) %_sysconfdir/%name/config.json.example
%config(noreplace) %attr(0640,root,_%name) %_sysconfdir/%name/token.txt

%changelog
* Fri Nov 13 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.0.0-alt1.gitf6ff44
- Initial build for Sisyphus.
