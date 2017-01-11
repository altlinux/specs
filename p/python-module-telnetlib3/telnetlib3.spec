%define _unpackaged_files_terminate_build 1
%define oname telnetlib3

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.0
Release: alt1
Summary: Telnet server and client Protocol library using asyncio
License: ISC
Group: Development/Python
Url: https://pypi.python.org/pypi/telnetlib3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jquast/telnetlib3.git
Source0: https://pypi.python.org/packages/5c/30/da58a2152561a7a6b6d49beee1bb14f292e1a3f4aab78ac1466a31909d3e/%{oname}-%{version}.tar.gz
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-pip
#BuildPreReq: python-module-pep257
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-pip
#BuildPreReq: python3-module-pep257
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-OpenSSL python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-idna python3-module-lxml python3-module-ntlm python3-module-pluggy python3-module-py python3-module-pyasn1 python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six
BuildRequires: python3-module-asyncio python3-module-html5lib python3-module-pep257 python3-module-pip python3-module-setuptools-tests rpm-build-python3

%description
telnetlib3 is a Telnet Client and Server Protocol library for python.

%package -n python3-module-%oname
Summary: Telnet server and client Protocol library using asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
telnetlib3 is a Telnet Client and Server Protocol library for python.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

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

%if_with python2
%python_install
%endif

rm -f requirements.txt

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.txt *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.git20140629.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1.git20140629.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20140629
- Initial build for Sisyphus

