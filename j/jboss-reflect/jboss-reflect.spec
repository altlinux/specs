Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jboss-reflect
Version:        2.0.2
Release:        alt4_4jpp7
Summary:        JBoss Reflection

Group:          Development/Java

License:        LGPLv2+
URL:            http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-reflect/tags/2.0.2.GA/ jboss-reflect-2.0.2
# tar cJf jboss-reflect-2.0.2.tar.xz jboss-reflect-2.0.2
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-pom.patch

BuildArch:      noarch

BuildRequires:  javassist
BuildRequires:  jboss-common-core
BuildRequires:  jboss-logging
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4

Requires:       javassist
Requires:       jboss-common-core
Requires:       jboss-logging
Requires:       jpackage-utils
Source44: import.info

%description
JBoss Reflection

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# can't compile the test dir because of missing deps
rm -rf src/test

find -type f -name *.jar -delete
find -type f -name *.class -delete

%patch0

%build
mvn-rpmbuild package javadoc:aggregate

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt4_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt4_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt3_2jpp7
- new version

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt2_4jpp6
- fixed build

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt1_4jpp6
- jpp 6 release

