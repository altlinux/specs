# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           buildnumber-maven-plugin
Version:        1.3
Release:        alt1_5jpp8
Summary:        Build Number Maven Plugin

Group:          Development/Other
License:        MIT and ASL 2.0
URL:            http://svn.codehaus.org/mojo/tags/buildnumber-maven-plugin-%{version}

Source0:        http://central.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch: 	noarch

# Basic stuff
BuildRequires: javapackages-tools rpm-build-java

# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: jna
BuildRequires: maven-scm

Requires: maven
Requires: maven-project
Requires: maven-scm
Requires: jna
Requires: javapackages-tools rpm-build-java
Requires: mojo-parent
Requires: plexus-containers-container-default
Requires: plexus-utils
Source44: import.info

%description
This mojo is designed to get a unique build number for each time you build
your project. So while your version may remain constant at 1.0-SNAPSHOT
for many iterations until release, you will have a build number that can
uniquely identify each build during that time. The build number is obtained
from scm, and in particular, at this time, from svn. You can then place that
build number in metadata, which can be accessed from your app, if desired.

The mojo also has a couple of extra functions to ensure you get the proper
build number. First, your local repository is checked to make sure it is
up to date. Second, your local repository is automatically updated, so that
you get the latest build number. Both these functions can be suppressed,
if desired.

Optionally, you can configure this mojo to produce a revision based on a
timestamp, or on a sequence, without requiring any interaction with an
SCM system. Note that currently, the only supported SCM is subversion.


%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp -p %{SOURCE1} .

%pom_remove_dep com.google.code.maven-scm-provider-svnjava:maven-scm-provider-svnjava
%pom_remove_dep org.tmatesoft.svnkit:svnkit
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-invoker-plugin

# junit dependency was removed in Plexus 1.6
%pom_add_dep junit:junit::test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_6jpp7
- new release

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- patched out dependency on maven2 (patch33)

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- complete build

* Tue Mar 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

