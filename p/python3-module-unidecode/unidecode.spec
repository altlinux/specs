%define oname unidecode

Name: python3-module-%oname
Version: 0.04.17
Release: alt1.git20141218.1.3
Summary: ASCII transliterations of Unicode text
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/Unidecode/

# http://www.tablix.org/~avian/git/unidecode.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
It often happens that you have text data in Unicode, but you need to
represent it in ASCII. For example when integrating with legacy code
that doesn't support Unicode, or for ease of entry of non-Roman names on
a US keyboard, or when constructing ASCII machine identifiers from
human-readable Unicode strings that should still be somewhat
intelligeble (a popular example of this is when making an URL slug from
an article title).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc ChangeLog README tools
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.04.17-alt1.git20141218.1.3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.04.17-alt1.git20141218.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.04.17-alt1.git20141218.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.04.17-alt1.git20141218.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.04.17-alt1.git20141218
- Version 0.04.17

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.04.16-alt1.git20140511
- Initial build for Sisyphus

