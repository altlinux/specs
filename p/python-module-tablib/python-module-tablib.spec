%global raw_version 0.9.11
%global checkout 20120702git752443f

Name:		python-module-tablib
Version:	%{raw_version}.%{checkout}
Release:	alt1
Summary:	Format agnostic tabular data library (XLS, JSON, YAML, CSV)

Group:		Development/Python
License:	MIT
URL:		http://github.com/kennethreitz/tablib
Source0:	%{name}-%{version}.tar.gz

# https://github.com/kennethreitz/tablib/pull/68
Patch0:		%{name}-py3-support.patch
Patch1:		%{name}-broken-setup.py.patch

BuildArch:	noarch

BuildRequires:	python-devel
Requires:	python-module-yaml

%description
Tablib is a format-agnostic tabular dataset library, written in Python.

Output formats supported:

 - Excel (Sets + Books)
 - JSON (Sets + Books)
 - YAML (Sets + Books)
 - HTML (Sets)
 - TSV (Sets)
 - CSV (Sets)

%prep
%setup -q
%patch0 -p1 -b .py3_support
%patch1 -p1 -b .broken_setup_py

# Remove shebangs
for lib in $(find . -name "*.py"); do
 sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%files
%doc README.rst LICENSE AUTHORS HACKING HISTORY.rst NOTICE TODO.rst
%{python_sitelibdir}/tablib
%{python_sitelibdir}/tablib-%{raw_version}*

%changelog
* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.9.11.20120702git752443f-alt1
- Initial release for Sisyphus (based on Fedora)
