%define _unpackaged_files_terminate_build 1

Name: capsule
Version: 0.3.8
Release: alt1

Summary: Tool for creating portable Linux containers from OCI images
Summary(ru_RU.UTF-8): Инструмент для создания портативных Linux-контейнеров из OCI-образов
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: https://altlinux.space/dmitry/capsule
Vcs: https://altlinux.space/dmitry/capsule.git

ExclusiveArch: %go_arches
# netavark is not built for i586
ExcludeArch: i586

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-golang
BuildRequires: golang
BuildRequires: meson
BuildRequires: libgpgme-devel
BuildRequires: libbtrfs-devel
BuildRequires: libdevmapper-devel

# Bundled into capsule-runtime at build time by scripts/create-utils.sh
BuildRequires: bubblewrap
BuildRequires: squashfuse
BuildRequires: squashfs-tools
BuildRequires: unionfs
BuildRequires: binutils

# Subprocess helpers of buildah (linked as a Go library).
# Invisible to lib.req (no ELF link) and golang.req (no devel sources).
Requires: squashfs-tools
Requires: shadow-submap
Requires: fuse-overlayfs
Requires: containers-common
Requires: netavark

%description
capsule is a tool for creating portable Linux containers from OCI images,
producing a single self-contained ELF binary that bundles a SquashFS rootfs
and a Go runtime which mounts and runs it via bubblewrap.

%description -l ru_RU.UTF-8
capsule — инструмент для создания портативных Linux-контейнеров из OCI-образов.
Результат сборки — единый самодостаточный ELF-файл, содержащий SquashFS-корень
и Go-рантайм, который монтирует и запускает его через bubblewrap.

%prep
%setup -a1

%build
export GOFLAGS="-mod=vendor"
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%doc README.md
%doc README.en.md
%doc README.ru.md
%doc LICENSE
%doc examples

%changelog
* Mon Jun 08 2026 Dmitry Udalov <udalov@altlinux.org> 0.3.8-alt1
- Use private build storage instead of podman shared store.

* Wed Jun 03 2026 Dmitry Udalov <udalov@altlinux.org> 0.3.7-alt1
- Add sandbox isolation levels: shared, isolated, strict.
- Guide the user to set up rootless subuid/subgid (ALT-specific).

* Sat May 30 2026 Dmitry Udalov <udalov@altlinux.org> 0.3.6-alt1
- Pull the image when it has been updated upstream.
- Fix icon export.

* Mon May 25 2026 Dmitry Udalov <udalov@altlinux.org> 0.3.5-alt1
- Auto-detect ld-linux and libgcc paths in the utils bundle.

* Sun May 17 2026 Dmitry Udalov <udalov@altlinux.org> 0.3.4-alt1
- Generate utils.tar.gz at build time.
- Align Requires with buildah subprocess deps.
- Install example capsule recipes as %%doc.

* Sun May 17 2026 Dmitry Udalov <udalov@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus.
