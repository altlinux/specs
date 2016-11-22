Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          BareBonesBrowserLaunch
Version:       3.1
Release:       alt1_12jpp8
Summary:       Simple library to launch a browser window from Java
License:       Public Domain
URL:           http://www.centerkey.com/java/browser/
Source0:       http://www.centerkey.com/java/browser/myapp/real/bare-bones-browser-launch-%{version}.jar

BuildRequires: javapackages-local

BuildArch:     noarch
Source44: import.info

%description
Utility class to open a web page from a Swing application in the user's 
default browser. Supports: Mac OS X, GNU/Linux, Unix, Windows XP

%package javadoc
Group: Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q -c

find * -name *.class -delete
rm -rf doc/*

%build

%{javac} com/centerkey/utils/BareBonesBrowserLaunch.java
%{jar} -cf %{name}.jar com/centerkey/utils/BareBonesBrowserLaunch.class
%{javadoc} -encoding UTF-8 -d doc com/centerkey/utils/BareBonesBrowserLaunch.java -windowtitle "%{name} %{version}"

%install
%mvn_artifact com.centerkey.utils:%{name}:%{version} %{name}.jar
%mvn_file com.centerkey.utils:%{name} %{name}
%mvn_install -J doc

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_5jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_4jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_3jpp7
- fc build

