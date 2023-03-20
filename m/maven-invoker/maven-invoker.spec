Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-invoker
Version:        3.1.0
Release:        alt1_6jpp11
Summary:        Fires a maven build in a clean environment
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-invoker/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Patch rejected upstream
Patch1:         %{name}-MSHARED-279.patch
# Disable two tests that are affected by bug in maven-surefire version 3.0.0-M6
# https://issues.apache.org/jira/browse/SUREFIRE-2056
# The bug is fixed in maven-surefire 3.0.0-M7.
Patch2:         0001-Disable-two-tests-in-DefaultInvokerTest.java.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
# Required by tests
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-clean-plugin
Source44: import.info

%description
This API is concerned with firing a Maven build in a new JVM. It accomplishes
its task by building up a conventional Maven command line from options given in
the current request, along with those global options specified in the invoker
itself. Once it has the command line, the invoker will execute it, and capture
the resulting exit code or any exception thrown to signal a failure to execute.
Input/output control can be specified using an InputStream and up to two
InvocationOutputHandlers.

This is a replacement package for maven-shared-invoker

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q
# Change line endings so patch can be applied
sed -i 's/\r$//' src/main/java/org/apache/maven/shared/invoker/MavenCommandLineBuilder.java
sed -i 's/\r$//' src/test/java/org/apache/maven/shared/invoker/DefaultInvokerTest.java
%patch1 -p1
%patch2 -p1
%pom_change_dep javax.inject:javax.inject:1  org.eclipse.sisu:org.eclipse.sisu.inject

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt1_6jpp11
- update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt1_1jpp11
- new version

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 3.0.1-alt2_2jpp11
- Port to maven-antrun-plugin 3.0.0

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 3.0.1-alt1_2jpp11
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_9jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_6jpp7
- new release

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_0jpp7
- hold obsoletes

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_6jpp7
- new version

