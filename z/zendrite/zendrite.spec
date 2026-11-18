%global import_path codefloe.com/pat-s/zendrite

%define helpers create-account generate-config generate-keys
%define targets zendrite %helpers

Name: zendrite
Version: 3.8.0
Release: alt1

Summary: Matrix homeserver, fork of element-hq/dendrite
License: AGPL-3.0-only
Group: Communications

Url: https://zendrite.pat-s.me
Vcs: https://codefloe.com/pat-s/zendrite

Source0: %name-%version.tar
Source1: vendor.tar
Source2: zendrite.service
Source3: zendrite.sysusers
Source4: README.ALT
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: libsqlite3-devel

ExclusiveArch: %go_arches
ExcludeArch: %ix86

%description
Zendrite is a second-generation Matrix homeserver written in Go!
Following the microservice architecture model, Zendrite is designed
to be efficient, reliable and scalable.

%prep
%setup -a 1
%autopatch -p1
cp -p %SOURCE4 README.ALT

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=1
export TAGS=libsqlite3
%golang_prepare
for target in %targets; do
    %golang_build cmd/$target
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export IGNORE_SOURCES=1
for target in %targets; do
    %golang_install cmd/$target
done
mkdir -p %buildroot%_libexecdir/%name/bin
for helper in %helpers; do
    mv %buildroot%_bindir/$helper %buildroot%_libexecdir/%name/bin/
done
mkdir -p %buildroot%_sysconfdir/%name %buildroot%_sharedstatedir/%name

install -Dm644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm644 %SOURCE3 %buildroot%_sysusersdir/%name.conf

%pre
%sysusers_create_package %name %SOURCE3

%post
# Generate config if missing
if [ ! -e /etc/%name/%name.yaml ]; then
    %_libexecdir/%name/bin/generate-config > /etc/%name/%name.yaml
fi
# Generate key if missing
if [ ! -e %_sharedstatedir/%name/matrix_key.pem ]; then
    %_libexecdir/%name/bin/generate-keys --private-key %_sharedstatedir/%name/matrix_key.pem
    chmod 640 %_sharedstatedir/%name/matrix_key.pem
    chgrp zendrite %_sharedstatedir/%name/matrix_key.pem
fi

%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_libexecdir/%name
%attr(750, root, zendrite) %_sysconfdir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%doc README.md README.ALT

%changelog
* Mon Nov 09 2026 Vladislav Tatjanin <l27001@altlinux.org> 3.8.0-alt1
- Initial build.

