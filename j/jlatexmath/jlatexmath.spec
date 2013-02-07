# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jlatexmath
Version:        1.0.0
Release:        alt1_2jpp7
Summary:        Java API to display mathematical formulas written in LaTeX

Group:          Development/Java
License:        GPLv2+
URL:            http://forge.scilab.org/index.php/p/jlatexmath/
Source0:        http://forge.scilab.org/index.php/p/jlatexmath/downloads/get/%{name}-src-all-%{version}.zip
# Fix incorrect-fsf-address /usr/share/doc/jlatexmath-fop-0.9.6/LICENSE
# upstream bug : http://forge.scilab.org/index.php/p/jlatexmath/issues/458/

BuildRequires:  jpackage-utils
BuildRequires:  ant

Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
The goal of this Java API is to display mathematical formulas written in LaTeX.
The default encoding is UTF-8 and most of LaTeX commands are available.

JLaTeXMath is a fork of the excellent project JMathTeX.

%package fop
Summary:        FOP plug-in for %{name}
Group:          Development/Java

BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  fop

Requires:       jpackage-utils
Requires:       %{name} = %{version}-%{release}
Requires:       fop


%description fop
This package contains the FOP plug-in for %%{name}.

%package javadoc
Summary:        API Documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

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
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- fc update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_3jpp7
- new version

