# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jboss-classpool-scoped
Version:        1.0.0
Release:        alt2_5jpp7
Summary:        A custom class pool for several JBoss products

Group:          Development/Java
License:        LGPLv2+
URL:            http://www.jboss.org/jbossreflect

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-classpool/tags/1.0.0.GA/scopedpool/ jboss-classpool-scoped-1.0.0
# tar cJf jboss-classpool-scoped-1.0.0.tar.xz jboss-classpool-scoped-1.0.0/
Source0:        jboss-classpool-scoped-1.0.0.tar.xz

Patch0:         %{name}-pom.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils

BuildRequires:  javassist
BuildRequires:  maven-local

BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin

Requires:       javassist
Requires:       jpackage-utils
Source44: import.info

%description
A custom class pool for several JBoss products.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -type f -name *.jar -delete
find -type f -name *.class -delete

%patch0

%build
mvn-rpmbuild package javadoc:aggregate

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/jboss-classpool-scoped.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp7
- new version

