# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global spname		ldapsp
%global filtname	ldapfilt
%global beansname	ldapbeans

Name:		ldapjdk
Version:	4.19
Release:	alt2_5jpp8
Epoch:		1
Summary: 	The Mozilla LDAP Java SDK
License:	MPLv1.1 or GPLv2+ or LGPLv2+
Group:		Development/Java
URL:		http://www-archive.mozilla.org/directory/javasdk.html
# mkdir ldapjdk-4.19 ; 
# cvs -d:pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot Export -r LDAPJavaSDK_419 DirectorySDKSourceJava
# tar -zcf ldapjdk-4.19.tar.gz ldapjdk-4.19
Source:		http://pki.fedoraproject.org/pki/sources/%{name}/%{version}/%{name}-%{version}.tar.gz
# originally taken from http://mirrors.ibiblio.org/pub/mirrors/maven2/ldapsdk/ldapsdk/4.1/ldapsdk-4.1.pom
# changed: gId, aId and version
Source1:	http://pki.fedoraproject.org/pki/sources/%{name}/%{version}/%{name}-%{version}.pom

#######################
## ldapjdk-4.19-4
#######################
Patch0:           ldapjdk-Added-getter-methods-for-JDAPFilter-classes.patch
Patch1:           ldapjdk-Added-gitignore-file.patch

Requires:	jpackage-utils >= 0:1.5
Requires:       jss
BuildRequires:  ant
BuildRequires:  java-devel
%if 0%{?rhel}
BuildRequires:	jpackage-utils >= 0:1.5
%else
BuildRequires:  javapackages-local
%endif
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
rm -f ./java-sdk/ldapjdk/lib/{jss32_stub,jsse,jnet,jaas,jndi}.jar
%patch0 -p1
%patch1 -p1

%build
# cleanup CVS dirs
rm -fr $(find . -name CVS -type d)
# Link to build-system BRs
pwd
%if 0%{?rhel}
( cd  java-sdk/ldapjdk/lib && build-jar-repository -s -p . jss4 jsse jaas jndi )
%else
( cd  java-sdk/ldapjdk/lib && build-jar-repository -s -p . jss4 )
ln -s /usr/lib/jvm-exports/java/{jsse,jaas,jndi}.jar java-sdk/ldapjdk/lib
%endif
cd java-sdk
if [ ! -e "$JAVA_HOME" ] ; then export JAVA_HOME="%{_jvmdir}/java" ; fi
sh -x ant dist

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 java-sdk/dist/packages/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 644 java-sdk/dist/packages/%{spname}.jar $RPM_BUILD_ROOT%{_javadir}/%{spname}.jar
install -m 644 java-sdk/dist/packages/%{filtname}.jar $RPM_BUILD_ROOT%{_javadir}/%{filtname}.jar
install -m 644 java-sdk/dist/packages/%{beansname}.jar $RPM_BUILD_ROOT%{_javadir}/%{beansname}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}-1.3.0

pushd $RPM_BUILD_ROOT%{_javadir}-1.3.0
	ln -fs ../java/*%{spname}.jar jndi-ldap.jar
popd

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "ldapsdk:ldapsdk"

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r java-sdk/dist/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
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
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.19-alt2_5jpp8
- new fc release

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.19-alt2_1jpp8
- added BR: javapackages-local for javapackages 5

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.19-alt1_1jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_19jpp8
- new fc release

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

