%define _unpackaged_files_terminate_build 1

%def_with python3
%def_with docs

%define oname pyface

Name: python-module-%oname
Version: 6.1.2
Release: alt1
Summary: Traits-capable windowing framework

Group: Development/Python
License: BSD, EPL and LGPL
URL: https://docs.enthought.com/pyface/
BuildArch: noarch

# https://github.com/enthought/pyface.git
Source: %name-%version.tar

Patch1: %oname-alt-docs.patch

BuildRequires: python-module-setuptools python-devel
BuildRequires: python-module-setupdocs

%if_with docs
BuildRequires(pre): python-module-sphinx-devel
BuildRequires: python2.7(traits)
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

%package tests
Summary: Tests for pyface
Group: Development/Python
Requires: %name = %EVR

%description tests
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

This package contains tests for pyface.

%if_with python3
%package -n python3-module-%oname
Summary: Traits-capable windowing framework
Group: Development/Python3
# skip wx requirements
%add_python3_req_skip pyface.ui.wx.split_dialog IPython.frontend.wx.wx_frontend IPython.kernel.core.interpreter
%add_python3_req_skip apptools.io.file
%add_python3_req_skip traitsui.wx traitsui.wx.helper wx.html wx.lib.agw wx.lib.gridmovers wx.lib.layoutf wx.lib.mixins.grid
%add_python3_req_skip wx.lib.scrolledpanel wx.lib.wxpTag wx.py wx.py.pseudo wx.py.shell wx.py.version wx.stc wx.wx wx.xrc

%description -n python3-module-%oname
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

%package -n python3-module-%oname-tests
Summary: Tests for pyface
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

This package contains tests for pyface.
%endif

%if_with docs
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
%endif

%prep
%setup
%patch1 -p1

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%if_with docs
%prepare_sphinx docs
ln -s ../objects.inv docs/source/
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%if_with docs
%make -C docs html
%make -C docs pickle
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_with docs
# pickles
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc image_LICENSE*.txt LICENSE.txt
%doc CHANGES.txt README.rst
%python_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/*/tests
%exclude %python_sitelibdir/%oname/*/*/tests
%exclude %python_sitelibdir/%oname/*/*/*/tests
%exclude %python_sitelibdir/%oname/*/testing.py*
%exclude %python_sitelibdir/%oname/*/*/*/testing.py*
%exclude %python_sitelibdir/%oname/*/*/*/gui_test_assistant.py*
%exclude %python_sitelibdir/%oname/*/*/*/modal_dialog_tester.py*

%files tests
%python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/*/tests
%python_sitelibdir/%oname/*/*/tests
%python_sitelibdir/%oname/*/*/*/tests
%python_sitelibdir/%oname/*/testing.py*
%python_sitelibdir/%oname/*/*/*/testing.py*
%python_sitelibdir/%oname/*/*/*/gui_test_assistant.py*
%python_sitelibdir/%oname/*/*/*/modal_dialog_tester.py*

%if_with docs
%files docs
%doc docs/build/html examples docs/*.txt docs/*.doc docs/*.pdf docs/*.ppt

%files pickles
%python_sitelibdir/%oname/pickle
%endif

%if_with python3
%files -n python3-module-%oname
%doc image_LICENSE*.txt LICENSE.txt
%doc CHANGES.txt README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests
%exclude %python3_sitelibdir/%oname/*/*/tests
%exclude %python3_sitelibdir/%oname/*/*/*/tests
%exclude %python3_sitelibdir/%oname/*/testing.py*
%exclude %python3_sitelibdir/%oname/*/*/testing*.py*
%exclude %python3_sitelibdir/%oname/*/*/*/testing.py*
%exclude %python3_sitelibdir/%oname/*/*/*/*/testing*.py*
%exclude %python3_sitelibdir/%oname/*/*/*/gui_test_assistant.py*
%exclude %python3_sitelibdir/%oname/*/*/*/modal_dialog_tester.py*
%exclude %python3_sitelibdir/%oname/*/*/*/*/gui_test_assistant*.py*
%exclude %python3_sitelibdir/%oname/*/*/*/*/modal_dialog_tester*.py*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/tests
%python3_sitelibdir/%oname/*/*/tests
%python3_sitelibdir/%oname/*/*/*/tests
%python3_sitelibdir/%oname/*/testing.py*
%python3_sitelibdir/%oname/*/*/testing*.py*
%python3_sitelibdir/%oname/*/*/*/testing.py*
%python3_sitelibdir/%oname/*/*/*/*/testing*.py*
%python3_sitelibdir/%oname/*/*/*/gui_test_assistant.py*
%python3_sitelibdir/%oname/*/*/*/modal_dialog_tester.py*
%python3_sitelibdir/%oname/*/*/*/*/gui_test_assistant*.py*
%python3_sitelibdir/%oname/*/*/*/*/modal_dialog_tester*.py*
%endif

%changelog
* Mon Jul 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2-alt1
- Updated to upstream version 6.1.2.
- Built modules for python-3.

* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.0-alt1
- Updated to upstream version 6.0.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt1
- automated PyPI update

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20150401
- Version 4.6.0

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20140923
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20140430
- Version 4.4.0

* Mon Oct 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130620
- Moved all tests into tests subpackage

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130620
- New snapshot

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130418
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130128
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20121010
- Version 4.2.1

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2.git20120504
- Extracted tests into separate package

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120504
- New snapshot

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120120
- Version 4.1.1

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111115
- Initial build for Sisyphus

