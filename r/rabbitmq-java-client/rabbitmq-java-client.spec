Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%bcond_without buildtex

%global jarname   rabbitmq-client

%global failjava  true
%global failjunit no
#global failjunit yes

Name:          rabbitmq-java-client
Version:       3.6.0
Release:       alt1_2jpp8
Summary:       Java Advanced Message Queue Protocol client library
License:       ASL 2.0 and GPLv2+ and MPLv1.1
URL:           http://www.rabbitmq.com/java-client.html
Source0:       http://www.rabbitmq.com/releases/%{name}/v%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: maven-local mvn(commons-cli:commons-cli) mvn(commons-io:commons-io) mvn(junit:junit)
BuildRequires: ant ant-junit
BuildRequires: java-headless
BuildRequires: python >= 2.6 python-module-simplejson

%if 0%{?with buildtex}
BuildRequires: texi2html
BuildRequires: %{_bindir}/pdflatex
%endif

%if 0%{?fedora}
Requires:       rabbitmq-server
Requires:       activemq
%endif
Source44: import.info


%description
The library allows Java code to interface to AMQP servers.
Please see the specification page for more information on AMQP
inter-operation and standards-conformance

You will need an AMQP server, such as our very own RabbitMQ server,
to use with the client library.


%package doc
Group: Development/Java
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}

%description doc
This package contains additional documentation for %{name}.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
find . -name "*.bat" -delete
find . -name "*.class" -delete
find . -name "*.jar" -print -delete
# use ant only
rm Makefile

ln -sf $(build-classpath commons-cli) lib/
ln -sf $(build-classpath commons-io) lib/
ln -sf $(build-classpath junit) lib/

# Disable Spring bundlor support
sed -i "s|, bundlor.do||" build.xml
sed -i "s|, test-bundlor.do||" build.xml

#sed -i 's,\(\"jar.name\" value=\"\).*\",\1%{jarname}\",' build.xml
sed -i 's,\(\"haltOnFailureJunit\" value=\"\).*\",\1%{failjunit}\",' build.xml
sed -i 's,\(\"haltOnFailureJava\" value=\"\).*\",\1%{failjava}\",' build.xml


%build
%mvn_file com.rabbitmq:amqp-client %{name} %{jarname} amqp-client
export JAVA_HOME=%{java_home}
ant -Dimpl.version=%{version} maven-bundle

# distribute documentation
cd doc/channels
%if 0%{?with buildtex}
find . -name \*.tex -print -exec 'texi2html {} ; pdflatex {}' \; -delete
%endif
find . -not -name channels.\* -delete


%check
ant test-jar

# client tests need a mock server
export RABBITMQ_LOG_BASE=.
export RABBITMQ_MNESIA_BASE=.
export RABBITMQ_NODENAME=testrabbit
su rabbitmq -c 'rabbitmq-server -detach' &disown

#ant test-suite
#ant -Dtest=testDoubleDeletionExchange test-single
ant test-server
ant test-client
# FIXME functional tests failure ahead!
#ant test-functional
#ant test-functional-and-server-with-ha


%install
%mvn_artifact build/bundle/amqp-client-%{version}.pom build/bundle/amqp-client-%{version}.jar
%mvn_install -J build/doc/api


%files -f .mfiles
%doc LICENSE*
%doc README*

%files doc
%doc doc/*

%files javadoc -f .mfiles-javadoc
%doc LICENSE*


%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.6.0-alt1_2jpp8
- new version

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 3.5.5-alt1_1jpp8
- java 8 mass update

