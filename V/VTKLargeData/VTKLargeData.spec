Name: VTKLargeData
Version: 1.1
Release: alt1.git20120227
Summary: Large data files for examples of The Visualization Toolkit (VTK)
License: MIT
Group: Development/Tools
Url: http://www.vtk.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

%description
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains large data files for examples of VTK.

%install
install -d %buildroot%_datadir
cd %buildroot%_datadir
tar -xf %SOURCE0
rm -fR %name/.gear

for i in $(find ./); do
	touch $i
done

%files
%_datadir/*

%changelog
* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20120227
- New snapshot

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20110728
- Initial build for Sisyphus

