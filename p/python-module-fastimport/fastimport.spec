%define oname fastimport

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt1
Summary: VCS fastimport/fastexport parser
License: GPLv2+
Group: Development/Python
Url: http://pypi.python.org/pypi/fastimport/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
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
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
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
%doc AUTHORS COPYING.txt NEWS
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS COPYING.txt NEWS
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2
- Add module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

