%global import_path github.com/fluxcd/flux2/
%define version 2.3.0

Name: flux2
Version: 2.7.5
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: Apache-2.0

Url: https://github.com/fluxcd/flux2/
Source0: %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang > 1.25
BuildRequires: /proc

%description
Flux is a tool for keeping Kubernetes clusters in sync with sources of
configuration (like Git repositories and OCI artifacts), and automating updates
to  configuration when there is new code to deploy.

%prep
# Regenerate standart flux-controllers manifests:
# $ ./manifests/scripts/bundle.sh

export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
%setup
%golang_prepare
for file in ./cmd/flux/manifests/*.yaml
do
  sed -E -i 's|image: fluxcd/([a-z-]+):v?([^"]+)|image: registry.altlinux.org/%_priority_distbranch/flux-\1:\2|' "$file"
done

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
LDFLAGS="-w -X main.VERSION=%version" %golang_build ./cmd/flux

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/flux
%doc *.md
%doc docs/*

%changelog
* Fri Feb 20 2026 Aleksandr Gamzin <gamzin@altlinux.org> 2.7.5-alt1
- 2.7.5
- Add note about manifest regeneration
- Support for new source-watcher manifest.

* Wed Feb 18 2026 Aleksandr Gamzin <gamzin@altlinux.org> 2.3.0-alt2
- Update controller image names to new ALT registry layout.

* Thu Oct 31 2024 Alexey Kostarev <kaf@altlinux.org> 2.3.0-alt1
- Initial build.
