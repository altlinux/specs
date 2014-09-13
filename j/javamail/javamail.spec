Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           javamail
Version:        1.5.0
Release:        alt1_6jpp7
Summary:        Java Mail API
License:        CDDL or GPLv2 with exceptions
URL:            http://www.oracle.com/technetwork/java/javamail
BuildArch:      noarch

# hg clone http://kenai.com/hg/javamail~mercurial
# (cd ./javamail~mercurial && hg archive -r JAVAMAIL-%(sed s/\\./_/g <<<"%{version}") ../%{name}-%{version})
# tar caf %{name}-%{version}.tar.xz %{name}-%{version}
Source:         %{name}-%{version}.tar.xz

BuildRequires:  maven-local
BuildRequires:  jvnet-parent
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-plugin-build-helper

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
%setup -q

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
%pom_xpath_inject /pom:project/pom:properties "<mail.osgiversion>%{version}</mail.osgiversion>"

# Alternative names for super JAR containing API and implementation.
%mvn_alias com.sun.mail:mailapi javax.mail:mailapi
%mvn_alias com.sun.mail:javax.mail javax.mail:mail \
           org.eclipse.jetty.orbit:javax.mail.glassfish
%mvn_file "com.sun.mail:{javax.mail}" %{name}/@1 %{name}/mail

%build
%mvn_build

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

