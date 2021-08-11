Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jakarta-mail
Version:        1.6.5
Release:        alt1_4jpp11
Summary:        Jakarta Mail API
License:        EPL-2.0 or GPLv2 with exceptions
URL:            https://github.com/eclipse-ee4j/mail
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/mail/archive/%{version}/mail-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.activation:jakarta.activation)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

# package renamed in fedora 34, remove in fedora 36+
Provides:       javamail = %{version}-%{release}
Obsoletes:      javamail < 1.5.2-16

# javadoc package is currently not built
Obsoletes:      javamail-javadoc  < 1.5.2-16
Source44: import.info

%description
The Jakarta Mail API provides a platform-independent and
protocol-independent framework to build mail and messaging applications.

%prep
%setup -n mail-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

# disable unnecessary maven plugins
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :osgiversion-maven-plugin

# disable android-specific code
%pom_disable_module android

# remove profiles that only add unnecessary things
%pom_xpath_remove "pom:project/pom:profiles"

# inject OSGi bundle versions manually instead of using osgiversion-maven-plugin
sed -i "s/\${mail\.osgiversion}/%{version}/g" mail/pom.xml
sed -i "s/\${mail\.osgiversion}/%{version}/g" mailapi/pom.xml

# add aliases for old maven artifact coordinates
%mvn_alias com.sun.mail:mailapi \
    javax.mail:mailapi
%mvn_alias com.sun.mail:jakarta.mail \
    com.sun.mail:javax.mail \
    javax.mail:mail \
    org.eclipse.jetty.orbit:javax.mail.glassfish
%mvn_alias jakarta.mail:jakarta.mail-api \
    javax.mail:javax.mail-api

# add symlinks for compatibilty with old classpaths
%mvn_file com.sun.mail:jakarta.mail \
    %{name}/jakarta.mail \
    javamail/mail \
    javamail/javax.mail \
    javax.mail/javax.mail

%build
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.6.5-alt1_4jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.6.5-alt1_2jpp11
- new version

