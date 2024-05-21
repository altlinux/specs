
Name: ansible-compat
Version: 24.5.1
Release: alt1
Summary: Ansible python helper functions

Url: https://github.com/ansible/ansible-compat
Source: %name-%version.tar
License: MIT
Group: Development/Python3
BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: python3-module-setuptools >= 65.3.0 python3-module-setuptools_scm >= 7.0.5
BuildRequires: python3-module-wheel python3-module-tox python3-module-pip
BuildRequires: %pyproject_buildrequires

# for tests
BuildRequires: python3-module-flaky python3-module-pytest python3-module-pytest-mock
BuildRequires: ansible-core python3-module-yaml
BuildRequires: python3-module-subprocess-tee >= 0.4.1 python3-module-jsonschema >= 4.6.0 
BuildRequires: /proc

%description
A python package containing functions that help interacting with
various versions of Ansible

%package -n python3-module-%name
Summary: %summary
Group: Development/Python3
Provides: %name = %EVR

%description -n python3-module-%name
A python package containing functions that help interacting with
various versions of Ansible

%prep
%setup
echo "ref-names: tag: v%version" >> .git_archival.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -k \
 " \
 not test_prepare_environment_with_collections \
 and not test_prerun_reqs_v1 \
 and not test_prerun_reqs_v2 \
 and not test_install_collection_from_disk \
 and not test_require_collection \
 and not test_install_collection_git \
 and not test_runtime_scan_path \
 "

%files -n python3-module-%name
%doc LICENSE
%python3_sitelibdir/*

%changelog
* Tue May 21 2024 Alexey Shabalin <shaba@altlinux.org> 24.5.1-alt1
- New version 24.5.1.

* Tue Jan 30 2024 Alexey Shabalin <shaba@altlinux.org> 4.1.11-alt1
- Initial build.
