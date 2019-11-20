%define oname pycosat

%def_disable check

Name: python3-module-%oname
Version: 0.6.1
Release: alt5

Summary: Bindings to picosat (a SAT solver)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pycosat/
# https://github.com/ContinuumIO/pycosat.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libpicosat-devel

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

rm -f picosat.*

%build
%add_optflags -fno-strict-aliasing -DDONT_INCLUDE_PICOSAT

%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
rm -fR build
py.test-%_python3_version

%files
%doc CHANGELOG *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/test*
%exclude %python3_sitelibdir/*/test*


%changelog
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

