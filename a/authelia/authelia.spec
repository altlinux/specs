%global _unpackaged_files_terminate_build 1
%global import_path github.com/authelia/authelia
# git rev-parse --short v%version
%global commit_hash 80828e60a

Name: authelia
Version: 4.39.14
Release: alt1
Summary: The Single Sign-On Multi-Factor portal for web apps
License: Apache-2.0
Group: System/Servers
Url: https://www.authelia.com
VCS: https://github.com/authelia/authelia

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar

# native rollup js bundler is needed to build
ExclusiveArch: x86_64

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
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules." --no-verify
# npm --prefix web install
# git add web/node_modules -f && git commit -m "Updated node modules." --no-verify
%setup -a 1 -a 2
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
    -X %import_path/v4/internal/utils.BuildDate=$(date +'%d-%m-%Y')" \
    -buildmode=pie -o authelia ./cmd/authelia
./authelia completion bash > authelia.bash
./authelia completion zsh > authelia.fish
./authelia completion fish > _authelia

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
* Sun Nov 09 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.39.14-alt1
- Updated to version 4.39.14.

* Sat Oct 11 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.39.12-alt1
- Updated to version 4.39.12.

* Sat Sep 27 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.39.10-alt1
- Initial build for ALT.
