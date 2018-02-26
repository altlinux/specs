%define oname pyface
Name: python-module-%oname
Version: 4.1.1
Release: alt2.git20120504
Summary: Traits-capable windowing framework

Group: Development/Python
License: BSD, EPL and LGPL
URL: http://www.enthought.com/
# https://github.com/enthought/pyface.git
Source: %oname-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-module-setuptools python-devel
BuildPreReq: python-module-setupdocs python-module-sphinx-devel
BuildArch: noarch

%description
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

%package docs
Summary: Documentation for pyface
Group: Development/Documentation

%description docs
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

This package contains documentation for pyface.

%package pickles
Summary: Pickles for pyface
Group: Development/Python

%description pickles
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

This package contains pickles for pyface.

%package tests
Summary: Tests for pyface
Group: Development/Python
Requires: %name = %version-%release

%description tests
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

This package contains tests for pyface.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%make -C docs html
%make -C docs pickle

%install
%python_install

# pickles
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%files docs
%doc docs/build/html examples docs/*.txt docs/*.doc docs/*.pdf docs/*.ppt

%files pickles
%python_sitelibdir/%oname/pickle

%changelog
* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2.git20120504
- Extracted tests into separate package

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120504
- New snapshot

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120120
- Version 4.1.1

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111115
- Initial build for Sisyphus

