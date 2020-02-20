%define oname poppler-qt5

Name: python3-module-%oname
Version: 0.24.2
Release: alt2

Summary: A Python binding to Poppler-Qt5
License: LGPLv2.1+
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-poppler-qt5/

# https://github.com/wbsoft/python-poppler-qt5.git
# tag: v0.24.2
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ qt5-base-devel libpoppler-qt5-devel
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sip-devel python3-module-PyQt5-devel


%description
A Python binding for libpoppler-qt5 that aims for completeness and for
being actively maintained.

%prep
%setup

%build
export PATH=$PATH:%_qt5_bindir
%python3_build_debug --debug -j6

%install
export PATH=$PATH:%_qt5_bindir
%python3_install

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc ChangeLog TODO *.rst demo.py
%python3_sitelibdir/*


%changelog
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

