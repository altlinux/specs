Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           json_simple
Version:        1.1.1
Release:        alt2_13jpp8
Summary:        Simple Java toolkit for JSON
License:        ASL 2.0
URL:            http://code.google.com/p/json-simple/
BuildArch:      noarch

# svn export http://json-simple.googlecode.com/svn/tags/tag_release_1_1_1/ json-simple-1.1.1
# tar czf json-simple-1.1.1-src-svn.tar.gz json-simple-1.1.1
Source0:        json-simple-1.1.1-src-svn.tar.gz

#https://code.google.com/p/json-simple/issues/detail?id=97
Patch0:         json-simple-hash-java-1.8.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
JSON.simple is a simple Java toolkit for JSON. You can use JSON.simple 
to encode or decode JSON text. 
  * Full compliance with JSON specification (RFC4627) and reliable 
  * Provides multiple functionalities such as encode, decode/parse 
    and escape JSON text while keeping the library lightweight 
  * Flexible, simple and easy to use by reusing Map and List interfaces 
  * Supports streaming output of JSON text 
  * Stoppable SAX-like interface for streaming input of JSON text 
  * Heap based parser 
  * High performance (see performance testing) 
  * No dependency on external libraries 
  * Both of the source code and the binary are JDK1.2 compatible 

%package javadoc
Group: Development/Java
Summary:       API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n json-simple-%{version}
find . -name '*.jar' -exec rm -f '{}' \;
# All the files have dos line endings, remove them.
find . -type f -exec %{__sed} -i 's/\r//' {} \;

%patch0 -p1

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS.txt ChangeLog.txt LICENSE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2jpp7
- new version

