%define oname purl

%def_with check

Name: python3-module-%oname
Version: 1.6
Release: alt1

Summary: An immutable URL class for easy URL-building and manipulation
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/purl/
Vcs: https://github.com/codeinthehole/purl

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
%endif

%py3_provides %oname

%description
A simple, immutable URL class with a clean API for interrogation and
manipulation. Supports Pythons 2.7, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8 and pypy.

Also supports template URLs as per RFC 6570.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -ra -qq tests

%files
%doc AUTHORS *.rst docs/*.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info


%changelog
* Tue Mar 28 2023 Anton Vyatkin <toni@altlinux.org> 1.6-alt1
- New version 1.6.

* Sat Dec 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.git20141212.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20141212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20141212
- Initial build for Sisyphus

