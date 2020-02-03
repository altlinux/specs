%define oname DIRECT

Name: python3-module-%oname
Version: 1.0.1
Release: alt3

Summary: Python wrapper to the DIRECT algorithm
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/DIRECT

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-fortran libnumpy-devel libnumpy-py3-devel
BuildRequires: python3-module-numpy-testing python-tools-2to3


%description
DIRECT is a method to solve global bound constraint optimization
problems and was originally developed by D. R. Jones, C. D. Perttunen
and B. E. Stuckmann.

The DIRECT package uses the fortan implementation of DIRECT written by
Joerg.M.Gablonsky, DIRECT Version 2.0.4.

%package pickles
Summary: Pickles for DIRECT
Group: Development/Python3

%description pickles
DIRECT is a method to solve global bound constraint optimization
problems and was originally developed by D. R. Jones, C. D. Perttunen
and B. E. Stuckmann.

The DIRECT package uses the fortan implementation of DIRECT written by
Joerg.M.Gablonsky, DIRECT Version 2.0.4.

This package contains pickles for DIRECT.

%package docs
Summary: Documentation for DIRECT
Group: Development/Documentation
BuildArch: noarch

%description docs
DIRECT is a method to solve global bound constraint optimization
problems and was originally developed by D. R. Jones, C. D. Perttunen
and B. E. Stuckmann.

The DIRECT package uses the fortan implementation of DIRECT written by
Joerg.M.Gablonsky, DIRECT Version 2.0.4.

This package contains documentation for DIRECT.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%add_optflags %optflags_shared
%python3_build_debug

%make -C doc pickle
%make -C doc html

%install
%python3_install

cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc AUTHORS
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*


%changelog
* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt3
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2.1.2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Jun 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2.1.2
- Updated build dependencies

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2.1
- NMU: Use buildreq for BR.

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Fixed build

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

