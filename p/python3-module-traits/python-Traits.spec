%define  oname traits
%def_with doc

Name:    python3-module-%oname
Version: 6.4.1
Release: alt1

Summary: Observable typed attributes for Python classes

License: BSD-3-Clause and CC-BY-3.0
Group:   Development/Python3
URL:     https://pypi.org/project/traits/

# https://github.com/enthought/traits.git
Source:  %name-%version.tar

BuildRequires(pre): python3-module-sphinx-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pygments
%if_with doc
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinx-pickles
BuildRequires: python3-module-sphinx-copybutton
%endif

%description
The traits package developed by Enthought provides a special type
definition called a trait. Although they can be used as normal Python object
attributes, traits also have several additional characteristics:

* Initialization: A trait can be assigned a default value.
* Validation: A trait attribute's type can be explicitly declared.
* Delegation: The value of a trait attribute can be contained either
  in another object.
* Notification: Setting the value of a trait attribute can trigger
  notification of other parts of the program.
* Visualization: User interfaces that permit the interactive
  modification of a trait's value can be automatically constructed
  using the trait's definition.

%package tests
Summary: Tests for Traits, explicitly typed attributes for Python 3
Group: Development/Python3
Requires: %name = %EVR

%description tests
The traits package developed by Enthought provides a special type
definition called a trait. This package contains tests for it.

%package doc
Summary: Documentation for Traits, explicitly typed attributes for Python
Group: Development/Documentation
BuildArch: noarch

%description doc
The traits package developed by Enthought provides a special type
definition called a trait. This package contains development
documentation for it.

%package pickles
Summary: Pickles for Traits, explicitly typed attributes for Python
Group: Development/Python3

%description pickles
The traits package developed by Enthought provides a special type
definition called a trait. This package contains pickles for it.

%prep
%setup

%if_with doc
%prepare_sphinx3 docs
%endif

%build
%pyproject_build

%install
%pyproject_install

%if_with doc
# pickles
install -d %buildroot%python3_sitelibdir/%oname
export PYTHONPATH=%buildroot%python3_sitelibdir
make -C docs html
%generate_pickles3 docs/source docs/source %oname
cp -fR pickle %buildroot%python3_sitelibdir/%oname/
%endif

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%doc README.rst LICENSE.txt LICENSE-CC-BY-3.0.txt
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests
%exclude %python3_sitelibdir/%oname/testing
%if_with doc
%exclude %python3_sitelibdir/%oname/pickle
%endif

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/tests
%python3_sitelibdir/%oname/testing

%if_with doc
%files doc
%doc image_LICENSE*.txt LICENSE.txt LICENSE-CC-BY-3.0.txt
%doc examples
%doc docs/build/html

%files pickles
%python3_sitelibdir/%oname/pickle
%endif

%changelog
* Mon Dec 19 2022 Anton Vyatkin <toni@altlinux.org> 6.4.1-alt1
- new version 6.4.1

* Wed Feb 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt4
- Updated build dependencies.

* Sun Jul 18 2021 Michael Shigorin <mike@altlinux.org> 6.2.0-alt3
- Fixed doc knob (overlooked %%exclude).

* Sun Jul 18 2021 Michael Shigorin <mike@altlinux.org> 6.2.0-alt2
- Added doc knob (on by default).

* Tue Jun 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt1
- Updated to upstream version 6.2.0.
- Updated license.

* Wed Sep 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.1-alt1
- Updated to upstream version 6.1.1.

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 5.1.2-alt2
- NMU: build without python2

* Fri Jul 19 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.2-alt1
- Updated to upstream version 5.1.2.
- Built modules for python-3.

* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.0-alt2
- Updated to upstream release version 4.6.0.

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20150320
- New snapshot

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20150224
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20141007
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20140507
- Version 4.6.0

* Mon Oct 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt3.git20131024
- Moved all tests into tests subpackage

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131024
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130329
- Rebuilt with updated NumPy

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130329
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130102
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20120905
- Version 4.2.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120331
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1.git20111221.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20111221
- Version 4.1.1

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20110914
- Version 4.0.1

* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt1.svn20110127.2
- Rebuild with Python-2.7

* Fri Oct 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.svn20110127.1
- Rebuilt with updated NumPy

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.svn20110127
- Version 3.6.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.svn20101105.2
- Rebuilt with python-module-sphinx-devel

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.svn20101105.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.svn20101105
- Version 3.5.1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20100714
- Version 3.4.1

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20100225
- Version 3.3.1
- Extracted tests into separate package
- Added pickles package

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090929.3
- Rebuilt with new NumPy

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090929.2
- Rebuilt with python 2.6

* Mon Oct 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090929.1
- Extracted documentation into separate package

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090929
- Version 3.2.1

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-2
- Fixed missing setupdocs BR

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-1
- Updated

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.2-2
- Fixed permissions for ctraits.so and _speedups.so
- Fixed license after confirming from upstream

* Sun Dec 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.2-1
- Initial package
