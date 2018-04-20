
%define _libexecdir /usr/libexec

# do not extract debuginfo
%define __find_debuginfo_files %nil

%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir %_libexecdir/origin
%brp_strip_none %_bindir/* %_libexecdir/origin/*

%global gopath      %_datadir/gocode
%global import_path github.com/openshift/origin
%global commit 191fece9305a76f262baacc9de72c2c8cb4d5601
%global kube_commit cbc5b493627e993e4e4f02301702c16ae28ea88f
%global etcd_commit 121edf0467052d55876a817b89875fb39a99bf78
%global registry_commit fef8b8b5ff6c348ff3efdd518398314234587d8e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global kube_shortcommit %(c=%{kube_commit}; echo ${c:0:7})
%global etcd_shortcommit %(c=%{etcd_commit}; echo ${c:0:7})
%global registry_shortcommit %(c=%{registry_commit}; echo ${c:0:7})


%global os_git_vars OS_GIT_VERSION=v3.9.0 OS_GIT_MINOR=9+ OS_GIT_COMMIT=%{shortcommit} OS_GIT_MAJOR=3 OS_GIT_TREE_STATE=clean KUBE_GIT_VERSION=v1.9.1+%{kube_shortcommit} KUBE_GIT_COMMIT=%{kube_shortcommit} ETCD_GIT_COMMIT=%{etcd_shortcommit} ETCD_GIT_VERSION=v3.2.16 OS_GIT_CATALOG_VERSION=v0.1.9

# docker_version is the version of docker requires by packages
%global docker_version 1.12
# openvswitch_version is the version of openvswitch requires by packages
%global openvswitch_version 2.6.1
%global golang_version 1.9.1
%global product_name Origin

Name: origin
Version: 3.9.0
Release: alt1%ubt
Summary: Open Source Container Management
License: ASL 2.0
Group: System/Configuration/Other
Url: https://%import_path
Source: %name-%version.tar

#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-golang rpm-build-ubt
BuildRequires: systemd
BuildRequires: bsdtar
BuildRequires: golang >= %golang_version
BuildRequires: libkrb5-devel
BuildRequires: rsync
BuildRequires: /proc
Requires: %name-clients = %version-%release
Requires: iptables

%description
OpenShift Origin is a distribution of Kubernetes optimized for continuous
application development and multi-tenant deployment.
OpenShift adds developer and operations-centric tools on top of Kubernetes
to enable rapid application development, easy deployment and scaling,
and long-term lifecycle maintenance for small and large teams.

%package master
Summary: %product_name Master
Requires: %name = %version-%release
Group: System/Configuration/Other

%description master
%summary

%package tests
Summary: %product_name Test Suite
Group: System/Configuration/Other

%description tests
%summary

%package node
Summary: %product_name Node
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: docker-ce >= %docker_version
Requires: util-linux
Requires: socat
Requires: nfs-utils
Requires: cifs-utils
Requires: ethtool
Requires: thin-provisioning-tools >= 0.6.2
Requires: conntrack-tools

%description node
%summary

%package clients
Summary: %product_name Client binaries for Linux
Group: System/Configuration/Other
Requires: git-core
Requires: bash-completion

%description clients
%summary

%package pod
Summary: %product_name Pod
Group: System/Configuration/Other

%description pod
%summary

%package sdn-ovs
Summary: %product_name SDN Plugin for Open vSwitch
Group: System/Configuration/Other
Requires: openvswitch >= %openvswitch_version
Requires: %name-node = %version-%release
Requires: bridge-utils
Requires: bind-utils
Requires: ethtool
Requires: procps
Requires: iproute

%description sdn-ovs
%summary

%package federation-services
Summary: %product_name Federation Services
Group: System/Configuration/Other

%description federation-services
%summary

%package service-catalog
Summary: %product_name Service Catalog
Group: System/Configuration/Other

%description service-catalog
%summary

%package template-service-broker
Summary: Template Service Broker
Group: System/Configuration/Other

%description template-service-broker
%summary

%package cluster-capacity
Summary: %product_name Cluster Capacity Analysis Tool
Group: System/Configuration/Other

%description cluster-capacity
%summary

%prep
%setup

%build
# Create Binaries only for building arch
%ifarch x86_64
  BUILD_PLATFORM="linux/amd64"
%endif
%ifarch %ix86
  BUILD_PLATFORM="linux/386"
%endif
%ifarch ppc64le
  BUILD_PLATFORM="linux/ppc64le"
%endif
%ifarch aarch64
  BUILD_PLATFORM="linux/arm64"
%endif
%ifarch %arm
  BUILD_PLATFORM="linux/arm"
%endif
%ifarch s390x
  BUILD_PLATFORM="linux/s390x"
%endif
GOMAXPROCS=10 OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %os_git_vars OS_BUILD_RELEASE_ARCHIVES=n make build-cross
GOMAXPROCS=10 OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %os_git_vars hack/build-go.sh vendor/github.com/onsi/ginkgo/ginkgo
GOMAXPROCS=10 OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %os_git_vars unset GOPATH; cmd/service-catalog/go/src/github.com/kubernetes-incubator/service-catalog/hack/build-cross.sh
GOMAXPROCS=10 OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %os_git_vars unset GOPATH; cmd/cluster-capacity/go/src/github.com/kubernetes-incubator/cluster-capacity/hack/build-cross.sh

# Generate man pages
%os_git_vars hack/generate-docs.sh

%install
PLATFORM="$(go env GOHOSTOS)/$(go env GOHOSTARCH)"
install -d %buildroot%_bindir

# Install linux components
for bin in oc oadm openshift template-service-broker
do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 _output/local/bin/${PLATFORM}/${bin} %buildroot%_bindir/${bin}
done

# Install tests
install -d %buildroot%_libexecdir/%name
install -p -m 755 _output/local/bin/${PLATFORM}/extended.test %buildroot%_libexecdir/%name/
install -p -m 755 _output/local/bin/${PLATFORM}/ginkgo %buildroot%_libexecdir/%name/

# Install federation services
install -p -m 755 _output/local/bin/${PLATFORM}/hyperkube %buildroot%_bindir/

# Install cluster capacity
install -p -m 755 cmd/cluster-capacity/go/src/github.com/kubernetes-incubator/cluster-capacity/_output/local/bin/${PLATFORM}/hypercc %buildroot%_bindir/
ln -s hypercc %buildroot%_bindir/cluster-capacity

# Install service-catalog
install -p -m 755 cmd/service-catalog/go/src/github.com/kubernetes-incubator/service-catalog/_output/local/bin/${PLATFORM}/service-catalog %buildroot%_bindir/

# Install pod
install -p -m 755 _output/local/bin/${PLATFORM}/pod %buildroot%_bindir/

install -d -m 0755 %buildroot%_unitdir

mkdir -p %buildroot%_sysconfdir/sysconfig

for cmd in \
    openshift-deploy \
    openshift-docker-build \
    openshift-sti-build \
    openshift-git-clone \
    openshift-manage-dockerfile \
    openshift-extract-image-content \
    openshift-f5-router \
    openshift-recycle \
    openshift-router \
    origin
do
    ln -s openshift %buildroot%_bindir/$cmd
done

ln -s oc %buildroot%_bindir/kubectl

install -d -m 0755 %buildroot%_sysconfdir/origin/{master,node}
touch %buildroot%_sysconfdir/origin/.config_managed

# different service for origin vs aos
install -m 0644 contrib/systemd/%name-master.service %buildroot%_unitdir/%name-master.service
install -m 0644 contrib/systemd/%name-node.service %buildroot%_unitdir/%name-node.service
# same sysconfig files for origin vs aos
install -m 0644 contrib/systemd/origin-master.sysconfig %buildroot%_sysconfdir/sysconfig/%name-master
install -m 0644 contrib/systemd/origin-node.sysconfig %buildroot%_sysconfdir/sysconfig/%name-node

# Install man1 man pages
install -d -m 0755 %buildroot%_mandir/man1
install -m 0644 docs/man/man1/* %buildroot%_mandir/man1/

mkdir -p %buildroot%_sharedstatedir/origin

# Install sdn scripts
install -d -m 0755 %buildroot%_sysconfdir/cni/net.d
install -d -m 0755 %buildroot%_libexecdir/cni
install -p -m 0755 _output/local/bin/${PLATFORM}/sdn-cni-plugin %buildroot%_libexecdir/cni/openshift-sdn
install -p -m 0755 _output/local/bin/${PLATFORM}/host-local %buildroot%_libexecdir/cni/
install -p -m 0755 _output/local/bin/${PLATFORM}/loopback %buildroot%_libexecdir/cni/

install -d -m 0755 %buildroot%_unitdir/%name-node.service.d
install -p -m 0644 contrib/systemd/openshift-sdn-ovs.conf %buildroot%_unitdir/%name-node.service.d/openshift-sdn-ovs.conf

# Install bash completions
install -d -m 755 %buildroot%_sysconfdir/bash_completion.d/
for bin in oc openshift
do
  echo "+++ INSTALLING BASH COMPLETIONS FOR ${bin} "
  %buildroot%_bindir/${bin} completion bash > %buildroot%_sysconfdir/bash_completion.d/${bin}
  chmod 644 %buildroot%_sysconfdir/bash_completion.d/${bin}
done

# Install origin-accounting
install -d -m 755 %buildroot%_sysconfdir/systemd/system.conf.d/
install -p -m 644 contrib/systemd/origin-accounting.conf %buildroot%_sysconfdir/systemd/system.conf.d/

# Install migration scripts
install -d %buildroot%_datadir/%name/migration
install -p -m 755 contrib/migration/* %buildroot%_datadir/%name/migration/

%files
%doc README.md
%doc LICENSE
%_bindir/openshift
%_bindir/openshift-deploy
%_bindir/openshift-f5-router
%_bindir/openshift-recycle
%_bindir/openshift-router
%_bindir/openshift-docker-build
%_bindir/openshift-sti-build
%_bindir/openshift-git-clone
%_bindir/openshift-extract-image-content
%_bindir/openshift-manage-dockerfile
%_bindir/origin
%_sharedstatedir/origin
%_sysconfdir/bash_completion.d/openshift
%dir %attr(0700, root, root) %_sysconfdir/origin
%ghost %config(noreplace) %_sysconfdir/origin/.config_managed
%_mandir/man1/openshift*

%files tests
%_libexecdir/%name
%_libexecdir/%name/extended.test

%files master
%_unitdir/%name-master.service
%config(noreplace) %_sysconfdir/sysconfig/%name-master
%dir %_datadir/%name/migration/
%_datadir/%name/migration/*
%defattr(-,root,root,0700)
%config(noreplace) %_sysconfdir/origin/master

%post master
%post_service %name-master
# Create master config and certs if both do not exist
if [[ ! -e %_sysconfdir/origin/master/master-config.yaml &&
     ! -e %_sysconfdir/origin/master/ca.crt ]]; then
  %_bindir/openshift start master --write-config=%_sysconfdir/origin/master
  # Create node configs if they do not already exist
  if ! find %_sysconfdir/origin/ -type f -name "node-config.yaml" | grep -E "node-config.yaml"; then
    %_bindir/oc adm create-node-config --node-dir=%_sysconfdir/origin/node/ --node=localhost --hostnames=localhost,127.0.0.1 --node-client-certificate-authority=%_sysconfdir/origin/master/ca.crt --signer-cert=%_sysconfdir/origin/master/ca.crt --signer-key=%_sysconfdir/origin/master/ca.key --signer-serial=%_sysconfdir/origin/master/ca.serial.txt --certificate-authority=%_sysconfdir/origin/master/ca.crt
  fi
  # Generate a marker file that indicates config and certs were RPM generated
  echo "# Config generated by RPM at "`date -u` > %_sysconfdir/origin/.config_managed
fi

%preun master
%preun_service %name-master

%files node
%_unitdir/%name-node.service
%_sysconfdir/systemd/system.conf.d/origin-accounting.conf
%config(noreplace) %_sysconfdir/sysconfig/%name-node
%defattr(-,root,root,0700)
%config(noreplace) %_sysconfdir/origin/node

%post node
%post_service %name-node

%preun node
%preun_service %name-node

%files sdn-ovs
%dir %_unitdir/%name-node.service.d/
%_libexecdir/cni/*
%_unitdir/%name-node.service.d/openshift-sdn-ovs.conf

%files service-catalog
%_bindir/service-catalog

%files clients
%doc LICENSE
%_bindir/oc
%_bindir/kubectl
%_bindir/oadm
%_sysconfdir/bash_completion.d/oc
%_mandir/man1/oc*

%files pod
%_bindir/pod

%files cluster-capacity
%_bindir/hypercc
%_bindir/cluster-capacity

%files template-service-broker
%_bindir/template-service-broker

%files federation-services
%_bindir/hyperkube

%changelog
* Thu Apr 19 2018 Alexey Shabalin <shaba@altlinux.ru> 3.9.0-alt1%ubt
- Initial build for ALT

