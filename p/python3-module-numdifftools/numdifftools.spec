%define oname numdifftools

%def_disable check

Name: python3-module-%oname
Version: 0.9.39
Release: alt2

Summary: Solves automatic numerical differentiation problems in one or more variables

License: BSD
Group: Development/Python3
Url: https://github.com/pbrod/numdifftools

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-scipy
BuildPreReq: python3-module-numpy python3-module-matplotlib
BuildPreReq: python3-module-coverage python3-module-setuptools
BuildPreReq: python3-module-setuptools_scm python3-module-six
BuildPreReq: python3-module-algopy
BuildRequires: python3-module-pytest-runner
%if_enabled check
BuildPreReq: python3-module-nose xvfb-run
BuildPreReq: python3-module-pytest-cov
%endif
BuildPreReq: texlive-latex-recommended

%py3_provides %oname
%py3_requires numpy scipy algopy

%description
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%if_enabled check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ~
xvfb-run python3 -c "import numdifftools as nd; nd.test(coverage=True)" || :
popd
xvfb-run py.test-%_python3_version -vv -rsxXf
%endif

%files
%python3_sitelibdir/*

%changelog
* Fri Jul 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.39-alt2
- Updated build dependencies.

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.39-alt1
- new version 0.9.39 (with rpmrb script)
- disable check (need rewrite)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.12-alt2.git20150828.2
- cleanup spec, update URL, switch to build from tarball, drop tests packing

* Thu Apr 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.12-alt2.git20150828.1
- Build for python2 disabled.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.12-alt1.git20150828.1.1.1.qa1
- NMU: applied repocop patch

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.12-alt1.git20150828.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.12-alt1.git20150828.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.12-alt1.git20150828.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.12-alt1.git20150828
- Version 0.9.12

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20141217
- Version 0.7.3

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2.svn20140221
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.svn20140221
- Version 0.6.0

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Version 0.3.5

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt1.1
- Rebuild with Python-2.7

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

