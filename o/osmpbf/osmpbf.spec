Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: zlib-devel
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           osmpbf
Version:        1.5.0
Release:        alt1_6jpp11
Summary:        C library to read and write OpenStreetMap PBF files

License:        LGPLv3
URL:            https://github.com/openstreetmap/OSM-binary
Source0:        https://github.com/openstreetmap/OSM-binary/archive/v%{version}/OSM-binary-%{version}.tar.gz

BuildRequires:  ctest cmake gcc-c++
BuildRequires:  libprotobuf-devel protobuf-java protobuf-compiler
BuildRequires:  maven-local maven-source-plugin
BuildRequires:  junit
Source44: import.info

%description
Osmpbf is a Java/C library to read and write OpenStreetMap PBF files.
PBF (Protocol buffer Binary Format) is a binary file format for OpenStreetMap
data that uses Google Protocol Buffers as low-level storage.

%package tools
Group: Development/Java
Summary:        Tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description tools
This package contains tools that use %{name}.

%package devel
Group: Development/Java
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%package java
Group: Development/Java
Summary:        Java OpenStreetMap PBF file format library
BuildArch:      noarch

%description java
Osmpbf is a Java/C library to read and write OpenStreetMap PBF files.
PBF (Protocol buffer Binary Format) is a binary file format for OpenStreetMap
data that uses Google Protocol Buffers as low-level storage.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n OSM-binary-%{version}

%pom_remove_plugin :protobuf-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin


%build
%{fedora_v2_cmake}
%fedora_v2_cmake_build
protoc --java_out=src.java src/osmformat.proto
protoc --java_out=src.java src/fileformat.proto
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%fedora_v2_cmake_install
rm %{buildroot}/%{_libdir}/libosmpbf.a
%mvn_install


%files
%doc README.md CHANGELOG.md
%doc --no-dereference LICENSE
%{_libdir}/libosmpbf.so.1
%{_libdir}/libosmpbf.so.1.*


%files tools
%{_bindir}/*
%{_mandir}/man1/*


%files devel
%{_includedir}/osmpbf
%{_libdir}/libosmpbf.so


%files java -f .mfiles
%doc --no-dereference LICENSE


%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Tue Aug 10 2021 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_6jpp11
- fixed build

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_3jpp11
- new version

