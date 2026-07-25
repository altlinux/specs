%global import_path github.com/gruntwork-io/terragrunt
%global _unpackaged_files_terminate_build 1

Name: terragrunt
Version: 1.0.7
Release: alt2
Summary: Terragrunt is a orchestration tool for OpenTofu/Terraform

Group: Development/Tools
License: MIT

Url: https://terragrunt.gruntwork.io/
Vcs: https://github.com/gruntwork-io/terragrunt.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.0
BuildPreReq: /proc

%{?!_without_test:%{?!_disable_test:%{?!_without_check:%{?!_disable_check:BuildRequires: git opentofu bash}}}}

%description
Terragrunt is a flexible orchestration tool that allows Infrastructure as Code
written in OpenTofu/Terraform to scale.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X github.com/gruntwork-io/terragrunt/internal/version.Version=v%{version} \
                -extldflags '-static'"
export CGO_ENABLED=0

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
export LDFLAGS="-X github.com/gruntwork-io/terragrunt/internal/version.Version=v%{version} \
                -extldflags '-static'"
export IMPORT_PATH="%import_path"
# Use tofu because terraform is not present in sisyphus now.
export TG_TFPATH=tofu
# Disable trace commands.
setx=
[[ $- = *x* ]] && setx=1
[ -n "$setx" ] && set +x
# Test skip patterns for all packages.
# Patterns must be separated by space.
commonskip=""
# Test skip patterns for specific packages.
# Patterns must be separated by space.
declare -A EXCLUDE_TESTS=(
  # Skip due to network usage.
  ["${IMPORT_PATH}/internal/cli/commands/catalog/tui"]="TestTUIScaffoldWithRealRepository"
  ["${IMPORT_PATH}/internal/git"]="^TestGitRunner"
  ["${IMPORT_PATH}/internal/providercache"]="^TestProviderCache"
  ["${IMPORT_PATH}/internal/runner/run"]="^TestDownloadTerraform"
  ["${IMPORT_PATH}/internal/shell"]="TestGitLevelTopDirCaching"
  ["${IMPORT_PATH}/test"]="^TestIncludeDirs"
  ["${IMPORT_PATH}/internal/tf"]="^TestToSourceUrl"
  ["${IMPORT_PATH}/pkg/config"]="TestStackLocalsCtyReading"
)

ALL_PKGS=($(go list ./...))
code=0
for package in ${ALL_PKGS[@]}; do
  patterns=("$commonskip")

  if [[ -v EXCLUDE_TESTS["$package"] ]]; then 
    for p in ${EXCLUDE_TESTS["$package"]}; do
      patterns+=("$p")
    done
  fi

  skip_pattern=$(IFS='|'; echo "${patterns[*]}")
  skip=
  if [ -n "$skip_pattern" ]; then
    skip="-skip ${skip_pattern}"
  fi
  %gotest $skip $package || code=$((code + $?))
done

# Fail if one of tests failed.
[ $code -gt 0 ] && exit 1

# Enable trace commands back.
[ -n "$setx" ] && set -x

%files
%_bindir/*

%changelog
* Sat Jul 25 2026 Alexey Romanyuta <r9odt@altlinux.org> 1.0.7-alt2
- Add check section to spec file.
- Fix ldflags to set correct version similar to upstream (ALT #59840).

* Tue Jun 09 2026 Alexey Romanyuta <r9odt@altlinux.org> 1.0.7-alt1
- New version 1.0.7.

* Fri Mar 06 2026 Alexey Romanyuta <r9odt@altlinux.org> 0.99.4-alt1
- New version v0.99.4
- Remove documentation from the package due to a change in the presentation
  of documentation in the parent project.

* Fri Jul 11 2025 Alexey Romanyuta <r9odt@altlinux.org> 0.83.0-alt1
- New version v0.83.0

* Fri Jul 04 2025 Alexey Romanyuta <r9odt@altlinux.org> 0.82.4-alt1
- New version v0.82.4
- Fix project url in spec

* Mon Jun 30 2025 Alexey Romanyuta <r9odt@altlinux.org> 0.82.3-alt1
- Initial build v0.82.3
