Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# use dcm4che-test as name, no use carrying the version in the name
%global svn_rev 15516

Name:           dcm4che-test
Version:        2.6
Release:        alt3_0.12.20110530svn15516jpp8
Summary:        Test images for dcm4che2
License:        MPLv1.1 or GPLv2 or LGPLv2
URL:            http://www.dcm4che.org/confluence/display/proj/The+Project
BuildArch:      noarch
# Generated from an svn checkout:
# svn export svn://svn.code.sf.net/p/dcm4che/svn/dcm4che2-test/tags/dcm4che2-test-2.6
# tar -cvJf dcm4che2-test-2.6.tar.xz dcm4che2-test-2.6/
Source0:        dcm4che2-test-%{version}.tar.xz

BuildRequires:    maven-local
Source44: import.info

%description
DCM4CHE Test Data and Libraries

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n dcm4che2-test-%{version}

%build

%mvn_file :%{name}-image %{name}-image
%mvn_build -X -- -Dproject.build.sourceEncoding=UTF-8
rm -rf target/site/apidocs/javadoc.sh

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt3_0.12.20110530svn15516jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt3_0.11.20110530svn15516jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt3_0.8.20110530svn15516jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt3_0.5.20110530svn15516jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt3_0.3.20110530svn15516jpp7
- new fc release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_0.3.20110530svn15516jpp7
- new fc release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_0.3.20110530svn15516jpp7
- new version

