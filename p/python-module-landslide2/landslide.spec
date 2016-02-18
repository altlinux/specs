%define oname landslide

%def_with python3

Name: python-module-%{oname}2
Version: 2.0.0
Release: alt1.git20150619.1
Summary: Lightweight markup language-based html5 slideshow generator
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/landslide
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/adamzap/landslide.git
# branch: v2
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-jinja2 python-module-markdown
#BuildPreReq: python-module-Pygments python-module-docutils
#BuildPreReq: python-module-six python-module-docopt
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-jinja2 python3-module-markdown
#BuildPreReq: python3-module-Pygments python3-module-docutils
#BuildPreReq: python3-module-six python3-module-docopt
%endif

%py_provides %oname
Conflicts: python-module-%oname
%py_requires jinja2 markdown pygments docutils six docopt

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-docutils python-module-html5lib python-module-markdown python-module-setuptools-tests python3-module-html5lib python3-module-markdown python3-module-setuptools-tests python3-module-sphinx rpm-build-python3 time

%description
Landslide takes your Markdown, ReST, or Textile file(s) and generates
fancy HTML5 slideshow.

%if_with python3
%package -n python3-module-%{oname}2
Summary: Lightweight markup language-based html5 slideshow generator
Group: Development/Python3
%py3_provides %oname
Conflicts: python3-module-%oname
%py3_requires jinja2 markdown pygments docutils six docopt

%description -n python3-module-%{oname}2
Landslide takes your Markdown, ReST, or Textile file(s) and generates
fancy HTML5 slideshow.
%endif

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
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test -v
#python tests.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v
#python3 tests.py -v
popd
%endif

%files
%doc *.md examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%{oname}2
%doc *.md examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt1.git20150619.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150619
- Initial build for Sisyphus

