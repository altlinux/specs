%define oname pycosat

%def_with check

Name: python3-module-%oname
Version: 0.6.6
Release: alt1

Summary: Bindings to picosat (a SAT solver)
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pycosat
VCS: https://github.com/conda/pycosat

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: libpicosat-devel

%if_with check
BuildRequires: python3-module-pytest
%endif

ExclusiveArch: x86_64 %ix86

%py3_provides %oname


%description
PicoSAT is a popular SAT solver written by Armin Biere in pure C. This
package provides efficient Python bindings to picosat on the C level,
i.e. when importing pycosat, the picosat solver becomes part of the
Python process itself. For ease of deployment, the picosat source
(namely picosat.c and picosat.h) is included in this project. These
files have been extracted from the picosat source (picosat-954.tar.gz).

%prep
%setup

rm -v picosat.*

# upstream only applies proper flags when build is invoked with --inplace
sed -i "s/if .--inplace. in sys.argv:/if True:/" setup.py

%build
%add_optflags -fno-strict-aliasing -DDONT_INCLUDE_PICOSAT
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE AUTHORS.md CHANGELOG.md *.rst examples
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version.dist-info
%python3_sitelibdir/%oname.cpython*.so
%python3_sitelibdir/test_pycosat.py

%changelog
* Fri May 24 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.6-alt1
- Automatically updated to 0.6.6.
- Build with check.

* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt5
- python2 disabled

* Fri Apr 12 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt4.git20140610
- Rebuild for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt3.git20140610.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt3.git20140610.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.6.1-alt3.git20140610
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2.git20140610
- Built with external PicoSAT

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20140610
- Initial build for Sisyphus

