Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             jline2
Version:          2.5
Release:          alt1_5jpp7
Summary:          JLine is a Java library for handling console input
Group:            Development/Java
License:          BSD and ASL 2.0
URL:              https://github.com/jline/jline2

# git clone git://github.com/jline/jline2.git
# cd jline2/ && git archive --format=tar --prefix=jline-2.5/ jline-2.5 | xz > jline-2.5.tar.xz
Source0:          jline-%{version}.tar.xz
Patch0:           %{name}-%{version}-pom.patch
Patch1:           %{name}-%{version}-protected-void-back.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    junit4
BuildRequires:    jansi
BuildRequires:    fusesource-pom
BuildRequires:    maven-surefire-provider-junit4

Requires:         jpackage-utils
Requires:         jansi
Source44: import.info

%description
JLine is a Java library for handling console input. It is similar
in functionality to BSD editline and GNU readline. People familiar
with the readline/editline capabilities for modern shells (such as
bash and tcsh) will find most of the command editing features of
JLine to be familiar. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jline-%{version}
%patch0 -p1
%patch1 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/jline-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# Uh, oh...
# http://sourceforge.net/mailarchive/message.php?msg_id=27330388
# https://github.com/jline/jline2/commit/7a4d27430999706f0fd30b4548d5879275a88de2#pom.xml
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "jline:jline"

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc README.md LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_5jpp7
- fc version

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_3jpp6
- new jpp relase

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp6
- new version

