%define oname traitsui

%def_without python3

Name: python-module-%oname
Version: 4.1.1
Release: alt1.git20120408
Summary: A set of user interface tools designed to complement Traits

Group: Development/Python
License: BSD, EPL and LGPL
URL: http://www.enthought.com/
# https://github.com/enthought/apptools.git
Source: %oname-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-module-setuptools python-devel
BuildPreReq: python-module-setupdocs python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setupdocs
BuildPreReq: python-tools-2to3
%endif
BuildArch: noarch

%description
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

%if_with python3
%package -n python3-module-%oname
Summary: A set of user interface tools designed to complement Traits (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

%package -n python3-module-%oname-tests
Summary: Tests for TraitsUI (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains tests for TraitsUI.
%endif

%package tests
Summary: Tests for TraitsUI
Group: Development/Python
Requires: %name = %version-%release
Conflicts: %name < %version-%release

%description tests
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains tests for TraitsUI.

%package docs
Summary: Documentation for TraitsUI
Group: Development/Documentation

%description docs
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains documentation for TraitsUI.

%package pickles
Summary: Pickles for TraitsUI
Group: Development/Python
AutoReq: nopython

%description pickles
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains pickles for TraitsUI.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i ||:
done
%python3_build_debug
popd
%endif

%make -C docs html
%make -C docs pickle

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# pickles
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html docs/*.txt docs/*.ppt docs/*.pdf docs/*.doc

%files pickles
%python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120408
- New snapshot
- Added module for Python 3

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120122
- Version 4.1.1

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2.git20111103
- Moved tests into separate package

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20111103
- Initial build for Sisyphus

