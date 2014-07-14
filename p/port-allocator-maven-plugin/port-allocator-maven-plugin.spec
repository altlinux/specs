BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		port-allocator-maven-plugin
Version:	1.2
Release:	alt2_3jpp7
Summary:	Port Allocator Maven Plugin

Group:		Development/Java
License:	ASL 2.0
URL:		http://github.com/sonatype/port-allocator-maven-plugin

# git clone git://github.com/sonatype/port-allocator-maven-plugin.git
# git archive --format=tar --prefix=port-allocator-maven-plugin-1.2/ port-allocator-maven-plugin-1.2 | xz > port-allocator-maven-plugin-1.2.tar.xz
Source0:	%{name}-%{version}.tar.xz
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt

# Switch parent to sonatype-oss-parent - seems to work
Patch0:		%{name}-parent.patch

BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	maven
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-enforcer-plugin
BuildRequires:	maven-plugin-plugin
BuildRequires:	maven-resources-plugin
BuildRequires:	maven-surefire-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-javadoc-plugin
BuildRequires:	sonatype-oss-parent

Requires:	jpackage-utils
Requires:	maven
Requires:	sonatype-oss-parent
Source44: import.info

%description
Allocate ports to be used during maven build process.

%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} .

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%patch0


%build
mvn-rpmbuild package javadoc:aggregate

%install

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POMs
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 0644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE-2.0.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE-2.0.txt
%{_javadocdir}/%{name}


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

