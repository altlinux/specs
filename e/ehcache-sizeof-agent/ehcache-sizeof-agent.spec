# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          ehcache-sizeof-agent
Version:       1.0.1
Release:       alt2_4jpp7
Summary:       Ehcache Size Of Agent
Group:         Development/Java
License:       ASL 2.0
URL:           http://www.terracotta.org/
# svn export http://svn.terracotta.org/svn/ehcache/tags/sizeof-agent-1.0.1
# tar czf ehcache-sizeof-agent-1.0.1.tar.gz sizeof-agent-1.0.1
Source0:       %{name}-%{version}.tar.gz
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-shared
BuildRequires: maven-compiler-plugin
BuildRequires: maven-gpg-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-pmd-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-jar-plugin
BuildRequires: ehcache-parent
Requires: ehcache-parent
Requires: jpackage-utils
BuildArch: noarch
Source44: import.info


%description
Ehcache is a widely used, pure Java, in-process, distributed cache.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep

%setup -q -n sizeof-agent-%{version}

%build
mvn-rpmbuild install javadoc:aggregate 

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 target/sizeof-agent-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/sizeof-agent-1.0.1-javadoc.jar $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2jpp7
- new version

