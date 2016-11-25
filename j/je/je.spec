Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          je
Version:       6.3.8
Release:       alt1_2jpp8
Summary:       Berkeley DB Java Edition
License:       AGPLv3 and BSD
URL:           http://www.oracle.com/us/products/database/berkeley-db/je/overview/index.html
# use SOURCE2: sh je-create-tarball.sh < VERSION >
Source0:       %{name}-%{version}-clean.tar.xz
Source1:       http://download.oracle.com/maven/com/sleepycat/%{name}/%{version}/%{name}-%{version}.pom
Source2:       %{name}-create-tarball.sh
# fix build
Patch0:        %{name}-6.3.8-build.patch
Patch1:        %{name}-6.3.8-use-system-asm.patch

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: hamcrest-core
BuildRequires: coreutils
BuildRequires: java-javadoc
BuildRequires: javapackages-local
BuildRequires: jboss-connector-1.6-api
BuildRequires: jboss-ejb-3.1-api
BuildRequires: junit
BuildRequires: mvn(org.ow2.asm:asm)

BuildArch:     noarch
Source44: import.info

%description
Berkeley DB Java Edition is a high performance, transactional storage
engine written entirely in Java. Like the highly successful Berkeley DB
product, Berkeley DB Java Edition executes in the address space of the
application, without the overhead of client/server communication. It
stores data in the application's native format, so no run-time data
translation is required. Berkeley DB Java Edition supports full ACID
transactions and recovery. It provides an easy-to-use, programmatic
interface, allowing developers to store and retrieve information
quickly, simply and reliably.

%package examples
Group: Development/Java
Summary:       Examples for %{name}
Requires:      %{name} = %{version}

%description examples
This package contains examples for %{name}.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package examples-javadoc
Group: Development/Java
Summary:       Javadoc for %{name}-examples
Requires:      %{name}-javadoc = %{version}

%description examples-javadoc
This package contains javadoc for %{name}-examples.

%prep
%setup -q
%patch0 -p1
cp -p %{SOURCE1} pom.xml
%patch1 -p1
rm -rf src/com/sleepycat/asm

%mvn_file com.sleepycat:%{name} %{name}

%build

ant \
 -Dj2ee.jarfile="$(build-classpath jboss-connector-1.6-api):$(build-classpath jboss-ejb-3.1-api)" \
 -Djdk6.home=%{_jvmdir}/java \
 -Dant.library.dir=%{_javadir} \
 jar javadoc compile-examples

cd build/classes
%jar -cf ../../%{name}-examples.jar collections je jmx persist

%install
%mvn_artifact pom.xml build/lib/%{name}.jar
%mvn_install -J docs/java

install -pm 644 %{name}-examples.jar %{buildroot}%{_javadir}/%{name}-examples.jar
cp -a docs/examples %{buildroot}%{_javadocdir}/%{name}-examples

%files -f .mfiles
%doc README
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%files examples
%{_javadir}/%{name}-examples.jar
%doc LICENSE

%files examples-javadoc
%{_javadocdir}/%{name}-examples
%doc LICENSE

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 6.3.8-alt1_2jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.97-alt1_4jpp8
- new version

