Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(ExtUtils/MakeMaker.pm) perl(Pod/Usage.pm) perl(Scalar/Util.pm) perl(Switch.pm) perl(cproton_perl.pm) perl(overload.pm) perl-devel perl-podlators python-devel swig
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          qpid-proton-java
Version:       0.10
Release:       alt1_1jpp8
Summary:       Java libraries for Qpid Proton
License:       ASL 2.0
URL:           http://qpid.apache.org/proton/
Source0:       http://www.apache.org/dist/qpid/proton/%{version}/qpid-proton-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.maven.doxia:doxia-module-markdown)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires: mvn(org.fusesource.hawtbuf:hawtbuf)
BuildRequires: mvn(org.fusesource.hawtdispatch:hawtdispatch-transport)
BuildRequires: mvn(org.mockito:mockito-core)

BuildArch:     noarch
Source44: import.info

%description
Java language bindings for the Qpid Proton messaging framework.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n qpid-proton-%{version}

# Unwanted
rm -r tools docs config.* examples/c examples/javascript \
  examples/php examples/python \
  examples/perl examples/ruby examples/engine/c \
  examples/include CMakeLists.txt bin proton-c \
  tests/smoke tests/ruby tests/python tests/tools tests/javascript

%if 0
sed -i 's|bcpkix-jdk15on|bcprov-jdk16|' tests/pom.xml
sed -i 's|PEMReader|PEMParser|' \
 proton-j/src/main/java/org/apache/qpid/proton/engine/impl/ssl/SslEngineFacadeFactory.java
sed -i 's|pemReader = new PEMParser(reader, passwordFinder);|pemReader = new PEMParser(reader);|' \
 proton-j/src/main/java/org/apache/qpid/proton/engine/impl/ssl/SslEngineFacadeFactory.java
%endif

%pom_remove_dep org.python:jython-standalone tests
rm -r tests/java/org/apache/qpid/proton/JythonTest.java

rm -r contrib/proton-hawtdispatch/src/test/java/org/apache/qpid/proton/hawtdispatch/api/SampleTest.java

%mvn_alias :proton-j org.apache.qpid:proton-api org.apache.qpid:proton-j-impl

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc proton-j/LICENSE
%doc examples/java/messenger/README.txt

%files javadoc -f .mfiles-javadoc
%doc proton-j/LICENSE

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1jpp8
- java8 mass update

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

