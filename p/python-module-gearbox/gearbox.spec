%define _unpackaged_files_terminate_build 1
%define oname gearbox

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt2
Summary: Toolkit born as a PasteScript replacement for the TurboGears2 web framework
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/gearbox/

# https://github.com/TurboGears/gearbox.git
Source: %{oname}-%{version}.tar.gz

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-cliff python-module-tempita
BuildRequires: python-module-PasteDeploy
BuildRequires: python-module-html5lib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-cliff python3-module-tempita
BuildRequires: python3-module-PasteDeploy
BuildRequires: python3-module-html5lib
%endif

%py_provides %oname
%py_requires cliff tempita paste.deploy

%description
gearbox is a paster command replacement for TurboGears2. It has been
created during the process of providing Python3 support to the
TurboGears2 web framework, while still being backward compatible with
the existing TurboGears projects.

%if_with python3
%package -n python3-module-%oname
Summary: Toolkit born as a PasteScript replacement for the TurboGears2 web framework
Group: Development/Python3
%py3_provides %oname
%py3_requires cliff tempita paste.deploy

%description -n python3-module-%oname
gearbox is a paster command replacement for TurboGears2. It has been
created during the process of providing Python3 support to the
TurboGears2 web framework, while still being backward compatible with
the existing TurboGears projects.
%endif

%prep
%setup -q -n %{oname}-%{version}

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
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.7-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20150205
- Initial build for Sisyphus

