BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		javamail
Version:	1.4.3
Release:	alt1_8jpp7
Summary:	Java Mail API

Group:		Development/Java
License:	CDDL or GPLv2 with exceptions
URL:		http://java.sun.com/products/javamail/

# Parent POM
Source0:	http://download.java.net/maven/2/com/sun/mail/all/%{version}/all-%{version}.pom

# POMs and source files for things that get built
Source1:	http://download.java.net/maven/2/javax/mail/mail/%{version}/mail-%{version}-sources.jar
Source2:	http://download.java.net/maven/2/javax/mail/mail/%{version}/mail-%{version}.pom
Source3:	http://download.java.net/maven/2/com/sun/mail/dsn/%{version}/dsn-%{version}-sources.jar
Source4:	http://download.java.net/maven/2/com/sun/mail/dsn/%{version}/dsn-%{version}.pom

# Additional POMs for things that are provided by the monolithic mail.jar
Source5:	http://download.java.net/maven/2/javax/mail/mailapi/%{version}/mailapi-%{version}.pom
Source6:	http://download.java.net/maven/2/com/sun/mail/imap/%{version}/imap-%{version}.pom
Source7:	http://download.java.net/maven/2/com/sun/mail/pop3/%{version}/pop3-%{version}.pom
Source8:	http://download.java.net/maven/2/com/sun/mail/smtp/%{version}/smtp-%{version}.pom

# http://kenai.com/projects/javamail/sources/mercurial/content/parent-distrib/pom.xml?raw=true
Source9:	%{name}-parent-distrib.pom

# Remove Maven plugins we don't have yet
# Remove unavailable-on-Fedora dependencies from pom.xml
Patch0:		%{name}-cleanup-poms.patch

BuildRequires:	jpackage-utils
BuildRequires:	maven
BuildRequires:	maven-assembly-plugin
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-dependency-plugin
BuildRequires:	maven-install-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-javadoc-plugin
BuildRequires:	maven-resources-plugin
BuildRequires:	maven-site-plugin
BuildRequires:	maven-plugin-bundle
BuildRequires:	maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:	tomcat6-jsp-2.1-api


Requires:	jpackage-utils

# Requirements from POMs
Requires:	tomcat6-jsp-2.1-api

# Adapted from the classpathx-mail (and JPackage glassfish-javamail) Provides
Provides:	javamail-monolithic = 0:%{version}

BuildArch:	noarch
Source44: import.info

%description
The JavaMail API provides a platform-independent and protocol-independent
framework to build mail and messaging applications.


%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	jpackage-utils >= 0:1.7.5
BuildArch: noarch

%description javadoc
%{summary}.


%prep
%setup -c -T
mkdir -p mail dsn

(cd mail && jar xvf %SOURCE1 && cp %SOURCE2 ./pom.xml)
(cd dsn && jar xvf %SOURCE3 && cp %SOURCE4 ./pom.xml)

for sub in *; do
	pushd $sub
	mkdir -p src/main/java src/main/resources
	mv META-INF src/main/resources
	[ -e com ] && mv com src/main/java
	[ -e javax ] && mv javax src/main/java
	popd
done

cp %SOURCE0 ./pom.xml
mkdir poms
cp %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9 poms

%patch0 -p1

# Convert license file to UTF-8
for file in mail/src/main/resources/META-INF/*.txt; do
	iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
	touch -r $file $file.new && \
	mv $file.new $file
done


%build
mvn-rpmbuild \
    -Dproject.build.sourceEncoding=UTF-8 \
	-P deploy \
	package javadoc:aggregate


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 p $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-all.pom
%add_maven_depmap JPP.%{name}-all.pom

# Install everything
for sub in mail dsn; do
    install -m 644 $sub/target/$sub.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$sub.jar
done

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -m 644 mail/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-mail.pom
install -m 644 dsn/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-dsn.pom

# Install the remaining POMs
for sub in mailapi imap pop3 smtp; do
 install -m 644 poms/$sub-%{version}.pom \
         $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-$sub.pom
done

# Add maven dependency information
%add_maven_depmap JPP.%{name}-mail.pom %{name}/mail.jar -a "javax.mail:mailapi,com.sun.mail:imap,com.sun.mail:pop3,com.sun.mail:smtp"
%add_maven_depmap JPP.%{name}-dsn.pom %{name}/dsn.jar

install -m 644 poms/%{name}-parent-distrib.pom \
	$RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-parent-distrib.pom
%add_maven_depmap JPP.%{name}-parent-distrib.pom


%files
%doc mail/src/main/resources/META-INF/LICENSE.txt mail/overview.html
%{_javadir}/%{name}
%config(noreplace) %{_mavendepmapfragdir}/*
%{_mavenpomdir}/*.pom

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_8jpp7
- new version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

