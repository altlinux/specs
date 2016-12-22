Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           SimplyHTML
Version:        0.16.17
Release:        alt1_1jpp8
Summary:        Application and a java component for rich text processing
License:        GPLv2 and BSD
URL:            http://simplyhtml.sourceforge.net/
BuildArch:      noarch

Source0:        http://heanet.dl.sourceforge.net/project/simplyhtml/stable/simplyhtml_src-%{version}.tar.gz

# Remove Gradle bintray plugin (not available in Fedora)
Patch0:         %{name}-remove-bintray-plugin.patch

BuildRequires:  gradle-local
BuildRequires:  mvn(gnu-regexp:gnu-regexp)
BuildRequires:  mvn(javax.help:javahelp)
BuildRequires:  mvn(org.dpolivaev.mnemonicsetter:mnemonicsetter)
Source44: import.info

%description
SimplyHTML is an application for text processing. 
It stores documents as HTML files in combination with 
Cascading Style Sheets (CSS). SimplyHTML is not intended 
to be used as an editor for web pages. 
The application combines text processing features as known from 
popular word processors with a simple and generic way of 
storing textual information and styles.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n simplyhtml-%{version}
%patch0
echo 'rootProject.name="%{name}"' >settings.gradle

%build
%gradle_build

%install
%mvn_install -J build/docs/javadoc

%files -f .mfiles
%doc readme.txt
%doc gpl.txt 

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.17-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_7jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_6jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_2jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_1jpp7
- new version

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.5-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1_7jpp7
- new version

