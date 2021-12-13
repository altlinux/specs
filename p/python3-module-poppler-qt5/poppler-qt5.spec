%define oname python-poppler-qt5
%def_without check

Name: python3-module-poppler-qt5
Version: 21.1.0
Release: alt2

Summary: A Python binding to Poppler-Qt5

License: LGPLv2.1+
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-poppler-qt5/

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

# https://github.com/frescobaldi/python-poppler-qt5/issues/43
Patch1: poppler-qt5-fix.patch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

BuildRequires: gcc-c++ qt5-base-devel libpoppler-qt5-devel
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sip6 python3-module-PyQt5-devel python3-module-PyQt-builder

%description
A Python binding for libpoppler-qt5 that aims for completeness and for
being actively maintained.

%prep
%setup
%patch1 -p1

%build
export PATH=$PATH:%_qt5_bindir
sip-build --verbose --no-make \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%optflags"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%optflags"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{?__global_ldflags}"'
%make_build -C build

%install
export PATH=$PATH:%_qt5_bindir
%makeinstall_std INSTALL_ROOT=%buildroot -C build
chmod +x %buildroot/%python3_sitelibdir/*.so

%check
%__python3 setup.py test

%files
%doc ChangeLog TODO *.rst
%python3_sitelibdir/popplerqt5*.so
%python3_sitelibdir/python_poppler*
%dir %python3_sitelibdir/PyQt5/bindings/
%python3_sitelibdir/PyQt5/bindings/popplerqt5/

%changelog
* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 21.1.0-alt2
- rebuild with sip6

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 21.1.0-alt1
- new version (21.1.0) with rpmgs script
- build from pypi tarball, build with sip5 (thanks, Fedora!)

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.24.2-alt2
- Building for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.24.2-alt1.git20170214.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.24.2-alt1.git20170214.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Oct 14 2017 Fr. Br. George <george@altlinux.ru> 0.24.2-alt1.git20170214.1
- Merge upstream updates

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24.1-alt1.git20150224.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.1-alt1.git20150224
- Initial build for Sisyphus

