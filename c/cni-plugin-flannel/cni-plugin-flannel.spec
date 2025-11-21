%global _unpackaged_files_terminate_build 1
%global import_path github.com/flannel-io/cni-plugin

%define git_commit e38aaba71b9d0c4ae810585bae578e00c735dba0
%define git_commit_short %(c="%git_commit"; echo "${c:0:8}")

Name: cni-plugin-flannel
Epoch: 1
Version: 1.8.0.2
Release: alt1

Summary: A CNI network plugin that is powered by flannel
License: Apache-2.0
Group: Other
Url: https://github.com/flannel-io/cni-plugin

Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24.3

%description
This plugin is designed to work in conjunction with flannel, a network fabric
for containers. When flannel daemon is started, it outputs
a /run/flannel/subnet.env file that looks like this:

FLANNEL_NETWORK=10.1.0.0/16
FLANNEL_SUBNET=10.1.17.1/24
FLANNEL_MTU=1472
FLANNEL_IPMASQ=true

This information reflects the attributes of flannel network on the host.
The flannel CNI plugin uses this information to configure another CNI plugin,
such as bridge plugin.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

# 1.8.0.2 -> v1.8.0
version='%(v="%version"; echo "v${v%.*}")'
export LDFLAGS="-X main.Version=$version -X main.Commit=%git_commit_short -X main.Program=flannel"
export TAGS="netgo osusergo no_stage"
export CGO_ENABLED=1

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -pD -m 755 %buildroot%_bindir/cni-plugin %buildroot%prefix/libexec/cni/flannel
rm %buildroot%_bindir/cni-plugin

%files
%prefix/libexec/cni/flannel
%doc README.md RELEASING.md LICENSE

%changelog
* Thu Oct 30 2025 Alexander Stepchenko <geochip@altlinux.org> 1:1.8.0.2-alt1
- 1.7.1.2 -> 1.8.0.2.

* Tue Sep 09 2025 Alexander Stepchenko <geochip@altlinux.org> 1:1.7.1.2-alt1
- Update to 1.7.1.2.

* Fri May 16 2025 Nadezhda Fedorova <fedor@altlinux.org> 1:1.7.1.1-alt1
- 1.5.1.3 -> 1.7.1.1

* Thu Sep 26 2024 Alexander Stepchenko <geochip@altlinux.org> 1:1.5.1.3-alt1
- 1.5.1 -> 1.5.1.3

* Wed Jul 24 2024 Alexey Shabalin <shaba@altlinux.org> 1:1.5.1-alt1
- 1.5.1

* Fri May 17 2024 Alexander Stepchenko <geochip@altlinux.org> 1:1.4.0-alt1
- 1.2.0 -> 1.4.0

* Mon Oct 16 2023 Alexander Stepchenko <geochip@altlinux.org> 1:1.2.0-alt1
- 1.1.2 -> 1.2.0

* Thu Apr 06 2023 Alexander Stepchenko <geochip@altlinux.org> 1:1.1.2-alt1
- Fix the wrong version.

* Mon Dec 05 2022 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- Build to Sisyphus.

* Mon Dec 05 2022 Alexander Stepchenko <geochip@altlinux.org> 1.2.0-alt0.1
- Initial build for ALT.
