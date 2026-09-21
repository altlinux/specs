%global import_path github.com/kubeshark/kubeshark

Name: kubeshark
Version: 53.4.0
Release: alt1

Summary:  Network Observability for SREs & AI Agents
Group: Monitoring
License: Apache-2.0
URL: https://kubeshark.com/
VCS: https://github.com/kubeshark/kubeshark

Source0: %name-%version.tar
Source1: vendor.tar

Patch0: kubeshark-53.4.0-alt-disable-version-check.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
eBPF-powered network observability for Kubernetes. Indexes L4/L7
traffic with full K8s context, intercepts TLS traffic at the 
application layer. Queryable by AI agents via MCP and humans via
dashboard.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
export LDFLAGS="-X 'github.com/kubeshark/kubeshark/misc.Ver=%version-%release'"
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
%gotest ./...

%files
%_bindir/%name
%doc LICENSE README.md


%changelog
* Tue Sep 15 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 53.4.0-alt1
- Initial build for Sisyphus.
