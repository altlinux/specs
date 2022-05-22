%define  modulename httpsig
%def_enable check

Name:    python3-module-%modulename
Version: 1.3.0
Release: alt1

Summary: Simple Python interface for Graphviz
License: MIT
Group:   Development/Python3
URL:     https://github.com/xflr6/httpsig

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-tox
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pycryptodome

BuildArch: noarch
Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

%description
Sign HTTP requests with secure signatures according to the IETF HTTP Signatures
specification (Draft 8). This is a fork of the original module to fully support
both RSA and HMAC schemes as well as unit test both schemes to prove they work.

%summary
Components for Joyent's HTTP Signature Scheme.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%python3_sitelibdir/%{modulename}*
%python3_sitelibdir/*.egg-info

%changelog
* Mon May 16 2022 Andrey Bergman <vkni@altlinux.org> 1.3.0-alt1
- Initial release for Sisyphus.

