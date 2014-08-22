Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bits 32
%global debug_package %{nil}

%ifarch x86_64 ppc64 s390x sparc64
  %global bits 64
%endif

Name:             jansi-native
Version:          1.4
Release:          alt1_5jpp7
Summary:          Jansi Native implements the JNI Libraries used by the Jansi project
Group:            Development/Java
License:          ASL 2.0
URL:              http://jansi.fusesource.org/

# git clone git://github.com/fusesource/jansi-native.git
# cd jansi-native && git archive --format=tar --prefix=jansi-native-1.4/ jansi-native-1.4 | xz > jansi-native-1.4.tar.xz
Source0:          jansi-native-%{version}.tar.xz

Patch0:           0001-Fixing-archiver-requires-AM_PROG_AR-in-configure.ac-.patch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-report-plugin
BuildRequires:    maven-project-info-reports-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-plugin-bundle
BuildRequires:    maven-plugin-jxr
BuildRequires:    junit4
BuildRequires:    hawtjni
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
BuildRequires:    make
BuildRequires:    fusesource-pom
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-hawtjni-plugin

Requires:         hawtjni
Requires:         jpackage-utils
Source44: import.info

%description
Jansi is a small java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it like Windows and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
# JAR
mkdir -p $RPM_BUILD_ROOT%{_jnidir}
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p target/%{name}-%{version}-linux%{bits}.jar $RPM_BUILD_ROOT%{_jnidir}/%{name}-linux.jar

# JAVADOC
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_to_maven_depmap org.fusesource.jansi jansi-native %{version} JPP %{name}
%add_to_maven_depmap org.fusesource.jansi jansi-native-linux%{bits} %{version} JPP %{name}-linux

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_jnidir}/*
%{_javadir}/*
%doc readme.md license.txt changelog.md

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%changelog
* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- new version

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp7
- new version

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_1jpp6
- fixed build

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp6
- new version

