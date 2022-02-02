%define _unpackaged_files_terminate_build 1
%define pypi_name pyquery

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.3
Release: alt1
Summary: A jQuery-like library for python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.io/project/pyquery/

# git://git.altlinux.org/gears/p/python3-module-pyquery.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(lxml)
BuildRequires: python3(cssselect)

BuildRequires: python3(requests)
BuildRequires: python3(webtest)
BuildRequires: python3(nose)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%description
%name allows you to make jQuery queries on XML documents.  The API is as much
as possible the similar to jQuery.  %name uses lxml for fast XML and HTML
manipulation.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%changelog
* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- 1.4.1 -> 1.4.3.

* Sun Aug 16 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.1.0.5.49eb-alt1
- Packaged pyquery-1.4.1-5-g49ebccf.
