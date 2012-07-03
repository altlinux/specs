%define module_name osm

Name: python-module-%module_name
Version: 0.0.1
Release: alt3.1

Summary: OpenStreetMap library for python

License: BSD
Group: Development/Python
Url: http://github.com/werner2101/python-osm

Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

%description
OpenStreetMap library for python

%package tools
Summary: Tools for OpenStreetMap
Group: Development/Python
Requires: %name = %version-%release
%description tools
OpenStreetMap library for python

%prep
%setup

%build
%python_build

%install
%python_install

for f in osmhistory relation2gpx; do
	mv %buildroot%_bindir/$f.py %buildroot%_bindir/$f
done

%files
%python_sitelibdir/python_osm*
%python_sitelibdir/osm

%files tools
%_bindir/osmhistory
%_bindir/relation2gpx


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt3.1
- Rebuild with Python-2.7

* Thu Apr 08 2010 Denis Klimov <zver@altlinux.org> 0.0.1-alt3
- Add require to python-module-osm for tools subpackage

* Thu Apr 08 2010 Denis Klimov <zver@altlinux.org> 0.0.1-alt2
- add tools subpackage

* Thu Apr 08 2010 Denis Klimov <zver@altlinux.org> 0.0.1-alt1
- Initial build for ALT Linux

