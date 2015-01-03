%define oname pyvisfile
Name: python-module-%oname
Version: 2014.1
Release: alt1.1
Summary: Large-scale Visualization Data Storage
License: MIT
Group: Development/Python
Url: http://mathema.tician.de/software/pyvisfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libsilo-devel libvtk-devel
BuildPreReq: python-module-sphinx-devel boost-python-devel
BuildPreReq: libhdf5-mpi-devel gcc-c++ libnumpy-devel
BuildPreReq: python-module-pyublas-devel python-module-pytest
BuildPreReq: python-module-py

%description
Pyvisfile allows you to write a variety of visualization file formats,
including

* Kitware's XML-style Vtk data files.
* Silo visualization files, as introduced by LLNL's MeshTV and more
  recently used by the VisIt large-scale visualization program.

pyvisfiles supports many mesh geometries, such such as unstructured and
rectangular structured meshes, particle meshes, as well as scalar and
vector variables on them. In addition, pyvisfile allows the
semi-automatic writing of parallelization-segmented visualization files
in both Silo and Vtk formats. For Silo files, pyvisfile also supports
the writing of expressions as visualization variables.

pyvisfile can write Vtk files without any extra software installed.

%package docs
Summary: Documentation for Pyvisfile
Group: Development/Documentation
BuildArch: noarch

%description docs
Pyvisfile allows you to write a variety of visualization file formats,
including

* Kitware's XML-style Vtk data files.
* Silo visualization files, as introduced by LLNL's MeshTV and more
  recently used by the VisIt large-scale visualization program.

pyvisfiles supports many mesh geometries, such such as unstructured and
rectangular structured meshes, particle meshes, as well as scalar and
vector variables on them. In addition, pyvisfile allows the
semi-automatic writing of parallelization-segmented visualization files
in both Silo and Vtk formats. For Silo files, pyvisfile also supports
the writing of expressions as visualization variables.

pyvisfile can write Vtk files without any extra software installed.

This package contains documentation for Pyvisfile.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
./configure.py \
	--update-user \
	--use-silo \
	--boost-python-libname=boost_python \
	--boost-compiler=g++ \
	--cxxflags="-g"
%python_build_debug

%make -C doc html

%install
%python_install

install -d %buildroot%_sysconfdir
install -m644 ~/.aksetup-defaults.py \
	%buildroot%_sysconfdir/aksetup-defaults.py

%files
%doc PKG-INFO
%_sysconfdir/*
%python_sitelibdir/*

%files docs
%doc doc/.build/html
%doc examples

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2014.1-alt1.1
- rebuild with boost 1.57.0

* Thu Jun 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.1-alt1
- Initial build for Sisyphus

