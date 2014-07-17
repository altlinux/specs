BuildRequires: maven-plugin-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
%global snapdate 20100827
#svn 990212.

Name:           apache-rat
Version:        0.8
Release:        alt3_6jpp7
Summary:        Apache Release Audit Tool (RAT)

Group:          Development/Java
License:        ASL 2.0
URL:            http://incubator.apache.org/rat/
#svn had a number of needed bugfixes
#svn export -r 990212 http://svn.apache.org/repos/asf/incubator/rat/main/trunk apache-rat-0.8-20100707
#Source0:        %{name}-%{version}-%{snapdate}.tar.bz2
Source0:        http://www.apache.org/dist/incubator/rat/sources/apache-rat-incubating-%{version}-src.tar.bz2
Patch0:         apache-rat-0.8-doxia-1.1.patch
Patch1:         apache-rat-compat.patch
Patch2:         apache-rat-0.8-test.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-wagon

BuildRequires:  ant-antunit
BuildRequires:  ant-testutil
BuildRequires:  apache-commons-compress

Requires:       jpackage-utils
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


%package core
Summary:        Core functionality for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       apache-commons-cli
Requires:       apache-commons-collections
Requires:       apache-commons-compress
Requires:       apache-commons-lang
Requires:       apache-commons-io
Requires:       junit

%description core
The core functionality of RAT, shared by the Ant tasks, and the Maven plugin.


%package plugin
Summary:        Maven plugin for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{version}-%{release}

%description plugin
Maven plugin for running RAT, the Release Audit Tool.


%package tasks
Summary:        Ant tasks for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{version}-%{release}

%description tasks
Ant tasks for running RAT.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .doxia-1.1
%patch1 -p1 -b .compat
%patch2 -p1 -b .test


%build
mvn-rpmbuild package javadoc:aggregate

%install
#Dirs
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}

#Parent pom
cp -p pom.xml \
  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom

#Components
for jarname in %{name}{-core,-plugin,-tasks}
do
  jarfile=$jarname/target/${jarname}-%{version}.jar
  cp -p $jarfile $RPM_BUILD_ROOT%{_javadir}/%{name}/${jarname}.jar
  cp -p ${jarname}/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-${jarname}.pom
  %add_maven_depmap JPP.%{name}-${jarname}.pom %{name}/${jarname}.jar
done

#Ant taksks
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "apache-rat/rat-core apache-rat/rat-tasks" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name}

#Javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/
cp -rp target/site/apidocs \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc DISCLAIMER.txt LICENSE NOTICE README.txt RELEASE_NOTES.txt
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavendepmapfragdir}/*
%dir %{_javadir}/%{name}

%files core
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
%{_javadir}/%{name}/%{name}-core.jar

%files plugin
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP.%{name}-%{name}-plugin.pom
%{_javadir}/%{name}/%{name}-plugin.jar

%files tasks
%doc LICENSE NOTICE
%{_sysconfdir}/ant.d/%{name}
%{_mavenpomdir}/JPP.%{name}-%{name}-tasks.pom
%{_javadir}/%{name}/%{name}-tasks.jar

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}


%changelog
* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt3_6jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_6jpp7
- new version

