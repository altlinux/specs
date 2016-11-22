Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# READ BEFORE UPDATING: After updating this package to new upstream
# version eclipse-ecf should be rebuilt.  For more info, see:
# https://fedoraproject.org/wiki/SIGs/Java#Package_Update.2FRebuild_Notes

%global base_name codec
%global short_name commons-%{base_name}

Name:          apache-%{short_name}
Version:       1.10
Release:       alt1_3jpp8
Summary:       Implementations of common encoders and decoders
License:       ASL 2.0
URL:           http://commons.apache.org/%{base_name}/
BuildArch:     noarch

Source0:       http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# Data in DoubleMetaphoneTest.java originally has an inadmissible license.
# The author gives MIT in e-mail communication.
Source1:       aspell-mail.txt

BuildRequires: maven-local
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
Source44: import.info

%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders. Examples include Base64, Hex,
Phonetic and URLs.

%package javadoc
Group: Development/Java
Summary:       API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} aspell-mail.txt
sed -i 's/\r//' RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

%mvn_file : %{short_name} %{name}
%mvn_alias : %{short_name}:%{short_name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES* aspell-mail.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt aspell-mail.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_5jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_5jpp7
- new version

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- added OSGi manifest

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp7
- new version

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_5jpp6
- fixed repolib

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_5jpp6
- fixed repolib

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp6
- new version

