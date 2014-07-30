# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-distribution-remote-resources
Version:        1.1
Release:        alt3_6jpp7
Summary:        Jetty toolchain artifact for distribution remote resources

Group:          Development/Java
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  jetty-toolchain

Requires:       jpackage-utils
Requires:       maven
Requires:       maven-remote-resources-plugin
Requires:       jetty-toolchain
Source44: import.info

%description
Jetty toolchain artifact for distribution remote distribution resources

%prep
%setup -q

%build
mvn-rpmbuild install javadoc:aggregate

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -Dp -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc src/main/resources/LICENSE*
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp7
- new version

