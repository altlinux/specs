Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Note to packagers: When rebasing this to a later version, do not
# forget to ensure that sources 1 and 2 are up to date as well as
# the Requires list.
%global majorversion 1.8
%global archiver 1_8_9

Name:           groovy18
Version:        1.8.9
Release:        alt1_24jpp8
Summary:        Dynamic language for the Java Platform

# Some of the files are licensed under BSD and CPL terms, but the CPL has been superceded
# by the EPL. We include copies of both for completeness.
# groovyConsole uses CC-BY licensed icons
# thanks to Michal Srb and Mikolaj Izdebski, and Tom Callaway
License:        ASL 2.0 and BSD and EPL and Public Domain and CC-BY
URL:            http://groovy-lang.org

Source0:        https://github.com/groovy/groovy-core/archive/GROOVY_%{archiver}.zip
# thanks to Johannes Lips and Matt Spaulding
Source1:        groovy18-script
Source2:        groovy18-starter.conf
Source4:        cpl-v10.txt
Source5:        epl-v10.txt
Source6:        http://www.apache.org/licenses/LICENSE-2.0.txt
# thanks to Andy Grimm
Patch0:         groovy-inner-interface-annotations.patch
Patch1:         groovy-build-with-java8.patch
Patch2:         groovy-servlet31.patch
Patch3:         groovy-commons-cli-1.3.patch

BuildRequires:  ant
BuildRequires:  antlr-tool
BuildRequires:  ant-antlr
BuildRequires:  objectweb-asm3
BuildRequires:  bsf
BuildRequires:  apache-ivy
BuildRequires:  jansi
BuildRequires:  jline1
BuildRequires:  glassfish-jsp-api
BuildRequires:  junit
BuildRequires:  glassfish-servlet-api
BuildRequires:  xstream
BuildRequires:  desktop-file-utils
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  apache-commons-cli
BuildRequires:  unzip
BuildRequires:  javapackages-local
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(javax.servlet:jsp-api)

Requires:       %{name}-lib = %{version}
# Following dependencies are optional from Maven POV,
# but upstream ships them in binary distribution
Requires:       mvn(junit:junit)
# Only used for command line tools:
Requires:       mvn(commons-cli:commons-cli)
# Only used for Ant tasks & scripting tool:
Requires:       mvn(org.apache.ant:ant)
Requires:       mvn(org.apache.ant:ant-antlr)
Requires:       mvn(org.apache.ant:ant-launcher)
Requires:       mvn(org.apache.ant:ant-junit)
# Only used for BSF adapter:
Requires:       mvn(bsf:bsf)
Requires:       mvn(commons-logging:commons-logging)
# Used for servlet / gsp:
Requires:       glassfish-jsp-api
Requires:       glassfish-servlet-api
# Used to dump out the AST, xpp only needed for reading:
Requires:       mvn(com.thoughtworks.xstream:xstream)
# Used for richer interactive groovysh support:
Requires:       mvn(jline:jline:1)
Requires:       mvn(org.fusesource.jansi:jansi)
# Used for @Grab and Grapes:
Requires:       mvn(org.apache.ivy:ivy)
Requires:       mvn(org.codehaus.gpars:gpars)

# Joint compilation requires tools.jar from java-devel

BuildArch:      noarch
Source44: import.info

%description
Groovy is an agile and dynamic language for the Java Virtual Machine,
built upon Java with features inspired by languages like Python, Ruby and
Smalltalk.  It seamlessly integrates with all existing Java objects and
libraries and compiles straight to Java byte-code so you can use it anywhere
you can use Java.

%package lib
Group: Development/Java
Summary:        Groovy JAR artifact
%description lib
This package contains Groovy JAR artifact.

%package javadoc
Group: Development/Java
Summary:        API Documentation for %{name}
BuildArch: noarch
%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q -n groovy-core-GROOVY_%{archiver}
find . -name "*.class" -delete
find . -name "*.jar" -delete

cp %{SOURCE4} %{SOURCE5} %{SOURCE6} .

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# We don't want to generate auto-R on optional dependencies
%pom_xpath_replace "pom:dependency[pom:optional[text()='true']]/pom:scope" "<scope>provided</scope>"

# java 7 apis
%pom_remove_dep org.livetribe:livetribe-jsr223
# explicit tomcat apis
sed -i "s|<groupId>javax.servlet</groupId>|<groupId>org.apache.tomcat</groupId>|" pom.xml
sed -i "s|<artifactId>jsp-api</artifactId>|<artifactId>tomcat-jsp-api</artifactId>|" pom.xml
sed -i "s|<version>2.0</version>|<version>any</version>|" pom.xml
sed -i "s|<artifactId>servlet-api</artifactId>|<artifactId>tomcat-servlet-api</artifactId>|" pom.xml
sed -i "s|<version>2.4</version>|<version>any</version>|" pom.xml

# fix non ASCII chars
for s in src/main/groovy/transform/NotYetImplemented.java\
  src/main/org/codehaus/groovy/transform/NotYetImplementedASTTransformation.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

# build against shaded asm3
# TODO: fast&ugly, this could use some improvements
find . -name "*.java" -exec sed -i 's|org.objectweb.asm|org.objectweb.distroshaded.asm|g' {} +
find . -name "*.groovy" -exec sed -i 's|org.objectweb.asm|org.objectweb.distroshaded.asm|g' {} +

%pom_change_dep :asm :asm-distroshaded
%pom_change_dep :asm-commons :asm-commons-distroshaded
%pom_change_dep :asm-util :asm-util-distroshaded
%pom_change_dep :asm-analysis :asm-analysis-distroshaded
%pom_change_dep :asm-tree :asm-tree-distroshaded

%mvn_package : %{name}-lib
%mvn_file : groovy %{name}

%mvn_alias : :groovy-all :%{name}-all :%{name}
%mvn_compat_version : "1.8" "1.8.9"

%build
mkdir -p target/lib/{compile,tools}

# Construct classpath
build-jar-repository target/lib/compile glassfish-servlet-api glassfish-jsp-api/javax.servlet.jsp-api \
        objectweb-asm3/asm-tree-distroshaded objectweb-asm3/asm-distroshaded \
        objectweb-asm3/asm-util-distroshaded objectweb-asm3/asm-analysis-distroshaded \
        antlr ant/ant-antlr antlr \
        bsf jline1/jline-1 xstream ant junit apache-ivy commons-cli \
        jansi

# Build
# TODO: Build at least tests, maybe examples
export CLASSPATH=$(build-classpath ant/ant-antlr) 
ant -DskipTests=on -DskipExamples=on -DskipFetch=on -DskipEmbeddable=on \
        createJars javadoc


%install
%mvn_artifact pom.xml target/dist/groovy.jar
%mvn_install -J target/html/api/

# Startup scripts
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
for TOOL in grape18 %{name}c %{name}Console java2%{name} %{name}sh
do
        ln $RPM_BUILD_ROOT%{_bindir}/%{name} \
                $RPM_BUILD_ROOT%{_bindir}/$TOOL
done

# Configuration
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m644 %{SOURCE2} \
        $RPM_BUILD_ROOT%{_sysconfdir}/%{name}-starter.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf


%files
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}-starter.conf
%doc README.md
%doc LICENSE.txt LICENSE-2.0.txt NOTICE.txt cpl-v10.txt epl-v10.txt
%config(noreplace,missingok) /etc/%{name}.conf

%files lib -f .mfiles-%{name}-lib
%doc LICENSE.txt LICENSE-2.0.txt NOTICE.txt cpl-v10.txt epl-v10.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt LICENSE-2.0.txt NOTICE.txt cpl-v10.txt epl-v10.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.9-alt1_24jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.9-alt1_23jpp8
- java 8 mass update

