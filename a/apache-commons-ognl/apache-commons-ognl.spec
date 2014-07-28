# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oversion 4.0-incubating-SNAPSHOT

Name:           apache-commons-ognl
Version:        3.0.2
Release:        alt2_4.20120313svn1102435jpp7
Summary:        Object Graph Navigation Library

Group:          Development/Java
License:        ASL 2.0
URL:            http://commons.apache.org/ognl/
# svn export -r1102435 http://svn.apache.org/repos/asf/commons/proper/ognl/trunk/ apache-commons-ognl-3.0.2
# tar caf apache-commons-ognl-3.0.2.tar.xz apache-commons-ognl-3.0.2
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-surefire-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: javassist
BuildRequires: junit
BuildRequires: jna
Requires:      javassist
Requires:      jpackage-utils
Source44: import.info

%description
OGNL is an expression language for getting and setting properties of
Java objects, plus other extras such as list projection and selection
and lambda expressions.

%package javadoc
Summary:      API documentation for %{name}
Group:        Development/Java
Requires:     jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 

%build
mvn-rpmbuild install javadoc:javadoc

%install
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/commons-ognl-%{oversion}.jar %{buildroot}%{_javadir}/%{name}.jar

install -d -m 755 %{buildroot}%{_mavenpomdir}
cp pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

install -d -m 755 %{buildroot}%{_javadocdir}
cp -rp target/site/apidocs %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_4.20120313svn1102435jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_2.20120313svn1102435jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_2.20120313svn1102435jpp7
- new version

