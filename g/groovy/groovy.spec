Obsoletes: groovy10 < 1.1
Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# Note to packagers: When rebasing this to a later version, do not
# forget to ensure that sources 1 and 2 are up to date as well as
# the Requires list.

Name:           groovy
Version:        1.8.6
Release:        alt1_2jpp7
Summary:        Dynamic language for the Java Platform

Group:          Development/Java
License:        ASL 2.0
URL:            http://groovy.codehaus.org/
Source0:        http://dist.groovy.codehaus.org/distributions/%{name}-src-%{version}.zip
Source1:        groovy-script
Source2:        groovy-starter.conf
Source3:        groovy.desktop
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  ant-antlr
BuildRequires:  objectweb-asm
BuildRequires:  bsf
BuildRequires:  apache-ivy
BuildRequires:  jansi
BuildRequires:  jline
BuildRequires:  jsp21
BuildRequires:  junit
BuildRequires:  servlet25
BuildRequires:  xstream
BuildRequires:  desktop-file-utils
BuildRequires:  jpackage-utils
BuildRequires:  apache-commons-cli
BuildRequires:  unzip
Requires:       jpackage-utils

# The are all runtime dependencies of the script
# TODO: Think of splitting them into a separate subpackage
Requires:       ant
Requires:       ant-junit
Requires:       antlr
Requires:       objectweb-asm
Requires:       bsf
Requires:       apache-commons-cli
Requires:       apache-commons-logging
Requires:       ivy
Requires:       jansi
Requires:       jline
Requires:       jsp21
Requires:       junit
Requires:       servlet25
Requires:       xstream
Source44: import.info


%description
Groovy is an agile and dynamic language for the Java Virtual Machine,
built upon Java with features inspired by languages like Python, Ruby and
Smalltalk.  It seamlessly integrates with all existing Java objects and
libraries and compiles straight to Java bytecode so you can use it anywhere
you can use Java.


%package javadoc
Summary:        API Documentation for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch
%description javadoc
JavaDoc documentation for %{name}


%prep
%setup -q


%build
mkdir -p target/lib/{compile,tools}

# Construct classpath
build-jar-repository target/lib/compile servlet jsp \
        objectweb-asm/asm-tree objectweb-asm/asm \
        objectweb-asm/asm-util objectweb-asm/asm-analysis \
        antlr ant/ant-antlr antlr \
        bsf jline xstream ant junit apache-ivy commons-cli \
        jansi

# Build
# TODO: Build at least tests, maybe examples
ant -DskipTests=on -DskipExamples=on -DskipFetch=on -DskipEmbeddable=on \
        createJars javadoc


%install

# Code
install -d $RPM_BUILD_ROOT%{_javadir}
install -p -m644 target/dist/groovy.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Startup scripts
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/groovy
for TOOL in grape groovyc groovyConsole java2groovy groovysh
do
        ln $RPM_BUILD_ROOT%{_bindir}/groovy \
                $RPM_BUILD_ROOT%{_bindir}/$TOOL
done

# Configuration
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m644 %{SOURCE2} \
        $RPM_BUILD_ROOT%{_sysconfdir}/groovy-starter.conf

# Desktop icon
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m644 src/main/groovy/ui/ConsoleIcon.png \
        $RPM_BUILD_ROOT%{_datadir}/pixmaps/groovy.png
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        %{SOURCE3}

# API Documentation
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
find target -type d |xargs chmod 755
cp -rp target/html/api/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

# Maven depmap
install -d $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m644 pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.groovy %{name} %{version} JPP %{name}

touch $RPM_BUILD_ROOT%{_sysconfdir}/groovy.conf

%files
%{_bindir}/*
%{_javadir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%config(noreplace) %{_sysconfdir}/groovy-starter.conf
%config(noreplace,missingok) %{_sysconfdir}/groovy.conf

%doc LICENSE.txt NOTICE.txt README.md 


%files javadoc
%{_javadocdir}/*


%changelog
* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.6-alt1_2jpp7
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_2jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_2jpp5
- use maven1

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- selected java5 compiler explicitly

* Sun May 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- disabled rebuild-java-repository

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Nov 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

