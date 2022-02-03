%define _unpackaged_files_terminate_build 1
%define oname factory_boy

%def_with check

Name: python3-module-%oname
Version: 3.2.1
Release: alt1

Summary: A test fixtures replacement for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/factory-boy/
BuildArch: noarch

# https://github.com/FactoryBoy/factory_boy.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(faker)

BuildRequires: python3(django)
BuildRequires: python3(sqlalchemy)
BuildRequires: python3(django.db.backends.sqlite3)
BuildRequires: python3(tox)
%endif

# PEP503 name
Provides: python3-module-factory-boy = %EVR
%py3_provides factory-boy

%description
factory_boy is a fixtures replacement based on thoughtbot's
factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to
maintain fixtures with easy-to-use factories for complex object.

%prep
%setup
%autopatch -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
# mongoengine is not packaged in Sisyphus
export SKIP_MONGOENGINE=1
export TOX_TESTENV_PASSENV='SKIP_MONGOENGINE'
tox.py3 --sitepackages -vvr -s false

%files
%doc *.rst
%python3_sitelibdir/factory/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1
- 2.4.1 -> 3.2.1.

* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.4.1-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.4.1-alt1.git20140903.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.1-alt1.git20140903.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.1-alt1.git20140903.1
- NMU: Use buildreq for BR.

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.git20140903
- Initial build for Sisyphus

