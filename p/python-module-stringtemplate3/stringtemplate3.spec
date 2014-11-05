%define oname stringtemplate3
Name: python-module-%oname
Version: 3.1
Release: alt1
Summary: A powerful template engine with strict model-view separation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/stringtemplate3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-antlr2

%py_provides %oname
Requires: python-module-antlr2

%description
ST (StringTemplate) is a template engine for generating source code, web
pages, emails, or any other formatted text output. ST is particularly
good at multi-targeted code generators, multiple site skins, and
internationalization/localization. It evolved over years of effort
developing jGuru.com.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Initial build for Sisyphus

