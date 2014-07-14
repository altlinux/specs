BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-parent
Version:        19
Release:        alt2_4jpp7
Summary:        Jetty parent POM file

Group:          Development/Java
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://repo1.maven.org/maven2/org/eclipse/jetty/%{name}/%{version}/%{name}-%{version}.pom
# rpmlint config file (fedpkg lint will use this)
Source1:        .rpmlint
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven

Requires:       jpackage-utils
Source44: import.info

%description
Jetty parent POM file

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE0} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 19-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 19-alt1_4jpp7
- new version

