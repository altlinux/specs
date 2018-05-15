%define oname alabaster

Name: python-module-%oname
Version: 0.7.6
Release: alt3

Summary: A configurable sidebar-enabled Sphinx theme
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/alabaster/
# https://github.com/bitprophet/alabaster.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-0.7.6-alt-valid-xhtml.patch

BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools

%description
This theme is a modified "Kr" Sphinx theme from @kennethreitz
(especially as used in his [Requests](https://python-requests.org)
project), which was itself originally based on @mitsuhiko's theme used
for [Flask](http://flask.pocoo.org/) & related projects.

%package -n python3-module-%oname
Summary: A configurable sidebar-enabled Sphinx theme
Group: Development/Python3

%description -n python3-module-%oname
This theme is a modified "Kr" Sphinx theme from @kennethreitz
(especially as used in his [Requests](https://python-requests.org)
project), which was itself originally based on @mitsuhiko's theme used
for [Flask](http://flask.pocoo.org/) & related projects.

%prep
%setup
%patch -p1

rm -rf python3
cp -R . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc *.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.7.6-alt3
- rebuild with python3.6

* Fri Apr 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.6-alt2.git20150703
- correct XHTML (sphinx 1.4.1 tests failed because of this!)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.6-alt1.git20150703.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1.git20150703
- Snapshot from git

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1
- Version 0.7.6
- Added module for Python 3

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

