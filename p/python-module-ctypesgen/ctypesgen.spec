%define _unpackaged_files_terminate_build 1
%define oname ctypesgen

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.r125
Release: alt1.1
Summary: Python wrapper generator for ctypes
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ctypesgen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davidjamesca/ctypesgen.git
Source0: https://pypi.python.org/packages/b8/9d/13bcf53a190d2a5b3512d3c116920b4a2fadf007600722114b1a17602524/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
BuildPreReq: python-modules-json python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires json logging

%description
ctypesgen is a pure-python ctypes wrapper generator. It can also
output JSON, which can be used with Mork, which generates bindings for
Lua, using the alien module (which binds libffi to Lua).

%if_with python3
%package -n python3-module-%oname
Summary: Python wrapper generator for ctypes
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
ctypesgen is a pure-python ctypes wrapper generator. It can also
output JSON, which can be used with Mork, which generates bindings for
Lua, using the alien module (which binds libffi to Lua).
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
	mv $i ${i}3
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
%doc PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.r125-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.r125-alt1
- automated PyPI update

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.r151-alt1.git20130821
- Initial build for Sisyphus

