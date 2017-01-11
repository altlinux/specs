%define _unpackaged_files_terminate_build 1
%define oname colorama

%def_with python3

Name: python-module-%oname
Version: 0.3.7
Release: alt1
Summary: Simple cross-platform colored terminal text in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/colorama/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tartley/colorama.git
Source0: https://pypi.python.org/packages/f0/d0/21c6449df0ca9da74859edc40208b3a57df9aca7323118c913e58d442030/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock
%endif

%py_provides %oname

%description
Makes ANSI escape character sequences for producing colored terminal
text and cursor positioning work under MS Windows.

ANSI escape character sequences have long been used to produce colored
terminal text and cursor positioning on Unix and Macs. Colorama makes
this work on Windows, too, by wrapping stdout, stripping ANSI sequences
it finds (which otherwise show up as gobbledygook in your output), and
converting them into the appropriate win32 calls to modify the state of
the terminal. On other platforms, Colorama does nothing.

Colorama also provides some shortcuts to help generate ANSI sequences
but works fine in conjunction with any other ANSI sequence generation
library, such as Termcolor.

%package -n python3-module-%oname
Summary: Simple cross-platform colored terminal text in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Makes ANSI escape character sequences for producing colored terminal
text and cursor positioning work under MS Windows.

ANSI escape character sequences have long been used to produce colored
terminal text and cursor positioning on Unix and Macs. Colorama makes
this work on Windows, too, by wrapping stdout, stripping ANSI sequences
it finds (which otherwise show up as gobbledygook in your output), and
converting them into the appropriate win32 calls to modify the state of
the terminal. On other platforms, Colorama does nothing.

Colorama also provides some shortcuts to help generate ANSI sequences
but works fine in conjunction with any other ANSI sequence generation
library, such as Termcolor.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst demos
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst demos
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.7-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.3-alt1.git20150709.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20150709
- Version 0.3.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141101
- Initial build for Sisyphus

