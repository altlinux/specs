BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jvnet-parent
Version:        3
Release:        alt1_1jpp7
Summary:        Java.net parent POM file

Group:          Development/Java
License:        ASL 2.0
URL:            http://www.java.net
Source0:        http://repo1.maven.org/maven2/net/java/%{name}/%{version}/%{name}-%{version}.pom

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-enforcer-plugin

Requires:       jpackage-utils
Requires:       maven
Source44: import.info

%description
Java.net parent POM file used by most Java.net subprojects such as
Glassfish

%prep
cp %{SOURCE0} pom.xml

%build
mvn-rpmbuild install

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 3-alt1_1jpp7
- new version

