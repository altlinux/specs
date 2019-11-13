%define oname canonicalize

Name: python3-module-%oname
Version: 1.3
Release: alt2

Summary: Canonicalize a cluster of records
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/canonicalize/
# https://github.com/datamade/canonicalize.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpy python3-module-affinegap

%py3_provides %oname
%py3_requires numpy affinegap


%description
Canoicalize a Cluster of Records.

%prep
%setup

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
export PYTHONPATH=$PWD
python3 tests/test_canonical.py -v

%files
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20150212.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20150212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20150212
- Initial build for Sisyphus

