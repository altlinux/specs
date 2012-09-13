Name:		python-module-iso8601
Version:	0.1.4
Release:	alt1
Summary:	Simple module to parse ISO 8601 dates

Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/iso8601/
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-distribute

%description
This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %buildroot

%files
%defattr(-,root,root,-)
%doc LICENSE README
%{python_sitelibdir}/*

%changelog
* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.1.4-alt1
- Initial release for Sisyphus (based on Fedora)
