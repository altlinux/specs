%define _unpackaged_files_terminate_build 1

Name: scorecard
Version: 5.5.0
Release: alt1

Summary: OpenSSF Scorecard - Security health metrics for Open Source
License: Apache-2.0
Group: Development/Other
URL: https://scorecard.dev/
VCS: https://github.com/ossf/scorecard

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang

%description
Scorecard is an automated tool that assesses a number of important checks
associated with software security and assigns each check a score
of 0-10. You can use these scores to understand specific areas to improve in
order to strengthen the security posture of your project. You can also assess
the risks that dependencies introduce, and make informed decisions about
accepting these risks, evaluating alternative solutions, or working with
the maintainers to make improvements.

%global build_dir .build
%global import_path github.com/ossf/scorecard

%prep
%setup -a1

# Correction of the executable file name in the help message and autocompletion scripts.
sed -i cmd/root.go -e 's|scorecardUse  = `./scorecard|scorecardUse  = `scorecard|'

export BUILDDIR="$PWD/%build_dir"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

%build
export BUILDDIR="$PWD/%build_dir"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
buildDate="$(date -u -d "@${SOURCE_DATE_EPOCH}" +'%%Y-%%m-%%d')"
export LDFLAGS="$LDFLAGS -w \
             -X sigs.k8s.io/release-utils/version.gitVersion=%version-%release \
             -X sigs.k8s.io/release-utils/version.gitCommit=%version \
             -X sigs.k8s.io/release-utils/version.gitTreeState=clean \
             -X sigs.k8s.io/release-utils/version.buildDate=$buildDate"
cd %build_dir/src/%import_path 
%golang_build .

%install
export BUILDDIR="$PWD/%build_dir"
export IGNORE_SOURCES=1
%golang_install

%check
# Same as make unit-test, but without network-depended tests
tests_list=`go list ./... \
    | sed '/github.com\/ossf\/scorecard\/v5\/internal\/gitfile/d'  \
    | sed '/github.com\/ossf\/scorecard\/v5\/checks\/raw/d'`

%ifarch i586
    SKIP_GINKGO=1 go test -covermode=atomic  -coverprofile=unit-coverage.out -coverpkg=./... $tests_list
%else
    SKIP_GINKGO=1 go test -race -covermode=atomic  -coverprofile=unit-coverage.out -coverpkg=./... $tests_list
%endif

%files
%doc LICENSE README.md
%_bindir/scorecard

%changelog
* Tue Jun 30 2026 Aleksandr Dovydenkov <asd@altlinux.org> 5.5.0-alt1
- New version 5.5.0.

* Tue Apr 07 2026 Aleksandr Dovydenkov <asd@altlinux.org> 5.4.0-alt2
- Display version correctly (closes #58489).
- Fix autocompletion scripts (closes #58488).

* Tue Mar 17 2026 Aleksandr Dovydenkov <asd@altlinux.org> 5.4.0-alt1
- Initial build for ALT Linux Sisyphus.
