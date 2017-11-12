# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global gittag v1.1.1
%global gitname svgSalamander
# spec file for package svgsalamander

Name:           svgsalamander
Version:        1.1.1
Release:        alt1_3jpp8
Summary:        An SVG engine for Java

Group:          Development/Other
License:        LGPLv2+ or BSD
URL:            https://github.com/blackears/svgSalamander/
Source0:        https://github.com/blackears/%{gitname}/archive/%{gittag}/%{gitname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  java-devel
BuildRequires:  javacc-maven-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  sonatype-oss-parent

Provides:       %{gitname}
Source44: import.info


%description
SVG Salamander is an SVG engine for Java that's designed to be small, fast, 
and allow programmers to use it with a minimum of fuss. It's in particular 
targeted for making it easy to integrate SVG into Java games and making it 
much easier for artists to design 2D game content - from rich interactive 
menus to charts and graphcs to complex animations.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{gitname}-%{version}

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
%mvn_file : %{name} svgSalamander svg-salamander
%mvn_alias : com.kitfox.svg:svg-salamander
%mvn_build
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

