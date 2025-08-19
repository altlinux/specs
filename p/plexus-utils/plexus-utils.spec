%define _unpackaged_files_terminate_build 1

Name: plexus-utils
Version: 4.0.2
Release: alt1

Summary: Plexus Common Utilities
License: Apache-2.0
Group: Development/Java
Url: https://codehaus-plexus.github.io/plexus-utils/
Vcs: https://github.com/codehaus-plexus/plexus-utils.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires: mvn(org.codehaus.plexus:plexus-xml)

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%{?javadoc_package}

%prep
%setup

%mvn_file : plexus/plexus-utils plexus/utils
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
%mvn_build -f -- -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=8 \
  #

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference NOTICE.txt LICENSE.txt

%changelog
* Fri Aug 15 2025 Ivan Khanas <xeno@altlinux.org> 4.0.2-alt1
- New version.
- Rename artifact.

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:3.3.0-alt1_7jpp11
- update

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 0:3.3.0-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_2jpp8
- new version

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_4jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.0.24-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.0.24-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.0.24-alt1_3jpp8
- new jpp release

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

