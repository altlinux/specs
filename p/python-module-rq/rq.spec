%define _unpackaged_files_terminate_build 1
%define oname rq

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt1.1
Summary: Simple job queues for Python
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/rq/

# https://github.com/nvie/rq.git
Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-redis-py
BuildRequires: python-module-click
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-click
%endif

%py_provides %oname

%description
RQ is a simple, lightweight, library for creating background jobs, and
processing them.

%if_with python3
%package -n python3-module-%oname
Summary: Simple job queues for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
RQ is a simple, lightweight, library for creating background jobs, and
processing them.
%endif

%prep
%setup -n %oname-%version

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.2-alt1
- Updated to upstream version 0.9.2.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.6-alt1.git20140917.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1.git20140917.1
- NMU: Use buildreq for BR.

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20140917
- Initial build for Sisyphus

