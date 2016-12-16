Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           avalon-framework
Epoch:          0
Version:        4.3
Release:        alt4_16jpp8
Summary:        Java components interfaces
License:        ASL 2.0
URL:            http://avalon.apache.org/
BuildArch:    	noarch

Source0:        http://archive.apache.org/dist/excalibur/avalon-framework/source/%{name}-api-%{version}-src.tar.gz
Source1:        http://archive.apache.org/dist/excalibur/avalon-framework/source/%{name}-impl-%{version}-src.tar.gz

Patch0001:      0001-Port-build-script-to-Maven-3.patch

BuildRequires:  maven-local
BuildRequires:  mvn(avalon-logkit:avalon-logkit)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info


%description
The Avalon framework consists of interfaces that define relationships
between commonly used application components, best-of-practice pattern
enforcements, and several lightweight convenience implementations of the
generic components.
What that means is that we define the central interface Component. We
also define the relationship (contract) a component has with peers,
ancestors and children.

%package javadoc
Group: Development/Java
Summary:      API documentation %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -qcT
tar xvf %{SOURCE0}
tar xvf %{SOURCE1}
%patch0001 -p1

%mvn_package :aggregator __noinstall
%mvn_file ":*api*" %{name}-api
%mvn_file ":*impl*" %{name}-impl %{name}

# Add proper Apache Felix Bundle Plugin instructions
# so that we get a reasonable OSGi manifest.
for mod in api impl; do
    %pom_xpath_inject pom:project "<packaging>bundle</packaging>" *${mod}*/project.xml
    %pom_xpath_inject pom:build "
      <plugins>
        <plugin>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <extensions>true</extensions>
          <configuration>
            <instructions>
              <Bundle-SymbolicName>avalon-framework-${mod}-4.3</Bundle-SymbolicName>
              <_nouses>true</_nouses>
            </instructions>
          </configuration>
        </plugin>
      </plugins>" *${mod}*/project.xml
done

%build
# Test use old jmock
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc avalon-framework-api-4.3/LICENSE.txt
%doc avalon-framework-api-4.3/NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc avalon-framework-api-4.3/LICENSE.txt
%doc avalon-framework-api-4.3/NOTICE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt4_16jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt4_15jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt4_14jpp8
- java 8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_7jpp7
- new release

* Tue May 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_5jpp7
- fc build

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt3_2jpp5
- fixed build with moved maven1

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt2_2jpp5
- fixed build

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt1_2jpp5
- restored in separate package due to repolib

