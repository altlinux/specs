%define _unpackaged_files_terminate_build 1

Name: junit
Epoch: 1
Version: 4.13.2
Release: alt1

Summary: Java regression testing framework
License: EPL-1.0
Group: Development/Java
URL: https://junit.org/junit4/
VCS: https://github.com/junit-team/junit4.git

BuildArch: noarch
AutoReq: yes,noosgi

Source0: %name-%version.tar
Source1: module-info.java
Patch0: 0001-Port-to-hamcrest-2.2.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java-osgi
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: hamcrest
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.surefire:surefire-junit4)
BuildRequires: mvn(org.apache.maven.surefire:surefire-junit47)

Provides: junit = 0:%version
Provides: junit4 = %epoch:%version-%release
Conflicts: junit4 < 1:4.11-alt3_1jpp7
Obsoletes: junit4 < 1:4.11-alt3_1jpp7
Obsoletes: junit-junit4 < 1:4.11-alt3_1jpp7
Obsoletes: junit-junit3 < 1:3.8.2-alt9_10jpp6
Conflicts: junit-junit4 < 1:4.11-alt3_1jpp7
Conflicts: junit-junit3 < 1:3.8.2-alt9_10jpp6

%description
JUnit is a regression testing framework written by Erich Gamma and Kent Beck.
It provides assertions, test runners, rules and support for automated Java
tests.

%package manual
Summary: Manual for JUnit

Group: Development/Java

%description manual
Documentation and release notes for JUnit.

%package javadoc
Summary: API documentation for JUnit

Group: Development/Java

%description javadoc
API documentation for JUnit.

%prep
%setup
%autopatch -p1

%pom_remove_plugin :replacer
sed 's/@version@/%version/' src/main/java/junit/runner/Version.java.template \
    > src/main/java/junit/runner/Version.java
%pom_remove_plugin :animal-sniffer-maven-plugin
# The system Javadoc build does not need Hamcrest source archives.
%pom_remove_plugin :maven-javadoc-plugin

# Hamcrest 3 includes both former core and library artifacts.
%pom_remove_dep org.hamcrest:hamcrest-library
%pom_change_dep org.hamcrest:hamcrest-core org.hamcrest:hamcrest:3.0

# Legacy security-manager tests require the supported Java 17 test JVM.
%pom_xpath_inject \
    '//pom:plugin[pom:artifactId="maven-surefire-plugin"]/pom:configuration' \
    '<jvm>%_jvmdir/java-17-openjdk/bin/java</jvm>'

%pom_xpath_inject pom:project '<packaging>bundle</packaging>'
%pom_xpath_inject pom:build/pom:plugins \
    "<plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Bundle-SymbolicName>org.junit</Bundle-SymbolicName>
          <Export-Package>
            {local-packages},!org.hamcrest*,*;x-internal:=true
          </Export-Package>
          <_nouses>true</_nouses>
        </instructions>
      </configuration>
    </plugin>"

%mvn_file : %name
%mvn_alias junit:junit junit:junit-dep
# Keep normal coordinates and provide the actual release requested by Takari.
%mvn_compat_version junit:junit '' %version

%build
%mvn_build -- -P\!restrict-doclint \
    -DjdkVersion=8 -Dmaven.compiler.release=8 -Dmaven.compiler.fork=false

# Preserve ALT JPMS support without raising ordinary library bytecode to Java 9.
mkdir -p module-classes
hamcrest_jar=$(xmvn-resolve org.hamcrest:hamcrest)
javac --release 9 --module-path "$hamcrest_jar" \
    --patch-module junit=target/classes \
    -d module-classes %SOURCE1
jar --update --file target/%name-%version.jar \
    --release 9 -C module-classes module-info.class

%install
%mvn_install
if [ -d %buildroot%_javadocdir/%name/legal ]; then
    mv %buildroot%_javadocdir/%name/legal javadoc-legal
    legal_target=$(realpath -m --relative-to="%_javadocdir/%name" \
        "%_defaultdocdir/%name-%version/javadoc-legal")
    ln -s "$legal_target" %buildroot%_javadocdir/%name/legal
fi

%files -f .mfiles
%doc LICENSE-junit.txt javadoc-legal

%files javadoc -f .mfiles-javadoc

%files manual
%doc doc/*

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1:4.13.2-alt1
- New version.

* Mon Nov 17 2025 Ivan Khanas <xeno@altlinux.org> 1:4.13.1-alt2
- Add JPMS support.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:4.13.1-alt1_7jpp11
- update

* Sat Jun 11 2022 Igor Vlasenko <viy@altlinux.org> 1:4.13.1-alt1_3jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:4.13-alt1_2jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_13jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_11jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt1_6jpp8
- new jpp release

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
