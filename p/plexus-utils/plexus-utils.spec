Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plexus-utils
Version:        3.0.22
Release:        alt2_3jpp8
Summary:        Plexus Common Utilities
# ASL 1.1: several files in src/main/java/org/codehaus/plexus/util/ 
# xpp: src/main/java/org/codehaus/plexus/util/xml/pull directory
# ASL 2.0 and BSD:
#      src/main/java/org/codehaus/plexus/util/cli/StreamConsumer
#      src/main/java/org/codehaus/plexus/util/cli/StreamPumper
#      src/main/java/org/codehaus/plexus/util/cli/Commandline            
# Public domain: src/main/java/org/codehaus/plexus/util/TypeFormat.java
# rest is ASL 2.0
License:        ASL 1.1 and ASL 2.0 and xpp and BSD and Public Domain
URL:            https://github.com/codehaus-plexus/plexus-utils
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Source44: import.info

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp %{SOURCE1} .

%mvn_file : plexus/utils
%mvn_alias : plexus:plexus-utils

# Generate OSGI info
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_xpath_inject "pom:build/pom:plugins" "
        <plugin>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <extensions>true</extensions>
          <configuration>
            <instructions>
              <_nouses>true</_nouses>
              <Export-Package>org.codehaus.plexus.util.*;org.codehaus.plexus.util.cli.*;org.codehaus.plexus.util.cli.shell.*;org.codehaus.plexus.util.dag.*;org.codehaus.plexus.util.introspection.*;org.codehaus.plexus.util.io.*;org.codehaus.plexus.util.reflection.*;org.codehaus.plexus.util.xml.*;org.codehaus.plexus.util.xml.pull.*</Export-Package>
            </instructions>
          </configuration>
        </plugin>"

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc NOTICE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc NOTICE.txt LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.22-alt2_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.22-alt2_2jpp8
- added osgi provides

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.22-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.22-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.14-alt1_1jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.9-alt1_5jpp7
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_3jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

