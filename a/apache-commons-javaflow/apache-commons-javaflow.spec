Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name apache-commons-javaflow
%define version 1.0
%global base_name  javaflow
%global short_name commons-%{base_name}
%global namedreltag -SNAPSHOT
%global namedversion %{version}%{?namedreltag}
Name:          apache-commons-javaflow
Version:       1.0
Release:       alt8_0.2.20120509SNAPSHOTjpp7
Summary:       Commons Javaflow
Group:         Development/Java
License:       ASL 2.0
Url:           http://commons.apache.org/sandbox/javaflow/
# svn export http://svn.apache.org/repos/asf/commons/sandbox/javaflow/trunk/  commons-javaflow-1.0-SNAPSHOT
# tar czf commons-javaflow-1.0-SNAPSHOT-src-svn.tar.gz commons-javaflow-1.0-SNAPSHOT
Source0:       %{short_name}-%{namedversion}-src-svn.tar.gz
Patch0:        %{name}-%{namedversion}-remove-sandbox-parent.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: apache-commons-io
BuildRequires: apache-commons-jci-core
BuildRequires: apache-commons-logging
BuildRequires: bcel
BuildRequires: objectweb-asm

# test deps
BuildRequires: junit
BuildRequires: junit-addons

BuildRequires: maven
#BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
#BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
#BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      apache-commons-io
Requires:      apache-commons-jci-core
Requires:      apache-commons-logging
Requires:      bcel
Requires:      objectweb-asm

Requires:      jpackage-utils
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
Summary:       Development files for Commons Javaflow
Group:         Development/Java
Requires:      ant
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description ant
This package enables support for the Commons Javaflow ant tasks.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{namedversion}
find . -name "*.class" -delete
find . -name "*.jar" -delete
#sed -i "s|commons-sandbox-parent|commons-parent|" pom.xml
%patch0 -p0

%build

mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{short_name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar
( cd %{buildroot}%{_javadir} && ln -sf %{name}.jar %{short_name}.jar )

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant %{short_name}" > %{short_name}
install -p -m 644 %{short_name} %{buildroot}%{_sysconfdir}/ant.d/%{short_name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavendepmapfragdir}/%{name}
%doc CREDITS.txt LICENSE.txt NOTICE.txt TODO.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files ant
%config(noreplace) %{_sysconfdir}/ant.d/%{short_name}

%changelog
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

