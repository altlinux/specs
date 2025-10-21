%define _unpackaged_files_terminate_build 1
%define pypi_name klaus

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.1
Release: alt1

Summary: The first Git web viewer that Just Works
License: ISC
Group: Development/Python3
Url: https://pypi.org/project/klaus/
Vcs: https://github.com/jonashaag/klaus

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

# for python without distutils
%filter_from_requires /python3(distutils.*)/d
Requires: python3(setuptools._distutils)

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

ExclusiveArch: x86_64

%description
%summary.
- Super easy to set up -- no configuration required;
- Syntax highlighting;
- Markdown + RestructuredText rendering support;
- Pull + push support (Git Smart HTTP);
- Code navigation using Exuberant ctags.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test_requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%files
%doc README.* LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 17 2025 Denis Rastyogin <gerben@altlinux.org> 3.0.1-alt1
- Initial build for ALT Sisyphus.
