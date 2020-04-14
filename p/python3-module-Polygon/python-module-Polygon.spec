Name:           python3-module-Polygon
Version:        3.0.8
Release:        alt1
Summary:        Python package that handles polygonal shapes in 2D

License:        LGPL with exception
Group:          Development/Python3
URL:            http://www.j-raedler.de/projects/polygon/
# VCS: https://bitbucket.org/jraedler/polygon3.git

Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        Polygon-%{version}.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-distribute
Provides:	python3-Polygon = %version-%release

%description
Polygon is a python package that handles polygonal shapes in 2D. It
contains Python bindings for gpc, the excellent General Polygon Clipping
Library by Alan Murta and some extensions written in C and pure Python.
With Polygon you may handle complex polygonal shapes in Python in a very
intuitive way. Polygons are simple Python objects, clipping operations
are bound to standard operators like +, -, |, & and ^. TriStrips can be
constructed from Polygons with a single statement. Functions to compute
the area, center point, convex hull, point containment and much more are
included. This package was already used to process shapes with more than
one million points!

gpc is included in Polygon and is distributed under other license.
gpc homepage: http://www.cs.man.ac.uk/~toby/alan/software/

GPC is free for non-commercial use only. We invite non-commercial users
to make a voluntary donation towards the upkeep of GPC. If you wish to
use GPC in support of a commercial product, you must obtain an official
GPC Commercial Use Licence from The University of Manchester.

%prep
%setup -q -n Polygon-%version

%build
%python3_build

%install
%python3_install

%files
%doc README HISTORY
%dir %python3_sitelibdir/Polygon 
%python3_sitelibdir/Polygon
%python3_sitelibdir/Polygon*.egg-info

%changelog
* Tue Apr 14 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.8-alt1
- New version.

* Tue Apr 14 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.8-alt2
- Build as Python3 module.

* Wed Nov 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.8-alt1
- new version 2.0.8

* Thu Feb 20 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.6-alt1
- Initial build in Sisyphus
