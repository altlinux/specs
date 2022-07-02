Group: System/Base
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        Diagrams Through ASCII Art
Name:           ditaa
Version:        0.10
Release:        alt1_17jpp11
License:        GPLv2+
URL:            http://ditaa.sourceforge.net/
Source0:        https://github.com/stathissideris/ditaa/archive/v%{version}.tar.gz
Source1:        ditaa.wrapper
Patch0:         ditaa-0.9-port-to-batik-1.8.patch
# Patch from Debian to build with JDK 10+
Patch1:         https://sources.debian.org/data/main/d/ditaa/0.10+ds1-1.2/debian/patches/remove-JavadocTaglet.patch
Patch2:         jdk17.patch
BuildArch:      noarch
BuildRequires:  ant
BuildRequires:  jpackage-utils
BuildRequires:  batik
BuildRequires:  jericho-html
BuildRequires:  xml-commons-apis
BuildRequires:  apache-commons-cli
Requires:       apache-commons-cli
Requires:       xml-commons-apis
Requires:       jericho-html
Requires:       batik
Requires:       jpackage-utils
Source44: import.info

%description
ditaa is a small command-line utility written in Java, that can
convert diagrams drawn using ASCII art ('drawings' that contain
characters that resemble lines like | / - ), into proper bitmap
graphics.

%prep 
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
find -name '*.class' -delete
find -name '*.jar' -delete

%build
install -d bin
build-jar-repository -s -p lib commons-cli batik-all xml-commons-apis-ext jericho-html
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -f build/release.xml

%install
install -D -p -m 0644 releases/%{name}0_9.jar %{buildroot}%{_javadir}/%{name}.jar
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING HISTORY
%{_bindir}/%{name}
%{_javadir}/%{name}.jar

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0.10-alt1_17jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0.10-alt1_12jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_8jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_7jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_6jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_10.r74jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_9.r74jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_8.r74jpp7
- new version

