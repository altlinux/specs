# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global spname		ldapsp
%global filtname	ldapfilt
%global beansname	ldapbeans

Name:		ldapjdk
Version:	4.18
Release:	alt1_18jpp8
Epoch:		1
Summary: 	The Mozilla LDAP Java SDK
License:	MPLv1.1 or GPLv2+ or LGPLv2+
Group:		Development/Java
URL:		http://www.mozilla.org/directory/javasdk.html
# mkdir ldapjdk-4.18 ; 
# cvs -d:pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot Export -r LDAPJavaSDK_418 DirectorySDKSourceJava
# tar -zcf ldapjdk-4.18,tar.gz ldapjdk-4.18
Source:		http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}.tar.gz
# originally taken from http://mirrors.ibiblio.org/pub/mirrors/maven2/ldapsdk/ldapsdk/4.1/ldapsdk-4.1.pom
# changed: gId, aId and version
Source1:	http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}.pom
Patch0: 	%{name}-jarnamefix.patch
Patch1:         matching-rule-parsing-640750.patch

Requires: javapackages-tools rpm-build-java
Requires:       jss
BuildRequires:  ant
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  jss

Provides:	jndi-ldap = 1.3.0
BuildArch:	noarch
Source44: import.info

Provides: ldapsdk = 1:%version-%release
Obsoletes: ldapsdk <= 1:4.18-alt1_2jpp6


%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
Obsoletes:      openjmx-javadoc
BuildArch: noarch

%description javadoc
Javadoc for %{name}

%prep
%setup -q
# Remove all bundled jars, we must build against build-system jars
rm -f ./mozilla/directory/java-sdk/ldapjdk/lib/{jss32_stub,jsse,jnet,jaas,jndi}.jar

%patch0 -p1
%patch1 -p1

%build
# cleanup CVS dirs
rm -fr $(find . -name CVS -type d)
# Link to build-system BRs
pwd
( cd  mozilla/directory/java-sdk/ldapjdk/lib && build-jar-repository -s -p . jss4 jsse jaas jndi )
cd mozilla/directory/java-sdk
if [ ! -e "$JAVA_HOME" ] ; then export JAVA_HOME="%{_jvmdir}/java" ; fi
sh -x ant dist

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 mozilla/directory/java-sdk/dist/packages/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 644 mozilla/directory/java-sdk/dist/packages/%{spname}.jar $RPM_BUILD_ROOT%{_javadir}/%{spname}.jar
install -m 644 mozilla/directory/java-sdk/dist/packages/%{filtname}.jar $RPM_BUILD_ROOT%{_javadir}/%{filtname}.jar
install -m 644 mozilla/directory/java-sdk/dist/packages/%{beansname}.jar $RPM_BUILD_ROOT%{_javadir}/%{beansname}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}-1.3.0

pushd $RPM_BUILD_ROOT%{_javadir}-1.3.0
	ln -fs ../java/*%{spname}.jar jndi-ldap.jar
popd

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "ldapsdk:ldapsdk"

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r mozilla/directory/java-sdk/dist/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s ldapjdk.jar %buildroot%_javadir/ldapsdk.jar

%files -f .mfiles
%{_javadir}/%{spname}*.jar
%{_javadir}/%{filtname}*.jar
%{_javadir}/%{beansname}*.jar
%{_javadir}-1.3.0/*.jar
%_javadir/ldapsdk.jar

%files javadoc
%defattr(-,root,root,)
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_18jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_17jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_13jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_12jpp7
- fc update

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_11jpp7
- fc release

* Tue Mar 30 2010 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_2jpp6
- new version

* Mon Sep 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:4.17-alt1_3jpp5
- fixed build with java5

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 1:4.17-alt1_3jpp1.7
- converted from JPackage by jppimport script

