# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          sshj
Version:       0.8.1
Release:       alt3_4jpp7
Summary:       SSHv2 library for Java
Group:         Development/Java
License:       ASL 2.0
URL:           http://schmizz.net/sshj/
# git clone git://github.com/shikhar/sshj.git sshj-0.8.1
# cd sshj-0.8.1 && git archive --format=tar --prefix=sshj-0.8.1/ v0.8.1 | xz > sshj-0.8.1.tar.xz
Source0:       %{name}-%{version}.tar.xz

Patch0:        %{name}-0.8.0-use-jzlib-as-system-dependency.patch

BuildRequires: jpackage-utils

BuildRequires: apache-sshd
BuildRequires: bouncycastle
BuildRequires: jzlib
BuildRequires: slf4j

# test deps
BuildRequires: junit
BuildRequires: logback
BuildRequires: mockito

BuildRequires: maven-local
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      apache-sshd
Requires:      bouncycastle
Requires:      jzlib
Requires:      slf4j

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
SSH, scp and sftp library for Java.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p0

# Some classes moved from JUnit to hamcrest
sed -i -e 's/org.junit.internal.matchers/org.hamcrest.core/' src/test/java/net/schmizz/sshj/transport/verification/OpenSSHKnownHostsTest.java

%build

mvn-rpmbuild -D_javadir=%{_javadir} install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc CONTRIBUTORS LICENSE NOTICE README.rst

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Tue Aug 12 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_4jpp7
- fixed build with new junit

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_1jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_1jpp7
- new version

