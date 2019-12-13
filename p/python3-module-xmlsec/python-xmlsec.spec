%def_enable check

Name: python3-module-xmlsec
Version: 1.3.6
Release: alt2

Summary: Python bindings for the XML Security Library
License: MIT
Group: Development/Python3
Url: https://github.com/mehcode/python-xmlsec

Source: %version.tar.gz

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest python3-module-setuptools-tests
%endif

BuildRequires: libxmlsec1-openssl-devel
BuildRequires: python3-module-Cython python3-module-lxml
BuildRequires: python3-module-pkgconfig
BuildRequires: python3-module-sphinx

Obsoletes: python3-module-mehcode-xmlsec


%description
Python bindings for the XML Security Library.

%prep
%setup -n python-xmlsec-%version

%build
%python3_build_debug -b build3
PYTHONPATH=`realpath build3/lib.linux*` make -C doc html SPHINXBUILD=py3_sphinx-build BUILDDIR=build3

%install
rm -f build && ln -s build3 build && %python3_install

%if_with check
%check
%__python3 setup.py test build_ext -i
py.test-%_python3_version -vv
%endif

%files
%doc README* 
%python3_sitelibdir/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.6-alt2
- build for python2 disabled

* Sun Jan 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt1
- Build new version.

* Tue May 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt2
- NMU: Add URL (Closes: #34693).

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 1.3.3-alt1
- Autobuild version bump to 1.3.3
- Introduce documentation

* Wed Jul 27 2016 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Fresh build from Pypi
- Thanks real@ for old python-module-mehcode-xmlsec

