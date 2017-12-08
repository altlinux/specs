%define _unpackaged_files_terminate_build 1
%define oname chevron

%def_with python3

Name: python-module-%oname
Version: 0.11.1
Release: alt1
Summary: Mustache templating language renderer
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/chevron/

Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
A python implementation of the mustache templating language.

%package -n python3-module-%oname
Summary: Mustache templating language renderer
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A python implementation of the mustache templating language.

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

%files
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Dec 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.1-alt1
- Updated to upstream version 0.11.1.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1
- Version 0.8.4

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1
- Version 0.7.6

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

