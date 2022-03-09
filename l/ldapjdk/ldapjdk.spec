%define _unpackaged_files_terminate_build 1

%define _localstatedir  %_var

# JSS built with Java11
%define jss_version 5.1.0

%define java_version 11

Name: ldapjdk
Epoch: 1
Version: 5.1.0
Release: alt1

Summary: LDAP SDK
License: MPL-1.1 or GPLv2+ or LGPLv2+
Group: Development/Java
# Source-git: https://github.com/dogtagpki/ldap-sdk.git
Url: https://www.dogtagpki.org/wiki/LDAP_SDK

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java

BuildRequires: /proc
BuildRequires: ant
BuildRequires: java-devel >= %java_version
BuildRequires: javapackages-local
BuildRequires: javapackages-tools
BuildRequires: jss >= %jss_version

BuildArch: noarch

Provides: ldapsdk = 1:%version-%release
Obsoletes: ldapsdk <= 1:4.18-alt1_2jpp6

Requires: jss >= %jss_version
Requires: java >= %java_version

%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

################################################################################
%package javadoc
Group: Development/Documentation
################################################################################

Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
Javadoc for %name

################################################################################
%prep
################################################################################

%setup
%patch -p1

################################################################################
%build
################################################################################

cd java-sdk
%ant -v dist

################################################################################
%install
################################################################################

install -d -m 755 %buildroot%_javadir
install -m 644 java-sdk/dist/packages/%name.jar %buildroot%_javadir/%name.jar
install -m 644 java-sdk/dist/packages/ldapsp.jar %buildroot%_javadir/ldapsp.jar
install -m 644 java-sdk/dist/packages/ldapfilt.jar %buildroot%_javadir/ldapfilt.jar
install -m 644 java-sdk/dist/packages/ldapbeans.jar %buildroot%_javadir/ldapbeans.jar

mkdir -p %buildroot%_mavenpomdir
install -pm 644 java-sdk/ldapjdk/pom.xml %buildroot%_mavenpomdir/JPP-ldapjdk.pom
install -pm 644 java-sdk/ldapfilter/pom.xml %buildroot%_mavenpomdir/JPP-ldapfilter.pom
install -pm 644 java-sdk/ldapbeans/pom.xml %buildroot%_mavenpomdir/JPP-ldapbeans.pom
install -pm 644 java-sdk/ldapsp/pom.xml %buildroot%_mavenpomdir/JPP-ldapsp.pom

install -d -m 755 %buildroot%_javadocdir/%name
cp -r java-sdk/dist/doc/* %buildroot%_javadocdir/%name
ln -s ldapjdk.jar %buildroot%_javadir/ldapsdk.jar

################################################################################
%files
################################################################################

%_javadir/%name.jar
%_javadir/ldapsp.jar
%_javadir/ldapfilt.jar
%_javadir/ldapbeans.jar
%_javadir/ldapsdk.jar
%_mavenpomdir/JPP-ldapjdk.pom
%_mavenpomdir/JPP-ldapsp.pom
%_mavenpomdir/JPP-ldapfilter.pom
%_mavenpomdir/JPP-ldapbeans.pom

################################################################################
%files javadoc
################################################################################

%dir %_javadocdir/%name
%_javadocdir/%name/*

################################################################################
%changelog
* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 1:5.1.0-alt1
- 5.0.0 -> 5.1.0.

* Thu Nov 25 2021 Stanislav Levin <slev@altlinux.org> 1:5.0.0-alt1
- 4.22.0 -> 5.0.0.

* Fri May 21 2021 Stanislav Levin <slev@altlinux.org> 1:4.22.0-alt2
- Built with Java11.

* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 1:4.22.0-alt1
- 4.21.0 -> 4.22.0.

* Mon Aug 26 2019 Stanislav Levin <slev@altlinux.org> 1:4.21.0-alt1
- 4.20.0 -> 4.21.0.

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

