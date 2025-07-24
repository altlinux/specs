%define _unpackaged_files_terminate_build 1

# used by mvn_build
%def_without javadoc

%define _localstatedir  %_var

# ldapjdk was renamed dogtag-ldapjdk
%define ldapjdk_rebranded_version 5.2.0-alt1

%define jss_version 5.6.0
%define java_version 21

Name: ldapjdk
Epoch: 1
Version: 5.6.0
Release: alt1

Summary: LDAP SDK
License: MPL-1.1 or GPLv2+ or LGPLv2+
Group: Development/Java
Url: https://github.com/dogtagpki/ldap-sdk
Vcs: https://github.com/dogtagpki/ldap-sdk
Source: %name-%version.tar
Patch: %name-%version-alt.patch

# - upstream doesn't support i586 (Fedora's Java 17 is not built for that arch)
# - ALT's Java 17 is not built for armh
ExcludeArch: %ix86 armh

BuildRequires(pre): rpm-macros-java
BuildRequires: java-devel >= %java_version
BuildRequires: maven-local
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-jdk14)
BuildRequires: mvn(org.dogtagpki.jss:jss-base) >= %jss_version

%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

%package -n dogtag-ldapjdk
Summary: LDAP SDK
Group: System/Libraries

Provides: ldapjdk = %EVR
Obsoletes: ldapjdk < %ldapjdk_rebranded_version

Requires: dogtag-jss >= %jss_version
Requires: java >= %java_version

%description -n dogtag-ldapjdk
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

%prep
%setup
%patch -p1
# flatten-maven-plugin is not available in RPM
%pom_remove_plugin org.codehaus.mojo:flatten-maven-plugin

# specify Maven artifact locations
%mvn_file org.dogtagpki.ldap-sdk:ldapjdk ldapjdk/ldapjdk ldapjdk
%mvn_file org.dogtagpki.ldap-sdk:ldapbeans ldapjdk/ldapbeans ldapbeans
%mvn_file org.dogtagpki.ldap-sdk:ldapfilter ldapjdk/ldapfilter ldapfilt
%mvn_file org.dogtagpki.ldap-sdk:ldapsp ldapjdk/ldapsp ldapsp
%mvn_file org.dogtagpki.ldap-sdk:ldaptools ldapjdk/ldaptools ldaptools

%build
%mvn_build

%install
%mvn_install

%files -n dogtag-ldapjdk -f .mfiles

%changelog
* Thu Feb 27 2025 Stanislav Levin <slev@altlinux.org> 1:5.6.0-alt1
- 5.4.1 -> 5.6.0.

* Tue Aug 01 2023 Stanislav Levin <slev@altlinux.org> 1:5.4.1-alt1
- 5.2.0 -> 5.4.1.

* Tue Aug 23 2022 Stanislav Levin <slev@altlinux.org> 1:5.2.0-alt1
- 5.1.0 -> 5.2.0.

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

