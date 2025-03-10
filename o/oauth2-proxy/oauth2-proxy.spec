%define _unpackaged_files_terminate_build 1
%global import_path github.com/oauth2-proxy/oauth2-proxy

Name: oauth2-proxy
Version: 7.8.1
Release: alt1

Group: Security/Networking
Summary: OAuth2 Proxy for authentication
License: MIT
Url: https://oauth2-proxy.github.io/oauth2-proxy
Vcs: https://github.com:oauth2-proxy/oauth2-proxy.git
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.22

%description
A reverse proxy and static file server that provides authentication using Providers (Google, 
Keycloak, GitHub and others) to validate accounts by email, domain or group.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"                   
export IMPORT_PATH="%import_path"               
export LDFLAGS="-X github.com/oauth2-proxy/oauth2-proxy/v7/pkg/version.VERSION=%version"
export GOPATH="$BUILDDIR:%go_path"              

%golang_prepare
%golang_build .
# %make release VERSION=%version

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1                         
%golang_install

%files
%doc *.md LICENSE
%_bindir/*

%changelog
* Thu Jan 20 2024 Artyom Sinyugin <writers@altlinux.org> 7.8.1-alt1
- Initial build.
