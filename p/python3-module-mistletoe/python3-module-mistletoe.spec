%define _unpackaged_files_terminate_build 1
%define pypi_name mistletoe
%define mod_name mistletoe

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.1
Release: alt1

Summary: A fast, extensible and spec-compliant Markdown parser in pure Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mistletoe/
Vcs: https://github.com/miyuchina/mistletoe

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
mistletoe is a Markdown parser in pure Python, designed to be fast,
spec-compliant and fully customizable.

Apart from being the fastest CommonMark-compliant Markdown parser
implementation in pure Python, mistletoe also supports easy definitions
of custom tokens. Parsing Markdown into an abstract syntax tree also
allows us to swap out renderers for different output formats, without
touching any of the core components.

Remember to spell mistletoe in lowercase!

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
cat requirements.txt test-requirements.txt > full-requirements.txt
%pyproject_deps_resync_check_pipreqfile full-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%_bindir/mistletoe
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 1.5.1-alt1
- Updated to 1.5.1.

* Thu Oct 30 2025 Anton Zhukharev <ancieg@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Tue Sep 24 2024 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Mon Feb 12 2024 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Fri Aug 25 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1.

* Tue Aug 22 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- initial build for Sisyphus
