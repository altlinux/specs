Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global long_ver  2010-12-19

Name:           base64coder
Version:        20101219
Release:        alt3_20jpp8
Summary:        Fast and compact Base64 encoder/decoder Java library
License:        EPL or LGPLv2+ or GPLv2+ or ASL 2.0 or BSD
BuildArch:      noarch
URL:            http://www.source-code.biz/%{name}/java/
Source0:        http://repo2.maven.org/maven2/biz/source_code/%{name}/%{long_ver}/%{name}-%{long_ver}-distribution.zip

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
Base64Coder is a fast and compact Base64 encoder/decoder class.

There is no Base64 encoder/decoder in the standard Java SDK class
library.  The undocumented classes sun.misc.BASE64Encoder and
sun.misc.BASE64Decoder should not be used.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{long_ver}
sed -i 's/\r//g' README.txt CHANGES.txt
%mvn_file : %{name}
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt CHANGES.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 20101219-alt3_20jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 20101219-alt3_19jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 20101219-alt3_17jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 20101219-alt3_15jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 20101219-alt3_14jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 20101219-alt3_13jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 20101219-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 20101219-alt1_9jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 20101219-alt1_7jpp7
- update

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 20101219-alt1_5jpp7
- new release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 20101219-alt1_2jpp7
- new version

