%define mname tw2
%define oname %mname.polymaps

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt2.git20131130
Summary: Python encapsulation of the polymaps javascript library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.polymaps/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.polymaps.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-mako
BuildPreReq: python-module-geojson python-module-markupsafe
BuildPreReq: python-module-nose python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-mako
BuildPreReq: python3-module-geojson python3-module-markupsafe
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core mako geojson markupsafe json

%description
toscawidgets2 wrapper for polymaps - amazing javascript maps.

%package -n python3-module-%oname
Summary: Python encapsulation of the polymaps javascript library
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core mako geojson markupsafe json

%description -n python3-module-%oname
toscawidgets2 wrapper for polymaps - amazing javascript maps.

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

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%check
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/polymaps
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/polymaps
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2.git20131130
- Applied repocop's python-module-tw2.polymaps-0.4-alt1.git20131130.diff

* Sun Feb 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20131130
- Initial build for Sisyphus

