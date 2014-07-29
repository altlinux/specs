# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: apache-sshd
Version: 0.7.0
Release: alt2_3jpp7
Summary: Apache SSHD

Group: Development/Java
License: ASL 2.0
URL: http://mina.apache.org/sshd

# Take into account that this URL will take you to a mirror
# system, so you will need to use a browser to get the real file:
Source0: http://www.apache.org/dyn/closer.cgi/mina/sshd/%{version}/%{name}-%{version}-src.tar.gz

# Build the core only:
Patch0: %{name}-build-the-core-only.patch

# Dont try to download the license file:
Patch1: %{name}-dont-download-license.patch

# Use jzlib and tomcat-apr as a system dependencies:
Patch2: %{name}-use-jzlib-as-system-dependency.patch
Patch3: %{name}-use-tomcat-apr-as-system-dependency.patch

# User version of bouncycastle for JDK6:
Patch4: %{name}-use-bouncycastle-for-jdk6.patch

BuildArch: noarch

Requires: jpackage-utils

Requires: apache-mina >= 2.0.4
Requires: jzlib >= 1.1.0
Requires: tomcat-lib >= 7.0.25

BuildRequires: jpackage-utils
BuildRequires: maven-local

BuildRequires: apache-mina >= 2.0.4
BuildRequires: jzlib >= 1.1.0
BuildRequires: bouncycastle >= 1.46
BuildRequires: tomcat-lib >= 7.0.25

BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
Source44: import.info


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description
Apache SSHD is a 100% pure java library to support the SSH protocols on both
the client and server side.


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build

# In the tarball distributed by Apache the source code is inside the srv
# directory:
cd src

# Skip the tests as they don't run correctly with the current
# version of the jzlib compression library that we have in the
# distribution at the moment:
mvn-rpmbuild \
  -Dmaven.test.skip=true \
  -Dproject.build.sourceEncoding=UTF-8 \
  -D_javadir=%{_javadir} \
  install \
  javadoc:aggregate


%install

# Jar files:
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -p src/sshd-core/target/sshd-core-%{version}.jar %{buildroot}%{_javadir}/%{name}/sshd-core.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 src/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-sshd-parent.pom
install -pm 644 src/sshd-core/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-sshd-core.pom

# Dependency map:
%add_maven_depmap JPP.%{name}-sshd-parent.pom
%add_maven_depmap JPP.%{name}-sshd-core.pom %{name}/sshd-core.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp src/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc src/LICENSE.txt
%doc src/NOTICE.txt


%files javadoc
%{_javadocdir}/%{name}
%doc src/LICENSE.txt
%doc src/NOTICE.txt


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_1jpp7
- new release

