%define oname landslide

%def_with python3

Name: python-module-%oname
Version: 1.1.3
Release: alt2.git20150525.1
Summary: Lightweight markup language-based html5 slideshow generator
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/landslide

# https://github.com/adamzap/landslide.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-jinja2 python-module-markdown
BuildRequires: python-module-Pygments python-module-docutils
BuildRequires: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-jinja2 python3-module-markdown
BuildRequires: python3-module-Pygments python3-module-docutils
BuildRequires: python3-module-six
%endif

%py_provides %oname
%py_requires jinja2 markdown pygments docutils six

%description
Landslide takes your Markdown, ReST, or Textile file(s) and generates
fancy HTML5 slideshow.

%if_with python3
%package -n python3-module-%oname
Summary: Lightweight markup language-based html5 slideshow generator
Group: Development/Python3
%py3_provides %oname
%py3_requires jinja2 markdown pygments docutils six

%description -n python3-module-%oname
Landslide takes your Markdown, ReST, or Textile file(s) and generates
fancy HTML5 slideshow.
%endif

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
python setup.py build_ext -i
python tests.py -v
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
python3 tests.py -v
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
%files -n python3-module-%oname
%doc *.md examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.3-alt2.git20150525.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.3-alt2.git20150525
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt1.git20150525.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20150525
- Initial build for Sisyphus

