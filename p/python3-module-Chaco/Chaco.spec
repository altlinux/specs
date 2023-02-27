%define _unpackaged_files_terminate_build 1
%define pypi_name chaco
%define mod_name %pypi_name

Name: python3-module-Chaco
Version: 5.1.1
Release: alt2

Summary: Interactive 2-Dimensional Plotting
License: BSD and GPLv2
Group: Development/Python3
URL: http://docs.enthought.com/chaco/
VCS: https://github.com/enthought/chaco
Source: %name-%version.tar

# well-known PyPI name
Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(cython)
BuildRequires: libnumpy-py3-devel

%description
Chaco is a Python plotting application toolkit that facilitates writing
plotting applications at all levels of complexity, from simple scripts with
hard-coded data to large plotting programs with complex data interrelationships
and a multitude of interactive tools. While Chaco generates attractive static
plots for publication and presentation, it also works well for interactive data
visualization and exploration.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%files
%doc CHANGES.txt
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/example*
%exclude %python3_sitelibdir/%mod_name/tests/
%exclude %python3_sitelibdir/%mod_name/*/tests/
%exclude %python3_sitelibdir/%mod_name/*/*/tests/

%changelog
* Mon Feb 27 2023 Stanislav Levin <slev@altlinux.org> 5.1.1-alt2
- Fixed FTBFS (setuptools 67.3.0).

* Fri Jan 27 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt1
- Automatically updated to 5.1.1.

* Thu Nov 03 2022 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.

* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Build new version.

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.0.0.91.git22972069-alt2
- Fixed build with new traits.

* Mon Feb 08 2021 Grigory Ustinov <grenka@altlinux.org> 4.8.0.0.91.git22972069-alt1
- Build from last commit for python3.9.

* Tue Dec 01 2020 Vitaly Lipatov <lav@altlinux.ru> 4.8.0-alt3
- NMU: drop tests packing

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.0-alt2
- Fixed build with numpy.

* Wed Dec 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.8.0-alt1
- porting on python3

* Mon May 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.dev.git20150427
- New snapshot

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.dev.git20141105
- Version 4.6.0-dev

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20141029
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140415
- Version 4.5.0

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131020
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130422
- Rebuilt with updated NumPy

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130422
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130128
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20120925
- Version 4.2.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120508
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1.git20120119.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120119
- Version 4.1.1

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.git20111107
- Version 4.1.0

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt1.svn20110127.2
- Rebuild with Python-2.7

* Mon Oct 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127.1
- Rebuilt with updated NumPy

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127
- Version 3.4.1

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101120.2
- Rebuilt with NumPy 2.0.0-alt2.git20110405.4

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101120.1
- Rebuilt for debuginfo

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101120
- Version 3.3.3

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1.svn20100706
- Version 3.3.2

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20091001.1
- Rebuilt with python 2.6

* Wed Oct 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20091001
- Initial build for Sisyphus

