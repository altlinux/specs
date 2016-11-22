Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             castor-maven-plugin
Version:          2.5
Release:          alt1_2jpp8
Summary:          Maven plugin for Castor XML's code generator
License:          ASL 2.0
URL:              http://www.mojohaus.org/castor-maven-plugin/

Source0:          https://github.com/mojohaus/castor-maven-plugin/archive/castor-maven-plugin-%{version}.tar.gz
Patch0:           duplicate-descriptors.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mojo-parent
BuildRequires:    castor >= 1.3.2
Source44: import.info

%description
The Castor plugin is a Maven plugin that provides the functionality of Castor
XML's code generator for generating Java beans and associated descriptor
classes (required for marshaling to and unmarshaling from XML documents) from
XML Schema files.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n castor-maven-plugin-castor-maven-plugin-%{version}

# Remove any pre-built binaries
find -name "*.jar" -exec rm {} \;
find -name "*.class" -exec rm {} \;

# Patch due to duplicate mojo descriptor generation
sed -i 's/\r/\n/g' src/main/java/org/codehaus/mojo/castor/ConvertDTD2XSDMojo.java
%patch0

# Missing dep on maven core/compat
%pom_add_dep org.apache.maven:maven-core
%pom_add_dep org.apache.maven:maven-compat

%build
%mvn_build -- -Denforcer.skip=true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%doc LICENSE.TXT

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_2jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_1jpp8
- unbootsrap build

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

