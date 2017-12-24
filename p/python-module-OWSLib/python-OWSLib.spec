%define modulename OWSLib

Name:           python-module-%modulename
Version:        0.16.0
Release:        alt1

Summary:        Client library for OGC web services
License:        BSD
Group:   	Development/Python
URL:            http://geopython.github.io/OWSLib

Packager:	Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires:  python-module-distribute
BuildRequires:  python-module-setuptools-tests

Provides:	python-%modulename = %version-%release

BuildArch:      noarch

Source0:	%modulename-%version.tar
#VCS:		git://github.com/geopython/OWSLib.git

%description
Package for client programming with Open Geospatial Consortium (OGC) web
service (hence OWS) interface standards, and their related content
models.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%doc LICENSE.txt README.txt CHANGES.txt CREDITS.txt
%python_sitelibdir/owslib/
%python_sitelibdir/*.egg-info

%changelog
* Sun Dec 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.16.0-alt1
- New version.

* Thu Sep 14 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1
- New version

* Sun Jan 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Wed Sep 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- new version 0.12.0

* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 0.11.2-alt1
- new version 0.11.2

* Wed Jul 16 2014 Andrey Cherepanov <cas@altlinux.org> 0.8.8-alt1
- Import to ALT Linux from Fedora

* Mon Jul  7 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.8-1
- New upstream release

* Wed Jul  2 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.7-3
- Changed package summary

* Tue Jul  1 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.7-2
- Correct BR python-setuptools-devel to python-setuptools

* Mon Jun 30 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.7-1
- Initial package for Fedora
