%define _unpackaged_files_terminate_build 1
%define oname jwt

%def_with python3

Name: python-module-%oname
Version: 1.4.2
Release: alt1
Summary: JSON Web Token implementation in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/PyJWT/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/progrium/pyjwt.gi
Source0: https://pypi.python.org/packages/8f/10/9ce7e91d8ec9d852db6f9f2b076811d9f51ed7b0360602432d95e6ea4feb/PyJWT-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
A Python implementation of JSON Web Token draft 01.

%package -n python3-module-%oname
Summary: JSON Web Token implementation in Python
Group: Development/Python3

%description -n python3-module-%oname
A Python implementation of JSON Web Token draft 01.

%prep
%setup -q -n PyJWT-%{version}

%if_with python3
cp -fR . ../python3
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

%files
%doc AUTHORS *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20150118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150118
- Version 0.4.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20140922
- Initial build for Sisyphus

