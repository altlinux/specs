%define oname pyev

Name: python3-module-%oname
Version: 0.9.0
Release: alt3

Summary: Python libev interface
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyev/

Source: %name-%version.tar
Patch: python3.9.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: libev-devel


%description
Python libev interface.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python libev interface.

This package contains documentation for %oname.

%prep
%setup
%patch -p1

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*

%files docs
%doc doc/*


%changelog
* Mon Jan 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt3
- Fixed build with python3.9.

* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

