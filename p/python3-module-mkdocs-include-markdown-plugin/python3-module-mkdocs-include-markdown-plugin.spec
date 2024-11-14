%define pypi_name mkdocs-include-markdown-plugin
%define mod_name mkdocs_include_markdown_plugin

%def_with check

Name:    python3-module-%pypi_name
Version: 7.0.0
Release: alt1

Summary: Mkdocs Markdown includer plugin
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/mondeja/mkdocs-include-markdown-plugin

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-wcmatch
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
skips="test_page_included_by_url_is_cached"
skips="$skips or test_examples_subprocess[http-cache]"
skips="$skips or test_examples_api[http-cache]"
skips="$skips or test_include[url]"
skips="$skips or test_include_markdown[url]"
skips="$skips or test_read_url_cached_content"
%pyproject_run_pytest -k "not ($skips)"

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 7.0.0-alt1
- Initial build for Sisyphus.
