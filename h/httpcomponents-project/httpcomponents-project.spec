BuildRequires: /proc
BuildRequires: jpackage-compat
Name:              httpcomponents-project
Summary:           Common POM file for HttpComponents
Version:           4.1.1
Release:           alt1_4jpp7
Group:             Development/Java
License:           ASL 2.0
URL:               http://hc.apache.org/
# svn export -r 1050387 http://svn.apache.org/repos/asf/httpcomponents/project httpcomponents-project-4.1.1
# tar cJvf httpcomponents-project-4.1.1.tar.xz httpcomponents-project-4.1.1
Source0:           httpcomponents-project-%{version}.tar.xz
Patch0:            0001-Clean-pom.patch
BuildArch:         noarch

BuildRequires:     jpackage-utils

# Requires are dependencies from pom.xml. This project should only be required for building with maven.
Requires:          jpackage-utils
Requires:          maven
Requires:          maven-antrun-plugin
Requires:          maven-assembly-plugin
Requires:          maven-clean-plugin
Requires:          maven-compiler-plugin
Requires:          maven-deploy-plugin
Requires:          maven-gpg-plugin
Requires:          maven-install-plugin
Requires:          maven-jar-plugin
Requires:          maven-javadoc-plugin
Requires:          maven-plugin-jxr
Requires:          maven-project-info-reports-plugin
Requires:          maven-release-plugin
Requires:          maven-resources-plugin
Requires:          maven-site-plugin
Requires:          maven-source-plugin
Requires:          maven-surefire-plugin
Requires:          maven-surefire-report-plugin
Requires:          maven-release-plugin
Requires:          maven-plugin-jxr
Requires:          maven-plugin-bundle

Requires(post):    jpackage-utils
Requires(postun):  jpackage-utils
Source44: import.info

Obsoletes: hc-project < 4.1.1-alt1_1jpp6
Provides: hc-project = %version-%release

%description
Common Maven POM  file for HttpComponents. This project should be
required only for building dependant packages with Maven. Please don't
use it as runtime requirement.

%prep
%setup -q
%patch0 -p1

%install
%{__install} -D -m 0644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP.httpcomponents-project.pom
%add_to_maven_depmap org.apache.httpcomponents project %{version} JPP/httpcomponents project

%files
%doc LICENSE.txt
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.%{name}.pom

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_4jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

