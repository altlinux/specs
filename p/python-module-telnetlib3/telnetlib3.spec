%define oname telnetlib3

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.3
Release: alt1.git20140629
Summary: Telnet server and client Protocol library using asyncio
License: ISC
Group: Development/Python
Url: https://pypi.python.org/pypi/telnetlib3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jquast/telnetlib3.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-pip
BuildPreReq: python-module-pep257
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-pip
BuildPreReq: python3-module-pep257
%endif

%py_provides %oname
%py_requires asyncio

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
%setup

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
* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20140629
- Initial build for Sisyphus

