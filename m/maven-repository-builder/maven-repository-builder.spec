Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global pkg_version 1.0-alpha-2

Name:           maven-repository-builder
Version:        1.0
# See http://fedoraproject.org/wiki/Packaging:NamingGuidelines#Package_Versioning
Release:        alt1_0.3.alpha2jpp7
# Maven-shared defines maven-repository-builder version as 1.0
Epoch:          1
Summary:        Maven repository builder
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-repository-builder/

# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-repository-builder-1.0-alpha-2 maven-repository-builder-1.0-alpha-2
# tar caf maven-repository-builder-1.0-alpha-2.tar.xz maven-repository-builder-1.0-alpha-2/
Source0:        %{name}-%{pkg_version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  easymock
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-test-tools
BuildRequires:  maven-wagon
BuildRequires:  maven-shared

Obsoletes:      maven-shared-repository-builder < %{epoch}:%{version}-%{release}
Provides:       maven-shared-repository-builder = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Maven repository builder.

This is a replacement package for maven-shared-repository-builder

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{pkg_version}

# Replace plexus-maven-plugin with plexus-component-metadata
find -name 'pom.xml' -exec sed \
    -i 's/<artifactId>plexus-maven-plugin<\/artifactId>/<artifactId>plexus-component-metadata<\/artifactId>/' '{}' ';'
find -name 'pom.xml' -exec sed \
    -i 's/<goal>descriptor<\/goal>/<goal>generate-metadata<\/goal>/' '{}' ';'

# Removing JARs because of binary code contained
find -iname '*.jar' -delete

cp %{SOURCE1} LICENSE.txt

%build
# Skipping tests because they don't work without the JARs
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.3.alpha2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.0.alpha2jpp7
- new release

