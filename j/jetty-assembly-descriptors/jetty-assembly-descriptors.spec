# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-assembly-descriptors
Version:        1.0
Release:        alt3_7jpp7
Summary:        Jetty assembly descriptors used for building

Group:          Development/Java
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
BuildArch:      noarch

Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        http://www.eclipse.org/legal/epl-v10.html

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  jetty-toolchain
BuildRequires:  maven-surefire-provider-junit

Requires:       maven
Requires:       jpackage-utils
Requires:       jetty-toolchain
Source44: import.info

%description
Jetty assembly descriptors used for building

%prep
%setup -q
cp -p %{SOURCE1} %{SOURCE2} .

%build
mvn-rpmbuild install javadoc:aggregate

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
# bug in upstream pom. It inherits version from toolchain parent
install -Dp -m 644 target/%{name}-1.4.jar %{buildroot}%{_javadir}/%{name}.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE-2.0.txt epl-v10.html
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4jpp7
- new version

