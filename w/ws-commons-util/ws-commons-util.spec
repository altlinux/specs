Epoch: 1
Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ws-commons-util
Version:        1.0.2
Release:        alt1_6jpp8
Summary:        Common utilities from the Apache Web Services Project

License:        ASL 2.0
URL:            http://ws.apache.org/commons/util

# svn checkout http://svn.apache.org/repos/asf/webservices/commons/tags/util/1.0.2/ ws-commons-util-1.0.2
# tar cJf ws-commons-util-1.0.2.tar.xz ws-commons-util-1.0.2
Source0:        ws-commons-util-1.0.2.tar.xz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
This is version 1.0.2 of the common utilities from the Apache Web
Services Project.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%mvn_file : %{name}
%mvn_alias org.apache.ws.commons:ws-commons-util org.apache.ws.commons.util:ws-commons-util
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.apache.ws.commons.util</Bundle-SymbolicName>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-Localization>plugin</Bundle-Localization>
    <Bundle-Version>${project.version}</Bundle-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

# This dep is supplied by the JRE
%pom_remove_dep "xml-apis:xml-apis"

# Avoid unnecessary runtime dependency on junit, used for tests only
%pom_xpath_inject 'pom:dependency[pom:artifactId="junit"]' "<scope>test</scope>"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_6jpp8
- fc27 update

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_32jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_27jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_26jpp7
- new release

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_23jpp7
- fc update

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_3jpp6
- dropped velocity14

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_3jpp6
- new jpp release; build with velocity 14

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_2jpp5
- build with velocity 15

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- added OSGi provides

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

