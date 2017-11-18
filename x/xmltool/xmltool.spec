BuildRequires: maven-assembly-plugin
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 26
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xmltool
Version:        3.3
Release:        alt4_18jpp8
Summary:        Tool to manage XML documents through a Fluent Interface

Group:          Development/Other
License:        ASL 2.0
URL:            http://code.google.com/p/xmltool
### upstream only provides binaries or source without build scripts
# tar creation instructions
# svn export http://xmltool.googlecode.com/svn/tags/xmltool-3.3 xmltool
# tar cfJ xmltool-3.3.tar.xz xmltool
Source0:        %{name}-%{version}.tar.xz
Patch0:         fix-deprecated-assembly-goal.patch
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-provider-testng
BuildRequires:  apache-resource-bundles
Source44: import.info

%description
XMLTool is a very simple Java library to be able to do all sorts of common 
operations with an XML document. Java developers often end up writing the same 
code for processing XML, transforming, etc. This easy to use class puts it all 
together, using the Fluent Interface pattern to facilitate XML manipulations. 

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%if 0%{?fedora} >= 26
%patch0 -p0
%endif

# Fix end-of-line encoding
sed -i 's/\r//' LICENSE.txt

%mvn_file : %{name}

# Remove dep on maven-wagon and maven-license plugins
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin com.google.code.maven-license-plugin:maven-license-plugin


%build
# Disable tests because they require an internet connection to run!
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt4_18jpp8
- added BR: maven-assembly-plugin for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt3_18jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt3_15jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt3_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt3_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt3_8jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt3_5jpp7
- rebuild with new apache-resource-bundles

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt2_5jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt2_4jpp7
- applied repocop patches

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_4jpp7
- dropped obsoletes on mojo-maven2-plugin-cobertura

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_2jpp6
- new jpp release

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

