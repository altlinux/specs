%define oname crypto

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.1.3
Release: alt1.git20150101.1.1
Summary: Simple symmetric GPG file encryption and decryption
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/crypto/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/chrissimpkins/crypto.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools /dev/pts /proc
BuildPreReq: python-module-Naked python-module-nose
BuildPreReq: python-module-pexpect python-module-yaml
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Naked python3-module-nose
BuildPreReq: python3-module-pexpect python3-module-yaml
%endif

%py_provides %oname
%py_requires Naked

%description
crypto provides a simple interface to symmetric Gnu Privacy Guard (gpg)
encryption and decryption for one or more files on Unix and Linux
platforms. It runs on top of gpg and requires a gpg install on your
system. Encryption is performed with the AES256 cipher algorithm.

%package -n python3-module-%oname
Summary: Simple symmetric GPG file encryption and decryption
Group: Development/Python3
%py3_provides %oname
%py3_requires Naked

%description -n python3-module-%oname
crypto provides a simple interface to symmetric Gnu Privacy Guard (gpg)
encryption and decryption for one or more files on Unix and Linux
platforms. It runs on top of gpg and requires a gpg install on your
system. Encryption is performed with the AES256 cipher algorithm.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test
pushd tests
./test.sh all
popd
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 setup.py test
pushd tests
sed -i 's|nosetests|nosetests3|' test.sh
sed -i 's|%oname|%oname.py3|' test_single-file.py
./test.sh all
popd
popd
%endif

%files
%doc *.md docs/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
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

