Name:           python-module-Polygon
Version:        2.0.8
Release:        alt1
Summary:        Python package that handles polygonal shapes in 2D

License:        LGPL with exception
Group:          Development/Python
URL:            http://www.j-raedler.de/projects/polygon/

Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        Polygon-%{version}.tar

BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute
Provides:	python-Polygon = %version-%release

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
%python_build

%install
%python_install

%files
%doc README HISTORY
%dir %python_sitelibdir/Polygon 
%python_sitelibdir/Polygon
%python_sitelibdir/Polygon*.egg-info

%changelog
* Wed Nov 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.8-alt1
- new version 2.0.8

* Thu Feb 20 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.6-alt1
- Initial build in Sisyphus
