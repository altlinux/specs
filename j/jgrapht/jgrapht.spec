Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:    jgrapht
Version: 0.8.1
Release: alt1_13jpp8
Summary: A free Java graph library that provides mathematical graph objs and algorithms
License: LGPLv2+
URL:     http://jgrapht.sourceforge.net/
Source0: http://downloads.sourceforge.net/project/jgrapht/JGraphT/Version%%200.8.1/jgrapht-%{version}.tar.gz
Patch0:  remove_uneccessary_hardcoded_classpath.patch
Patch1:  jgrapht-0.8.1-disable-doclint.patch

BuildRequires: javapackages-local
BuildRequires: ant

BuildArch: noarch
Source44: import.info

%description
JGraphT is a free Java graph library that provides mathematical graph-theory 
objects and algorithms.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0
%patch1 -p0

# remove uneccessary dirs/files
# removing touchgraph/jgraph support as we don't currently have deps packaged
rm -rf src/org/jgrapht/demo/ src/org/jgrapht/experimental/touchgraph src/org/jgrapht/ext/JGraphModelAdapter.java

# remove builting jars/classes
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
ant jar
ant javadoc

%install
%mvn_artifact thirdparty:%{name}-jdk1.6:%{version} %{name}-jdk1.6.jar
%mvn_file thirdparty:%{name}-jdk1.6 %{name}
%mvn_install -J javadoc

%files -f .mfiles
%doc README.html
%doc license-LGPL.txt

%files javadoc -f .mfiles-javadoc
%doc license-LGPL.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_6jpp7
- new release

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_5jpp7
- fc update

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.8.2-alt1_1jpp6
- new version

