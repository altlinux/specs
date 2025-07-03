%define pypi_name codechecker
%define pypi_nname CodeChecker

%def_with check

Name: CodeChecker-alt-suite
Version: 6.25.1
Release: alt2.git36a6cf62

Summary: CodeChecker static analysis tooling (without web server)
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/codechecker/6.25.1/
Vcs: https://github.com/Ericsson/codechecker

Source: %name-%version.tar

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pycodestyle
BuildRequires: python3-module-pylint
BuildRequires: python3-module-mypy
BuildRequires: python3-module-coverage
BuildRequires: python3-module-mkdocs
Requires: python3-module-portalocker
Requires: python3-module-pyyaml
Requires: python3-module-lxml
Requires: python3-module-psutil
Requires: python3-module-multiprocess
Requires: python3-module-sarif-tools

# Only build logger on x86_64
ExclusiveArch: x86_64

%description
CodeChecker is a static analysis infrastructure built on the LLVM/Clang Static
Analyzer toolchain, replacing scan-build in a Linux development environment.

%package -n python3-module-%pypi_name
Summary: CodeChecker static analysis tooling (without web server)
License: Apache-2.0
Group: Development/Python3

%description -n python3-module-%pypi_name
CodeChecker is a static analysis infrastructure built on the LLVM/Clang Static
Analyzer toolchain, replacing scan-build in a Linux development environment.

%package -n python3-module-%pypi_name-doc
Summary: User documentation for %pypi_name
Group: Documentation
BuildArch: noarch

%description -n python3-module-%pypi_name-doc
User documentation for %pypi_name.

%package doc
Summary: User documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
User documentation for %name.

%prep
%setup

%build
make mkdocs_build -B
make preinstall
BUILD_LOGGER_64_BIT_ONLY=YES make build -B

%install
make preinstall
cp -ra build %buildroot
mkdir -p %buildroot/%_sysconfdir/%name-%version
cp -ra homework*.txt %buildroot/%_sysconfdir/%name-%version

%files -n python3-module-%pypi_name
%doc LICENSE.TXT CONTRIBUTING.md CODEOWNERS SECURITY.md
%_bindir/%pypi_nname
%_bindir/ldlogger
%_libdir/ldlogger.so
%python3_sitelibdir/%pypi_nname
%python3_sitelibdir/codechecker_analyzer
%python3_sitelibdir/codechecker_common
%python3_sitelibdir/bazel_compile_commands
%python3_sitelibdir/codechecker_merge_clang_extdef_mappings
%python3_sitelibdir/codechecker_statistics_collector
%python3_sitelibdir/codechecker_report_converter
%python3_sitelibdir/tu_collector

%files -n python3-module-%pypi_name-doc
%doc site

%files doc
%doc README_alt-static-analysis.md
%doc mapping-checkers-alt.md
%_sysconfdir/%name-%version/homework_clangsa_args.txt
%_sysconfdir/%name-%version/homework_clang-tidy_args.txt
%_sysconfdir/%name-%version/homework_cppcheck_args.txt
%_sysconfdir/%name-%version/homework_gcc_args.txt

%changelog
* Wed Jun 25 2025 Denis Rastyogin <gerben@altlinux.org> 6.25.1-alt2.git36a6cf62
- Improved analysis methodology.

* Tue Jun 24 2025 Denis Rastyogin <gerben@altlinux.org> 6.25.1-alt1.git36a6cf62
- Initial build(without webserver) for ALT Sisyphus.
