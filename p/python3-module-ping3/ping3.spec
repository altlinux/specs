%define _unpackaged_files_terminate_build 1
%define pypi_name ping3
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 5.1.6
Release: alt1
Summary: Pure Python3 version of ICMP ping, shipped with command-line command.
License: MIT
Group: Development/Python3
Vcs: http://pypi.org/project/ping3/
Url: https://github.com/kyan001/ping3

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
#These tests require network
%tox_check_pyproject -- -vra --ignore=tests/test_benchmark.py \
-k "not test_ping and not test_command_line" || :

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 27 2026 Pavel Shilov <zerospirit@altlinux.org> 5.1.6-alt1
- updated from 4.0.4 to 5.1.6

* Wed Jul 23 2025 Pavel Shilov <zerospirit@altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus.
