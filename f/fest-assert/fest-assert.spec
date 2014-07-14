BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           fest-assert
Version:        1.4
Release:        alt2_7jpp7
Summary:        FEST Fluent Assertions

Group:          Development/Java
License:        ASL 2.0
URL:            http://fest.easytesting.org

# from https://github.com/alexruiz/fest-assert-1.x/tarball/1.4
Source0:        https://github.com/alexruiz/fest-assert-1.x/tarball/1.4/fest-assert-1.x.tar.gz

BuildArch:      noarch
BuildRequires:  jpackage-utils

BuildRequires:  maven
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-dependency-plugin

BuildRequires:  fest-common = 1.0.11
BuildRequires:  fest-util = 1.2.0

Requires:       fest-common = 1.0.11
Requires:       fest-util = 1.2.0
Source44: import.info

%description
Flexible or fluent assertions for testing

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n alexruiz-fest-assert-1.x-7a64c52
sed -i 's/\r//' README.md

# skip test because this package requires junit 4.8 but we only have
# junit 4.10, which is incompatible, also, the test depend on
# fest-mocks which is not packaged because it indirectly depends a
# package not allowed in fedora due to licensing issues
%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        -e \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar  %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_7jpp7
- new version

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt4_1jpp7
- fixed build

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_1jpp7
- fixed build with maven3

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_1jpp6
- added maven2-plugin-resources dep

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_1jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_1jpp6
- new version

