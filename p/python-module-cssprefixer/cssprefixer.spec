%define oname cssprefixer

%def_with python3

Name: python-module-%oname
Version: 1.4.2
Release: alt1.git20130518.1
Summary: Rewrite your CSS files, adding vendor-prefixed versions of CSS3 rules
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/cssprefixer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/myfreeweb/cssprefixer.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-cssutils
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-cssutils
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires cssutils

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-google python-module-setuptools python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-google python3-module-setuptools
BuildRequires: python-module-cssutils python3-module-cssutils rpm-build-python3 time

%description
A tool that rewrites your CSS files, adding vendor-prefixed versions of
(popular) CSS3 rules. It also can combine and minify your stylesheets.
Keep your styles clean!

It supports many CSS3 stuff including keyframe animations, Flexbox and
gradients.

%package -n python3-module-%oname
Summary: Rewrite your CSS files, adding vendor-prefixed versions of CSS3 rules
Group: Development/Python3
%py3_provides %oname
%py3_requires cssutils

%description -n python3-module-%oname
A tool that rewrites your CSS files, adding vendor-prefixed versions of
(popular) CSS3 rules. It also can combine and minify your stylesheets.
Keep your styles clean!

It supports many CSS3 stuff including keyframe animations, Flexbox and
gradients.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python tests.py -v
%if_with python3
pushd ../python3
python3 tests.py -v
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.2-alt1.git20130518.1
- NMU: Use buildreq for BR.

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1.git20130518
- Initial build for Sisyphus

