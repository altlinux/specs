%define _unpackaged_files_terminate_build 1

%define oname nbclient

Name: python3-module-%oname
Version: 0.5.3
Release: alt1
Summary: A client library for executing notebooks. Formally nbconvert's ExecutePreprocessor.
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/nbclient/

BuildArch: noarch

# https://github.com/jupyter/nbclient.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(traitlets)
BuildRequires: python3(jupyter_client)
BuildRequires: python3(nbformat)
BuildRequires: python3(async_generator)
BuildRequires: python3(nest_asyncio)
BuildRequires: python3(xmltodict)
BuildRequires: python3(nbconvert)
BuildRequires: python3(ipywidgets)

%description
NBClient, a client library for programmatic notebook execution,
is a tool for running Jupyter Notebooks in different execution contexts.
NBClient was spun out of nbconvert's former ExecutePreprocessor.

NBClient lets you execute notebooks.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv

%files
%doc LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.3-alt1
- Updated to upstream version 0.5.3.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Initial build for ALT.
