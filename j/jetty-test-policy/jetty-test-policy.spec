BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-test-policy
Version:        1.2
Release:        alt1_4jpp7
Summary:        Jetty test policy files

Group:          Development/Java
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
#Source1:        .rpmlint
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  jetty-toolchain
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-surefire-provider-junit

Requires:       maven
Requires:       jpackage-utils
Requires:       jetty-toolchain
Source44: import.info

%description
Jetty test policy files

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
mvn-rpmbuild install javadoc:aggregate

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -Dp -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp7
- new version

