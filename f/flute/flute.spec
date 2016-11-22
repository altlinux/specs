# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name: flute
Version: 1.3.0
Release: alt1_15.OOo31jpp8
Summary: Java CSS parser using SAC
# The entire source code is W3C except ParseException.java which is LGPLv2+
License: W3C and LGPLv2+
Group: System/Libraries
Source0: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}-OOo31.zip
URL: http://www.w3.org/Style/CSS/SAC/
BuildRequires: ant javapackages-tools rpm-build-java sac
Requires: javapackages-tools rpm-build-java sac
BuildArch: noarch
Source44: import.info

%description
A Cascading Style Sheets parser using the Simple API for CSS, for Java.

%package javadoc
Group: Development/Documentation
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib sac

%build
ant jar javadoc

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc COPYRIGHT.html
%{_javadir}/*.jar

%files javadoc
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_15.OOo31jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_14.OOo31jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_11.OOo31jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_10.OOo31jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_9.OOo31jpp7
- fc update

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_6.OOo31jpp6
- new version

