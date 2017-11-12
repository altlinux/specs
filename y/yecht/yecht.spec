Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commitversion 157cf13
%global dlversion 0.0.2-0-g157cf13
%global cluster jruby

Name:     yecht
Version:  1.0
Release:  alt1_6jpp8
Summary:  A YAML processor based on Syck
License:  MIT
URL:      http://github.com/%{cluster}/%{name}
Source0:  https://github.com/%{cluster}/%{name}/archive/%{name}-%{version}.zip
Patch0:   disable-jruby-dep.patch

BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
Requires: jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Yecht is a Syck port, a YAML 1.0 processor for Ruby.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -n %{name}-%{name}-%{version}
%patch0

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_8jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_7jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_6jpp7
- new version

