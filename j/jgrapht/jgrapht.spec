Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:    jgrapht
Version: 0.8.1
Release: alt1_6jpp7
Summary: A free Java graph library that provides mathematical graph objs and algorithms
Group:   Development/Java
License: LGPLv2+
URL:     http://jgrapht.sourceforge.net/
Source0: http://downloads.sourceforge.net/project/jgrapht/JGraphT/Version%%200.8.1/jgrapht-%{version}.tar.gz
Patch0:  remove_uneccessary_hardcoded_classpath.patch

BuildRequires: jpackage-utils
BuildRequires: ant
Requires: jpackage-utils

BuildArch: noarch
Source44: import.info

%description
JGraphT is a free Java graph library that provides mathematical graph-theory 
objects and algorithms.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0

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
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp %{name}-jdk1.6.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%doc license-LGPL.txt README.html

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_6jpp7
- new release

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_5jpp7
- fc update

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.8.2-alt1_1jpp6
- new version

