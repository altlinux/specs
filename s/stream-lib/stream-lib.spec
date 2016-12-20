Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# NB: this package includes a forked version of Bloom filter code
# from Apache Cassandra.  FPC has granted a bundling exception since
# it is a fork; see https://fedorahosted.org/fpc/ticket/401 and
# http://meetbot.fedoraproject.org/fedora-meeting-1/2014-03-20/fedora-meeting-1.2014-03-20-17.05.html

%global streamlib_version 2.6.0
%global commit 214c92595d5be3a1cedc881b50231ccb34862074
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           stream-lib
Version:        %{streamlib_version}
Release:        alt1_5jpp8
Summary:        Stream summarizer and cardinality estimator
License:        ASL 2.0
URL:            https://github.com/addthis/stream-lib/
Source0:        https://github.com/addthis/stream-lib/archive/%{commit}/stream-lib-%{commit}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(it.unimi.dsi:fastutil)
Source44: import.info

%description
A Java library for summarizing data in streams for which it is
infeasible to store all events. More specifically, there are classes
for estimating: cardinality (i.e. counting things); set membership;
top-k elements and frequency. One particularly useful feature is that
cardinality estimators with compatible configurations may be safely
merged.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -qn %{name}-%{commit}

%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin pom.xml
# Unneeded task
%pom_remove_plugin :maven-source-plugin
# Fix doclint issues
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.mdown
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_5jpp8
- new version

