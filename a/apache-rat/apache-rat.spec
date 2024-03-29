Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           apache-rat
Summary:        Apache Release Audit Tool (RAT)
Version:        0.13
Release:        alt1_9jpp11
License:        ASL 2.0

URL:            http://creadur.apache.org/rat/
Source0:        http://www.apache.org/dist/creadur/%{name}-%{version}/%{name}-%{version}-src.tar.bz2

Patch1:         0001-Port-to-current-doxia-sitetools.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-antunit)
BuildRequires:  mvn(org.apache.ant:ant-testutil)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-decoration-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-artifact:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-model:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-settings:2.2.1)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(org.mockito:mockito-core)
Source44: import.info

%description
Release Audit Tool (RAT) is a tool to improve accuracy and efficiency when
checking releases. It is heuristic in nature: making guesses about possible
problems. It will produce false positives and cannot find every possible
issue with a release. It's reports require interpretation.

RAT was developed in response to a need felt in the Apache Incubator to be
able to review releases for the most common faults less labor intensively.
It is therefore highly tuned to the Apache style of releases.

This package just contains meta-data, you will want either apache-rat-tasks,
or apache-rat-plugin.


%package        api
Group: Development/Other
Summary:        API module for %{name}

%description    api
Shared beans and services.


%package        core
Group: Development/Java
Summary:        Core functionality for %{name}

# explicit requires for javapackages-tools since apache-rat-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description    core
The core functionality of RAT, shared by the Ant tasks, and the Maven plugin.
It also includes a wrapper script "apache-rat" that should be the equivalent
to running upstream's "java -jar apache-rat.jar".


%package        plugin
Group: Development/Java
Summary:        Maven plugin for %{name}

%description    plugin
Maven plugin for running RAT, the Release Audit Tool.


%package        tasks
Group: Development/Java
Summary:        Ant tasks for %{name}

%description    tasks
Ant tasks for running RAT.


%package        javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q

%patch1 -p1

# apache-rat is a module bundling other RAT modules together and as
# such it is not needed.
%pom_disable_module apache-rat

# maven-antrun-plugin is used for running tests only and tests are
# skipped anyways.  See rhbz#988561
%pom_remove_plugin -r :maven-antrun-plugin

# don't run apache-rat's checks on apache-rat:
# these tests fail and would introduce a circular self-dependency
%pom_remove_plugin -r :apache-rat-plugin

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

# runs non-xmvn maven and downloads stuff
%pom_remove_plugin -r :maven-invoker-plugin

# wagon-ssh is not needed in Fedora.
%pom_xpath_remove pom:extensions

# trivial port to commons-lang3
%pom_change_dep -r :commons-lang org.apache.commons:commons-lang3:3.8.1

sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    apache-rat-core/src/main/java/org/apache/rat/document/impl/guesser/GuessUtils.java
sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    apache-rat-core/src/main/java/org/apache/rat/report/claim/impl/xml/SimpleXmlClaimReporter.java
sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    apache-rat-core/src/main/java/org/apache/rat/Report.java

# incompatible with our plexus-container
rm apache-rat-plugin/src/test/java/org/apache/rat/mp/RatCheckMojoTest.java


%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8


%install
%mvn_install

# create wrapper script
%jpackage_script org.apache.rat.Report "" "" %{name}/%{name}-core:commons-cli:commons-io:commons-collections:commons-compress:commons-lang:junit apache-rat true

# install ant taksks
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "apache-rat/rat-core apache-rat/rat-tasks" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/apache-rat.conf`
touch $RPM_BUILD_ROOT/etc/java/apache-rat.conf


%files -f .mfiles-%{name}-project
%doc LICENSE NOTICE

%files api -f .mfiles-%{name}-api
%doc README.txt RELEASE-NOTES.txt
%doc LICENSE NOTICE

%files core -f .mfiles-%{name}-core
%{_bindir}/%{name}
%config(noreplace,missingok) /etc/java/apache-rat.conf

%files plugin -f .mfiles-%{name}-plugin

%files tasks -f .mfiles-%{name}-tasks
%{_sysconfdir}/ant.d/%{name}
%doc ant-task-examples.xml

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Sat Jul 16 2022 Igor Vlasenko <viy@altlinux.org> 0.13-alt1_9jpp11
- update

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 0.13-alt1_8jpp11
- rebuild with java11 and use jvm_run

* Sun Oct 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_7jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_8jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_6jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_4jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_3jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1jpp7
- new release

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt3_10jpp7
- new release

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt3_8jpp7
- fixed build

* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt3_6jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_6jpp7
- new version

