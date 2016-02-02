Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plantuml
Version:        8027
Release:        alt2_1jpp8
Summary:        Program to generate UML diagram from a text description

License:        LGPLv3+
URL:            http://plantuml.sourceforge.net
Source0:        http://downloads.sourceforge.net/sourceforge/plantuml/plantuml-lgpl-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant

Requires:       jpackage-utils

Patch1:         plantuml-doc-errors.patch
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
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c -n plantuml
%patch1 -p1 -b .doc-errors

%build
ant

# build javadoc
javadoc -d javadoc -sourcepath src net.sourceforge.plantuml

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true 

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files
%{_javadir}/%{name}.jar
%{_bindir}/plantuml
%doc README COPYING
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 8027-alt2_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 8027-alt1_1jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 7978-alt1_1jpp7
- new release

