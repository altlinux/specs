Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name apache-commons-javaflow
%define version 1.0
%global base_name  javaflow
%global short_name commons-%{base_name}
%global namedreltag -SNAPSHOT
%global namedversion %{version}%{?namedreltag}
Name:          apache-commons-javaflow
Version:       1.0
Release:       alt8_0.11.20120509SNAPSHOTjpp8
Summary:       Commons Javaflow
License:       ASL 2.0
Url:           http://commons.apache.org/sandbox/javaflow/
# svn export http://svn.apache.org/repos/asf/commons/sandbox/javaflow/trunk/  commons-javaflow-1.0-SNAPSHOT
# tar czf commons-javaflow-1.0-SNAPSHOT-src-svn.tar.gz commons-javaflow-1.0-SNAPSHOT
Source0:       %{short_name}-%{namedversion}-src-svn.tar.gz

BuildRequires: mvn(asm:asm)
BuildRequires: mvn(asm:asm-analysis)
BuildRequires: mvn(asm:asm-commons)
BuildRequires: mvn(asm:asm-tree)
BuildRequires: mvn(asm:asm-util)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(junit-addons:junit-addons)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.bcel:bcel)
BuildRequires: mvn(org.apache.commons:commons-jci-core)
BuildRequires: maven-local

BuildArch:     noarch
Source44: import.info
Obsoletes:       jakarta-%{short_name} < 0:%{version}-%{release}

%description
Sometimes it is useful if we can capture the state of the application,
its stack of function calls, which includes local variables, the global
variables and the program counter, and save them into an object. If
this object would give us the ability to restart the processing from
the point stored in it.
A continuation is exactly the type of object that we need. Think of a
continuation as an object that, for a given point in your program,
contains a snapshot of the stack trace, including all the local
variables, and the program counter. You can not only store these
things in the continuation object, but also restore the execution
of the program from a continuation object. This means that the stack
trace and the program counter of the running program become the ones
stored in a continuation.
Continuations are powerful concepts from the world of functional
languages, like Scheme, but they are becoming popular in other
languages as well.

%package ant
Group: Development/Java
Summary:       Development files for Commons Javaflow
Requires:      ant
Requires:      %{name} = %{version}

%description ant
This package enables support for the Commons Javaflow ant tasks.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{namedversion}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%pom_remove_parent
#sed -i "s|commons-sandbox-parent|commons-parent|" pom.xml
%pom_xpath_inject "pom:project" "<groupId>org.apache.commons</groupId>"

%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId = 'ant' ]" "<scope>provided</scope>"

%mvn_file :%{short_name} %{name}
%mvn_file :%{short_name} %{short_name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant %{short_name}" > %{short_name}
install -p -m 644 %{short_name} %{buildroot}%{_sysconfdir}/ant.d/%{short_name}

%files -f .mfiles
%doc CREDITS.txt TODO.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%files ant
%config(noreplace) %{_sysconfdir}/ant.d/%{short_name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8_0.11.20120509SNAPSHOTjpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8_0.10.20120509SNAPSHOTjpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8_0.6.20120509SNAPSHOTjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8_0.4.20120509SNAPSHOTjpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8_0.2.20120509SNAPSHOTjpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.2.20120509SNAPSHOTjpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_0.r618928.1jpp5
- build w/new jci

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.r618928.1jpp5
- fixed build w/new commons-parent

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.r618928.1jpp5
- fixed build with new asm

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.r618928.1jpp5
- fixed build with new maven 2.0.8

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.r618928.1jpp5
- fixes for java6 support

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.r618928.1jpp5
- new version

