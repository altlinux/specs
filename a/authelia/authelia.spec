%global _unpackaged_files_terminate_build 1
%global import_path github.com/authelia/authelia
%global commit_hash 1b524f7

Name: authelia
Version: 4.39.20
Release: alt1
Summary: The Single Sign-On Multi-Factor portal for web apps
License: Apache-2.0
Group: System/Servers
URL: https://www.authelia.com
VCS: https://github.com/authelia/authelia

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: npm

%description
Authelia is an open-source authentication and authorization server
providing two-factor authentication and single sign-on (SSO) for
your applications via a web portal. It acts as a companion for
reverse proxies by allowing, denying, or redirecting requests.
Documentation is available at https://www.authelia.com.

%prep
%setup -a1 -a2
# allow user namespace creation in containers
sed -i '/PrivateUsers=yes/d' authelia.service

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export CGO_ENABLED=1
export CGO_LDFLAGS="-Wl,-z,relro,-z,now"

npm --prefix web run build

%golang_prepare
cp -r api .gopath/src/%import_path/internal/server/public_html
cd .gopath/src/%import_path
go build -ldflags "-linkmode=external \
    -X %import_path/v4/internal/utils.BuildTag=%version \
    -X '%import_path/v4/internal/utils.BuildState=tagged clean' \
    -X %import_path/v4/internal/utils.BuildCommit=%commit_hash \
    -X %import_path/v4/internal/utils.BuildExtra=%release \
    -X %import_path/v4/internal/utils.BuildDate=$(date +'%%d-%%m-%%Y')" \
    -buildmode=pie -o authelia ./cmd/authelia
./authelia completion bash > authelia.bash
./authelia completion zsh > _authelia
./authelia completion fish > authelia.fish

%install
mkdir -p %buildroot%_bindir \
    %buildroot%_unitdir \
    %buildroot%_sysconfdir/authelia \
    %buildroot%_sharedstatedir/authelia \
    %buildroot%_datadir/bash-completion/completions \
    %buildroot%_datadir/zsh/site-functions \
    %buildroot%_datadir/fish/vendor_completions.d
install -m 0755 .gopath/src/%import_path/authelia %buildroot%_bindir
install -m 0644 authelia.service %buildroot%_unitdir
install -m 0644 .gopath/src/%import_path/authelia.bash %buildroot%_datadir/bash-completion/completions
install -m 0644 .gopath/src/%import_path/authelia.fish %buildroot%_datadir/fish/vendor_completions.d
install -m 0644 .gopath/src/%import_path/_authelia %buildroot%_datadir/zsh/site-functions
touch %buildroot%_sysconfdir/authelia/{configuration,users_database}.yml

%pre
%_sbindir/groupadd -r -f authelia
%_sbindir/useradd -r -g authelia -s /sbin/nologin \
    -d %_sharedstatedir/authelia authelia 2>/dev/null ||:

%post
%post_service authelia

%preun
%preun_service authelia

%files
%_bindir/authelia
%_unitdir/authelia.service
%_datadir/bash-completion/completions/authelia.bash
%_datadir/zsh/site-functions/_authelia
%_datadir/fish/vendor_completions.d/authelia.fish
%dir %_sysconfdir/authelia
%dir %attr(0750, authelia, authelia) %_sharedstatedir/authelia
%ghost %config(noreplace) %_sysconfdir/authelia/configuration.yml
%ghost %config(noreplace) %_sysconfdir/authelia/users_database.yml
%doc examples/compose/lite/authelia/configuration.yml
%doc examples/compose/lite/authelia/users_database.yml
%doc LICENSE

%changelog
* Sun Aug 30 2026 Alexander Makeenkov <amakeenk@altlinux.org> 4.39.20-alt1
- Updated to version 4.39.20.

* Mon Dec 15 2025 Vladislav Eliseev <general@altlinux.org> 4.39.15-alt1
- Updated to version 4.39.15.

* Sun Nov 09 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.39.14-alt1
- Updated to version 4.39.14.

* Sat Oct 11 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.39.12-alt1
- Updated to version 4.39.12.

* Sat Sep 27 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.39.10-alt1
- Initial build for ALT.
