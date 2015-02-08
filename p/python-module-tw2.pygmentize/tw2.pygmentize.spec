%define mname tw2
%define oname %mname.pygmentize

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20140118
Summary: Syntax Highlighting using Pygments within a ToscaWidgets2 widget
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.pygmentize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/moschlar/tw2.pygmentize.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-mako
BuildPreReq: python-module-Pygments python-module-nose
BuildPreReq: python-module-BeautifulSoup python-module-FormEncode
BuildPreReq: python-module-webtest python-module-strainer
BuildPreReq: python-module-sieve
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-mako
BuildPreReq: python3-module-Pygments python3-module-nose
BuildPreReq: python3-module-BeautifulSoup python3-module-FormEncode
BuildPreReq: python3-module-webtest python3-module-strainer
BuildPreReq: python3-module-sieve
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core mako pygments

%description
Syntax Highlighting using Pygments within a ToscaWidgets2 widget.

%package -n python3-module-%oname
Summary: Syntax Highlighting using Pygments within a ToscaWidgets2 widget
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core mako pygments

%description -n python3-module-%oname
Syntax Highlighting using Pygments within a ToscaWidgets2 widget.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/pygmentize
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/pygmentize
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Feb 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140118
- Initial build for Sisyphus

