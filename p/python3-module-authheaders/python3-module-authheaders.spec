%define _unpackaged_files_terminate_build 1
%define pypi_name authheaders

%def_with check

Name: python3-module-%pypi_name
Version: 0.15.3
Release: alt1

Summary: library for the generation of email authentication headers
License: MIT and ZPL-2.1 and MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/authheaders
Vcs: https://github.com/ValiMail/authentication-headers
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: publicsuffix-list
%if_with check
%pyproject_builddeps_metadata
%endif

%description
This is a Python library for the generation of email authentication headers.

%prep
%setup

# Remove bundled publicsuffix data
rm -f %pypi_name/public_suffix_list.txt
# Use public suffix data from installed RPM
cp %_datadir/publicsuffix/public_suffix_list.dat %pypi_name/public_suffix_list.txt

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run -- %__python3 %pypi_name/test/test_authentication.py -v

%files
%doc README.*
%_bindir/dmarc-policy-find
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 20 2023 Anton Vyatkin <toni@altlinux.org> 0.15.3-alt1
- New version 0.15.3.

* Thu Sep 07 2023 Anton Vyatkin <toni@altlinux.org> 0.15.2-alt1
- Initial build for Sisyphus
