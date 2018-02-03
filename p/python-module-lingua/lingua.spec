%define oname lingua

%def_with python3

Name: python-module-%oname
Version: 4.13
Release: alt1.1
Summary: Translation toolset
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lingua/

# https://github.com/wichert/lingua.git
Source: %name-%version.tar
BuildArch: noarch
Patch1: %oname-%version-alt-build.patch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-polib python-module-chameleon.core
BuildPreReq: python-module-mock
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-polib python3-module-chameleon.core
BuildPreReq: python3-module-mock
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
Lingua is a package with tools to extract translateable texts from your
code, and to check existing translations. It replaces the use of the
xgettext command from gettext, or pybabel from Babel.

%package -n python3-module-%oname
Summary: Translation toolset
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Lingua is a package with tools to extract translateable texts from your
code, and to check existing translations. It replaces the use of the
xgettext command from gettext, or pybabel from Babel.

%prep
%setup
%patch1 -p1

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
%doc *.rst docs/examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.13-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.13-alt1
- Updated to upstream release 4.13

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7-alt1.git20141111.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt1.git20141111
- Version 3.7

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.git20141103
- Version 3.4
- Enabled testing

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.git20141003
- Initial build for Sisyphus

