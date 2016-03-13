%define oname skimpyGimpy

%def_with python3

Name: python-module-%oname
Version: 1.4
Release: alt1.1
Summary: Skimpy Gimpy Audio/visual Tools
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/skimpyGimpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Skimpy is a tool for generating HTML visual, PNG visual, and WAVE audio
representations for strings which people can understand but which web
robots and other computer programs will have difficulty understanding.
Skimpy is an example of a Captcha: an acronym for "Completely Automated
Public Turing test to tell Computers and Humans Apart".

%package -n python3-module-%oname
Summary: Skimpy Gimpy Audio/visual Tools
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Skimpy is a tool for generating HTML visual, PNG visual, and WAVE audio
representations for strings which people can understand but which web
robots and other computer programs will have difficulty understanding.
Skimpy is an example of a Captcha: an acronym for "Completely Automated
Public Turing test to tell Computers and Humans Apart".

%prep
%setup

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

