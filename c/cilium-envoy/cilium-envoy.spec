%global import_path github.com/cilium/proxy
%global git_sha ff3fe7f0bb9e4ac6a283ea38bf9ee3f375530d56

Name:           cilium-envoy
Version:        1.35.3
Release:        alt1
Summary:        Envoy proxy for Cilium

License:        Apache-2.0
Group:          Development/Tools
URL:            https://github.com/cilium/proxy

Source:			%name-%version.tar

BuildRequires:  clang18.1
BuildRequires:  libstdc++-devel
BuildRequires:  libstdc++-devel-static
BuildRequires:  llvm18.1
BuildRequires:  llvm18.1-devel
BuildRequires:  lld18.1
BuildRequires:  patchelf
BuildRequires:  rpm-build
BuildRequires:  ca-certificates
BuildRequires:  golang >= 1.24.0
BuildRequires:  java-21-openjdk-devel
BuildRequires:  cilium-envoy-deps
BuildRequires:  cilium-envoy-cache
BuildRequires:  bazel-for-cilium

ExcludeArch:    i586

%description
Envoy proxy for Cilium with minimal Envoy extensions and Cilium 
policy enforcement filters. Cilium uses this as its host proxy for 
enforcing HTTP and other L7 policies as specified in network policies 
for the cluster. Cilium proxy is distributed within the Cilium images.

%prep
%setup -q
# First, update the additional packages required for buildig cilium-envoy 
# according to the instructions in .gear/README.md

tar -xf %_datadir/%name-deps/bazel-external-deps.tar.gz
tar -xf %_datadir/%name-cache/bazel-cache.tar.gz

# Change symlinks in external to build env
find %_builddir/%name-%version/external -type l ! -path "%_builddir/%name-%version/external/local_jdk/*" | while read symlink; do
    target=$(readlink "$symlink")
    if [[ "$target" == /* ]]; then
        new_target=$(echo "$target" | sed "s|.*/external|%_builddir/%name-%version/external|")
        ln -sf "$new_target" "$symlink"
    fi
done

rm -f external/local_jdk/bin
ln -s /usr/lib/jvm/java-21-openjdk/bin external/local_jdk/bin

sed -i 's/go_register_toolchains(go_version)/go_register_toolchains()/g' external/envoy/bazel/dependency_imports.bzl

awk '
BEGIN {skip=0; level=0}
/^[[:space:]]*local_repository[[:space:]]*\(/ {skip=1; level=1; next}
/^[[:space:]]*git_repository[[:space:]]*\(/ {skip=1; level=1; next}
skip {
	n_open = gsub(/\(/, "(")
		n_close = gsub(/\)/, ")")
		level += n_open - n_close
		if (level <= 0) {skip=0; level=0}
	next
}
{print}
' WORKSPACE > WORKSPACE.tmp && mv WORKSPACE.tmp WORKSPACE

awk '/^workspace\(/ {print; system("cat %_datadir/cilium-envoy-deps/WORKSPACE.localdeps"); next}1' \
	WORKSPACE > WORKSPACE.tmp && mv WORKSPACE.tmp WORKSPACE

sed -i \
    -e 's/const char build_scm_revision\[\] *= *BUILD_SCM_REVISION;/const char build_scm_revision[] = "%git_sha";/' \
    -e 's/const char build_scm_status\[\] *= *BUILD_SCM_STATUS;/const char build_scm_status[] = "clean";/' \
    external/envoy/source/common/version/version_linkstamp.cc

sed -i \
    '/name = "version_lib"/,/^)/ s/srcs = \[/srcs = [ "version_linkstamp.cc",/' \
    external/envoy/source/common/version/BUILD

cat > bazel/get_workspace_status <<EOF
#!/usr/bin/env bash
echo "BUILD_SCM_REVISION %git_sha"
echo "ENVOY_BUILD_SCM_REVISION %git_sha"
echo "STABLE_BUILD_SCM_REVISION %git_sha"
echo "BUILD_SCM_STATUS clean"
echo "STABLE_BUILD_SCM_STATUS clean"
echo "BUILD_SCM_HASH %git_sha"
echo "BUILD_SCM_BRANCH unknown"
EOF
chmod +x bazel/get_workspace_status

%build
export NO_DOCKER=1
export BAZEL_SKIP_SETUP_CLANG=1
export CC=/usr/bin/clang-18
export CXX=/usr/bin/clang-18
export LD=/usr/bin/lld-18
export CARGO_BAZEL_SKIP_LOCKFILE_UPDATE=1
export CARGO_BAZEL_REPIN=false
export PKG_CONFIG=/bin/pkg-config

cd proxylib
CGO_ENABLED=1 go build -ldflags '-extldflags -Wl,-soname,libcilium.so' -o libcilium.so -buildmode=c-shared
cd ..

%ifarch x86_64
CPU=amd64
%elifarch aarch64
CPU=arm64
export BAZEL_COPTS="-target aarch64-unknown-linux-gnu"
%else
%error Unsupported architecture
%endif

BUILD_CILIUM_ENVOY="bazel build \
  --config=release \
  --repository_cache=$BAZEL_REPO_CACHE \
  --experimental_repository_disable_download \
  --workspace_status_command=bazel/get_workspace_status \
  --override_repository=dynamic_modules_rust_sdk_crate_index=external/dynamic_modules_rust_sdk_crate_index \
  --override_repository=go_sdk=external/go_sdk \
  --override_repository=go_linux_$CPU=external/go_sdk \
  --define=BAZEL_USE_LOCAL_JAVA_RUNTIME=1 \
  --host_javabase=@local_jdk//:jdk \
  --javabase=@local_jdk//:jdk \
  --action_env=PKG_CONFIG \
  --linkopt=-latomic \
  --host_linkopt=-latomic \
  --copt=-Wno-error \
  --copt=-Wno-error=parentheses \
  --copt=-Wno-error=uninitialized \
  --cxxopt=-Wno-error \
  --cxxopt=-Wno-error=return-type \
  --cxxopt=-Wno-error=parentheses \
  --cxxopt=-Wno-error=uninitialized \
  --cxxopt=-Wno-error=infinite-recursion"

$BUILD_CILIUM_ENVOY //:%name
$BUILD_CILIUM_ENVOY //:%name-starter

%install
rm -rf %buildroot
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot%_libexecdir

install -m 0755 bazel-bin/%name %buildroot/%_bindir/%name
install -m 0755 bazel-bin/%name-starter %buildroot/%_bindir/%name-starter
install -m 0755 proxylib/libcilium.so %buildroot%_libexecdir/libcilium.so

%files
%_bindir/%name
%_bindir/%name-starter
%_libexecdir/libcilium.so

%changelog
* Fri Nov 07 2025 Aleksandr Gamzin <gamzin@altlinux.org> 1.35.3-alt1
- Initial build for Sysiphus.
