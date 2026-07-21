%global _unpackaged_files_terminate_build 1
%global import_path github.com/binwiederhier/ntfy
%global commit_hash d9295e7
%def_with check
%def_with docs

# Convert --with/--without check into a value usable in compound conditions.
%if_with check
%global check_enabled 1
%else
%global check_enabled 0
%endif

# Convert --with/--without docs into a value usable in compound conditions.
%if_with docs
%global docs_enabled 1
%else
%global docs_enabled 0
%endif

# Native Node.js dependencies are unavailable on these architectures; build
# the server with embedded static-file stubs instead.
%ifarch %ix86 aarch64
%global build_web 0
%else
%global build_web 1
%endif

Name: ntfy
Version: 2.26.0
Release: alt1
Summary: Send push notifications to your phone or desktop using PUT/POST
License: Apache-2.0 and GPL-2.0
Group: System/Servers
URL: https://ntfy.sh
VCS: https://github.com/binwiederhier/ntfy

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: %name.service
Source4: %name.sysusers

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%if %build_web
BuildRequires: npm
%endif

%if %build_web && %docs_enabled
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-material
BuildRequires: python3-module-mkdocs-minify-plugin
%endif

%if %build_web && %check_enabled
BuildRequires: curl
%endif

%description
ntfy (pronounced "notify") is a simple HTTP-based pub-sub notification
service. With ntfy, you can send notifications to your phone or desktop
via scripts from any computer, without having to sign up or pay any fees.
If you'd like to run your own instance of the service, you can easily
do so since ntfy is open source.

%prep
%if %build_web
%setup -a1 -a2
%else
%setup -a1
%endif

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export CGO_ENABLED=1

%if %build_web
make web-build
%endif

%if %build_web && %docs_enabled
python3 -m mkdocs build
%endif
%if !%build_web || !%docs_enabled
mkdir -p server/docs
touch server/docs/index.html
%endif

%if !%build_web
mkdir -p server/site
touch server/site/app.html server/site/sw.js
%endif

%golang_prepare
cd .gopath/src/%import_path

go build -o=%name \
    -ldflags "-X main.version=%version \
        -X main.commit=%commit_hash \
        -X main.date=$(date -u +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
    .

%install
install -Dm 0755 .gopath/src/%import_path/%name %buildroot%_bindir/%name

install -Dm 0644 server/server.yml %buildroot%_sysconfdir/%name/server.yml
install -Dm 0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -Dm 0644 %SOURCE4 %buildroot%_sysusersdir/%name.conf
install -d -m 0750 \
    %buildroot%_var/lib/%name \
    %buildroot%_cachedir/%name

%check
%if %build_web && %check_enabled
export GOFLAGS=-mod=vendor
export CGO_ENABLED=1
cd .gopath/src/%import_path
go test -skip '^TestManager_AddUser_Timing$' \
    $(go list -f '{{if .TestGoFiles}}{{.ImportPath}}{{end}}' ./... | \
        grep -vE 'ntfy/v2/(test|examples|tools)')
npm --prefix web run test
%endif

%pre
%sysusers_create_package %name %SOURCE4

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name

%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/server.yml
%dir %attr(0750, _%name, _%name) %_sharedstatedir/%name
%dir %attr(0750, _%name, _%name) %_cachedir/%name

%changelog
* Mon Jul 20 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.26.0-alt1
- Initial build for ALT.
