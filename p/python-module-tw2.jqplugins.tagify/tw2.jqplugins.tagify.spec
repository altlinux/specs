%define mname tw2.jqplugins
%define oname %mname.tagify

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt1.b1.git20120306
Summary: TagBox for ToscaWidgets2
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jqplugins.tagify/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.jqplugins.tagify.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-mako
BuildPreReq: python-module-tw2.forms python-module-tw2.jqplugins.ui
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-mako
BuildPreReq: python3-module-tw2.forms python3-module-tw2.jqplugins.ui
BuildPreReq: python3-module-nose
%endif

%py_provides %oname
%py_requires %mname tw2.core mako tw2.forms tw2.jqplugins.ui

%description
Tagify for ToscaWidgets2.

%package -n python3-module-%oname
Summary: TagBox for ToscaWidgets2
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core mako tw2.forms tw2.jqplugins.ui

%description -n python3-module-%oname
Tagify for ToscaWidgets2.

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

%files
%doc docs/*.rst
%python_sitelibdir/tw2/jqplugins/tagify
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc docs/*.rst
%python3_sitelibdir/tw2/jqplugins/tagify
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1.git20120306
- Initial build for Sisyphus

