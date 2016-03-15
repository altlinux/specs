%define oname unidecode

%def_with python3

Name: python-module-%oname
Version: 0.04.17
Release: alt1.git20141218.1.1
Summary: ASCII transliterations of Unicode text
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Unidecode/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://www.tablix.org/~avian/git/unidecode.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python-modules-unittest rpm-build-python3

%description
It often happens that you have text data in Unicode, but you need to
represent it in ASCII. For example when integrating with legacy code
that doesn't support Unicode, or for ease of entry of non-Roman names on
a US keyboard, or when constructing ASCII machine identifiers from
human-readable Unicode strings that should still be somewhat
intelligeble (a popular example of this is when making an URL slug from
an article title).

%package -n python3-module-%oname
Summary: ASCII transliterations of Unicode text
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
It often happens that you have text data in Unicode, but you need to
represent it in ASCII. For example when integrating with legacy code
that doesn't support Unicode, or for ease of entry of non-Roman names on
a US keyboard, or when constructing ASCII machine identifiers from
human-readable Unicode strings that should still be somewhat
intelligeble (a popular example of this is when making an URL slug from
an article title).

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%doc ChangeLog README tools
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README tools
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.04.17-alt1.git20141218.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.04.17-alt1.git20141218.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.04.17-alt1.git20141218
- Version 0.04.17

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.04.16-alt1.git20140511
- Initial build for Sisyphus

