%define mname tw2
%define oname %mname.devtools

%def_with python3

Name: python-module-%oname
Version: 2.2.0.4
Release: alt1.git20140118
Summary: The development tools for ToscaWidgets 2, a web widget toolkit
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.devtools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.devtools.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-gearbox
BuildPreReq: python-module-weberror python-module-webhelpers
BuildPreReq: python-module-docutils python-module-tw2.jquery
BuildPreReq: python-module-tw2.jqplugins.ui python-module-Pygments
BuildPreReq: python-module-decorator python-module-genshi
BuildPreReq: python-module-mako python-module-webtest
BuildPreReq: python-module-nose python-module-sieve
BuildPreReq: python-module-PasteScript
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-gearbox
BuildPreReq: python3-module-weberror python3-module-webhelpers
BuildPreReq: python3-module-docutils python3-module-tw2.jquery
BuildPreReq: python3-module-tw2.jqplugins.ui python3-module-Pygments
BuildPreReq: python3-module-decorator python3-module-genshi
BuildPreReq: python3-module-mako python3-module-webtest
BuildPreReq: python3-module-nose python3-module-sieve
BuildPreReq: python3-module-PasteScript
%endif

%py_provides %oname
%py_requires %mname tw2.core gearbox weberror webhelpers docutils genshi
%py_requires tw2.jquery tw2.jqplugins.ui pygments decorator mako
%py_requires paste.script

%description
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

tw2.devtools contains features for developers, including the widget
browser and widget library quickstart template.

%package -n python3-module-%oname
Summary: The development tools for ToscaWidgets 2, a web widget toolkit
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core gearbox weberror webhelpers docutils genshi
%py3_requires tw2.jquery tw2.jqplugins.ui pygments decorator mako
%py3_requires paste.script

%description -n python3-module-%oname
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

tw2.devtools contains features for developers, including the widget
browser and widget library quickstart template.

%prep
%setup

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
%doc *.rst examples
%python_sitelibdir/%mname/devtools
%python_sitelibdir/%mname/paste_templates
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/%mname/devtools
%python3_sitelibdir/%mname/paste_templates
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0.4-alt1.git20140118
- Initial build for Sisyphus

