# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-parent
Version:        20
Release:        alt1_2jpp7
Summary:        Apache Maven parent POM

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org
Source0:        http://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.5-5

Requires:          jpackage-utils
Requires(post):    jpackage-utils >= 0:1.7.5-5
Requires(postun):  jpackage-utils >= 0:1.7.5-5
Source44: import.info

%description
Apache Maven parent POM file used by other Maven projects.

%prep
%setup -q

%build
#nothing to do for the pom

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom

%files
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_2jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

