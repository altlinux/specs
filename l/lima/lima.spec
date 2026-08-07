%define _unpackaged_files_terminate_build 1
%define import_path github.com/lima-vm/lima/v2

Name: lima
Version: 2.2.0
Release: alt1

Summary: Linux virtual machines, with a focus on running containers
License: Apache-2.0
Group: Emulators
Url: https://lima-vm.io/
Vcs: https://github.com/lima-vm/lima

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

Source2: alt-sisyphus.yaml
Source3: alt-p11.yaml
Source4: alt-p10.yaml
Source5: alt-sisyphus-images.yaml
Source6: alt-p11-images.yaml
Source7: alt-p10-images.yaml

Patch: %name-%version-alt.patch

Requires: openssh-clients
Requires: rsync

%ifarch x86_64 %ix86
Requires: qemu-system-x86
%endif
%ifarch aarch64
Requires: qemu-system-aarch64
%endif
%ifarch riscv64
Requires: qemu-system-riscv
%endif
%ifarch loongarch64
Requires: qemu-system-loongarch
%endif

BuildRequires(pre): rpm-build-golang

%description
Lima launches Linux virtual machines with automatic file sharing and
port forwarding. It provides a lightweight and declarative way to run
Linux virtual machines locally, with particular focus on container
workloads and integration with containerd and nerdctl.

%prep
%setup -a1
%autopatch -p1

# install ALT cloud-image templates for sisyphus, p11, and p10
for repo in sisyphus p11 p10; do
    cp -v %_sourcedir/alt-$repo.yaml templates/alt-$repo.yaml
    cp -v %_sourcedir/alt-$repo-images.yaml templates/_images/alt-$repo.yaml
done

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path

# limactl (CGO=1 for DNS resolver)
CGO_ENABLED=1 \
LDFLAGS="-X %import_path/pkg/version.Version=v%version" \
%golang_build ./cmd/limactl

# limactl-mcp
%golang_build ./cmd/limactl-mcp

# guest agents (CGO=0, static, cross-compiled)
mkdir -p "$BUILDDIR/guestagents"
for entry in aarch64:arm64 x86_64:amd64 riscv64:riscv64 i586:386 loongarch64:loong64; do
    uname_m="${entry%%:*}"
    goarch="${entry#*:}"

    output="$BUILDDIR/guestagents/lima-guestagent.Linux-${uname_m}"

    echo "build lima-guestagent: Linux/${uname_m} (GOARCH=${goarch})"
    CGO_ENABLED=0 GOOS=linux GOARCH="${goarch}" \
        go build -v -x -mod=vendor \
        -ldflags="-s -w -X %import_path/pkg/version.Version=v%version" \
        -o "${output}" \
        ./cmd/lima-guestagent

    chmod 644 "${output}"
    gzip -n "${output}"
done

# man pages
cd -
mkdir -p .build/share/man/man1
.build/bin/limactl generate-doc .build/share/man/man1 \
    --output .build --prefix %_prefix

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

mkdir -p %buildroot%_libexecdir/lima
mkdir -p %buildroot%_datadir/lima

mv %buildroot%_bindir/limactl-mcp %buildroot%_libexecdir/lima/

install -Dpm 0755 cmd/limactl-url-fedora-rawhide \
    %buildroot%_libexecdir/lima/limactl-url-fedora-rawhide

install -Dpm 0755 cmd/lima %buildroot%_bindir/lima
for helper in nerdctl apptainer docker podman kubectl; do
    install -Dpm 0755 cmd/$helper.lima %buildroot%_bindir/$helper.lima
done

cp -a "$BUILDDIR/guestagents/"* %buildroot%_datadir/lima/
cp -a templates %buildroot%_datadir/lima/templates

install -Dpm 0644 .build/share/man/man1/*.1 -t %buildroot%_mandir/man1/

%check
%buildroot%_bindir/limactl --version 2>&1 | grep -qF '%version'

%files
%_bindir/lima
%_bindir/limactl
%_bindir/*.lima
%_libexecdir/lima/
%_datadir/lima/
%_man1dir/lima.1*
%_man1dir/limactl*.1*

%changelog
* Sat Aug 08 2026 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- Packaged for ALT Sisyphus.
