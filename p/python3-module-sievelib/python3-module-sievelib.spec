%define pypi_name sievelib

Name: python3-module-%pypi_name
Version: 1.4.2
Release: alt1

Summary: Client-side Sieve and ManageSieve library written in Python

License: MIT
Group: Development/Python3
Url: https://github.com/tonioo/sievelib

# Source-url: https://github.com/tonioo/sievelib/archive/refs/tags/%version.tar.gz
Source: %pypi_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools_scm

Requires: python3-module-typing_extensions

%description
Client-side Sieve and ManageSieve library written in Python.

Sieve is a filtering language for email (RFC 5228).
ManageSieve is a protocol to remotely manage Sieve scripts (RFC 5804).

%prep
%setup -n %pypi_name-%version
# Set version for setuptools_scm
echo %version > VERSION

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pypi_name}-%version.dist-info/

%changelog
* Sun Dec 21 2025 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- initial build for ALT Sisyphus
