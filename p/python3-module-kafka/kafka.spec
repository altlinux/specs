%define _unpackaged_files_terminate_build 1
%define oname kafka

%def_with check

Name: python3-module-%oname
Version: 1.4.6
Release: alt2
Summary: Pure Python client for Apache Kafka
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/kafka-python/

# https://github.com/dpkp/kafka-python.git
Source: %name-%version.tar.gz
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: liblz4
BuildRequires: python3(crc32c)
BuildRequires: python3(lz4)
BuildRequires: python3(mock)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(snappy)
BuildRequires: python3(tox)
BuildRequires: python3(xxhash)
%endif

%description
This module provides low-level protocol support for Apache Kafka as well
as high-level consumer and producer classes. Request batching is
supported by the protocol as well as broker-aware request routing. Gzip
and Snappy compression is also supported for message sets.

%prep
%setup
%patch -p1

# remove bundled packages, raise an error on unexpected one
rm %oname/vendor/{__init__,enum34,selectors34,six,socketpair}.py
rmdir %oname/vendor || { echo "There is a new bundled package: $(ls -A \
%oname/vendor)"; exit 1; }
grep -rlEZ \
-e 'from kafka\.vendor( import|\.)' \
-e 'import kafka\.vendor\.' | \
xargs -0 sed -i \
-e '/from kafka\.vendor import socketpair/d' \
-e 's/from kafka\.vendor import /import /g' \
-e 's/from kafka\.vendor\./from /g' \
-e 's/import kafka\.vendor\./import /g'

# check unbundling result
find -name '*.py' -print0 | xargs -0 \
grep -qsF 'kafka.vendor' && { echo "There is the usage of bundled package"; \
exit 1; }

# unpin Pytest
grep -qsF 'pytest<4.0' tox.ini || exit 1
sed -i 's/pytest<4\.0/pytest/g' tox.ini

%build
%python3_build

%install
%python3_install

# since we are packaging example.py as doc
sed -i '1{/#!/d}' example.py
chmod -x example.py

%check
sed -i -e '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' \
-e '/setenv =$/a\
    py3: _PYTEST_BIN=%_bindir\/py.test3' \
tox.ini
export PIP_NO_INDEX=YES

# set the CRC32C_SW_MODE environment variable before loading the package to
# one of the following values:
#
#  * 'auto' to use software implementation if no CPU hardware support is found.
#  * 'force' to use software implementation regardless of CPU hardware support.
#  * '1' means 'force', but will be eventually discontinued.
export CRC32C_SW_MODE=auto
export TOX_TESTENV_PASSENV='CRC32C_SW_MODE'
export TOXENV=py3
%_bindir/tox.py3 --sitepackages -vvr -- -ra

%files
%doc *.md example.py
%python3_sitelibdir/kafka/
%python3_sitelibdir/kafka_python-%version-py%_python3_version.egg-info/

%changelog
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

