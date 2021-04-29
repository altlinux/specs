Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global gittag v1.1.2
%global gitname svgSalamander
# spec file for package svgsalamander

Name:           svgsalamander
Version:        1.1.2
Release:        alt1_5jpp11
Summary:        An SVG engine for Java

License:        LGPLv2+ or BSD
URL:            https://github.com/blackears/svgSalamander/
Source0:        https://github.com/blackears/%{gitname}/archive/%{gittag}/%{gitname}-%{version}.tar.gz
# Pulled from version 1.1.1
Source1:        pom.xml
# The interesting code changes from release to the commit 658fd1a
# https://github.com/blackears/svgSalamander/compare/v1.1.2...658fd1a
Patch1:         svgsalamander-master.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  javacc-maven-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  sonatype-oss-parent
BuildRequires:  dos2unix
BuildRequires:  ant

Provides:       %{gitname}
Source44: import.info


%description
SVG Salamander is an SVG engine for Java that's designed to be small, fast, 
and allow programmers to use it with a minimum of fuss. It's in particular 
targeted for making it easy to integrate SVG into Java games and making it 
much easier for artists to design 2D game content - from rich interactive 
menus to charts and graphcs to complex animations.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{gitname}-%{version}
# To apply patches, we need normal line endings
find . -name '*.java' -exec dos2unix '{}' \;
%patch1 -p1

find . -name '*.jar' -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

# Remove DOS line endings
for file in www/docs/*.html www/docs/exampleCode/*.html; do
  sed 's|\r||g' $file >$file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done


%build
pushd svg-core
cp %SOURCE1 pom.xml
%mvn_file : %{name} svgSalamander svg-salamander
%mvn_alias : com.kitfox.svg:svg-salamander
%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8
popd

%install
pushd svg-core
%mvn_install
popd

%files -f svg-core/.mfiles
%doc www/docs/exampleCode/
%doc www/docs/use.html
%doc www/license/*

%files javadoc -f svg-core/.mfiles-javadoc
%doc www/license/*

%changelog
* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt1_5jpp11
- new version

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.39-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.33-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.19-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.10-alt1_3jpp7
- new release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.10-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_2jpp7
- new version

