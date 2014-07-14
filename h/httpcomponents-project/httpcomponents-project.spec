BuildRequires: /proc
BuildRequires: jpackage-compat
Name:              httpcomponents-project
Summary:           Common POM file for HttpComponents
Version:           6
Release:           alt2_1jpp7
Group:             Development/Java
License:           ASL 2.0
URL:               http://hc.apache.org/
# svn export http://svn.apache.org/repos/asf/httpcomponents/project/tags/%{version} %{name}-%{version}
# tar cJf %{name}-%{version}.tar.xz %{name}-%{version}
Source:            %{name}-%{version}.tar.xz
BuildArch:         noarch

BuildRequires:     jpackage-utils

# Requires are dependencies from pom.xml. This project should only be required for building with maven.
Requires:          jpackage-utils
Requires:          maven
Requires:          maven-compiler-plugin
Requires:          maven-gpg-plugin
Requires:          maven-jar-plugin
Requires:          maven-project-info-reports-plugin
Requires:          maven-site-plugin
Source44: import.info

Obsoletes: hc-project < 4.1.1-alt1_1jpp6
Provides: hc-project = %version-%release

%description
Common Maven POM  file for HttpComponents. This project should be
required only for building dependant packages with Maven. Please don't
use it as runtime requirement.

%prep
%setup -q
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :maven-notice-plugin

%install
install -dm 755 %{buildroot}/%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}.pom
%add_maven_depmap JPP.%{name}.pom

%files
%doc LICENSE.txt NOTICE.txt
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.%{name}.pom

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 6-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 6-alt1_1jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_4jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

