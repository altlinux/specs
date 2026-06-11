Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: java-17-openjdk-devel

Name:           plantuml
Version:        1.2026.5
Release:        alt1
Epoch:          2
Summary:        Program to generate UML diagram from a text description

License:        LGPLv3+
URL:            https://plantuml.com/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  javapackages-local
Requires:       java >= 17

# Explicit requires for javapackages-tools since plantuml script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Source44: import.info
# see https://bugzilla.altlinux.org/48358
Requires: graphviz

%description
PlantUML is a program allowing to draw UML diagrams, using a simple
and human readable text description. It is extremely useful for code
documenting, sketching project architecture during team conversations
and so on.

PlantUML supports the following diagram types
  - sequence diagram
  - use case diagram
  - class diagram
  - activity diagram
  - component diagram
  - state diagram

%prep
%setup

%build
ant

%install
# Set jar location
%mvn_file net.sourceforge.%{name}:%{name} %{name}
# Configure maven depmap
%mvn_artifact net.sourceforge.%{name}:%{name}:%{version} %{name}.jar
%mvn_install

%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%{_bindir}/plantuml
%doc README.md
%doc --no-dereference COPYING plantuml-lgpl/lgpl-license.txt
%config(noreplace,missingok) /etc/java/%{name}.conf

%changelog
* Thu Jun 11 2026 Anton Meleshnikov <alton@altlinux.org> 2:1.2026.5-alt1
- new version (thanks fedora for the spec) (closes: #50011)
- remove javadoc

* Fri Dec 01 2023 Igor Vlasenko <viy@altlinux.org> 2:1.2022.6-alt1_2jpp11
- new version

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 2:1.2022.5-alt1_3jpp11
- new version

* Wed Apr 06 2022 Igor Vlasenko <viy@altlinux.org> 2:1.2022.2-alt1_1jpp11
- new version (closes: #42069)

* Mon Jun 07 2021 Igor Vlasenko <viy@altlinux.org> 2:1.2021.0-alt1_2jpp11
- rebuild with java11 and use jvm_run

* Sun Sep 13 2020 Igor Vlasenko <viy@altlinux.ru> 2:1.2019.1-alt1_6jpp8
- new version (closes: #38927)

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 8033-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 8033-alt1_6jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 8033-alt1_5jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 8033-alt1_4jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 8027-alt2_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 8027-alt1_1jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 7978-alt1_1jpp7
- new release

