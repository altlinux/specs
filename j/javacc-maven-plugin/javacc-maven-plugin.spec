BuildRequires: maven-plugin-plugin
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           javacc-maven-plugin
Version:        2.6
Release:        alt3_10jpp7
Summary:        JavaCC Maven Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://mojo.codehaus.org/javacc-maven-plugin/
#svn export http://svn.codehaus.org/mojo/tags/javacc-maven-plugin-2.6
#tar cjf javacc-maven-plugin-2.6.tar.bz2 javacc-maven-plugin-2.6
Source0:        javacc-maven-plugin-2.6.tar.bz2
Patch0:         javacc-maven-plugin-pom.patch

BuildArch: noarch

BuildRequires: maven-local
BuildRequires: javacc >= 5.0
BuildRequires: plexus-utils
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-compiler-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: mojo-parent
BuildRequires: plexus-containers-component-javadoc
BuildRequires: junit
Requires: javacc >= 5.0
Requires: plexus-utils
Requires: jpackage-utils
Requires: mojo-parent
Source44: import.info

%description
Maven Plugin for processing JavaCC grammar files.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0 -b .sav

%build
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  package javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc src/main/resources/NOTICE

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_10jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt2_10jpp7
- fixed build

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_10jpp7
- fc update

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_7jpp6
- new version

