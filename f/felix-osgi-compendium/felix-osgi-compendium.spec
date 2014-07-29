# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global bundle org.osgi.compendium
%global felixdir %{_javadir}/felix
%global POM %{_mavenpomdir}/JPP.felix-%{bundle}.pom

Name:    felix-osgi-compendium
Version: 1.4.0
Release: alt3_14jpp7
Summary: Felix OSGi R4 Compendium Bundle

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

Patch0:         0001-Fix-servlet-api-dependency.patch
Patch1:         0002-Fix-compile-target.patch
Patch2:         0003-Add-CM_LOCATION_CHANGED-property-to-ConfigurationEve.patch
Patch3:         0004-Add-TARGET-property-to-ConfigurationPermission.patch
# This is an ugly patch that adds getResourceURL method. This prevents jbosgi-framework
# package from bundling osgi files. Once the jbosgi-framework will be updated
# to a new version without the need for this patch, REMOVE it!
Patch4:         0005-Add-getResourceURL-method-to-make-jbosgi-framework-h.patch

BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-provider-junit4
BuildRequires: felix-osgi-core
BuildRequires: felix-osgi-foundation
BuildRequires: tomcat-servlet-3.0-api

Requires: felix-osgi-core
Requires: felix-osgi-foundation
Requires: tomcat-servlet-3.0-api
Source44: import.info

%description
OSGi Service Platform Release 4 Compendium Interfaces and Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

# fix servlet api properly
%patch0 -p1
# fix compile source/target
%patch1 -p1
# add CM_LOCATION_CHANGED property
%patch2 -p1
# add TARGET property
%patch3 -p1
# add getResourceURL method
%patch4 -p1

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jar
install -pD -T -m 644 target/%{bundle}-%{version}.jar \
  %{buildroot}%{felixdir}/%{bundle}.jar

# pom
install -pD -T -m 644 pom.xml %{buildroot}%{POM}
%add_maven_depmap JPP.felix-%{bundle}.pom felix/%{bundle}.jar -a "org.osgi:%{bundle}"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE
%{_mavendepmapfragdir}/%{name}
%{felixdir}
%{POM}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_14jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_12jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_12jpp7
- new release

* Mon Sep 05 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_3jpp6
- dropped tomcat6-servlet-2.5-api dep to fix apache-commons-chain

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_3jpp6
- new jpp release

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

