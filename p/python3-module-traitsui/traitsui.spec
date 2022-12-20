%define _unpackaged_files_terminate_build 1

%define oname traitsui

%def_disable bootstrap

Name: python3-module-%oname
Version: 7.4.2
Release: alt1
Summary: A set of user interface tools designed to complement Traits
Group: Development/Python3
License: EPL-1.0 and LGPL-2.1 and LGPL-3.0 and BSD-3-Clause
URL: https://docs.enthought.com/traitsui

# https://github.com/enthought/traitsui.git
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel

%if_disabled bootstrap
BuildRequires(pre): python3-module-sphinx-devel
BuildRequires: python3-module-traits
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinx-copybutton
%endif

# skip wx requirements
%add_python3_req_skip pyface.ui.wx.grid.api
%add_python3_req_skip pyface.ui.wx.grid.trait_grid_cell_adapter
%add_python3_req_skip pyface.ui.wx.image_list
%add_python3_req_skip pyface.ui.wx.progress_dialog
%add_python3_req_skip pyface.wx.dialog
%add_python3_req_skip pyface.wx.drag_and_drop
%add_python3_req_skip wx.animate wx.calendar wx.combo wx.gizmos
%add_python3_req_skip wx.grid wx.html wx.lib.masked wx.lib.mixins.listctrl
%add_python3_req_skip wx.lib.scrolledpanel wx.stc wx.wizard
%add_python3_req_skip pyface.wx.python_stc wx.adv

%description
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

%package tests
Summary: Tests for TraitsUI
Group: Development/Python3
Requires: %name = %EVR

%description tests
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains tests for TraitsUI.

%package examples
Summary: Examples for TraitsUI
Group: Development/Python3
Requires: %name = %EVR

%description examples
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains examples for TraitsUI.

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
Group: Development/Python3
AutoReq: nopython3

%description pickles
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains pickles for TraitsUI.

%prep
%setup

%build
%pyproject_build

%if_disabled bootstrap
%make -C docs html
%make -C docs pickle
%endif

%install
%pyproject_install

%if_disabled bootstrap
# pickles
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%files
%doc image_LICENSE*.txt LICENSE.txt README.rst CHANGES.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/%oname/examples
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests
%exclude %python3_sitelibdir/%oname/testing
%if_disabled bootstrap
%exclude %python3_sitelibdir/%oname/pickle
%endif

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/tests
%python3_sitelibdir/%oname/testing

%files examples
%python3_sitelibdir/%oname/examples

%if_disabled bootstrap
%files docs
%doc image_LICENSE*.txt LICENSE.txt
%doc docs/build/html docs/*.txt docs/*.ppt docs/*.pdf

%files pickles
%python3_sitelibdir/%oname/pickle
%endif

%changelog
* Mon Dec 19 2022 Anton Vyatkin <toni@altlinux.org> 7.4.2-alt1
- new version 7.4.2

* Sat Feb 05 2022 Grigory Ustinov <grenka@altlinux.org> 7.2.1-alt5
- Disable bootstrap.

* Sat Dec 25 2021 Grigory Ustinov <grenka@altlinux.org> 7.2.1-alt4
- Bootstrap for python3.10.

* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 7.2.1-alt3
- NMU: fixed BuildRequires.

* Tue Jul 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.2.1-alt2
- Added NoneType comparison behaviour similar to python-2 (Closes: #40382).

* Tue Jun 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.2.1-alt1
- Updated to upstream version 7.2.1.
- Updated license.

* Wed Sep 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 7.0.1-alt1
- Updated to upstream version 7.0.1.

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 6.1.1-alt2
- NMU: build without python2

* Fri Jul 19 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.1-alt1
- Updated to upstream version 6.1.1.
- Built modules for python-3.

* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.0-alt1
- Updated to upstream version 6.0.0.

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20150224
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140911
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140110
- Version 4.5.0

* Mon Oct 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131022
- Moved all tests into tests subpackage

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20131022
- New snapshot

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130413
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130108
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20121009
- Version 4.2.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120408
- New snapshot
- Added module for Python 3

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120122
- Version 4.1.1

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2.git20111103
- Moved tests into separate package

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20111103
- Initial build for Sisyphus

