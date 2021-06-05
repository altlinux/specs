Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jline2
Version:        2.14.6
Release:        alt1_2jpp11
Summary:        Java library for handling console input
License:        BSD
URL:            http://jline.github.io/jline2/

Source0:        https://github.com/jline/jline2/archive/jline-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.fusesource.jansi:jansi:1)
Source44: import.info

%description
JLine is a Java library for handling console input.  It is similar in
functionality to BSD editline and GNU readline.  People familiar with
the readline/editline capabilities for modern shells (such as bash and
tcsh) will find most of the command editing features of JLine to be
familiar.

%{?javadoc_package}

%prep
%setup -q -n jline2-jline-%{version}


# remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove maven-shade-plugin usage
%pom_remove_plugin "org.apache.maven.plugins:maven-shade-plugin"
# Remove animal sniffer plugin in order to reduce deps
%pom_remove_plugin "org.codehaus.mojo:animal-sniffer-maven-plugin"

# Remove unavailable and unneeded deps
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin

# Makes the build fail on deprecation warnings from jansi
%pom_xpath_remove 'pom:arg[text()="-Werror"]'

# Do not import non-existing internal package
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Import-Package"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions" "<Import-Package>javax.swing;resolution:=optional,org.fusesource.jansi,!org.fusesource.jansi.internal</Import-Package>"

# Be sure to export jline.internal, but not org.fusesource.jansi.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1317551
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Export-Package" "jline.*;-noimport:=true"

# Update required version of jansi 1.x
%pom_xpath_set //pom:jansi.version 1.18

# drop a nondeterministic test
find -name TerminalFactoryTest.java -delete
# it's also the only test that uses powermock, so drop the powermock dependency
%pom_remove_dep org.powermock:

# Fix javadoc generation on java 11
%pom_xpath_inject pom:build/pom:plugins "<plugin>
<artifactId>maven-javadoc-plugin</artifactId>
<configuration><source>1.8</source></configuration>
</plugin>"

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.md README.md
%doc --no-dereference LICENSE.txt

%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 0:2.14.6-alt1_2jpp11
- new version

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_7jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_7jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_6jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_5jpp7
- fc version

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_3jpp6
- new jpp relase

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp6
- new version

