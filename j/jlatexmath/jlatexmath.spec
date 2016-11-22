Serial: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jlatexmath
Version:        1.0.3
Release:        alt1_4jpp8
Summary:        Java API to display mathematical formulas written in LaTeX

Group:          Development/Other
License:        GPLv2+
URL:            http://forge.scilab.org/index.php/p/jlatexmath/
Source0:        http://forge.scilab.org/index.php/p/jlatexmath/downloads/get/%{name}-src-all-%{version}.zip

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant

Requires: javapackages-tools rpm-build-java

BuildArch:      noarch
Source44: import.info

%description
The goal of this Java API is to display mathematical formulas written in LaTeX.
The default encoding is UTF-8 and most of LaTeX commands are available.

JLaTeXMath is a fork of the excellent project JMathTeX.

%package fop
Summary:        FOP plug-in for %{name}
Group:          Development/Other

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires:  fop

Requires: javapackages-tools rpm-build-java
Requires:       %{name} = %{version}
Requires:       fop


%description fop
This package contains the FOP plug-in for %{name}.

%package javadoc
Summary:        API Documentation for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
Requires:       %{name} = %{version}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Fix class-path-in-manifest error
sed -i '/class-path/I d' plugin/fop/MANIFEST.MF

%build
ant buildJar
ant fop
ant doc

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p dist/%{name}-fop-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-fop.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp doc/ $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%doc README
%doc COPYING
%doc LICENSE

%files fop
%{_javadir}/%{name}-fop.jar
%doc plugin/fop/COPYING
%doc plugin/fop/LICENSE

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.3-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.3-alt1_3jpp8
- new version

* Mon Sep 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.3-alt1_2jpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_1jpp7
- new release

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- new version

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1jpp7
- new version (closes: 29019)

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1jpp7
- fc update

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- fc update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_3jpp7
- new version

