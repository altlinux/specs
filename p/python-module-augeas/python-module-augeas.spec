%define oname augeas

%define _unpackaged_files_terminate_build 1

Name: python-module-%oname
Version: 1.0.3
Release: alt2
Summary: Python bindings to augeas
Group: Development/Python
License: LGPLv2+
Url: http://augeas.net/
Source0: %oname-%version.tar

BuildArch: noarch

BuildRequires: libaugeas python-devel python-modules-unittest rpm-build-python3

BuildRequires: python-module-setuptools python-module-cffi

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-module-cffi

Requires: libaugeas

%description
python-augeas is a set of Python bindings around augeas.

%package -n python3-module-%oname
Summary: Python bindings to augeas
Group: Development/Python3
Requires: libaugeas

%description -n python3-module-%oname
python-augeas is a set of Python bindings around augeas.

%prep
%setup -n augeas-%version

rm -rf ../python3
cp -fR . ../python3
sed -i 's|python|python3|' ../python3/test/Makefile

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
%make check

pushd ../python3
%make check
popd

%files
%doc COPYING AUTHORS README.txt
%python_sitelibdir/*

%files -n python3-module-%oname
%doc COPYING AUTHORS README.txt
%python3_sitelibdir/*


%changelog
* Wed Apr 04 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt2
- Added unpackaged files

* Mon Mar 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt1
- Version 1.0.3

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.git20140831.1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.git20140831.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt2.git20140831.1
- NMU: Use buildreq for BR.

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.git20140831
- Added requirement on libaugeas (ALT #30455)

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20140831
- Version 0.5.0
- Added module for Python 3

* Tue Aug 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt2
- rebuild for autoimports (https://bugzilla.altlinux.org/show_bug.cgi?id=27419)

* Mon Aug 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt1
- build for ALT
