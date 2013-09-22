# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# Automatically added by buildreq on Wed Aug 21 2013
# optimized out: cmake cmake-modules libstdc++-devel pkg-config
BuildRequires: ctest dos2unix gcc-c++ libpcre-devel libxml2-devel

# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname openCOLLADA
# Upstream does not maintain a soversion so we define one here.
# abi-compliance-checker will be used to determine if an abi breakage occurs
# and the soversion will be incremented.
%global sover 0.1

%global commit 828b60384552b83e55d2af7055f07d2c40b4d3f4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global upname OpenCOLLADA


Name:           libopenCOLLADA
Version:        0
Release:        alt2.git%{shortcommit}
License:        MIT
Summary:        Collada 3D import and export libraries
Url:            https://collada.org/mediawiki/index.php/OpenCOLLADA

Source0:        https://github.com/KhronosGroup/OpenCOLLADA/archive/%{commit}/%{upname}-%{shortcommit}.tar
Source1:        Changelog

Patch0:         openCOLLADA-svn863-cmake.patch
Patch1:         openCOLLADA-svn863-libs.patch
Patch2:         openCOLLADA-smp_build.patch
Patch3:         openCOLLADA-svn871-memcpy.patch
Patch4:         openCOLLADA-non-existant_includes.patch
Patch5:         openCOLLADA-svn876-no_var_tracking_assigenments.patch

#?BuildRequires:  libfftw3-devel
#?BuildRequires:  zlib-devel
Source44: import.info
Provides: openCOLLADA = %{version}-%{release}

Conflicts: blender <= 2.68a-alt1

%description 
COLLADA is a royalty-free XML schema that enables digital asset
exchange within the interactive 3D industry.
OpenCOLLADA is a Google summer of code opensource project providing
libraries for 3D file interchange between applications like blender.
COLLADABaseUtils          Utils used by many of the other projects
COLLADAFramework          Datamodel used to load COLLADA files
COLLADAStreamWriter       Sources (Library to write COLLADA files)
COLLADASaxFrameworkLoader Library that loads COLLADA files in a sax
                          like manner into the framework data model
COLLADAValidator          XML validator for COLLADA files, based on
                          the COLLADASaxFrameworkLoader
GeneratedSaxParser        Library used to load xml files in the way
                          used by COLLADASaxFrameworkLoader

%package        doc
Summary:        Developer documentation for %{oldname}
Group:          Documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides: openCOLLADA-doc = %{version}-%{release}

%description doc
This package provides documentation for %{oldname}.

%package        devel
Summary:        Include files for openCOLLADA development
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides: openCOLLADA-devel = %{version}-%{release}

%description devel
This package provides the include files necessary to build and
develop with the %{oldname} export and import libraries.

%package        utils
Summary:        XML validator for COLLADA files
Group:          Development/Tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides: openCOLLADA-utils = %{version}-%{release}

%description utils
XML validator for COLLADA files, based on the COLLADASaxFrameworkLoader.


%prep
%setup -q -n %{upname}-%{commit}
%patch0 -p1 -b .cmake
%patch1 -p1 -b .libs
#patch2 -p1 -b .smp
#patch4 -p1 -b .includes
%patch5 -p1 -b .no_var_trk

# Remove unused bundled libraries
rm -rf Externals/{Cg,expat,lib3ds,LibXML,MayaDataModel,pcre,zlib,zziplib}

# Add some docs, need to fix eol encoding with dos2unix in some files.
find ./ -name .project -delete
cp -pf COLLADAStreamWriter/README README.COLLADAStreamWriter
cp -pf COLLADAStreamWriter/LICENSE ./

iconv -f ISO_8859-1 -t utf-8 COLLADAStreamWriter/AUTHORS > \
  COLLADAStreamWriter/AUTHORS.tmp
touch -r COLLADAStreamWriter/AUTHORS COLLADAStreamWriter/AUTHORS.tmp
mv COLLADAStreamWriter/AUTHORS.tmp COLLADAStreamWriter/AUTHORS

dos2unix -f -k README.COLLADAStreamWriter
dos2unix -f -k LICENSE
dos2unix -f -k README
find htdocs/ -name *.php -exec dos2unix -f {} \;
find htdocs/ -name *.css -exec dos2unix -f {} \;

# Install Changelog
install -p -m 0644 %{S:1} ./


%build
rm -rf Build && mkdir -p Build && pushd Build
%{fedora_cmake} -DUSE_STATIC=OFF \
       -DUSE_SHARED=ON \
       -Dsoversion=%{sover} \
       -DCMAKE_SKIP_RPATH=ON \
       -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
       ../

make %{?_smp_mflags}


%install
pushd Build
make DESTDIR=%{buildroot} install

# Manually install binary
mkdir -p %{buildroot}%{_bindir}/
install -p -m 0755 bin/* %{buildroot}%{_bindir}/

popd

# Install MathMLSolver headers
mkdir -p %{buildroot}%{_includedir}/MathMLSolver
cp -a Externals/MathMLSolver/include/* %{buildroot}%{_includedir}/MathMLSolver/


%files
%doc README LICENSE README.COLLADAStreamWriter COLLADAStreamWriter/AUTHORS Changelog
%{_libdir}/lib*.so.%{sover}

%files doc
%doc htdocs/

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/cmake/OpenCOLLADA/*.cmake

%files utils
%{_bindir}/*


%changelog
* Wed Aug 21 2013 Andrey Liakhovets <aoliakh@altlinux.org> 0-alt2.git828b603
- blender bug #36325 fixed: "Collada Import: Vertex-Groups missing"
- devel: *.cmake files packaged
- conflict with blender <= 2.68a-alt1 added
- updated patches: cmake, libs
- dropped patches (fixed in upstream): smp_build, non-existant_includes
- removed:
 - BuildRequires: zlib-devel, libfftw3-devel (by buildreq)
 - fedora el6 test for cmake28

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_16.git9665d16
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_15.git9665d16
- update to new release by fcimport

* Sun Apr 28 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_14.svn871
- initial fc import

