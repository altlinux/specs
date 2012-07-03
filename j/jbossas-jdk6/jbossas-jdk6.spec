Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jbossas-jdk6
Version:        1
Release:        alt1_1jpp6
Summary:        Compatibility patch for allowing jbossas-4.2.X to run against JDK6

Group:          Development/Java
License:        GPL
URL:            http://www.jpackage.org/
BuildArch: noarch

BuildRequires: jbossas >= 4.2.0 jbossas < 5.0.0
Requires: jbossas >= 4.2.0 jbossas < 5.0.0

%description
JavaSE 6 includes support for JAX-WS, Version 2.1. Before starting your server, you need replace the APIs included in JDK 6 with the JBossWS jars from JBossASSee: http://www.redhat.com/docs/en-US/JBoss_Enterprise_Application_Platform/4.3.0.cp06/html-single/JDK6_Compatibility_Notes/index.html

%install
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/jbossas/lib/endorsed/
jboss_ws_jars="jboss-jaxrpc.jar jboss-jaxws-ext.jar jboss-jaxws.jar jboss-saaj.jar"
for jar in $jboss_ws_jars; do
	ln -s /usr/share/java/jbossws/$jar $RPM_BUILD_ROOT/usr/share/jbossas/lib/endorsed/
	echo "/usr/share/jbossas/lib/endorsed/$jar" >> files
done

%files -f files

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1-alt1_1jpp6
- new version

