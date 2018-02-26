Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           umlgraph
Version:        5.4
Release:        alt1_2jpp6
Summary:        Automated Drawing of UML Diagrams

Group:          Development/Java
License:        BSD
URL:            http://umlgraph.org/
Source0:        http://umlgraph.org/UMLGraph-%{version}.tar.gz
Source1:        http://repo2.maven.org/maven2/org/umlgraph/doclet/5.1/doclet-5.1.pom

Requires(post):   jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

BuildRequires: ant
BuildRequires: graphviz
Requires: graphviz

BuildArch: noarch
Source44: import.info

%description
UMLGraph allows the declarative specification and drawing of UML class
and sequence diagrams. The specification is done in text diagrams, 
that are then transformed into the appropriate graphical representations. 

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n UMLGraph-%{version}
sed -i -e 's|<attribute name=\"Class-Path\" value=\"tools.jar\"/>||g' build.xml
for f in $(find . -name "*.jar"); do
    mv $f $f.no
done

%build
ant compile test javadocs

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 lib/UmlGraph.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%add_to_maven_depmap org.umlgraph doclet %{version} JPP %{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -fr javadoc/gr/spinellis/umlgraph/doclet/*.dot
rm -fr javadoc/org/umlgraph/doclet/*.dot
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc README.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.4-alt1_2jpp6
- update to new release by jppimport

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.6-alt4_1jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.6-alt3_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.6-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.6-alt1_1jpp5
- converted from JPackage by jppimport script

