Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name apache-commons-jci
%define version 1.0
%global base_name  jci
%global short_name commons-%{base_name}
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}

Name:          apache-commons-jci
Version:       1.0
Release:       alt2_5jpp7
Summary:       Commons Java Compiler Interface
Group:         Development/Java
License:       ASL 2.0
URL:           http://commons.apache.org/jci/
Source0:       ftp://ftp.gbnet.net/pub/apache/dist/commons/%{base_name}/source/%{short_name}-%{namedversion}-src.tar.gz
# force ecj 4.x use
Source1:       %{name}-%{namedversion}-depmap
# fix parent relative path
# fix groovy gId and aId
# add org.codehaus.janino commons-compiler
# remove org.codehaus.mojo findbugs-maven-plugin 1.0.0
Patch0:        %{name}-%{namedversion}-fixbuild.patch
# asm 3 test build
Patch1:        %{name}-%{namedversion}-ExtendedDump.patch
Patch2:        %{name}-%{namedversion}-SimpleDump.patch
# fix parent relative path
# remove jetty-maven-plugin
# use tomcat 7.x apis
Patch3:        %{name}-%{namedversion}-examples-pom.patch

Patch4:        %{name}-%{namedversion}-janino26.patch

Patch5:        %{name}-%{namedversion}-ecj4.patch

BuildRequires: jpackage-utils

BuildRequires: maven
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-resources-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

BuildRequires: apache-commons-logging
BuildRequires: apache-commons-io
BuildRequires: ecj >= 3.4.2-13
BuildRequires: groovy
BuildRequires: janino
BuildRequires: rhino

# test deps
BuildRequires: apache-commons-lang
BuildRequires: junit
BuildRequires: objectweb-asm

Requires:      %{name}-core = %{?epoch:%epoch:}%{version}-%{release}

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

#* javac Commons JCI compiler implementation for the javac compiler (up to JDK 1.5).
#* jsr199 Commons JCI compiler implementation for JDK 1.6 and up.

%description
JCI is a java compiler interface featuring a compiling class loader.
The current implementation supports compilation via the following
compilers:

* eclipse
* groovy
* janino
* rhino

%package core
Group:         Development/Java
Summary:       Commons Java Compiler Interface - core
Requires:      apache-commons-io
Requires:      %{name}-fam = %{?epoch:%epoch:}%{version}-%{release}

%description core
Commons JCI core interfaces and implementations.

%package fam
Group:         Development/Java
Summary:       Commons Java Compiler Interface - FAM
Requires:      apache-commons-logging
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description fam
Commons JCI FileAlterationMonitor (FAM) to
monitor local file systems and get notified
about changes.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %%{name}.

# compilers

%package eclipse
Group:         Development/Java
Summary:       Commons Java Compiler Interface - eclipse
Requires:      ecj >= 3.4.2-13
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description eclipse
Commons JCI compiler implementation for the eclipse compiler.

%package groovy
Group:         Development/Java
Summary:       Commons Java Compiler Interface - groovy
Requires:      groovy
Requires:      %{name}-core = %{?epoch:%epoch:}%{version}-%{release}

%description groovy
Commons JCI compiler implementation for the groovy compiler.

%package janino
Group:         Development/Java
Summary:       Commons Java Compiler Interface - janino
Requires:      janino
Requires:      %{name}-core = %{?epoch:%epoch:}%{version}-%{release}

%description janino
Commons JCI compiler implementation for the janino compiler.

%package rhino
Group:         Development/Java
Summary:       Commons Java Compiler Interface - rhino
Requires:      rhino
Requires:      %{name}-core = %{?epoch:%epoch:}%{version}-%{release}

%description rhino
Commons JCI compiler implementation for rhino JavaScript.

%prep
%setup -q -n %{short_name}-%{namedversion}-src
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p0

# require old version of jdependency
%pom_disable_module compilers/javac
%pom_disable_module examples

sed -i "s|<maven.compile.source>1.4<|<maven.compile.source>1.5<|" pom.xml
sed -i "s|<maven.compile.target>1.4<|<maven.compile.target>1.5<|" pom.xml

%build

# random tests failures
mvn-rpmbuild \
  -Dmaven.test.failure.ignore=true \
  -Dmaven.local.depmap.file="%{SOURCE1}" \
  package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-parent.pom
%add_maven_depmap JPP.%{short_name}-parent.pom

mkdir -p %{buildroot}%{_javadir}/%{short_name}
for m in core \
  fam;do
    install -m 644 ${m}/target/%{short_name}-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-${m}.jar
    install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-${m}.pom
    %add_maven_depmap -f ${m} JPP.%{short_name}-%{short_name}-${m}.pom %{short_name}/%{short_name}-${m}.jar
done

#  javac
for mc in eclipse \
  janino \
  groovy \
  rhino;do
    install -m 644 compilers/${mc}/target/%{short_name}-${mc}-%{namedversion}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-${mc}.jar
    install -pm 644 compilers/${mc}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-${mc}.pom
    %add_maven_depmap  -f ${mc} JPP.%{short_name}-%{short_name}-${mc}.pom %{short_name}/%{short_name}-${mc}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/JPP.%{short_name}-parent.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt NOTICE.txt README.txt TODO.txt

%files core
%{_javadir}/%{short_name}/%{short_name}-core.jar
%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-core.pom
%{_mavendepmapfragdir}/%{name}-core

%files fam
%{_javadir}/%{short_name}/%{short_name}-fam.jar
%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-fam.pom
%{_mavendepmapfragdir}/%{name}-fam

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files eclipse
%{_javadir}/%{short_name}/%{short_name}-eclipse.jar
%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-eclipse.pom
%{_mavendepmapfragdir}/%{name}-eclipse

%files groovy
%{_javadir}/%{short_name}/%{short_name}-groovy.jar
%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-groovy.pom
%{_mavendepmapfragdir}/%{name}-groovy

%files janino
%{_javadir}/%{short_name}/%{short_name}-janino.jar
%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-janino.pom
%{_mavendepmapfragdir}/%{name}-janino

%files rhino
%{_javadir}/%{short_name}/%{short_name}-rhino.jar
%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-rhino.pom
%{_mavendepmapfragdir}/%{name}-rhino

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2_5jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_5jpp7
- fc update

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_4jpp7
- fc release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_0.r831715.4jpp6
- fixed build with new asm

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_0.r831715.4jpp6
- fixed build with maven3

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r831715.4jpp6
- new version

