Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plantuml
Version:        8033
Release:        alt1_4jpp8
Summary:        Program to generate UML diagram from a text description

License:        LGPLv3+
URL:            http://plantuml.com/
Source0:        http://downloads.sourceforge.net/plantuml/%{name}-lgpl-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  javapackages-local
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

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' README
touch -r README.orig README
rm README.orig

%build

ant

# build javadoc
%javadoc -encoding UTF-8 -Xdoclint:none -classpath %{name}.jar -d javadoc $(find src -name "*.java") -windowtitle "PlantUML %{version}"

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
%doc COPYING
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 8033-alt1_4jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 8027-alt2_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 8027-alt1_1jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 7978-alt1_1jpp7
- new release

