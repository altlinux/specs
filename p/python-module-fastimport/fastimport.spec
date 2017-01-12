%define _unpackaged_files_terminate_build 1
%define oname fastimport

%def_with python3

Name: python-module-%oname
Version: 0.9.6
Release: alt1
Summary: VCS fastimport/fastexport parser
License: GPLv2+
Group: Development/Python
Url: http://pypi.python.org/pypi/fastimport/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/f0/42/ae12d69ee5cca6bc8164765f186c12945d63d63d5107b6f9b81c746cabda/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

It is currently used by bzr-fastimport and dulwich. hg-fastimport and
git-remote-hg use a slightly modified version of it.

%if_with python3
%package -n python3-module-%oname
Summary: VCS fastimport/fastexport parser (Python 3)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

It is currently used by bzr-fastimport and dulwich. hg-fastimport and
git-remote-hg use a slightly modified version of it.

%package -n python3-module-%oname-tests
Summary: Tests for fastimport (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

It is currently used by bzr-fastimport and dulwich. hg-fastimport and
git-remote-hg use a slightly modified version of it.

This package contains tests for fastimport.
%endif

%package tests
Summary: Tests for fastimport
Group: Development/Python
Requires: %name = %version-%release

%description tests
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

It is currently used by bzr-fastimport and dulwich. hg-fastimport and
git-remote-hg use a slightly modified version of it.

This package contains tests for fastimport.

%prep
%setup -q -n %{oname}-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
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

