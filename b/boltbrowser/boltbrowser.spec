%global import_path github.com/br0xen/boltbrowser
%global _unpackaged_files_terminate_build 1

Name: boltbrowser
Version: 2.2
Release: alt1.1
Summary: A CLI Browser for BoltDB Files

Group: Databases
License: GPL-3.0-only
Url: https://%import_path
Packager: Ivan Pepelyaev <fl0pp5@altlinux.org>

Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

BuildRequires: /proc

Patch1: boltbrowser-alt-add-loongarc64-support-for-vendored-github.com-boltd.patch

%description
%summary.

%prep
%setup
%patch1 -p 1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.gopath"

%golang_install

rm -rf -- %buildroot%go_root

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Tue Aug 20 2024 Ivan A. Melnikov <iv@altlinux.org> 2.2-alt1.1
- NMU: fix FTBFS on loongarch64.

* Tue Aug 20 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.2-alt1
- Initial build for ALT.
