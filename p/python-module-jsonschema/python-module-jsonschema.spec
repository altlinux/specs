Name:		python-module-jsonschema
Version:	0.2
Release:	alt1
Summary:	An implementation of JSON Schema validation for Python

License:	MIT
Group:		Development/Python
URL:		http://pypi.python.org/pypi/jsonschema/0.2
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python-devel

%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst COPYING
%{python_sitelibdir}/*

%changelog
* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2-alt1
- Initial release for Sisyphus (based on Fedora)
