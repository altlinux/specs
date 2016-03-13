%define oname pmw2

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt1.rc1.1
Summary: Toolkit for building high-level compound widgets
License: BSD
Group: Development/Python
Url: http://pmw.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%py_provides %oname
Conflicts: python-module-pmw
%add_python_req_skip Test

%description
Pmw (Python megawidgets) is a toolkit for building high-level compound
widgets in Python using the Tkinter module.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_findreq_skiplist %python_sitelibdir/Pmw/Pmw_2_0_0/demos/DemoVersion.py
%add_python_req_skip DemoVersion

%description tests
Pmw (Python megawidgets) is a toolkit for building high-level compound
widgets in Python using the Tkinter module.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Toolkit for building high-level compound widgets
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip Test

%description -n python3-module-%oname
Pmw (Python megawidgets) is a toolkit for building high-level compound
widgets in Python using the Tkinter module.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_findreq_skiplist %python3_sitelibdir/Pmw/Pmw_2_0_0/demos/DemoVersion.py
%add_python3_req_skip DemoVersion

%description -n python3-module-%oname-tests
Pmw (Python megawidgets) is a toolkit for building high-level compound
widgets in Python using the Tkinter module.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
for i in $(find ../python3 -type f -name '*.py'); do
	2to3 -w -n $i ||:
done
%endif

find -type f -name '*.py' -exec \
	sed -i 's|import tkinter|import Tkinter|' '{}' +

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

%files
%doc Pmw/README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/demos

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/demos

%if_with python3
%files -n python3-module-%oname
%doc Pmw/README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/demos

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/demos
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.rc1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.rc1
- Initial build for Sisyphus

