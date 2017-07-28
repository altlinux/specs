%def_with python3

%define modname svg.path

Name: python-module-svg-path
Version: 2.2
Release: alt2
Summary: SVG path objects and parser

Group: Development/Python
License: CC0
Url: http://pypi.python.org/pypi/svg.path

Source: %name-%version.tar
#Source-url: https://github.com/regebro/svg.path/archive/%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

Requires: python-module-svg

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-devel
%endif

%description
svg.path is a collection of objects that implement the different path
commands in SVG, and a parser for SVG path definitions.

%package tests
Summary: Tests for %name
Group: Development/Python
Requires: python-module-svg-path = %version-%release

%description tests
Tests for python-module-svg-path.

%package -n python3-module-svg-path
Summary: SVG path objects and parser
Group: Development/Python3
Requires: python3-module-svg

%description -n python3-module-svg-path
svg.path is a collection of objects that implement the different path
commands in SVG, and a parser for SVG path definitions.

%package -n python3-module-svg-path-tests
Summary: Tests for %name
Group: Development/Python3
Requires: python3-module-svg-path = %version-%release

%description -n python3-module-svg-path-tests
Tests for python3-module-svg-path.

%prep
%setup
%if_with python3
rm -fR ../python3-module-%modname
cp -fR . ../python3-module-%modname
%endif

%build
%python_build
%if_with python3
pushd ../python3-module-%modname
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3-module-%modname
%python3_install
popd
%endif
%python_install

%check
python setup.py test
%if_with python3
pushd ../python3-module-%modname
python3 setup.py test
popd
%endif

%files
%doc README.rst CHANGES.txt CONTRIBUTORS.txt
%python_sitelibdir/svg/path
%python_sitelibdir/%modname-%{version}*
%exclude %python_sitelibdir/svg/path/tests

%files tests
%python_sitelibdir/svg/path/tests

%if_with python3
%files -n python3-module-svg-path
%doc README.rst CHANGES.txt CONTRIBUTORS.txt
%python3_sitelibdir/svg/path
%python3_sitelibdir/%modname-%version-*
%exclude %python3_sitelibdir/svg/path/tests

%files -n python3-module-svg-path-tests
%python3_sitelibdir/svg/path/tests
%endif

%changelog
* Fri Jul 28 2017 Anton Midyukov <antohami@altlinux.org> 2.2-alt2
- New subpackages tests

* Wed Jul 26 2017 Anton Midyukov <antohami@altlinux.org> 2.2-alt1
- Initial build for ALT Sisyphus
