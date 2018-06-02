Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-osgi
Version:        0.2.0
Release:        alt1_15jpp8
# Maven-shared defines maven-osgi version as 0.3.0
Epoch:          1
Summary:        Library for Maven-OSGi integration
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-osgi
BuildArch:      noarch

# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-osgi-0.2.0 maven-osgi-0.2.0
# find -name *.jar -delete
# tar caf maven-osgi-0.2.0.tar.xz maven-osgi-0.2.0/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute:bndlib)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)

Obsoletes:      maven-shared-osgi < %{epoch}:%{version}-%{release}
Provides:       maven-shared-osgi = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Library for Maven-OSGi integration.

This is a replacement package for maven-shared-osgi

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
cp -p %{SOURCE1} LICENSE

sed -i 's/import aQute\.lib\.osgi/import aQute.bnd.osgi/g' src/main/java/org/apache/maven/shared/osgi/DefaultMaven2OsgiConverter.java

# Replace plexus-maven-plugin with plexus-component-metadata
%pom_xpath_set "pom:plugin[pom:artifactId[text()='plexus-maven-plugin']]//pom:goal[text()='descriptor']" generate-metadata
%pom_xpath_set "pom:artifactId[text()='plexus-maven-plugin']" plexus-component-metadata

%build
# Tests depend on binary JARs which were removed from sources
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.2.0-alt1_15jpp8
- java fc28+ update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.2.0-alt1_14jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.2.0-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.2.0-alt1_12jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.2.0-alt1_11jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.2.0-alt1_4jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.2.0-alt1_0jpp7
- new release

