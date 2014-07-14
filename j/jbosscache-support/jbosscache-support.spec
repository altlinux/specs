Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:    jbosscache-support
Version: 1.6
Release: alt4_2jpp7
Summary: JBossCache support package

Group:   Development/Java
License: LGPL
URL:     http://www.jboss.org/jbosscache
# svn export http://anonsvn.jboss.org/repos/jbosscache/support/tags/1.6 jbosscache-support-1.6
# tar cJf jbosscache-support-1.6.tar.xz jbosscache-support-1.6
Source0: %{name}-%{version}.tar.xz

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: jpackage-utils

Requires:      jpackage-utils

BuildArch:     noarch
Source44: import.info

%description
JBossCache support package is required by jbosscache.

%package -n jbosscache-common-parent
Summary:  Parent pom for jbosscache
Group:    Development/Java
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n jbosscache-common-parent
The jbosscache-common-parent package contains the parent pom file
required by jbosscache.

%package xslt
Summary:  Xslt doc support for jbosscache
Group:    Development/Java
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description xslt
The %{name}-xslt package contains xslt doc support for jbosscache.

%prep
%setup -q
find . -name \*.jar -exec rm -f {} \;

%build
# Does not include javadocs or tests
mvn-rpmbuild install -Dmaven.test.skip=true

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 xslt/target/jbosscache-doc-xslt-support-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-xslt.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -m 644 common/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-jbosscache-common-parent.pom
install -m 644 xslt/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-xslt.pom

%add_maven_depmap JPP-%{name}-xslt.pom %{name}-xslt.jar
%add_maven_depmap JPP-jbosscache-common-parent.pom -a 'org.jboss.cache:jbosscache-common-parent'
%add_maven_depmap JPP-%{name}.pom -a 'org.jboss.cache:jbosscache-support'

%files
%doc README-Maven.txt
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files -n jbosscache-common-parent
%doc README-Maven.txt
%{_mavenpomdir}/JPP-jbosscache-common-parent.pom

%files xslt
%doc README-Maven.txt
%{_javadir}/%{name}-xslt.jar
%{_mavenpomdir}/JPP-%{name}-xslt.pom

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt4_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt3_2jpp7
- new version

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt3_2jpp6
- fixed build

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp6
- fixed build with maven3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp6
- new version

