%define oname jinja2_markdown

Name: python3-module-%oname
Version: 0.0.3
Release: alt2

Summary: A jinja2 extension that adds a {%% markdown %%} tag to templates
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jinja2_markdown/
BuildArch: noarch

# https://github.com/danielchatfield/jinja2_markdown.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-markdown python3-module-jinja2

%py3_provides %oname
%py3_requires markdown jinja2


%description
A simple extension for adding a {%% markdown %%}{%% endmarkdown %%} tag
to Jinja.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
%__python3 tests.py -v

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.3-alt1.git20150120.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20150120.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150120
- Initial build for Sisyphus

