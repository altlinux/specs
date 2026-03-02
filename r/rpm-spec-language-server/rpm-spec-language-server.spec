%define _unpackaged_files_terminate_build 1
%define pypi_name rpm_spec_language_server

Name: rpm-spec-language-server
Version: 0.0.2
Release: alt4
Summary: Language Server for RPM spec files
License: GPL-2.0-or-later
Group: Development/Python3
Url: https://github.com/dcermak/rpm-spec-language-server
Vcs: https://github.com/dcermak/rpm-spec-language-server.git

Source: %name-%version.tar
#Source1: %pyproject_deps_config_name
Patch: %name-%version-%release.patch

BuildArch: noarch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-python3 rpm-macros-pyproject
BuildRequires: rpm-build-python3 rpm-build-pyproject
BuildRequires: python3(poetry) python3(poetry.core)
BuildRequires: python3(typeguard)
BuildRequires: python3(pygls)
BuildRequires: python3(specfile)
BuildRequires: python3(rpm)

# For tests
BuildRequires: python3(lsprotocol)

%pyproject_builddeps_build

%description
This is a server implementing the Language Server Protocol for RPM Spec files.

Supported LSP endpoints:
- autocompletion of macro names, spec sections and preamble keywords
- jump to macro definition
- expand macros on hover
- breadcrumbs/document sections

%prep
%setup
%patch -p1

# Relax poetry dependencies
sed -i 's/pygls = "^2.0"/pygls = "*"/' pyproject.toml
sed -i 's/_DEFAULT_DEPRECATED_MACRO_PROFILE = "fedora"/_DEFAULT_DEPRECATED_MACRO_PROFILE = "altlinux"/' rpm_spec_language_server/server.py

%build
%pyproject_build

%install
%pyproject_install

# TODO
#%%check
#%%pyproject_run_pytest -vra -k \
#    " \
#    not test_fetch_upstream_spec_md \
#    and not test_parse_upstream_spec_md \
#    and not test_cache_creation \
#    and not test_spec_md_fetched_from_upstream_if_not_in_rpm_package \
#    "

%files
%doc LICENSE README.rst
%_bindir/rpm_lsp_server
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Mar 02 2026 Alexey Shabalin <shaba@altlinux.org> 0.0.2-alt4
- Load macro profiles from per-distro JSON files.
- Make spec.md loading offline-first.

* Fri Feb 13 2026 Alexey Shabalin <shaba@altlinux.org> 0.0.2-alt3
- Update fixes and tests.

* Mon Jan 19 2026 Alexey Shabalin <shaba@altlinux.org> 0.0.2-alt2
- Fix errors and update tests.

* Sun Dec 21 2025 Alexey Shabalin <shaba@altlinux.org> 0.0.2-alt1
- Initial build.
