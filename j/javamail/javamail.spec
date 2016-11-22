Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           javamail
Version:        1.5.2
Release:        alt1_3jpp8
Summary:        Java Mail API
License:        CDDL or GPLv2 with exceptions
URL:            http://www.oracle.com/technetwork/java/javamail
BuildArch:      noarch

Source:        https://java.net/projects/javamail/downloads/download/source/javamail-%{version}-src.zip

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

# Adapted from the classpathx-mail (and JPackage glassfish-javamail) Provides.
Provides:       javamail-monolithic = %{version}-%{release}

Provides:       javax.mail
Source44: import.info

%description
The JavaMail API provides a platform-independent and protocol-independent
framework to build mail and messaging applications.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.


%prep
%setup -q -c

add_dep() {
    %pom_xpath_inject pom:project "<dependencies/>" ${2}
    %pom_add_dep com.sun.mail:${1}:%{version}:provided ${2}
}

add_dep smtp mailapi
add_dep javax.mail smtp
add_dep javax.mail pop3
add_dep javax.mail imap
add_dep javax.mail mailapijar

# Remove profiles containing demos and other stuff that is not
# supposed to be deployable.
%pom_xpath_remove /pom:project/pom:profiles

# osgiversion-maven-plugin is used to set ${mail.osgiversion} property
# based on ${project.version}. We don't have osgiversion plugin in
# Fedora so we'll set ${mail.osgiversion} explicitly.
%pom_remove_plugin org.glassfish.hk2:osgiversion-maven-plugin
%pom_remove_dep javax.activation:activation
%pom_xpath_inject /pom:project/pom:properties "<mail.osgiversion>%{version}</mail.osgiversion>"
%pom_xpath_inject /pom:project/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:instructions "<_nouses>true</_nouses>"

# Alternative names for super JAR containing API and implementation.
%mvn_alias com.sun.mail:mailapi javax.mail:mailapi
%mvn_alias com.sun.mail:javax.mail javax.mail:mail \
           org.eclipse.jetty.orbit:javax.mail.glassfish
%mvn_file "com.sun.mail:{javax.mail}" %{name}/@1 %{name}/mail

%build
# Some tests fail on Koji due to networking limitations
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

install -d -m 755 %{buildroot}%{_javadir}/javax.mail/
ln -sf ../%{name}/javax.mail.jar %{buildroot}%{_javadir}/javax.mail/

%files -f .mfiles
%doc mail/src/main/java/overview.html
%doc mail/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/javax.mail/

%files javadoc -f .mfiles-javadoc
%doc mail/src/main/resources/META-INF/LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_16jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_12jpp7
- added OSGi info

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_8jpp7
- new version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

