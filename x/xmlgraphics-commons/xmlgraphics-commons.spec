Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xmlgraphics-commons
Version:        2.7
Release:        alt2_2jpp11
Epoch:          0
Summary:        XML Graphics Commons

License:        ASL 2.0
URL:            http://xmlgraphics.apache.org/
Source0:        http://archive.apache.org/dist/xmlgraphics/commons/source/xmlgraphics-commons-%{version}-src.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(xml-resolver:xml-resolver)
Source44: import.info

%description
Apache XML Graphics Commons is a library that consists of
several reusable components used by Apache Batik and
Apache FOP. Many of these components can easily be used
separately outside the domains of SVG and XSL-FO. You will
find components such as a PDF library, an RTF library,
Graphics2D implementations that let you generate PDF &
PostScript files, and much more.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q %{name}-%{version}

find -name "*.jar" -delete

# Disable plugins not needed for RPM build
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :findbugs-maven-plugin

# Make into OSGi bundle
%pom_xpath_inject pom:project '<packaging>bundle</packaging>'
%pom_add_plugin org.apache.felix:maven-bundle-plugin . \
" <extensions>true</extensions>
  <configuration>
    <instructions>
      <Bundle-SymbolicName>org.apache.xmlgraphics</Bundle-SymbolicName>
    </instructions>
  </configuration>"

%build
%mvn_file : %{name}
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc README

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed Oct 25 2023 Igor Vlasenko <viy@altlinux.org> 0:2.7-alt2_2jpp11
- fixed build (closes: #48160)

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:2.7-alt1_2jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:2.6-alt1_1jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_2jpp8
- new version

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_3jpp8
- fc update & java 8 build

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_2jpp8
- java update

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_4jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_2jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp7
- new version

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_6jpp7
- fc update

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_4jpp6
- fixed build with java 7

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_4jpp6
- new jpp relase

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp5
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

