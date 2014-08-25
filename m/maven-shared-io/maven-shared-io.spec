Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-shared-io
Version:        1.1
Release:        alt1_5jpp7
# Maven-shared defines maven-shared-io version as 1.2
Epoch:          1
Summary:        API for I/O support like logging, download or file scanning.
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-io
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-shared-io-1.1 maven-shared-io-1.1
# tar caf maven-shared-io-1.1.tar.xz maven-shared-io-1.1/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  easymock

Obsoletes:      maven-shared-io < %{epoch}:%{version}-%{release}
Provides:       maven-shared-io = %{epoch}:%{version}-%{release}
Source44: import.info

%description
API for I/O support like logging, download or file scanning.

This is a replacement package for maven-shared-io

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q

%pom_add_dep org.apache.maven:maven-compat

# Failing tests
rm src/test/java/org/apache/maven/shared/io/location/ArtifactLocatorStrategyTest.java
rm src/test/java/org/apache/maven/shared/io/download/DefaultDownloadManagerTest.java

cp %{SOURCE1} LICENSE.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_5jpp7
- update

* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

