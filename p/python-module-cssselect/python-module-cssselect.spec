Name: python-module-cssselect
Version: 0.8
Release: alt1

Summary: Parses CSS3 Selectors and translates them to XPath 1.0
Group: Development/Python
License: BSD-style
Url: http://packages.python.org/cssselect/
BuildArch: noarch

%setup_python_module cssselect

BuildRequires: python-module-lxml

# http://pypi.python.org/packages/source/c/cssselect/cssselect-%version.tar.gz
Source: cssselect-%version.tar

%description
Cssselect parses CSS3 Selectors and translates them to XPath 1.0
expressions.  Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document.

%prep
%setup -n cssselect-%version

%build
%python_build

%install
%python_install

%check
PYTHONPATH=%buildroot%python_sitelibdir %__python cssselect/tests.py

%files
%python_sitelibdir/*
%doc AUTHORS docs README.rst CHANGES LICENSE PKG-INFO

%changelog
* Tue May 21 2013 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt1
- Initial revision.
