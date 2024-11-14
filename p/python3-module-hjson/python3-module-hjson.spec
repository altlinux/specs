%define pypi_name hjson

%def_with check

Name:    python3-module-%pypi_name
Version: 3.0.2
Release: alt1

Summary: Hjson for Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/hjson/hjson-py

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
sed -i 's/from UserDict import DictMixin/from collections import MutableMapping as DictMixin/' hjson/ordered_dict.py
sed -i 's/python/python3/' bin/hjson
find . -name '*.py' -o -name 'cxxtestgen' | xargs sed -i \
    -e '1 s:#!%_bindir/env python$:#!%_bindir/python3:' \
    -e '1 s:#! %_bindir/env python$:#! %_bindir/python3:' \
    %nil

%build
%pyproject_build

%install
%pyproject_install
rm -f %buildroot%_bindir/%pypi_name.cmd
rm -fr %buildroot%python3_sitelibdir/%pypi_name/tests

%check
rm -f hjson/tests/test_tool.py
%pyproject_run_unittest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus.
