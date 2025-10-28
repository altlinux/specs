%define pypi_name codechecker
%define pypi_nname CodeChecker

%def_with check

Name: python3-module-%pypi_name
Version: 6.25.1
Release: alt3.git36a6cf62

Summary: CodeChecker static analysis tooling (without web server)
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/codechecker/
Vcs: https://github.com/Ericsson/codechecker

Source0: %name-%version.tar
Source1: fix-installation-paths.sh

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

%package -n python3-module-%pypi_name-doc
Summary: User documentation for %pypi_name
Group: Documentation
BuildArch: noarch

%description -n python3-module-%pypi_name-doc
User documentation for %pypi_name.

%prep
%setup
%SOURCE1

%build
make mkdocs_build -B
make preinstall
BUILD_LOGGER_64_BIT_ONLY=YES make build -B

%install
make preinstall
cp -ra build %buildroot

%files
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

%changelog
* Tue Oct 14 2025 Denis Rastyogin <gerben@altlinux.org> 6.25.1-alt3.git36a6cf62
- Initial build(without webserver) for ALT Sisyphus.
