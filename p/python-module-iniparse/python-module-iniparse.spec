Name:		python-module-iniparse
Version:	0.4
Release:	alt1
Summary:	Python Module for Accessing and Modifying Configuration Data in INI files
Group:		Development/Python
License:	MIT
URL:		http://code.google.com/p/iniparse/
Source:		%{name}-%{version}.tar.gz
Patch0:		python-module-iniparse-fix-issue-28.patch

BuildRequires:	python-module-distribute

BuildArch:	noarch

%description
iniparse is an INI parser for Python which is API compatible with the
standard library's ConfigParser, preserves structure of INI files
(order of sections & options, indentation, comments, and blank lines
are preserved when data is updated), and is more convenient to use.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %buildroot
# fixes
chmod 644 %buildroot/%{_docdir}/iniparse-%{version}/index.html
mv %buildroot/%{_docdir}/iniparse-%{version} %buildroot/%{_docdir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/*
%{python_sitelibdir}/*

%changelog
* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4-alt1
- Initial release for Sisyphus (based on Fedora)
