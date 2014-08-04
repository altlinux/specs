# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           buildnumber-maven-plugin
Version:        1.2
Release:        alt2_3jpp7
Summary:        Build Number Maven Plugin

Group:          Development/Java
License:        MIT and ASL 2.0
URL:            http://svn.codehaus.org/mojo/tags/buildnumber-maven-plugin-1.2

# svn export http://svn.codehaus.org/mojo/tags/buildnumber-maven-plugin-1.2 buildnumber-maven-plugin
# tar caf buildnumber-maven-plugin-1.2.tar.xz buildnumber-maven-plugin
Source0:        buildnumber-maven-plugin-1.2.tar.xz
Source1:	%{name}-depmap.xml
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch: 	noarch

# Basic stuff
BuildRequires: jpackage-utils

# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: maven2-common-poms
BuildRequires: maven-plugin-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: plexus-containers-component-javadoc
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-utils
BuildRequires: jna
BuildRequires: mojo-parent
#BuildRequires: maven-project
BuildRequires: maven-scm


Requires: maven
Requires: maven-project
Requires: maven-scm
Requires: jna
Requires: jpackage-utils
Requires: mojo-parent
Requires: plexus-containers-container-default
Requires: plexus-utils
Source44: import.info
Patch33: buildnumber-maven-plugin-1.2-alt-no-maven2.patch

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
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}
cp -p %{SOURCE2} .

%pom_remove_dep com.google.code.maven-scm-provider-svnjava:maven-scm-provider-svnjava
%pom_remove_dep org.tmatesoft.svnkit:svnkit

%patch33 -p1

%build

# tests skipped due to invoker problems with local repository tests
mvn-rpmbuild -DskipTests=true \
        -Dmaven.test.skip=true \
        -Dmaven.compile.target=1.5 \
        install javadoc:aggregate

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar


# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc LICENSE.txt LICENSE-2.0.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt LICENSE-2.0.txt
%{_javadocdir}/%{name}

%changelog
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

