%define oname repoze.urispace

Name: python3-module-%oname
Version: 0.3.2
Release: alt4

Summary: Library / middleware for URI-based assertions

License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.urispace/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-tools

%py3_requires repoze paste zope.interface elementtree

%description
repoze.urispace implements the URISpace 1.0 spec, as proposed to the W3C
by Akamai. Its aim is to provide an implementation of that language as a
vehicle for asserting declarative metadata about a resource based on
pattern matching against its URI.

Once asserted, such metadata can be used to guide the application in
serving the resource, with possible applciations including:

* Setting cache control headers.
* Selecting externally applied themes, e.g. in Deliverance.
* Restricting access, e.g. to emulate Zope's "placeful security."

%prep
%setup
find . -type f -name '*.py' -exec python3-2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install
%python3_prune

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd


%files
%doc *.txt docs/*.rst docs/examples
%_bindir/*.py3
%python3_sitelibdir/*

%changelog
* Sun Jul 11 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt4
- build python3 module separately

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.3.2-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

