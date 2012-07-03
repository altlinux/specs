%define oname coopr
Name: python-module-%oname
Version: 3.2
Release: alt1.svn20120212
Summary: COmmon Optimization Python Repository 
License: BSD
Group: Development/Python
Url: https://projects.coin-or.org/Coopr
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://software.sandia.gov/svn/public/coopr
Source: %oname-%version.tar.gz

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: texlive-latex-recommended asciidoc
BuildArch: noarch

%description
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

%package -n %oname-docs
Summary: Documentation and examples for Coopr
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-docs
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This package contains documentation and examples for Coopr.

%package core
Summary: Cross-cutting utilities for other Coopr packages
Group: Development/Python
Requires: %name = %version-%release

%description core
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This package contains cross-cutting utilities used by other Coopr
packages.

%package openopt
Summary: Coopr interfaces for the OpenOpt project
Group: Development/Python
Requires: %name = %version-%release

%description openopt
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This package contains Coopr interfaces for the OpenOpt project.

%package extras
Summary: Variety of extra Python packages that Coopr can leverage
Group: Development/Python
Requires: %name = %version-%release

%description extras
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This is an extension package that includes a variety of extra Python
packages that Coopr can leverage.  Additionally, this package includes
a variety of other optimization-related packages that a user might find
useful (e.g. PuLP-OR).

%package colin
Summary: Interfaces for COLIN optimization solvers
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.component.core pyutilib.misc pyutilib.common
%py_requires pyutilib.math pyutilib.enum coopr.opt.base

%description colin
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package includes interfaces for COLIN optimization solvers.

%package fdt
Summary: Implementations of the FDT MIP heuristic
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.misc coopr.opt coopr.pyomo

%description fdt
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package includes implementations of the FDT MIP heuristic.

%package gui-%oname
Summary: Jython GUI for Coopr
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip java pawt

%description gui-%oname
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package includes a Jython GUI for Coopr.

%package gui-pyomo
Summary: Jython GUI for executing the Pyomo command
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip javax

%description gui-pyomo
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package includes a Jython GUI for executing the Pyomo
command.

%package misc
Summary: Miscellaneous Coopr utilities
Group: Development/Python
Requires: %name = %version-%release
%py_requires coopr.opt coopr.pyomo pyutilib.workflow pyutilib.pyro

%description misc
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package defines miscellaneous Coopr utilities.

%package misc-doc
Summary: Documentation for miscellaneous Coopr utilities
Group: Development/Documentation

%description misc-doc
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This package contains documentation for miscellaneous Coopr utilities.

%package opt
Summary: Generic interfaces for optimization solvers
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.services pyutilib.subprocess pyutilib.component.core
%py_requires pyutilib.enum pyutilib.math pefile

%description opt
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package includes generic interfaces for optimization
solvers.

%package plugins
Summary: Plugins used within Coopr
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.component.core coopr.opt.base

%description plugins
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package includes plugins used within Coopr.

%package pyomo
Summary: Pythonic modeling language for math programming
Group: Development/Python
Requires: %name = %version-%release
%py_requires ordereddict pyutilib.ply pyutilib.excel coopr.opt
%py_requires pyutilib.component.core pyutilib.math pyutilib.misc
%py_requires pyutilib.enum

%description pyomo
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package defines a Pythonic modeling language for math
programming.

%package pyomo-examples
Summary: Examples for Pythonic modeling language for math programming
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-pyomo = %version-%release

%description pyomo-examples
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package contains examples for a Pythonic modeling language
for math programming.

%package pysos
Summary: Classes used to define heterogeneous optimization formulations
Group: Development/Python
Requires: %name = %version-%release
%py_requires coopr.pyomo.scripting.pyomo pyutilib.component.core
%py_requires pyutilib.math pyutilib.misc pyutilib.enum coopr.opt

%description pysos
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package defines classes used to define heterogeneous
optimization formulations (e.g. which integrate spreadsheet calculations
with linear programming models).

%package pysos-examples
Summary: Examples for classes used to define heterogeneous optimization formulations
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-pysos = %version-%release

%description pysos-examples
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package contains examples for classes used to define
heterogeneous optimization formulations (e.g. which integrate
spreadsheet calculations with linear programming models).

%package pysp
Summary: Stochastic programming extensions for the Pyomo modeling language
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.component.core coopr.pyomo

%description pysp
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package defines stochastic programming extensions for the
Pyomo modeling language.

%package pysp-examples
Summary: Examples for stochastic programming extensions for the Pyomo modeling language
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-pysp = %version-%release

%description pysp-examples
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package contains examples for stochastic programming
extensions for the Pyomo modeling language.

%package skel
Summary: Skel for Coopr
Group: Development/Python
Requires: %name = %version-%release

%description skel
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package contains skel for Coopr.

%package sucasa
Summary: Scripts for customizing integer programming solvers
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.misc pyutilib.ply pyutilib.subprocess

%description sucasa
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package defines scripts for customizing integer programming
solvers.

%package sucasa-examples
Summary: Examples for scripts for customizing integer programming solvers
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-sucasa = %version-%release

%description sucasa-examples
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package examples for scripts for customizing integer
programming solvers.

%package age
Summary: A QT Interface for formulating and solving Pyomo models
Group: Development/Python
Requires: %name = %version-%release

%description age
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package provides a Qt interface for formulating and solving
Pyomo models.

%package os
Summary: Coopr interfaces for the COIN-OR Optimization Services project
Group: Development/Python
Requires: %name = %version-%release
%py_requires coopr.opt

%description os
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package provides Coopr interfaces for the COIN-OR
Optimization Services project.

%package gdp
Summary: Generalized Disjunctive Programming (GDP) extensions to the Pyomo environment
Group: Development/Python
Requires: %name = %version-%release

%description gdp
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This Python package provides Generalized Disjunctive Programming (GDP)
extensions to the Pyomo environment.

%package tests
Summary: Tests for Coopr
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-colin = %version-%release
Requires: %name-fdt = %version-%release
Requires: %name-misc = %version-%release
Requires: %name-opt = %version-%release
Requires: %name-plugins = %version-%release
Requires: %name-pyomo = %version-%release
Requires: %name-pysp = %version-%release
Requires: %name-skel = %version-%release
Requires: %name-sucasa = %version-%release
#Requires: %name-os = %version-%release
%py_requires pyutilib.dev.runtests pyutilib.th pyutilib.component.app
%py_requires pyutilib.component.loader pyutilib.autotest

%description tests
Coopr is a collection of Python optimization-related packages. Coopr
supports a diverse set of optimization capabilities that can be used to
formulate and analyze optimization applications. In particular, it
include Pyomo, a Python-based modeling tool that can model abstract
linear and integer programs. Coopr strongly leverages a Python component
architecture to support extensibility in a modular manner, and plug-ins
for optimization solvers can be added without editing any Coopr
software.

This package contains tests for Coopr.

%prep
%setup
rm -f %oname.pysp/trunk/examples/pysp/cap/testinstance/ReferenceModel.dat~

%build
pushd ceps
%make_build
popd

for i in %{oname}* ATTIC/%oname.colin ATTIC/%oname.gui.coopr \
	ATTIC/%oname.gui.pyomo ATTIC/%oname.skel
do
	if [ "$i" != "coopr.doc" ]; then
		pushd $i/trunk
		%python_build
		popd
	fi
done

#pushd %oname.colin/trunk/doc/opt
pushd %oname.opt/trunk/doc/opt
%make
popd

pushd ATTIC/%oname.colin/trunk/doc/opt
%make
popd

cp %oname.data.samples/trunk/%oname/data/samples/CooprGettingStarted \
	%oname.doc/trunk/GettingStarted/current/examples/ -fR

%install
export PYTHONPATH=%buildroot%python_sitelibdir

for i in %{oname}* ATTIC/%oname.colin ATTIC/%oname.gui.coopr \
	ATTIC/%oname.gui.pyomo ATTIC/%oname.skel
do
	if [ "$i" != "coopr.doc" ]; then
		pushd $i/trunk
		%python_install
		popd
	fi
done

install -m644 %oname/trunk/%oname/__init__.py \
	%buildroot%python_sitelibdir/%oname
for i in $(find %buildroot%python_sitelibdir -type d)
do
	touch $i/__init__.py
done

rm -f \
	%buildroot%python_sitelibdir/%oname/pyomo/tests/NL/CUTE/gigomez1_cute.py*

mv %buildroot%_bindir/OSSolverService \
	%buildroot%_bindir/OSSolverService.%oname

install -d %buildroot%_docdir/%oname
pushd %oname.doc/trunk/GettingStarted/current
cp -fR *.html *.pdf *.txt examples %buildroot%_docdir/%oname/
popd

%files
%doc *.txt
%_bindir/%oname
%_bindir/%{oname}_python
%python_sitelibdir/Coopr*
%dir %python_sitelibdir/%oname
%dir %python_sitelibdir/%oname/gui
%python_sitelibdir/%oname/gui/__init__.py*
%python_sitelibdir/%oname/__init__.py*
%python_sitelibdir/%oname/%oname

%files -n %oname-docs
%_docdir/%oname

%files core
%doc %oname.core/trunk/*.txt %oname.core/trunk/doc/examples
%doc %oname.core/trunk/doc/api.*
%python_sitelibdir/%oname.core*
%python_sitelibdir/%oname/core
%exclude %python_sitelibdir/%oname/core/tests

%files openopt
%doc %oname.openopt/trunk/*.txt
%python_sitelibdir/%oname.openopt*
%python_sitelibdir/%oname/openopt
%exclude %python_sitelibdir/%oname/openopt/test*

%files extras
%doc %oname.extras/trunk/*.txt
%python_sitelibdir/%oname.extras*
%python_sitelibdir/%oname/extras
%exclude %python_sitelibdir/%oname/extras/test*

%files colin
%doc ATTIC/%oname.colin/trunk/*.txt
%doc ATTIC/%oname.colin/trunk/examples
%python_sitelibdir/%oname.colin*
%python_sitelibdir/%oname/colin
%exclude %python_sitelibdir/%oname/colin/tests
%exclude %python_sitelibdir/*.pth
%_bindir/results_attributes

%files fdt
%doc %oname.fdt/trunk/*.txt
%doc %oname.fdt/trunk/data
%python_sitelibdir/%oname.fdt*
%python_sitelibdir/%oname/fdt
%exclude %python_sitelibdir/%oname/fdt/tests
%exclude %python_sitelibdir/*.pth
%_bindir/fdt

%files gui-%oname
%doc ATTIC/%oname.gui.%oname/trunk/
%python_sitelibdir/%oname.gui.%{oname}*
%python_sitelibdir/%oname/gui/%oname
%exclude %python_sitelibdir/*.pth

%files gui-pyomo
%doc ATTIC/%oname.gui.pyomo/trunk/*.txt
%python_sitelibdir/%oname.gui.pyomo*
%python_sitelibdir/%oname/gui/pyomo
%exclude %python_sitelibdir/*.pth

%files misc
%doc %oname.misc/trunk/*.txt
%python_sitelibdir/%oname.misc*
%python_sitelibdir/%oname/misc
%exclude %python_sitelibdir/%oname/misc/runtests.py*
%exclude %python_sitelibdir/*.pth
%_bindir/OSSolverService.%oname
%_bindir/CooprOSSolverService
%_bindir/kill_pyro_mip_servers
%_bindir/readsol
%_bindir/launch_pyro_mip_servers
#_bindir/register_com.py
#_bindir/%oname
%_bindir/%{oname}_ns*
%_bindir/pyro_mip_server*

%files misc-doc
%doc %oname.misc/trunk/doc/pub/*

%files opt
%doc %oname.opt/trunk/*.txt
%python_sitelibdir/%oname.opt*
%python_sitelibdir/%oname/opt
%exclude %python_sitelibdir/%oname/opt/test*
%exclude %python_sitelibdir/*.pth
%_bindir/results_schema

%files plugins
%doc %oname.plugins/trunk/*.txt
%doc ATTIC/%oname.colin/trunk/doc/opt/*.pdf
%python_sitelibdir/%oname.plugins*
%python_sitelibdir/%oname/plugins
%exclude %python_sitelibdir/%oname/plugins/test*
#exclude %python_sitelibdir/%oname/plugins/skel/tests
#exclude %python_sitelibdir/%oname/plugins/mip/GUROBI*
%exclude %python_sitelibdir/%oname/plugins/solvers/GUROBI*
#exclude %python_sitelibdir/%oname/plugins/mip/CPLEX*
#exclude %python_sitelibdir/%oname/plugins/mip/ASL*
%exclude %python_sitelibdir/%oname/plugins/converter/ampl.py*
%exclude %python_sitelibdir/*.pth

%files pyomo
%doc %oname.pyomo/trunk/*.txt
%python_sitelibdir/%oname.pyomo*
%python_sitelibdir/%oname/pyomo
%exclude %python_sitelibdir/%oname/pyomo/tests
%exclude %python_sitelibdir/*.pth
%_bindir/pyomo*

%files pyomo-examples
%doc %oname.pyomo/trunk/examples/pyomo/*

%files pysos
%doc %oname.pysos/trunk/*.txt
%python_sitelibdir/%oname.pysos*
%python_sitelibdir/%oname/pysos
%exclude %python_sitelibdir/*.pth
%_bindir/pysos*

%files pysos-examples
%doc %oname.pysos/trunk/examples/pysos

%files pysp
%doc %oname.pysp/trunk/*.txt
%doc %oname.pysp/trunk/doc/pysp/*.pdf
%python_sitelibdir/%oname.pysp*
%python_sitelibdir/%oname/pysp
%exclude %python_sitelibdir/%oname/pysp/tests
%exclude %python_sitelibdir/*.pth
%_bindir/runph*
%_bindir/computeconf*
%_bindir/ph_test_client
%_bindir/phsolverserver
%_bindir/runef*

%files pysp-examples
%doc %oname.pysp/trunk/examples/pysp/*

%files skel
%doc ATTIC/%oname.skel/trunk/*.txt
%python_sitelibdir/%oname.skel*
%python_sitelibdir/%oname/skel
%exclude %python_sitelibdir/%oname/skel/tests
%exclude %python_sitelibdir/*.pth

%files sucasa
%doc %oname.sucasa/trunk/*.txt
%python_sitelibdir/%oname.sucasa*
%python_sitelibdir/%oname/sucasa
%exclude %python_sitelibdir/%oname/sucasa/tests
%exclude %python_sitelibdir/*.pth
%_bindir/sucasa

%files sucasa-examples
%doc %oname.sucasa/trunk/examples/sucasa/*

%files age
%doc %oname.age/trunk/*.txt
%python_sitelibdir/%oname.age*
%python_sitelibdir/%oname/age
%exclude %python_sitelibdir/*.pth
%exclude %_bindir/CooprAge

#files os
#doc %oname.os/trunk/*.txt
%exclude %python_sitelibdir/%oname.os*
%exclude %python_sitelibdir/%oname/os
%exclude %python_sitelibdir/%oname/os/tests

%files gdp
%doc %oname.gdp/trunk/*.txt
%python_sitelibdir/%oname.gdp*
%python_sitelibdir/%oname/gdp
%exclude %python_sitelibdir/%oname/gdp/tests
%exclude %python_sitelibdir/*.pth

%files tests
%_bindir/test*
%python_sitelibdir/%oname/colin/tests
%python_sitelibdir/%oname/fdt/tests
%python_sitelibdir/%oname/misc/runtests.py*
%python_sitelibdir/%oname/opt/test*
%python_sitelibdir/%oname/plugins/test*
#python_sitelibdir/%oname/plugins/skel/tests
%python_sitelibdir/%oname/pyomo/tests
%python_sitelibdir/%oname/pysp/tests
%python_sitelibdir/%oname/skel/tests
%python_sitelibdir/%oname/sucasa/tests
%python_sitelibdir/%oname/gdp/tests
%python_sitelibdir/%oname/data
%python_sitelibdir/%oname.data*
%python_sitelibdir/%oname/os/tests
%python_sitelibdir/%oname/core/tests
%python_sitelibdir/%oname/extras/test*
%python_sitelibdir/%oname/openopt/test*

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.svn20120212
- Version 3.2

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.5325-alt1.svn20111123
- Version 3.1.5325

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt1.svn20110424.1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20110424.1
- Excluded *.pth

* Wed Apr 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20110424
- New snapshot

* Sun Dec 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20101218
- New snapshot

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20101119.1
- Rebuilt with Pyro4 4.2

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20101119
- Version 2.5

* Wed Sep 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.svn20100909.1
- Fixed backup-file-in-package
- Fixed conflict with CoinOS

* Tue Sep 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.svn20100909
- Initial build for Sisyphus

