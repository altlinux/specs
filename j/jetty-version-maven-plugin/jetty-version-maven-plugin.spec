BuildRequires: maven-enforcer-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-version-maven-plugin
Version:        1.0.7
Release:        alt3_4jpp7
Summary:        Jetty version management Maven plugin

Group:          Development/Java
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
#Source1:        .rpmlint
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  apache-commons-lang3
BuildRequires:  maven >= 3.0.3-14
BuildRequires:  maven-compiler-plugin
BuildRequires:  jetty-toolchain

Requires:       maven
Requires:       maven-project
Requires:       jpackage-utils
Requires:       jetty-toolchain
Requires:       apache-commons-lang3
Source44: import.info

%description
Jetty version management Maven plugin

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q

%build
pushd %{name}
# skip tests because we don't have jetty-test-helper (yet)
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -Dmaven.test.skip=true install javadoc:aggregate

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
pushd %{name}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -Dp -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
popd


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_4jpp7
- new version

