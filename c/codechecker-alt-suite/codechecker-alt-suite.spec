%define _unpackaged_files_terminate_build 1

Name: codechecker-alt-suite
Version: 6.25.1
Release: alt3.git36a6cf62

Provides: CodeChecker-alt-suite = %EVR
Obsoletes: CodeChecker-alt-suite < %EVR

Summary: CodeChecker static analysis tooling (without web server)
License: Apache-2.0
Group: Development/Python3

Source: %name-%version.tar

ExclusiveArch: x86_64

Requires: python3-module-codechecker

%description
CodeChecker is a static analysis infrastructure built on the LLVM/Clang Static
Analyzer toolchain, replacing scan-build in a Linux development environment.

%package doc
Summary: User documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
User documentation for %name.

%prep
%setup

%install
mkdir -p %buildroot/%_sysconfdir/%name-%version
cp -ra homework*.txt %buildroot/%_sysconfdir/%name-%version

%files doc
%doc README_alt-static-analysis.md
%doc mapping-checkers-alt.md
%_sysconfdir/%name-%version/homework_clangsa_args.txt
%_sysconfdir/%name-%version/homework_clang-tidy_args.txt
%_sysconfdir/%name-%version/homework_cppcheck_args.txt
%_sysconfdir/%name-%version/homework_gcc_args.txt

%files

%changelog
* Tue Oct 14 2025 Denis Rastyogin <gerben@altlinux.org> 6.25.1-alt3.git36a6cf62
- Initial build for ALT Sisyphus.
