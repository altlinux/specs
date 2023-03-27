%global import_path github.com/containers/skopeo

%global _unpackaged_files_terminate_build 1
%def_without check

Name: skopeo
Version: 1.11.1
Release: alt1

Summary: skopeo is a command line utility that performs various operations on container images and image repositories
License: Apache-2.0
Group: Other
Url: https://github.com/containers/skopeo

Source: %name-%version.tar

Requires: containers-common >= 1:1

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-md2man
BuildRequires: glib2-devel libgpgme-devel libbtrfs-devel
BuildRequires: libgio-devel libostree-devel libselinux-devel libdevmapper-devel
BuildRequires: libassuan-devel
%if_with check
BuildRequires: /proc
BuildRequires: podman
%endif

%description
Skopeo works with API V2 registries such as Docker registries, the Atomic
registry, private registries, local directories and local OCI-layout
directories. Skopeo does not require a daemon to be running to perform these
operations which consist of:
- Copying an image from and to various storage mechanisms. For example you can
  copy images from one registry to another, without requiring privilege.
- Inspecting a remote image showing its properties including its layers,
  without requiring you to pull the image to the host.
- Deleting an image from an image repository.
- When required by the repository,
  skopeo can pass the appropriate credentials and certificates for
  authentication.

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export GIT_COMMIT=%release

%golang_prepare

pushd .gopath/src/%import_path
#%%golang_build cmd/%%name
%make_build bin/skopeo
for doc in $(find docs -name '*.1.md'); do
    go-md2man -in "$doc" -out "docs/$(basename "${doc%%.md}")"
done
popd

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"
# export IGNORE_SOURCES=1
#%%golang_install
pushd .gopath/src/%import_path
%make DESTDIR=%buildroot PREFIX=%_prefix install-binary install-docs install-completions
popd

%check
make check

%files
%doc README.md
%_bindir/*
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/skopeo.fish
%_datadir/zsh/site-functions/_skopeo
%_man1dir/%{name}*

%changelog
* Mon Mar 27 2023 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- New version 1.11.1.

* Sun Jan 22 2023 Alexey Shabalin <shaba@altlinux.org> 1.10.0-alt1
- new version 1.10.0

* Sun Jul 31 2022 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt3
- drop containers-common package

* Sun Jul 31 2022 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt2
- move registry.altlinux.org after docker.io in registries.conf
- add quay.io to unqualified-search-registries in registries.conf

* Tue Jul 26 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.9.1-alt1
- new version 1.9.1

* Thu Jul 14 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.9.0-alt1
- new version 1.9.0

* Mon May 09 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.8.0-alt1
- new version 1.8.0

* Fri Mar 25 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.7.0-alt1
- new version 1.7.0

* Thu Feb 17 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.6.1-alt1
- new version 1.6.1

* Thu Feb 03 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.6.0-alt1
- new version 1.6.0

* Mon Nov 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.5.2-alt1
- new version 1.5.2

* Thu Nov 11 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.5.1-alt1
- new version 1.5.1

* Mon Oct 11 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Wed Sep 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.4.1-alt1
- new version 1.4.1
- add /usr/share/alt/secrets to containers-common package, fix mounts.conf

* Tue Nov 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Wed Sep 09 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Wed May 13 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.0-alt1
- new version 0.2.0

* Mon Mar 23 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.41-alt2
- Change registries search order

* Thu Mar 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.41-alt1
- new version 0.1.41

* Fri Sep 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.39-alt1
- new version 0.1.39

* Tue Jan 08 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.34-alt1
- Initial build for Sisyphus
