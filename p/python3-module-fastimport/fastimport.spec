%define _unpackaged_files_terminate_build 1
%define oname fastimport

%def_with check

Name: python3-module-%oname
Version: 0.9.14
Release: alt1
Summary: VCS fastimport/fastexport parser
License: GPLv2+
Group: Development/Python3
Url: http://pypi.python.org/pypi/fastimport/
BuildArch: noarch

Source0: %{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-nose
%endif

%py3_provides %oname

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

It is currently used by bzr-fastimport and dulwich. hg-fastimport and
git-remote-hg use a slightly modified version of it.

%package tests
Summary: Tests for fastimport
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

It is currently used by bzr-fastimport and dulwich. hg-fastimport and
git-remote-hg use a slightly modified version of it.

This package contains tests for fastimport.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir %_bindir/nosetests-3.* %oname

%files
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%_bindir/*

%files tests
%python3_sitelibdir/*/tests

%changelog
* Thu Oct 14 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.14-alt1
- Build new version.

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.8-alt2
- Drop python2 support.

* Mon May 06 2019 Anatoly Kitaykin <cetus@altlinux.org> 0.9.8-alt1
- Version 0.9.8

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.9.2-alt1.1
- Rebuild with Python-3.3

* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2
- Add module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

