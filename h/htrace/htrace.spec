Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: htrace
Version: 3.1.0
Release: alt1_7jpp8
Summary: Tracing framework for java based distributed systems
License: ASL 2.0
URL:     https://%{name}.incubator.apache.org
Source0: https://archive.apache.org/dist/incubator/%{name}/%{name}-%{version}-incubating/%{name}-%{version}-incubating-src.tar.gz

#BuildRequires: golang
#BuildRequires: godep
BuildRequires: java-devel
BuildRequires: jackson-core
BuildRequires: jackson-databind
BuildRequires: jetty-util-ajax
#BuildRequires: leveldb-devel
BuildRequires: libthrift-java
BuildRequires: maven-local
BuildRequires: apache-parent
BuildArch: noarch
Source44: import.info

%description
HTrace is a tracing framework intended for use with distributed systems
written in java. 

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}-incubating


# disable hbase module because hbase package was retired
%pom_disable_module htrace-hbase

# disable flume module because flume is currently not packaged
%pom_disable_module htrace-flume

# remove test jar plugin
%pom_remove_plugin :maven-jar-plugin

# Remove apache-rat-plugin because it causes build failure on xmvn generated
# files
%pom_remove_plugin org.apache.rat:apache-rat-plugin
%pom_remove_plugin org.apache.rat:apache-rat-plugin htrace-core
%pom_remove_plugin org.apache.rat:apache-rat-plugin htrace-zipkin

# Remove assembly plugins not needed
%pom_remove_plugin :maven-assembly-plugin htrace-zipkin

# remove go build 
%pom_remove_plugin :maven-antrun-plugin htrace-core

# remove problematic javadoc
%pom_remove_plugin :maven-javadoc-plugin htrace-core
%pom_remove_plugin :maven-javadoc-plugin htrace-zipkin

# remove source plugin
%pom_remove_plugin :maven-source-plugin htrace-core
%pom_remove_plugin :maven-source-plugin htrace-zipkin

# remove shaded plugin to prevent bundling 
%pom_remove_plugin :maven-shade-plugin htrace-core

# skip install for zipkin
%mvn_package ":%{name}-zipkin" __noinstall

%mvn_package ":%{name}-core"

%build
%mvn_build -j -- -DskipTests

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt
%doc NOTICE.txt
%doc README.md
%doc DISCLAIMER.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_7jpp8
- java update

* Tue Oct 31 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_6jpp8
- new jpp release

