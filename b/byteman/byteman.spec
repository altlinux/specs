Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name byteman
%define version 2.1.4.1
%global apphomedir %{_datadir}/%{name}
%global bindir %{apphomedir}/bin
%global hash 373601b4e608ea622b2fec947824b99cd0edb124

Name:             byteman
Version:          2.1.4.1
Release:          alt1_7jpp8
Summary:          Java agent-based bytecode injection tool
License:          LGPLv2+
URL:              http://www.jboss.org/byteman
Source0:          https://github.com/bytemanproject/byteman/archive/%{hash}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-shade-plugin
BuildRequires:    maven-failsafe-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-verifier-plugin
BuildRequires:    java_cup
BuildRequires:    jarjar
BuildRequires:    objectweb-asm3
BuildRequires:    junit
BuildRequires:    testng

# Bundling
#BuildRequires:    java_cup = 1:0.11a-12
#BuildRequires:    objectweb-asm = 0:3.3.1-7

%if 0%{?fedora} > 20
Provides:         bundled(objectweb-asm) = 0:5.0.1-1
Provides:         bundled(java_cup) = 1:0.11a-16
%else
Provides:         bundled(objectweb-asm) = 0:3.3.1-8
Provides:         bundled(java_cup) = 1:0.11a-15
%endif
Source44: import.info

%description
Byteman is a tool which simplifies tracing and testing of Java programs.
Byteman allows you to insert extra Java code into your application,
either as it is loaded during JVM startup or even after it has already
started running. The injected code is allowed to access any of your data
and call any application methods, including where they are private.
You can inject code almost anywhere you want and there is no need to
prepare the original source code in advance nor do you have to recompile,
repackage or redeploy your application. In fact you can remove injected
code and reinstall different code while the application continues to execute.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n byteman-%{hash}
# Fix doclint problem
%pom_xpath_inject  "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:configuration" "<additionalparam>-Xdoclint:none</additionalparam>"

# Fix the gid:aid for java_cup
sed -i "s|net.sf.squirrel-sql.thirdparty-non-maven|java_cup|" agent/pom.xml
sed -i "s|java-cup|java_cup|" agent/pom.xml

# org.jboss.byteman:byteman-download requires "-sources" and "-javadoc" artifacts
%mvn_package ':::{sources,javadoc}:' __default

# Remove tools.jar from dependencyManagement (Fedora-specific patch).
# In Fedora tools.jar doesn't need to use system scope or provide
# systemPath - Maven will find it anyways.
%pom_remove_dep com.sun:tools

%build
%mvn_build

%install
%mvn_install

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}

install -d -m 755 $RPM_BUILD_ROOT%{apphomedir}
install -d -m 755 $RPM_BUILD_ROOT%{apphomedir}/lib
install -d -m 755 $RPM_BUILD_ROOT%{bindir}

install -m 755 bin/bmsubmit.sh $RPM_BUILD_ROOT%{bindir}/bmsubmit
install -m 755 bin/bminstall.sh  $RPM_BUILD_ROOT%{bindir}/bminstall
install -m 755 bin/bmjava.sh  $RPM_BUILD_ROOT%{bindir}/bmjava
install -m 755 bin/bmcheck.sh  $RPM_BUILD_ROOT%{bindir}/bmcheck

for f in bmsubmit bmjava bminstall bmcheck; do
cat > $RPM_BUILD_ROOT%{_bindir}/${f} << EOF
#!/bin/sh

export BYTEMAN_HOME=/usr/share/byteman
export JAVA_HOME=/usr/lib/jvm/java

\$BYTEMAN_HOME/bin/${f} \$*
EOF
done

chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

for m in bmunit dtest install sample submit; do
  ln -s %{_javadir}/byteman/byteman-${m}.jar $RPM_BUILD_ROOT%{apphomedir}/lib/byteman-${m}.jar
done

ln -s %{_javadir}/byteman/byteman.jar $RPM_BUILD_ROOT%{apphomedir}/lib/byteman.jar

%files -f .mfiles
%{apphomedir}/*
%{_bindir}/*
%doc README docs/ProgrammersGuide.pdf
%doc docs/copyright.txt

%files javadoc -f .mfiles-javadoc
%doc docs/copyright.txt

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.4.1-alt1_7jpp8
- java8 mass update

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_3jpp7
- new version

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_5jpp7
- new fc release

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_4jpp7
- fc build

