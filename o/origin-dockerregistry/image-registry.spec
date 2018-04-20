%define _libexecdir /usr/libexec

# do not extract debuginfo
%define __find_debuginfo_files %nil

%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

%global gopath      %_datadir/gocode
%global import_path github.com/openshift/image-registry
%global commit fef8b8b5ff6c348ff3efdd518398314234587d8e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global os_git_vars OS_GIT_VERSION=v3.9.0 OS_GIT_MINOR=9+ OS_GIT_COMMIT=%{shortcommit} OS_GIT_MAJOR=3 OS_GIT_TREE_STATE=clean

%global golang_version 1.8.1
%global product_name OpenShift Docker Registry
%global import_path github.com/openshift/image-registry

Name: origin-dockerregistry 
Version: 3.9.0
Release: alt1%ubt
Summary: Docker Registry v2 for OpenShift Origin
License: ASL 2.0
Group: Networking/Other
Url: https://%import_path
Source: %name-%version.tar
#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-golang rpm-build-ubt
BuildRequires: golang >= %golang_version
BuildRequires: /proc

%description
OpenShift Image Registry is a tightly integrated with OpenShift Origin application
that lets you distribute Docker images.

Features:
 - Pull and cache images from remote registries.
 - Role-based access control (RBAC).
 - Audit log.
 - Promethus metrics.


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
OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %os_git_vars make build-cross

%install
PLATFORM="$(go env GOHOSTOS)/$(go env GOHOSTARCH)"
install -d %buildroot%_bindir

# Install linux components
for bin in dockerregistry
do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 _output/local/bin/${PLATFORM}/${bin} %buildroot%_bindir/${bin}
done

%files
%doc README.md
%doc LICENSE
%_bindir/dockerregistry

%changelog
* Fri Apr 20 2018 Alexey Shabalin <shaba@altlinux.ru> 3.9.0-alt1%ubt
- Initial build for ALT

