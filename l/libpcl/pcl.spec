# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
BuildRequires: vtk-python libgomp-devel
%add_optflags %optflags_shared
%define oldname pcl
Name:           libpcl
Version:        1.6.0
Release:        alt1_2
Summary:        Library for point cloud processing

Group:          System/Libraries
License:        BSD
URL:            http://pointclouds.org/
Source0:        http://www.pointclouds.org/assets/files/1.6.0/PCL-1.6.0-Source.tar.bz2
Patch0:         PCL-1.4.0-Source-fedora.patch
Patch1:         pcl-1.5.1-gcc47.patch

# For plain building
BuildRequires:  ctest cmake gcc-c++ boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel
# Documentation
BuildRequires:  doxygen graphviz python-module-sphinx
%if ! 0%{?rhel} || 0%{?rhel} >= 6
BuildRequires:  texlive-latex-recommended
%else
BuildRequires:  /usr/bin/latex texlive-latex-recommended
%endif

# mandatory
BuildRequires:  eigen3 flann-devel cminpack-devel libvtk-devel libgl2ps-devel
# optional
BuildRequires:  qhull-devel libusb-devel libgtest-devel libqt4-devel
%ifarch %{ix86} x86_64
BuildRequires:  openni-devel
%endif
Source44: import.info
Provides: pcl = %{version}-%{release}

%description
The Point Cloud Library (or PCL) is a large scale, open project for point
cloud processing.

The PCL framework contains numerous state-of-the art algorithms including
filtering, feature estimation, surface reconstruction, registration, model
fitting and segmentation. 

%package        devel
Summary:        Development files for %{oldname}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Provides: pcl-devel = %{version}-%{release}

%description    devel
The %%{oldname}-devel package contains libraries and header files for
developing applications that use %%{oldname}.


%package        tools
Summary:        Point cloud tools and viewers
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}
Provides: pcl-tools = %{version}-%{release}

%description    tools
This package contains tools for point cloud file processing and viewers
for point cloud files and live Kinect data.


%package        doc
Summary:        PCL API documentation
Group:          Documentation
%if ! 0%{?rhel} || 0%{?rhel} >= 6
BuildArch:      noarch
%endif
Provides: pcl-doc = %{version}-%{release}

%description    doc
The %%{oldname}-doc package contains API documentation for the Point Cloud
Library.


%prep
%setup -q -n PCL-%{version}-Source
%patch0 -p2 -b .fedora

# Just to make it obvious we're not using any of these
rm -rf  3rdparty


%build
mkdir build
pushd build
%{fedora_cmake} \
  -DCMAKE_BUILD_TYPE=NONE \
  -DOPENNI_INCLUDE_DIR:PATH=/usr/include/ni \
  -DLIB_INSTALL_DIR=$(echo %{_libdir} | sed -e 's|%{_prefix}/||') \
  -DPCL_PKGCONFIG_SUFFIX:STRING="" \
  -DBUILD_documentation=ON \
  -DCMAKE_SKIP_RPATH=ON \
  ..

# Don't use mflags, we're hitting out of memory errors on the koji builders
make 
make -j 2
#%{?_smp_mflags}
make doc
popd

pushd doc/overview
make
popd

pushd doc/tutorials
sed -i "s/, 'sphinxcontrib.doxylink.doxylink'//" content/conf.py
make
popd

pushd doc/advanced
make
popd


%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Just a dummy test
rm $RPM_BUILD_ROOT%{_bindir}/timed_trigger_test

#mv $RPM_BUILD_ROOT%{_datadir}/doc/%{oldname} $RPM_BUILD_ROOT%{_datadir}/doc/%{oldname}-%{version}
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{oldname}
mv doc/doxygen/html doc/doxygen/api

popd

mv doc/tutorials/html doc/tutorials/tutorials

for f in $RPM_BUILD_ROOT%{_bindir}/{openni_image,pcd_grabber_viewer,pcd_viewer,openni_viewer,oni_viewer}; do
	mv $f $RPM_BUILD_ROOT%{_bindir}/pcl_$(basename $f)
done
rm $RPM_BUILD_ROOT%{_bindir}/{openni_fast_mesh,openni_ii_normal_estimation,openni_voxel_grid}

mkdir -p $RPM_BUILD_ROOT%{_libdir}/cmake/pcl
mv $RPM_BUILD_ROOT%{_datadir}/%{oldname}-*/*.cmake $RPM_BUILD_ROOT%{_libdir}/cmake/pcl

# Remove installed documentation, will add with doc tags later
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{oldname}-1.6

#mv $RPM_BUILD_ROOT%{_libdir}/pcl/*.cmake $RPM_BUILD_ROOT%{_libdir}/cmake/pcl
#rmdir $RPM_BUILD_ROOT%{_libdir}/pcl

# This is required to fix crashes in programs linked against pcl_visualization lib
#sed -i -e 's/vtkWidgets/vtkRendering/' $RPM_BUILD_ROOT%{_libdir}/cmake/pcl/PCLDepends-release.cmake

# At the moment fails due to RPATH problem
# (RPATH not built into test apps as required)
#%check
#cd build
#make test

%files
%doc AUTHORS.txt LICENSE.txt
%{_libdir}/*.so.*
%{_datadir}/%{oldname}-1.6

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/pcl

%files tools
%{_bindir}/pcl_*
# There are no .desktop files because the GUI tools are rather examples
# to understand a particular feature of PCL.

%files doc
%doc build/doc/doxygen/api
%doc doc/tutorials/tutorials


%changelog
* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- initial fc import

