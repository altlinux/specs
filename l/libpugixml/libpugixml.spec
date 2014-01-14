%define rname pugixml

Name:           libpugixml
Version:        1.0
Release:        alt2
Summary:        A light-weight C++ XML processing library

Group:          System/Libraries
License:        MIT
URL:            http://pugixml.org

Source0:        http://pugixml.googlecode.com/files/%rname-%version.tar.gz
Patch0:         pugixml-1.0-set_lib_soversion.patch

BuildRequires:  ctest cmake
BuildRequires:  gcc-c++
Provides:	%rname = %version-%release

%description
pugixml is a light-weight C++ XML processing library.
It features:
- DOM-like interface with rich traversal/modification capabilities
- Extremely fast non-validating XML parser which constructs the DOM tree
  from an XML file/buffer
- XPath 1.0 implementation for complex data-driven tree queries
- Full Unicode support with Unicode interface variants and automatic
  encoding conversions


%package devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires: 	%name = %version-%release
Provides: 	%rname-devel = %version-%release

%description devel
Development files for package %{name}

%prep
%setup -q -n %rname-%version
%patch0
cp scripts/CMakeLists.txt .

%build
%cmake -DBUILD_SHARED_LIBS=1
%make_build -C BUILD

%install
mkdir -p %buildroot%_datadir/%rname/contrib/
mkdir -p %buildroot%_includedir/
mkdir -p %buildroot%_libdir/
install -p -m 0644 contrib/* %buildroot%_datadir/%rname/contrib/
install -p -m 0644 src/*.hpp %buildroot%_includedir/
install -p -m 0755 BUILD/*.so %buildroot%_libdir/

%files
%doc readme.txt
%_libdir/*.so.*

%files devel
%doc docs/*
%_libdir/*.so
%_datadir/%rname
%_includedir/*.hpp

%changelog
* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Build in Sisyphus under name libpugixml

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- initial fc import

