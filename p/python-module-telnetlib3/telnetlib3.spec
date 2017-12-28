%define _unpackaged_files_terminate_build 1
%define oname telnetlib3

%def_without python2
%def_with python3
%def_enable check

Name: python-module-%oname
Version: 1.0.0
Release: alt1
Summary: Telnet server and client Protocol library using asyncio
License: ISC
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/telnetlib3/

# https://github.com/jquast/telnetlib3.git
Source: %name-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python2.7(asyncio)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3(asyncio)
BuildRequires: python3-module-html5lib
%endif

%py_provides %oname
%py_requires asyncio

%description
telnetlib3 is a Telnet Client and Server Protocol library for python.

%if_with python3
%package -n python3-module-%oname
Summary: Telnet server and client Protocol library using asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
telnetlib3 is a Telnet Client and Server Protocol library for python.
%endif

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
%doc LICENSE.txt *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc LICENSE.txt *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.git20140629.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1.git20140629.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20140629
- Initial build for Sisyphus

