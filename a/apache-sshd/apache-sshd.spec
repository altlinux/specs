Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: apache-sshd
Version: 0.9.0
Release: alt1_2jpp7
Summary: Apache SSHD
License: ASL 2.0
URL: http://mina.apache.org/sshd-project/

# Take into account that this URL will take you to a mirror
# system, so you will need to use a browser to get the real file:
Source0: http://www.apache.org/dyn/closer.cgi/mina/sshd/%{version}/%{name}-%{version}-src.tar.gz

# User version of bouncycastle for JDK6:
Patch0: %{name}-use-bouncycastle-for-jdk6.patch

# Use tomcat-coyote instead of unavailable tomcat-apr
Patch1: %{name}-use-tomcat-coyote.patch

BuildArch: noarch

BuildRequires: apache-mina
BuildRequires: bouncycastle >= 1.46
BuildRequires: jzlib >= 1.1.0
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-shared
BuildRequires: tomcat-lib >= 7.0.25

# This is needed to avoid generating a version specific requirement for the
# bouncycastle package:
AutoReqProv: no
Requires: jpackage-utils
Requires: mvn(com.jcraft:jzlib)
Requires: mvn(org.apache.mina:mina-core)
Requires: mvn(org.apache.tomcat:tomcat-coyote)
Requires: mvn(org.bouncycastle:bcprov-jdk16)
Provides: mvn(org.apache.sshd:sshd) = %{version}
Provides: mvn(org.apache.sshd:sshd-core) = %{version}
Provides: mvn(org.apache.sshd:sshd-sftp) = %{version}
Provides: mvn(org.apache.sshd:sshd:pom:) = %{version}
Source44: import.info


%description
Apache SSHD is a 100% pure java library to support the SSH protocols on both
the client and server side.


%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

# Build the core only:
%pom_disable_module assembly
%pom_disable_module sshd-pam

# Disable the plugins that we don't need:
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :apache-rat-plugin

%build

# Skip the tests as they don't run correctly with the current
# version of the jzlib compression library:
%mvn_build -f


%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt
%doc NOTICE.txt


%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt
%doc NOTICE.txt


%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_1jpp7
- new release

