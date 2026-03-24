%define _unpackaged_files_terminate_build 1

Name: scorecard
Version: 5.4.0
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
export BUILDDIR="$PWD/%build_dir"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

%build
export BUILDDIR="$PWD/%build_dir"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
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
* Tue Mar 17 2026 Aleksandr Dovydenkov <asd@altlinux.org> 5.4.0-alt1
- Initial build for ALT Linux Sisyphus.
