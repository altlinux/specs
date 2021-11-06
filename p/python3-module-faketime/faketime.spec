%global optflags_lto %nil
%define _unpackaged_files_terminate_build 1
%define oname faketime

Name: python3-module-%oname
Version: 0.9.8
Release: alt2

Summary: Python wrapper around libfaketime
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/faketime/

# https://github.com/crdoconnor/faketime.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%py3_provides %oname


%description
Libfaketime is a C library which can fake the passage of time for UNIX
applications, written by Wolfgang Hommel.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%check
%__python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Sat Nov 06 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.9.8-alt2
- NMU: build without LTO

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.8-alt1
- Version updated to 0.9.8
- build for python2 disabled.

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.6.6-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.6.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.6.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.6.3-alt1.git20150622.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.3-alt1.git20150622
- Initial build for Sisyphus

