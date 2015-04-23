%define oname pyrsslocal
Name: python3-module-%oname
Version: 0.8.97
Release: alt1.git20150422
Summary: Local RSS reader/viewer
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyrsslocal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sdpython/pyrsslocal.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyquickhelper python3-module-pyensae
BuildPreReq: python3-module-feedparser python3-module-sphinx-devel
BuildPreReq: python3-module-requests
BuildPreReq: python3-module-hachibee_sphinx_theme

%py3_provides %oname
%py3_requires pyquickhelper pyensae feedparser requests

%description
This extension proposes a way to download new posts from blogs
and to navigate through them with a couple of HTML pages
managed by a local python server using a SQLite database.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This extension proposes a way to download new posts from blogs
and to navigate through them with a couple of HTML pages
managed by a local python server using a SQLite database.

This package contains documentation for %oname.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAl"
git init-db
git remote add origin https://github.com/sdpython/pyrsslocal.git
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%prepare_sphinx _doc/sphinxdoc
ln -s ../objects.inv _doc/sphinxdoc/source/

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug --verbose

python3 setup.py build_sphinx

%install
export LC_ALL=en_US.UTF-8
%python3_install

%check
export LC_ALL=en_US.UTF-8
python3 setup.py test
#python3 setup.py unittests

%files
%doc *.rst
%python3_sitelibdir/*

%files docs
%doc _doc/sphinxdoc/build/html/*

%changelog
* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.97-alt1.git20150422
- Initial build for Sisyphus

