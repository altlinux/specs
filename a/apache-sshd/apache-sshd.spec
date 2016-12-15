Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           apache-sshd
Version:        0.14.0
Release:        alt1_3jpp8
Summary:        Apache SSHD
License:        ASL 2.0
URL:            http://mina.apache.org/sshd-project

Source0:        http://www.eu.apache.org/dist/mina/sshd/%{version}/dist/%{name}-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.mina:mina-core)
BuildRequires:  mvn(org.apache.tomcat:tomcat-jni)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch:      noarch
Source44: import.info

%description
Apache SSHD is a 100% pure java library to support the SSH protocols on both
the client and server side.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{name}.

%prep
%setup -q

# Use tomcat-jni instead of unavailable tomcat-apr
%pom_change_dep -r tomcat:tomcat-apr org.apache.tomcat:tomcat-jni:8.0.23

# Build the core only:
%pom_disable_module assembly
%pom_disable_module sshd-pam
%pom_disable_module sshd-sftp
%pom_disable_module sshd-git

# Disable the plugins that we don't need:
%pom_remove_plugin :maven-remote-resources-plugin
# Too many files with unapproved license
%pom_remove_plugin org.apache.rat:apache-rat-plugin

%build
# tests require ch.ethz.ganymed:ganymed-ssh2
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_3jpp8
- new version

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_1jpp7
- new release

