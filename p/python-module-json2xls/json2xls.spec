%define _unpackaged_files_terminate_build 1
%define oname json2xls

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.3c
Release: alt1
Summary: Generate excel by json
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/json2xls/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/axiaoxin/json2xls.git
Source0: https://pypi.python.org/packages/b5/15/d42f0e21acd8b6d14ae40be08ca50b32c2b3d97b1b7207575c2629a2e5db/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-requests python-module-click
#BuildPreReq: python-module-xlwt
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests python3-module-click
#BuildPreReq: python3-module-xlwt-future
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires json requests click xlwt

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-enum34 python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-setuptools python-module-urllib3 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-enum34 python3-module-future python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-setuptools python3-module-urllib3
BuildRequires: python-module-click python-module-pytest python-module-requests python-module-xlwt python3-module-click python3-module-pytest python3-module-requests python3-module-xlwt rpm-build-python3 time

%description
json2xls: Generate Excel by JSON data.

%package -n python3-module-%oname
Summary: Generate excel by json
Group: Development/Python3
%py3_provides %oname
%py3_requires json requests click xlwt

%description -n python3-module-%oname
json2xls: Generate Excel by JSON data.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
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
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3c-alt1
- automated PyPI update

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2.git20150116
- NMU: rebuild with xlwt

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150116.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150116
- Initial build for Sisyphus

