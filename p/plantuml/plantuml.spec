Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           plantuml
Version:        1.2022.5
Release:        alt1_3jpp11
Epoch:          2
Summary:        Program to generate UML diagram from a text description

License:        LGPLv3+
URL:            http://plantuml.com/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-lgpl-%{version}.tar.gz
#Fix compilation under openjdk
#Patch0:         build-with-javac-utf8-encoding.patch

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  xmvn
Requires:       java >= 1.8.0
BuildRequires:  javapackages-local
# Explicit requires for javapackages-tools since plantuml script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Source44: import.info

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

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c -n plantuml
#%patch0 -p1

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' README
touch -r README.orig README
rm README.orig

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 

# build javadoc
export CLASSPATH=$(build-classpath ant):plantuml.jar
%javadoc -source 1.8 -source 1.8 -encoding UTF-8 -Xdoclint:none -d javadoc $(find src -name "*.java") -windowtitle "PlantUML %{version}"

%install
# Set jar location
%mvn_file net.sourceforge.%{name}:%{name} %{name}
# Configure maven depmap
%mvn_artifact net.sourceforge.%{name}:%{name}:%{version} %{name}.jar
%mvn_install -J javadoc

%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%{_bindir}/plantuml
%doc README
%doc --no-dereference COPYING
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYING

%changelog
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

