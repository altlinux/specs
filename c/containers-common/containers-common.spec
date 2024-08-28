# Below definitions are used to deliver config files from a particular branch
# of c/image, c/common, c/storage vendored in all of Buildah, Podman and Skopeo.
# These vendored components must have the same version. If it is not the case,
# pick the oldest version on c/image, c/common, c/storage vendored in
# Buildah/Podman/Skopeo.

%global image_branch v5.32.2
%global storage_branch v1.55.0
%global shortnames_branch main

%global github_containers https://raw.githubusercontent.com/containers

Epoch: 2
Name: containers-common
Version: 0.60.2
Release: alt1
License: Apache-2.0
Group: System/Configuration/Other
Url: https://github.com/containers/common
BuildArch: noarch
Summary: Common configuration and documentation for containers

%global common_branch v%{version}

Source1: %github_containers/common/%common_branch/docs/containers.conf.5.md
Source2: %github_containers/common/%common_branch/pkg/config/containers.conf
Source3: %github_containers/common/%common_branch/pkg/seccomp/seccomp.json
Source4: %github_containers/common/%common_branch/pkg/subscriptions/mounts.conf
Source5: %github_containers/image/%image_branch/docs/containers-auth.json.5.md
Source6: %github_containers/image/%image_branch/docs/containers-certs.d.5.md
Source7: %github_containers/image/%image_branch/docs/containers-policy.json.5.md
Source8: %github_containers/image/%image_branch/docs/containers-registries.conf.5.md
Source9: %github_containers/image/%image_branch/docs/containers-registries.conf.d.5.md
Source10: %github_containers/image/%image_branch/docs/containers-registries.d.5.md
Source11: %github_containers/image/%image_branch/docs/containers-signature.5.md
Source12: %github_containers/image/%image_branch/docs/containers-transports.5.md
Source13: %github_containers/image/%image_branch/registries.conf
Source14: %github_containers/common/%common_branch/docs/containers-mounts.conf.5.md
Source15: %github_containers/shortnames/%shortnames_branch/shortnames.conf
Source16: %github_containers/image/%image_branch/default.yaml
Source17: %github_containers/image/%image_branch/default-policy.json
Source18: %github_containers/storage/%storage_branch/docs/containers-storage.conf.5.md
Source19: %github_containers/storage/%storage_branch/storage.conf
Source23: %github_containers/common/%common_branch/docs/Containerfile.5.md
Source24: %github_containers/common/%common_branch/docs/containerignore.5.md
Source25: %github_containers/common/%common_branch/docs/links/.containerignore.5

Provides: skopeo-containers = %EVR
# Requires: (container-selinux >= 2:2.162.1 if selinux-policy)
BuildRequires: go-md2man

%description
This package contains common configuration files and documentation for container
tools ecosystem, such as Podman, Buildah and Skopeo.

It is required because the most of configuration files and docs come from projects
which are vendored into Podman, Buildah, Skopeo, etc. but they are not packaged
separately.

%package extra
Summary: Extra dependencies for Podman and Buildah
Group: System/Configuration/Other
Requires: %name = %EVR
Requires: container-network-stack
Requires: oci-runtime
Requires: crun
# netavark build for not all arches
#Requires: netavark >= 1.6.0
Requires: slirp4netns
Requires: passt
Requires: iptables
Requires: nftables
# Recommends: qemu-user-static

%description extra
This subpackage will handle dependencies common to Podman and Buildah which are
not required by Skopeo.

%prep
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .
cp %SOURCE4 .
cp %SOURCE5 .
cp %SOURCE6 .
cp %SOURCE7 .
cp %SOURCE8 .
cp %SOURCE9 .
cp %SOURCE10 .
cp %SOURCE11 .
cp %SOURCE12 .
cp %SOURCE13 .
cp %SOURCE14 .
cp %SOURCE15 000-shortnames.conf
cp %SOURCE16 .
cp %SOURCE17 policy.json
cp %SOURCE18 .
cp %SOURCE19 .
cp %SOURCE23 .
cp %SOURCE24 .
cp %SOURCE25 .

%build
mkdir -p man5
for FILE in $(ls *.5.md); do
    go-md2man -in $FILE -out man5/$(basename $FILE .md)
done

cp man5/containerignore.5 man5/.containerignore.5

%install
# install config and policy files for registries
install -dp %buildroot%_sysconfdir/containers/{certs.d,oci/hooks.d,systemd}
install -dp %buildroot%_sharedstatedir/containers/sigstore
install -dp %buildroot%_datadir/containers/systemd
install -dp %{buildroot}%_prefix/lib/containers/storage
install -dp -m 700 %buildroot%_prefix/lib/containers/storage/overlay-images
touch %buildroot%_prefix/lib/containers/storage/overlay-images/images.lock
install -dp -m 700 %buildroot%_prefix/lib/containers/storage/overlay-layers
touch %buildroot%_prefix/lib/containers/storage/overlay-layers/layers.lock

install -Dp -m0644 default.yaml -t %buildroot%_sysconfdir/containers/registries.d
install -Dp -m0644 storage.conf -t %buildroot%_datadir/containers
install -Dp -m0644 registries.conf -t %buildroot%_sysconfdir/containers
install -Dp -m0644 000-shortnames.conf -t %buildroot%_sysconfdir/containers/registries.conf.d
install -Dp -m0644 policy.json -t %buildroot%_sysconfdir/containers
touch %buildroot%_sysconfdir/containers/{storage,containers}.conf

# install manpages
for FILE in $(ls -a man5 | grep 5); do
    install -Dp -m0644 man5/$FILE -t %buildroot%_mandir/man5
done

# install config files for mounts, containers and seccomp
install -m0644 mounts.conf %buildroot%_datadir/containers/mounts.conf
install -m0644 seccomp.json %buildroot%_datadir/containers/seccomp.json
install -m0644 containers.conf %buildroot%_datadir/containers/containers.conf

# install secrets patch directory
install -d -p -m 755 %buildroot%_datadir/alt/secrets

%files
%dir %_sysconfdir/containers
%dir %_sysconfdir/containers/certs.d
%dir %_sysconfdir/containers/oci
%dir %_sysconfdir/containers/oci/hooks.d
%dir %_sysconfdir/containers/registries.conf.d
%dir %_sysconfdir/containers/registries.d
%dir %_sysconfdir/containers/systemd
%dir %_prefix/lib/containers/storage
%dir %_prefix/lib/containers/storage/overlay-images
%dir %_prefix/lib/containers/storage/overlay-layers
%_prefix/lib/containers/storage/overlay-images/images.lock
%_prefix/lib/containers/storage/overlay-layers/layers.lock

%config(noreplace) %_sysconfdir/containers/policy.json
%config(noreplace) %_sysconfdir/containers/registries.conf
%config(noreplace) %_sysconfdir/containers/registries.conf.d/000-shortnames.conf
%config(noreplace) %_sysconfdir/containers/registries.d/default.yaml
%ghost %_sysconfdir/containers/storage.conf
%ghost %_sysconfdir/containers/containers.conf
%dir %_sharedstatedir/containers/sigstore
%_man5dir/*
%_man5dir/.containerignore.5.*
%_datadir/containers
%dir %_datadir/alt/secrets

%files extra

%changelog
* Wed Aug 28 2024 Alexey Shabalin <shaba@altlinux.org> 2:0.60.2-alt1
- Update sources

* Mon Apr 15 2024 Alexey Shabalin <shaba@altlinux.org> 2:0.58.1-alt1
- Update sources
- Add support for additionalstore /usr/lib/containers/storage
- Add passt to R: in extra package

* Thu Dec 07 2023 Alexey Shabalin <shaba@altlinux.org> 1:3-alt1
- Update sources

* Tue May 16 2023 Alexey Shabalin <shaba@altlinux.org> 1:2-alt1
- Update sources
- Add containers-common-extra subpackage

* Mon Aug 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1:1-alt2
- Add ALT images to shortnames.conf

* Sun Jul 31 2022 Alexey Shabalin <shaba@altlinux.org> 1:1-alt1
- Initial build as separated package.

