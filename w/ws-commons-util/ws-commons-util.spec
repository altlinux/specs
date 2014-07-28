Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           ws-commons-util
Version:        1.0.1
Release:        alt1_26jpp7
Summary:        Common utilities from the Apache Web Services Project

Group:          System/Libraries
License:        ASL 2.0
URL:            http://apache.osuosl.org/ws/commons/util/
Source0:        http://apache.osuosl.org/ws/commons/util/sources/ws-commons-util-1.0.1-src.tar.gz
Patch0:         %{name}-addosgimanifest.patch
# Remove maven-eclipse-plugin from build dependencies to simplify the
# dependency chain.
Patch1:         %{name}-maven-eclipse-plugin.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils >= 1.5
BuildRequires:  maven-local
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  java-javadoc

Requires:       jpackage-utils
Source44: import.info

%description
This is version 1.0.1 of the common utilities from the Apache Web
Services Project.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch0
%patch1

%build
mvn-rpmbuild install javadoc:javadoc

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# install maven pom file
install -Dm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# ... and maven depmap
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.ws.commons.util:%{name}"

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pR target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
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

