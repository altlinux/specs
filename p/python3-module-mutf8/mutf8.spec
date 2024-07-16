%define pypi_name mutf8

%def_with check

Name:    python3-module-%pypi_name
Version: 1.0.6
Release: alt1

Summary: Pure-python and optional C encoders/decoders for MUTF-8/CESU-8

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/mutf8
VCS:     https://github.com/TkTech/mutf8

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

Source: %name-%version.tar

%description
This package contains simple pure-python as well as C encoders and decoders for
the MUTF-8 character encoding. In most cases, you can also parse the even-rarer
CESU-8.

These days, you'll most likely encounter MUTF-8 when working on files
or protocols related to the JVM. Strings in a Java .class file are encoded using
MUTF-8, strings passed by the JNI, as well as strings exported by the object
serializer.

This library was extracted from Lawu, a Python library for working with JVM
class files.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -vra

%files
%doc LICENCE *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 16 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus.
