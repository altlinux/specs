%define oname pyface

Name: python3-module-%oname
Version: 7.4.4
Release: alt1

Summary: Traits-capable windowing framework

License: BSD, EPL and LGPL
Group: Development/Python3
URL: https://docs.enthought.com/pyface/

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.4

BuildRequires: python3 >= 3.8
# As of Python 3.8, this functionality has been added to the Python standard library.
#py3_use importlib-metadata
#py3_use importlib-resources >= 1.1.0
%py3_use traits >= 6

# TODO: extra requires


# skip wx requirements
%add_python3_req_skip pyface.ui.wx.split_dialog pyface.ui.wx.grid.combobox_focus_handler IPython.frontend.wx.wx_frontend IPython.kernel.core.interpreter
%add_python3_req_skip traitsui.wx traitsui.wx.helper wx.html wx.lib.agw wx.lib.gridmovers wx.lib.layoutf wx.lib.mixins.grid
%add_python3_req_skip wx.lib.scrolledpanel wx.lib.wxpTag wx.py wx.py.pseudo wx.py.shell wx.py.version wx.stc wx.wx wx.xrc

%description
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

%prep
%setup
# Users of Python 3.9 and beyond should use the standard library module
subst 's|importlib_resources|importlib.resources|' pyface/resource/resource_manager.py pyface/tests/test_image_resource.py
sed -i -e 's|"importlib-resources>=1.1.0",||' -e 's|"importlib-metadata",||' pyface/__init__.py

%build
%python3_build

%install
%python3_install
%python3_prune

# not all tests are removed. remove remaining ones
rm -f \
	%buildroot%python3_sitelibdir/%oname/ui/qt4/util/gui_test_assistant.py \
	%buildroot%python3_sitelibdir/%oname/ui/qt4/util/modal_dialog_tester.py \
	%buildroot%python3_sitelibdir/%oname/ui/qt4/util/testing.py \
	%buildroot%python3_sitelibdir/%oname/util/testing.py \
	|| exit 1

%files
%doc image_LICENSE*.txt LICENSE.txt
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Dec 22 2022 Grigory Ustinov <grenka@altlinux.org> 7.4.4-alt1
- Automatically updated to 7.4.4.

* Tue Nov 15 2022 Grigory Ustinov <grenka@altlinux.org> 7.4.3-alt1
- Automatically updated to 7.4.3.

* Mon Jul 18 2022 Grigory Ustinov <grenka@altlinux.org> 7.4.2-alt1
- Automatically updated to 7.4.2.

* Fri May 20 2022 Grigory Ustinov <grenka@altlinux.org> 7.4.1-alt1
- Build new version.

* Wed Jun 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.3.0-alt1
- Updated to upstream version 7.3.0.
- Fixed runtime dependencies.

* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 7.2.0-alt1
- new version (7.2.0) with rpmgs script
- switch to build from tarball

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 6.1.2-alt2
- NMU: disable build python2 module

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

