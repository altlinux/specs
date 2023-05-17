%define _unpackaged_files_terminate_build 1
%define pypi_name kafka-python
%define mod_name kafka

%def_with check

Name: python3-module-%mod_name
Version: 2.0.2
Release: alt2
Summary: Pure Python client for Apache Kafka
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/kafka-python/
VCS: https://github.com/dpkp/kafka-python.git

Source: %name-%version.tar
Source1: debundler.py.in
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(crc32c)
BuildRequires: python3(lz4)
BuildRequires: python3(mock)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(snappy)
BuildRequires: python3(xxhash)
%endif

%filter_from_requires /python3(kafka\.vendor\..*)/d
%py3_requires six

%py3_provides %pypi_name
Provides: python3-module-%pypi_name

%description
This module provides low-level protocol support for Apache Kafka as well
as high-level consumer and producer classes. Request batching is
supported by the protocol as well as broker-aware request routing. Gzip
and Snappy compression is also supported for message sets.

%prep
%setup
%patch -p1

VENDORED_PATH='kafka/vendor'
UNVENDORED_PATH="$VENDORED_PATH/__init__.py"
rm -r "$VENDORED_PATH"
mkdir "$VENDORED_PATH"
cp "%SOURCE1" "$UNVENDORED_PATH"
sed -i \
    -e 's/@VENDORED_ROOT@/"kafka.vendor"/' \
    -e 's/@VENDORED_FAKE_PACKAGES@/None/' \
    "$UNVENDORED_PATH"

%build
%pyproject_build

%install
%pyproject_install

# since we are packaging example.py as doc
sed -i '1{/#!/d}' example.py
chmod -x example.py

%check
%tox_check_pyproject -- -vra

%files
%doc *.md example.py
%python3_sitelibdir/kafka/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun May 14 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.2-alt2
- (NMU) Added missing provide.

* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 1.4.6 -> 2.0.2.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 1.4.6-alt2
- Stopped Python2 package build.

* Mon Sep 02 2019 Ivan A. Melnikov <iv@altlinux.org> 1.4.6-alt1
- 1.4.6
- Fixed build on mipsel.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.4.4-alt3
- Fixed testing against Pytest 5.

* Mon Jun 03 2019 Stanislav Levin <slev@altlinux.org> 1.4.4-alt2
- Allowed testing against Pytest4.x.

* Sat Feb 16 2019 Stanislav Levin <slev@altlinux.org> 1.4.4-alt1
- 1.3.3 -> 1.4.4.
- Dropped dependency on sphinxcontrib.napoleon.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Nov 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.dev.git20150219.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.dev.git20150219.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1.dev.git20150219.1
- NMU: Use buildreq for BR.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.dev.git20150219
- Version 0.9.4-dev
- Added docs

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.dev.git20150102
- Initial build for Sisyphus

