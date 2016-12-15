Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           junit
Epoch:          1
Version:        4.12
Release:        alt1_5jpp8
Summary:        Java regression test package
License:        EPL
URL:            http://www.junit.org/
BuildArch:      noarch

# ./clean-tarball.sh %{version}
Source0:        %{name}-%{version}-clean.tar.gz
Source3:        create-tarball.sh

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)

Obsoletes:      %{name}-demo < 4.12
Source44: import.info

Provides: junit = 0:%{version}
Provides: junit4 = %{epoch}:%{version}-%{release}
Conflicts: junit4 < 1:4.11-alt3_1jpp7
Obsoletes: junit4 < 1:4.11-alt3_1jpp7
Obsoletes: junit-junit4 < 1:4.11-alt3_1jpp7
Obsoletes: junit-junit3 < 1:3.8.2-alt9_10jpp6
Conflicts: junit-junit4 < 1:4.11-alt3_1jpp7
Conflicts: junit-junit3 < 1:3.8.2-alt9_10jpp6

%description
JUnit is a regression testing framework written by Erich Gamma and Kent Beck. 
It is used by the developer who implements unit tests in Java. JUnit is Open
Source Software, released under the Common Public License Version 1.0 and 
hosted on GitHub.

%package manual
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-r%{version}

# InaccessibleBaseClassTest fails with Java 8
sed -i /InaccessibleBaseClassTest/d src/test/java/org/junit/tests/AllTests.java

%pom_remove_plugin :replacer
sed s/@version@/%{version}/ src/main/java/junit/runner/Version.java.template >src/main/java/junit/runner/Version.java

%pom_remove_plugin :animal-sniffer-maven-plugin

# Removing hamcrest source jar references (not available and/or necessary)
%pom_remove_plugin :maven-javadoc-plugin

# Add proper Apache Felix Bundle Plugin instructions
# so that we get a reasonable OSGi manifest.
%pom_xpath_inject pom:project "<packaging>bundle</packaging>"
%pom_xpath_inject pom:build/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Bundle-SymbolicName>org.junit</Bundle-SymbolicName>
          <Export-Package>{local-packages},!org.hamcrest*,*;x-internal:=true</Export-Package>
          <_nouses>true</_nouses>
        </instructions>
      </configuration>
    </plugin>"

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-junit.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE-junit.txt

%files manual
%doc LICENSE-junit.txt
%doc doc/*

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_3jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt3_1jpp7
- replacement for junit4

* Thu Sep 04 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt2_1jpp7
- bugfix (closes: #30279)

* Tue Aug 12 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt1_1jpp7
- new version

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.10-alt5_6jpp7
- bumped epoch for junit-junit4

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt4_6jpp7
- made junit-junit4 provider default

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt3_6jpp7
- added junit-junit4 provider

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt2_6jpp7
- added OSGi manifest

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt1_6jpp7
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.8.2-alt1_5jpp6
- new jpp relase

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.8.2-alt1_4jpp6
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_4jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_1jpp5
- converted from JPackage by jppimport script

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt1_1.1jpp1.7
- new version
- resolved conflict with junit3.

* Sun Mar 25 2007 Denis Smirnov <mithraen@altlinux.ru> 4.1-alt2
- Update from upstream
- Add conflict with junit 3.8

* Sun Jul 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 4.1-alt1
- New package for JUnit 4.x
- Patch0: ignore a test relying on Java VM exit code that fails
- Relocated samples to /usr/share/junit4
