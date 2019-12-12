%define oname crypto

%def_disable check

Name: python3-module-%oname
Version: 1.1.3
Release: alt2

Summary: Simple symmetric GPG file encryption and decryption
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/crypto/
BuildArch: noarch

# https://github.com/chrissimpkins/crypto.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  /dev/pts /proc
BuildRequires: python3-module-Naked python3-module-nose
BuildRequires: python3-module-pexpect python3-module-yaml

%py3_provides %oname
%py3_requires Naked


%description
crypto provides a simple interface to symmetric Gnu Privacy Guard (gpg)
encryption and decryption for one or more files on Unix and Linux
platforms. It runs on top of gpg and requires a gpg install on your
system. Encryption is performed with the AES256 cipher algorithm.

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
%__python3 setup.py test
pushd tests
sed -i 's|nosetests|nosetests3|' test.sh
sed -i 's|%oname|%oname.py3|' test_single-file.py
./test.sh all
popd

%files
%doc *.md docs/*
%_bindir/*
%python3_sitelibdir/*


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.3-alt2
- build for python disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1.git20150101.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt1.git20150101.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20150101
- Version 1.1.3

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141231
- Version 1.1.2

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20141124
- Version 1.0.3

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20141122
- Version 1.0.2

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20141119
- Initial build for Sisyphus

