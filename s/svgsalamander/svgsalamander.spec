# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
#
# spec file for package svgsalamander

Name:           svgsalamander
Version:        0.1.10
Release:        alt1_3jpp7
Summary:        An SVG engine for Java

Group:          Development/Java
License:        LGPLv2+ or BSD
URL:            http://svgsalamander.java.net/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-generate-tarball.sh
#Source built using the following commands : sh svgSalamander-generate-tarball.sh

BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  javacc-maven-plugin
BuildRequires:  maven-enforcer-plugin
Requires:       jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
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
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

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
mvn-rpmbuild install javadoc:aggregate 
popd

%install
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_javadocdir}/%{name}

install -Dpm 0644 svg-core/target/kitfox-svg-salamander-1.0.8.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/svgSalamander.jar

install -Dpm 644 www/maven/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap com.kitfox.svg svg-salamander %{version} JPP %{name}

%files
%doc  www/docs/{exampleCode/,use.html}
%{_javadir}/%{name}.jar
%{_javadir}/svgSalamander.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%files javadoc
%{_javadocdir}/%{name}



%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.10-alt1_3jpp7
- new release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.10-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_2jpp7
- new version

