%define oname jinja2_markdown

%def_with python3

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20150120.1.1
Summary: A jinja2 extension that adds a {%% markdown %%} tag to templates
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jinja2_markdown/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/danielchatfield/jinja2_markdown.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-markdown python-module-jinja2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-markdown python3-module-jinja2
%endif

%py_provides %oname
%py_requires markdown jinja2

%description
A simple extension for adding a {%% markdown %%}{%% endmarkdown %%} tag
to Jinja.

%package -n python3-module-%oname
Summary: A jinja2 extension that adds a {%% markdown %%} tag to templates
Group: Development/Python3
%py3_provides %oname
%py3_requires markdown jinja2

%description -n python3-module-%oname
A simple extension for adding a {%% markdown %%}{%% endmarkdown %%} tag
to Jinja.

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

%check
python setup.py test
python tests.py -v
%if_with python3
pushd ../python3
python3 setup.py test
python3 tests.py -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.3-alt1.git20150120.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20150120.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150120
- Initial build for Sisyphus

