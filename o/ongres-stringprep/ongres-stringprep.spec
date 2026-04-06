Name:           ongres-stringprep
Version:        2.2
Release:        alt1

Summary:        Stringprep (RFC 3454) Java implementation
License:        BSD-2-Clause
Group:          Development/Java
URL:            https://github.com/ongres/stringprep
VCS:            https://github.com/ongres/stringprep

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildArch:  noarch

%description
The stringprep protocol does not stand on its own;
it has to be used by other protocols at precisely-defined
places in those other protocols.

%javadoc_package

%prep
%setup

%pom_remove_dep org.junit:junit-bom parent
 
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:archive' '
<manifestEntries>
  <Multi-Release>true</Multi-Release>
</manifestEntries>
' parent

%mvn_package com.ongres.stringprep:codegenerator __noinstall


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Fri Mar 20 2026 Evgeniy Serov <scala@altlinux.org> 2.2-alt1
- Updated to 2.2.

* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 1.1-alt1_2jpp11
- new version

