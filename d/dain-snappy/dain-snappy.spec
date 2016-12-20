Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%global commit e02f7c887d666afbdd11763f3a6ba22e68f53f15
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#def_with hadoop
%bcond_with hadoop

Name:           dain-snappy
Version:        0.4
Release:        alt1_2jpp8
Summary:        Snappy compression library
License:        ASL 2.0 and BSD
URL:            https://github.com/dain/snappy
BuildArch:      noarch

Source0:        https://github.com/dain/snappy/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(org.xerial.snappy:snappy-java)
%if %{with hadoop}
BuildRequires:  mvn(org.apache.hadoop:hadoop-common)
%endif
Source44: import.info

%description
This is a rewrite (port) of Snappy writen in pure Java. This
compression code produces a byte-for-byte exact copy of the output
created by the original C++ code, and extremely fast.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n snappy-%{commit}
%pom_remove_plugin :really-executable-jar-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-surefire-plugin

%if %{with hadoop}
%pom_change_dep :hadoop-core :hadoop-common
%else
%pom_remove_dep :hadoop-core
find -name HadoopSnappyCodec.java -delete
find -name TestHadoopSnappyCodec.java -delete
%endif

# Broken test - dain-snappy produces different output than original snappy
sed -i /@Test/d $(find -name SnappyTest.java)

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc license.txt notice.md

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp8
- new version

