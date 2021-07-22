%define _unpackaged_files_terminate_build 1
%global pypi_name iso8601

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.16
Release: alt1
Summary: Simple module to parse ISO 8601 dates

Group: Development/Python3
License: MIT
Url: https://pypi.org/project/iso8601/
Source0: %name-%version.tar

BuildRequires: rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.

%prep
%setup

%build
%python3_build

%install
%python3_install

# don't ship tests
rm %buildroot%python3_sitelibdir/%pypi_name/test_iso8601.py
rm %buildroot%python3_sitelibdir/%pypi_name/__pycache__/test_iso8601.cpython*

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%changelog
* Thu Jul 22 2021 Stanislav Levin <slev@altlinux.org> 0.1.16-alt1
- 0.1.11 -> 0.1.16.
- Enabled testing.

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.11-alt1
- 0.1.11

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Lenar Shakirov <snejok@altlinux.ru> 0.1.10-alt1
- 0.1.10
- Enable python3

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.1.4-alt1
- Initial release for Sisyphus (based on Fedora)
