%define _unpackaged_files_terminate_build 1
%define pypi_name fastcore
%define mod_name fastcore

Name: python3-module-%pypi_name
Version: 1.8.0
Release: alt1

Summary: Library that uses customization flexibility to add features to Python

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/fastcore/
VCS: https://github.com/AnswerDotAI/fastcore/

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Fastcore is an utility library created as a part of the fastai ecosystem.
It provides advanced Python capabilities, enhanced classes, decorators,
collection utilities, types, and metaprogramming.

%prep
%setup

# force setting our version to workaround weird upstream versioning
sed -i '/^version = /s/.*/version = %version/' settings.ini
echo '__version__ = "%version"' > fastcore/__init__.py

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/py2pyi
%_bindir/replace_wildcards
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 02 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.8.0-alt1
- Update to 1.8.0.

* Tue Feb 18 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.7.29-alt1
- Initial Build for Sisyphus.
