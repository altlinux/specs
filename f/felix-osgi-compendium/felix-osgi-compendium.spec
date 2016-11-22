# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global bundle org.osgi.compendium

Name:    felix-osgi-compendium
Version: 1.4.0
Release: alt5_22jpp8
Summary: Felix OSGi R4 Compendium Bundle
Group:   Development/Other
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

BuildRequires: javapackages-tools rpm-build-java
BuildRequires: maven-local
BuildRequires: felix-osgi-core
BuildRequires: felix-osgi-foundation
BuildRequires: felix-parent
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mockito

Source44: import.info

%description
OSGi Service Platform Release 4 Compendium Interfaces and Classes.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

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

%mvn_file :%{bundle} "felix/%{bundle}"
%mvn_alias "org.apache.felix:%{bundle}" "org.osgi:%{bundle}"

%build
%mvn_build -- -Drat.numUnapprovedLicenses=100

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt5_22jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt5_21jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_16jpp7
- new release

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

