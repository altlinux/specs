Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           javacc-maven-plugin
Version:        2.6
Release:        alt5_21jpp8
Summary:        JavaCC Maven Plugin
License:        ASL 2.0
URL:            http://mojo.codehaus.org/javacc-maven-plugin/
BuildArch:      noarch

#svn export http://svn.codehaus.org/mojo/tags/javacc-maven-plugin-2.6
#tar cjf javacc-maven-plugin-2.6.tar.bz2 javacc-maven-plugin-2.6
Source0:        javacc-maven-plugin-2.6.tar.bz2
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         javacc-maven-plugin-pom.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
Maven Plugin for processing JavaCC grammar files.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
%patch0 -b .sav
cp -p %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt src/main/resources/NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt src/main/resources/NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_21jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_20jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_15jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_14jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_10jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt2_10jpp7
- fixed build

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_10jpp7
- fc update

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_7jpp6
- new version

