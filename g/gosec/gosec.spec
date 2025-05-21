%define _unpackaged_files_terminate_build 1

Name: gosec
Version: 2.22.4
Release: alt1

Summary: Inspects source code for security problems by scanning the Go AST and SSA code representation
License: Apache-2.0
Group: Development/Other
Url: https://securego.io
Vcs: https://github.com/securego/gosec.git
# Tests fail due to unsafe type casting.
# https://github.com/securego/gosec/issues/1349
ExcludeArch: i586

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Gosec is a static analysis tool that scans
Go source code to identify potential
security vulnerabilities by analyzing
the AST (Abstract Syntax Tree) and SSA
(Static Single Assignment) representations.
It detects issues like:
- Hardcoded credentials
- SQL injection risks
- Insecure file permissions
- Weak cryptographic algorithms
- Improper error handling
- Other common Go security pitfalls.

%prep
%setup -a1

%build
%make BIN=bin/gosec \
  GIT_TAG=v%version \
  BUILD_DATE="$(date -u -d "@${SOURCE_DATE_EPOCH}")" \
  build-linux \
  #

%install
export BUILDDIR="$PWD"

%golang_install

%check
# Don`t launch 'test' section: 'install-test-deps' and 'govulncheck' require internet connection.
%make BIN=bin/gosec \
  sec \
  fmt \
  vet \
  #

%files
%_bindir/gosec

%changelog
* Wed May 21 2025 Ivan Khanas <xeno@altlinux.org> 2.22.4-alt1
- First Build for Alt Linux Sisyphus.
