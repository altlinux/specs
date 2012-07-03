Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             jansi
Version:          1.6
Release:          alt2_2jpp7
Summary:          Jansi is a java library for generating and interpreting ANSI escape sequences
Group:            Development/Java
License:          ASL 2.0
URL:              http://jansi.fusesource.org/

# git clone git://github.com/fusesource/jansi.git
# cd jansi && git archive --format=tar --prefix=jansi-1.6/ jansi-project-1.6 | xz > jansi-1.6.tar.xz
Source0:          %{name}-%{version}.tar.xz
Patch0:           %{name}-%{version}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-license-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    jansi-native
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-plugin-bundle
BuildRequires:    junit4
BuildRequires:    fusesource-pom
BuildRequires:    maven-surefire-provider-junit4

Requires:         jpackage-utils
Requires:         jansi-native
Requires:         hawtjni
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
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}/target/%{name}-%{version}.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# JAVADOC
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-project.pom
install -pm 644 %{name}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}-project.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc readme.md license.txt changelog.md

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp7
- fixed pom

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp7
- fc version

* Sat Feb 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp6
- new version

