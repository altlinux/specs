
%global import_path github.com/kubernetes/kubernetes

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%define prog_name            kubernetes
%define kubernetes_major     1
%define kubernetes_minor     31
%define kubernetes_patch     1

Name: %prog_name%kubernetes_major.%kubernetes_minor
Version: %kubernetes_major.%kubernetes_minor.%kubernetes_patch
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: Apache-2.0
Url: https://kubernetes.io
Vcs: https://github.com/kubernetes/kubernetes
Source: %name-%version.tar


Source2: genmanpages.sh
Source3: kubernetes-accounting.conf
Source4: 10-kubeadm.conf

#systemd services
Source10: kube-apiserver.service
Source11: kube-controller-manager.service
Source12: kubelet.service
Source13: kube-proxy.service
Source14: kube-scheduler.service
#config files
Source20: apiserver
Source21: config
Source22: controller-manager
Source23: kubelet
Source24: proxy
Source25: scheduler
Source26: kubernetes.tmpfiles
Source27: crio.conf
Source28: 99-kubernetes-cri.conf

Patch1: runc-alt-loongarch64-support.patch
Patch2: kubernets-alt-loongarch64-support.patch
Patch3: ebpf-alt-loongarch64-support.patch

Provides: %prog_name = %EVR
Conflicts: %prog_name < %EVR
Conflicts: %prog_name > %EVR

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang > 1.21
BuildRequires: /proc
BuildRequires: rsync
BuildRequires: go-md2man go-bindata

%description
Kubernetes is an open source system for managing containerized applications
across multiple hosts; providing basic mechanisms
for deployment, maintenance, and scaling of applications.

%package common
Summary: Kubernetes common files
Group: System/Configuration/Other
BuildArch: noarch
Provides: %prog_name-common = %EVR
Conflicts: %prog_name-common < %EVR
Conflicts: %prog_name-common > %EVR

%description common
Kubernetes is an open source system for managing containerized applications
across multiple hosts; providing basic mechanisms
for deployment, maintenance, and scaling of applications.

This subpackage contains the Kubernetes common files.

%package unit-test
Summary: %summary - for running unit tests
Group: System/Configuration/Other
Provides: %prog_name-unit-test = %EVR
Conflicts: %prog_name-unit-test < %EVR
Conflicts: %prog_name-unit-test > %EVR

Requires: golang >= 1.20
Requires: etcd >= 2.0.9
Requires: hostname
Requires: rsync

%description unit-test
%summary - for running unit tests

%package master
Summary: Kubernetes services for master host
Group: System/Configuration/Other
Provides: %prog_name-master = %EVR
Conflicts: %prog_name-master < %EVR
Conflicts: %prog_name-master > %EVR

Requires: %prog_name-client = %EVR
# if node is installed with node, version and release must be the same
Conflicts: %prog_name-node < %EVR
Conflicts: %prog_name-node > %EVR

%description master
Kubernetes services for master host.

%package node
Summary: Kubernetes services for node host
Group: System/Configuration/Other
Provides: %prog_name-node = %EVR
Conflicts: %prog_name-node < %EVR
Conflicts: %prog_name-node > %EVR

Requires: conntrack-tools
Requires: ethtool
Requires: iptables
Requires: socat
Requires: %prog_name-client = %EVR
Requires: %prog_name-kubelet = %EVR
# if master is installed with node, version and release must be the same
Conflicts: %prog_name-master < %EVR
Conflicts: %prog_name-master > %EVR

%description node
Kubernetes services for node host.

%package kubelet
Summary: Kubernetes kubelet daemon
Group: System/Configuration/Other
Provides: %prog_name-kubelet = %EVR
Conflicts: %prog_name-kubelet < %EVR
Conflicts: %prog_name-kubelet > %EVR

Requires: %prog_name-common = %EVR
# if master is installed with node, version and release must be the same
Conflicts: %prog_name-master < %EVR
Conflicts: %prog_name-master > %EVR

%description kubelet
Kubernetes kubelet service.

%package  kubeadm
Summary:  Kubernetes tool for standing up clusters
Group: System/Configuration/Other
Provides: %prog_name-kubeadm = %EVR
Conflicts: %prog_name-kubeadm < %EVR
Conflicts: %prog_name-kubeadm > %EVR

Requires: %prog_name-node = %EVR
Requires: cni-plugins >= 0.7.5
Requires: ebtables
Requires: iptables
Requires: ethtool
Requires: socat

%description kubeadm
Kubernetes tool for standing up clusters.

%package client
Summary: Kubernetes client tools
Group: System/Configuration/Other
Provides: %prog_name-client = %EVR
Conflicts: %prog_name-client < %EVR
Conflicts: %prog_name-client > %EVR

Requires: %prog_name-common = %EVR

%description client
Kubernetes client tools like kubectl

%package crio
Summary: Kubernetes crio files
Group: System/Configuration/Other
BuildArch: noarch
Provides: %prog_name-crio = %EVR
Conflicts: %prog_name-crio < %EVR
Conflicts: %prog_name-crio > %EVR

Requires: cri-o%kubernetes_major.%kubernetes_minor

%description crio
Packege contains files specific for using crio.

%prep
%setup -q
%autopatch -p1

%build
export GOTOOLCHAIN=local
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export KUBE_GIT_COMMIT=%release
export KUBE_GIT_TREE_STATE="clean"
export KUBE_GIT_VERSION="v%version"

# Fixes https://github.com/golang/go/issues/58425
%ifarch %arm
export CGO_ENABLED=0
%endif

%golang_prepare
# .go-version is needed for successfull build
cp -alv -- .go-version "$BUILDDIR/src/$IMPORT_PATH"
pushd .gopath/src/%import_path
export KUBE_EXTRA_GOPATH=$(pwd)/Godeps/_workspace

GOMAXPROCS=10 make WHAT="${BINS[*]}"

# convert md to man
./hack/update-generated-docs.sh || true
pushd docs
pushd admin
cp kube-apiserver.md kube-controller-manager.md kube-proxy.md kube-scheduler.md kubelet.md ..
popd
cp %SOURCE2 genmanpages.sh
bash genmanpages.sh
popd
popd

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

cd .gopath/src/%import_path
%ifarch ppc64le aarch64 loongarch64
output_path="_output/local/go/bin"
%else
output_path="_output/local/bin/linux/%go_hostarch"
%endif

install -m 755 -d %buildroot%_bindir

echo "+++ INSTALLING kubeadm"
install -p -m 755 -t %buildroot%_bindir ${output_path}/kubeadm
install -d -m 755 %buildroot%_sysconfdir/systemd/system/kubelet.service.d
install -p -m 644 -t %buildroot/%_sysconfdir/systemd/system/kubelet.service.d %SOURCE4

echo "+++ INSTALLING kubelet and kubelet"
install -p -m 755 -t %buildroot%_bindir ${output_path}/kubelet

echo "+++ INSTALLING kubelet and kubectl"
install -p -m 755 -t %buildroot%_bindir ${output_path}/kubectl

echo "+++ INSTALLING kubelet and kube-apiserver"
install -p -m 755 -t %buildroot%_bindir ${output_path}/kube-apiserver

echo "+++ INSTALLING kubelet and kube-controller-manager"
install -p -m 755 -t %buildroot%_bindir ${output_path}/kube-controller-manager

echo "+++ INSTALLING kubelet and kube-scheduler"
install -p -m 755 -t %buildroot%_bindir ${output_path}/kube-scheduler

echo "+++ INSTALLING kubelet and kube-proxy"
install -p -m 755 -t %buildroot%_bindir ${output_path}/kube-proxy

# install the bash completion
install -d -m 0755 %buildroot%_datadir/bash-completion/completions/
%buildroot%_bindir/kubectl completion bash > %buildroot%_datadir/bash-completion/completions/kubectl
# install the zsh completion
install -d -m 0755 %buildroot%_datadir/zsh/site-functions/
%buildroot%_bindir/kubectl completion zsh > %buildroot/%_datadir/zsh/site-functions/_kubectl

# systemd service
install -d -m 0755 %buildroot%_unitdir
for src in %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 ; do
  install -m 0644 -t %buildroot%_unitdir/ "$src"
done

# install manpages
install -d %buildroot%_man1dir
install -p -m 644 docs/man/man1/* %buildroot%_man1dir

# install config files
install -d -m 0775 %buildroot%_sysconfdir/%prog_name
for src in %SOURCE20 %SOURCE21 %SOURCE22 %SOURCE23 %SOURCE24 %SOURCE25 ; do
  install -m 0644 -t %buildroot%_sysconfdir/%prog_name "$src"
done

# install home dir kube user
install -d -m 0775 %buildroot%_localstatedir/%prog_name
# manifests file for the kubelet
install -d -m 0775 %buildroot%_sysconfdir/%prog_name/manifests

# place kubernetes.tmpfiles to /lib/tmpfiles.d/kubernetes.conf
install -d -m 0755 %buildroot%_tmpfilesdir
install -D -m 0644 %SOURCE26 %buildroot%_tmpfilesdir/kubernetes.conf

# load needed module
install -D -m 0644 %SOURCE27 %buildroot%_modulesloaddir/crio.conf

# install sysctl settings
install -D -m 0644 %SOURCE28 %buildroot%_sysctldir/99-kubernetes-cri.conf

# install the place the kubelet defaults to put volumes
install -d %buildroot%_localstatedir/kubelet

# enable CPU and Memory accounting
install -d -m 0755 %buildroot/%_sysconfdir/systemd/system.conf.d
install -p -m 0644 -t %buildroot/%_sysconfdir/systemd/system.conf.d %SOURCE3

%pre common
groupadd -r -f kube > /dev/null 2>&1 ||:
useradd -r -g kube -M -d %_localstatedir/%prog_name -s /dev/null -c "Kubernetes user" kube > /dev/null 2>&1 ||:

%post master
%post_service kube-apiserver
%post_service kube-scheduler
%post_service kube-controller-manager

%preun master
%preun_service kube-apiserver
%preun_service kube-scheduler
%preun_service kube-controller-manager

%post kubelet
%post_service kubelet

%preun kubelet
%preun_service kubelet

%post node
%post_service kube-proxy

%preun node
%preun_service kube-proxy

%post crio
if [ -f /etc/net/sysctl.conf ]; then
    sed \
        -i.kubernetes-crio \
        -e 's/^net.ipv4.ip_forward = 0$/# net.ipv4.ip_forward = 0/' \
        /etc/net/sysctl.conf
fi

%files common
%attr(775,root,kube) %dir %_sysconfdir/%prog_name
%config(noreplace) %_sysconfdir/%prog_name/config
%_tmpfilesdir/%prog_name.conf
%attr(775,kube,kube) %dir %_localstatedir/%prog_name

%files master
%doc README.md LICENSE
%_man1dir/kube-apiserver.*
%_man1dir/kube-controller-manager.*
%_man1dir/kube-scheduler.*
%_bindir/kube-apiserver
%_bindir/kube-controller-manager
%_bindir/kube-scheduler
%_unitdir/kube-apiserver.service
%_unitdir/kube-controller-manager.service
%_unitdir/kube-scheduler.service
%config(noreplace) %_sysconfdir/%prog_name/apiserver
%config(noreplace) %_sysconfdir/%prog_name/scheduler
%config(noreplace) %_sysconfdir/%prog_name/controller-manager

%files node
%doc README.md LICENSE
%_man1dir/kube-proxy.*
%_bindir/kube-proxy
%_unitdir/kube-proxy.service
%config(noreplace) %_sysconfdir/%prog_name/proxy
%config(noreplace) %_sysconfdir/systemd/system.conf.d/kubernetes-accounting.conf

%files kubelet
%doc README.md LICENSE
%_man1dir/kubelet.*
%_bindir/kubelet
%_unitdir/kubelet.service
%dir %_localstatedir/kubelet
%config(noreplace) %_sysconfdir/%prog_name/kubelet
%attr(775,root,kube) %dir %_sysconfdir/%prog_name/manifests

%files kubeadm
%doc README.md LICENSE
%_man1dir/kubeadm*
%_bindir/kubeadm
%dir %_sysconfdir/systemd/system/kubelet.service.d
%config(noreplace) %_sysconfdir/systemd/system/kubelet.service.d/10-kubeadm.conf

%files client
%doc README.md LICENSE
%_man1dir/kubectl*
%_bindir/kubectl
%_datadir/bash-completion/completions/kubectl
%_datadir/zsh/site-functions/_kubectl

%files crio
%_modulesloaddir/crio.conf
%_sysctldir/99-kubernetes-cri.conf

%changelog
* Thu Sep 12 2024 Alexander Stepchenko <geochip@altlinux.org> 1.31.1-alt1
- 1.30.5 -> 1.31.1

* Thu Sep 12 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.5-alt1
- 1.30.4 -> 1.30.5

* Thu Aug 15 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.4-alt1
- 1.30.3 -> 1.30.4

* Fri Jul 19 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.3-alt1
- 1.30.2 -> 1.30.3 (Fixes: CVE-2024-5321)

* Wed Jul 10 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.2-alt1
- 1.30.1 -> 1.30.2

* Fri May 24 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.1-alt1
- 1.29.5 -> 1.30.1

* Thu May 23 2024 Alexander Stepchenko <geochip@altlinux.org> 1.29.5-alt1
- 1.28.10 -> 1.29.5

* Thu May 23 2024 Alexander Stepchenko <geochip@altlinux.org> 1.28.10-alt1
- 1.28.8 -> 1.28.10 (Fixes: CVE-2024-3177, CVE-2023-45288)

* Tue Mar 19 2024 Alexey Shabalin <shaba@altlinux.org> 1.28.8-alt1
- 1.28.8

* Wed Mar 06 2024 Ivan A. Melnikov <iv@altlinux.org> 1.28.7-alt1.1
- NMU: loongarch64 support

* Tue Mar 05 2024 Alexey Shabalin <shaba@altlinux.org> 1.28.7-alt1
- 1.28.7

* Tue Mar 05 2024 Alexey Shabalin <shaba@altlinux.org> 1.27.11-alt1
- 1.27.11

* Fri Nov 03 2023 Alexey Shabalin <shaba@altlinux.org> 1.27.7-alt1
- 1.27.7

* Wed Nov 01 2023 Alexey Shabalin <shaba@altlinux.org> 1.26.10-alt1
- 1.26.10.
- Rename the package to include major and minor versions.

* Wed Oct 04 2023 Alexander Stepchenko <geochip@altlinux.org> 1.26.9-alt1
- 1.26.6 -> 1.26.9 (Fixes: CVE-2023-3955, CVE-2023-3676)
- Make kubernetes-common and kubernetes-crio noarch packages

* Wed Jul 12 2023 Alexander Stepchenko <geochip@altlinux.org> 1.26.6-alt1
- 1.26.3. -> 1.26.6 (Fixes: CVE-2023-2727, CVE-2023-2728).
- Closes ALT#46869.
- Fix build on %%arm architectures.
- Add CVE fixes information.

* Thu Apr 27 2023 Alexey Shabalin <shaba@altlinux.org> 1.26.3-alt2
- Allow write to config dir /etc/kubernetes for kube group
- Allow write to home dir /var/lib/kubernetes for kube group

* Fri Mar 24 2023 Alexander Stepchenko <geochip@altlinux.org> 1.26.3-alt1
- 1.26.3 (Fixes: CVE-2022-3172, CVE-2022-3162, CVE-2022-3294, CVE-2021-25743)

* Fri Mar 17 2023 Alexander Stepchenko <geochip@altlinux.org> 1.24.11-alt1
- 1.24.11

* Mon Nov 21 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.24.8-alt1
- 1.24.8

* Tue Mar 22 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.8-alt1
- 1.22.8

* Sun Feb 20 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.7-alt1
- 1.22.7

* Thu Jan 20 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.6-alt1
- 1.22.6

* Fri Dec 24 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.5-alt2
- Comment etcnet hardcoded net.ipv4.ip_forward default
- Add zsh completion

* Tue Dec 21 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.5-alt1
- 1.22.5
- Use crio cri by default in kubeadm.conf

* Fri Dec 10 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.4-alt2
- Add cve fixes information
- Add cri-o requires to kubernetes-crio

* Thu Dec 02 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.4-alt1
- 1.22.4
- Fixes: CVE-2021-25741

* Wed Jun 30 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.20.8-alt1
- 1.20.8
- Fixes: CVE-2021-25737

* Thu Jan 21 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.20.2-alt1
- 1.20.2
- crio support

* Fri Sep 11 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.18.8-alt1
- 1.18.8

* Fri Jul 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.18.6-alt1
- 1.18.6
- Fixes: CVE-2020-8559

* Thu Jul 02 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.18.5-alt1
- 1.18.5
- Fixes: CVE-2020-8558

* Thu Apr 02 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.18.0-alt1
- 1.18.0

* Tue Dec 31 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.17.0-alt1
- 1.17.0

* Fri Dec 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.16.4-alt1
- 1.16.4

* Fri Oct 11 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.15.4-alt2
- Partly revert b378c886 because some deprecated optons steel needed

* Thu Sep 26 2019 Alexey Shabalin <shaba@altlinux.org> 1.15.4-alt1
- 1.15.4

* Thu Sep 26 2019 Alexey Shabalin <shaba@altlinux.org> 1.15.3-alt1
- 1.15.3 (Fixes: CVE-2019-9512, CVE-2019-9514)

* Tue Sep 24 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.15.2-alt2
- Remove deprecated and removed flags from kubeadm.conf

* Tue Aug 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.15.2-alt1
- 1.15.2

* Wed Apr 24 2019 Alexey Shabalin <shaba@altlinux.org> 1.14.1-alt1
- 1.14.1

* Wed Mar 27 2019 Alexey Shabalin <shaba@altlinux.org> 1.14.0-alt1
- 1.14.0

* Sun Mar 24 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.4-alt1
- 1.13.4

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.3-alt1
- 1.13.3

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.2-alt1
- 1.13.2

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.13.0-alt1
- 1.13.0

* Mon Oct 01 2018 Alexey Shabalin <shaba@altlinux.org> 1.12.0-alt1
- 1.12.0

* Fri Aug 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.2-alt1
- 1.11.2

* Fri Jul 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Wed Jun 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1.10.4-alt1
- 1.10.4

* Mon May 14 2018 Alexey Shabalin <shaba@altlinux.ru> 1.10.2-alt1
- Initial build for ALT
