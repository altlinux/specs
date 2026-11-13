%define _unpackaged_files_terminate_build 1
%define gazelle_dir %_datadir/bazel/rules/gazelle
%define gazelle_import github.com/bazelbuild/bazel-gazelle

Name: bazel-gazelle
Version: 0.54.0
Release: alt1

Summary: BUILD file generator and Go repository APIs for Bazel
License: Apache-2.0 AND BSD-3-Clause AND MIT
Group: Development/Other
URL: https://github.com/bazel-contrib/bazel-gazelle
VCS: https://github.com/bazel-contrib/bazel-gazelle.git
ExclusiveArch: %go_arches

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: rpm-build-python3

%description
Gazelle generates and updates Bazel BUILD files from source code. The package
includes the native generator, repository helpers, Starlark extension APIs and
original Go library sources. Helpers are built offline with the genuine Go
dependencies vendored in the upstream release.

%prep
%setup
sed -i 's/version = "",/version = "%version",/' MODULE.bazel

%build
export BUILDDIR="$PWD/.build"
export GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local
export GOFLAGS="-trimpath -buildmode=pie"
%golang_build cmd/gazelle cmd/autogazelle cmd/fetch_repo \
    cmd/generate_repo_config cmd/move_labels

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export RPM_BINDIR=%_libexecdir/%name
%golang_install
install -d %buildroot%_bindir
mv %buildroot%_libexecdir/%name/gazelle %buildroot%_bindir/gazelle

install -d %buildroot%gazelle_dir
cp -a BUILD.bazel MODULE.bazel WORKSPACE WORKSPACE.bzlmod \
    def.bzl deps.bzl extensions.bzl go_tools.bzl go.mod go.sum go.work \
    cmd config flag internal label language merger pathtools repo resolve \
    rule testtools third_party tools v2 walk %buildroot%gazelle_dir/
find %buildroot%gazelle_dir -iname 'README*' -delete
mkdir licenses
find vendor -type f \( -iname '*LICENSE*' -o -iname '*NOTICE*' \
    -o -name 'PATENTS' -o -name 'AUTHORS' \) \
    -exec cp --parents '{}' licenses/ \;

%check
export GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local
unset GOFLAGS
# The tests/ tree contains generator input fixtures, not Go packages.
# internal/{gazellebinarytest,generationtest} and internal itself need
# Bazel-generated executables and a resolved external toolchain graph.
export RUNFILES_DIR="$PWD/.test-runfiles"
mkdir -p "$RUNFILES_DIR"
ln -s "$PWD" "$RUNFILES_DIR/bazel_gazelle"
# The converter roundtrip fixtures require the pinned upstream Go SDK
# and external module archives unavailable in the offline build.
# These update-repos cases fetch modules from public Go proxies.
offline_tests='^Test(ImportCollision(WithReplace)?|UpdateRepos('\
'With(QueryToWorkspace|GlobalBuildTags)|WithBzlmod(With|Without)ToMacro|'\
'(Old|New)BoilerplateNew(Repo|Macro)|SkipsDirectiveRepo|DoesNotModifyGoSum))$'
%gotest -mod=vendor -v -skip "$offline_tests" \
    -ldflags "-X %gazelle_import/cmd/gazelle.goRootFile=$(go env GOROOT)/VERSION" \
    ./cmd/... ./config/... ./flag/... ./label/... ./language/... \
    ./merger/... ./pathtools/... ./repo/... ./resolve/... ./rule/... \
    ./walk/... ./v2/... ./internal/module/... ./internal/version/... \
    ./internal/wspace/... ./tools/override-generator

%files
%_bindir/gazelle
%_libexecdir/%name
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%gazelle_dir
%doc LICENSE AUTHORS CONTRIBUTORS licenses

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 0.54.0-alt1
- Initial build for ALT.
