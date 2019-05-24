Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ perl(AutoLoader.pm) perl(Carp.pm) perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Socket.pm) perl(fastcwd.pl) perl-devel rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
################################################################################
Name:             ldapjdk
################################################################################

Summary:          LDAP SDK
URL:              http://www.dogtagpki.org/
License:          MPLv1.1 or GPLv2+ or LGPLv2+

BuildArch:        noarch

Version:          4.20.0
Release:          alt1_2jpp8
# global           _phase -a1

%global spname		ldapsp
%global filtname	ldapfilt
%global beansname	ldapbeans

# To create a tarball from a version tag:
# $ git archive \
#     --format=tar.gz \
#     --prefix ldap-sdk-<version>/ \
#     -o ldap-sdk-<version>.tar.gz \
#     <version tag>
Source: https://github.com/dogtagpki/ldap-sdk/archive/v%{version}%{?_phase}/ldap-sdk-%{version}%{?_phase}.tar.gz

# To create a patch for all changes since a version tag:
# $ git format-patch \
#     --stdout \
#     <version tag> \
#     > ldap-sdk-VERSION-RELEASE.patch
# Patch: ldap-sdk-VERSION-RELEASE.patch

################################################################################
# Build Dependencies
################################################################################

# autosetup
BuildRequires:    git

BuildRequires:    ant
BuildRequires:    java-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:	  jpackage-utils >= 0:1.5
%else
BuildRequires:    javapackages-local
%endif
BuildRequires:    jss >= 4.5.0

################################################################################
# Runtime Dependencies
################################################################################

Requires:         jpackage-utils >= 0:1.5
Requires:         jss >= 4.5.0
Source44: import.info

Provides: ldapsdk = 1:%version-%release
Obsoletes: ldapsdk <= 1:4.18-alt1_2jpp6



%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

################################################################################
%package javadoc
Group: Development/Documentation
################################################################################

Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}

################################################################################
%prep
################################################################################

%setup -q -n ldap-sdk-%{version}%{?_phase}


# Remove all bundled jars, we must build against build-system jars
rm -f ./java-sdk/ldapjdk/lib/{jss32_stub,jsse,jnet,jaas,jndi}.jar

################################################################################
%build
################################################################################

# Link to build-system BRs
pwd
%if 0%{?rhel} && 0%{?rhel} <= 7
( cd  java-sdk/ldapjdk/lib && build-jar-repository -s -p . jss4 jsse jaas jndi )
%else
( cd  java-sdk/ldapjdk/lib && build-jar-repository -s -p . jss4 )
ln -s /usr/lib/jvm-exports/java/{jsse,jaas,jndi}.jar java-sdk/ldapjdk/lib
%endif
cd java-sdk
if [ ! -e "$JAVA_HOME" ] ; then export JAVA_HOME="%{_jvmdir}/java" ; fi
sh -x ant dist

################################################################################
%install
################################################################################

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
install -pm 644 %{name}.pom %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "ldapsdk:ldapsdk"

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r java-sdk/dist/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s ldapjdk.jar %buildroot%_javadir/ldapsdk.jar

################################################################################
%files -f .mfiles
################################################################################

%{_javadir}/%{spname}*.jar
%{_javadir}/%{filtname}*.jar
%{_javadir}/%{beansname}*.jar
%{_javadir}-1.3.0/*.jar
%_javadir/ldapsdk.jar

################################################################################
%files javadoc
################################################################################

%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*

################################################################################
%changelog
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.20.0-alt1_2jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.19-alt2_7jpp8
- java fc28+ update

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

