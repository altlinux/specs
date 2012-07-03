Name: paraview-data
Version: 3.8.1
Release: alt1
Summary: Data files for ParaView (Scientific Visualization)
# http://www.paraview.org/paraview/project/license.html
License: ParaView License Version 1.2
Group: Sciences/Other
Url: http://www.paraview.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.paraview.org/files/v3.8/ParaViewData-3.8.1.zip
BuildArch: noarch

BuildPreReq: unzip

%description
Summary: Data files for ParaView (Scientific Visualization)

%install
install -d %buildroot%_datadir
pushd %buildroot%_datadir
unzip %SOURCE0
popd

%files
%_datadir/*

%changelog
* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus

