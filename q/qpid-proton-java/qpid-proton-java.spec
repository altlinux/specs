Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen /usr/bin/epydoc /usr/bin/gem /usr/bin/go /usr/bin/mvn /usr/bin/openssl /usr/bin/php /usr/bin/php-config /usr/bin/rspec /usr/bin/ruby /usr/bin/sphinx-build /usr/bin/swig /usr/bin/tox /usr/bin/valgrind /usr/sbin/saslpasswd2 gcc-c++ java-devel-default libruby-devel libsasl2-devel perl(ExtUtils/MakeMaker.pm) perl(Pod/Usage.pm) perl(Scalar/Util.pm) perl(Switch.pm) perl(overload.pm) perl-devel python-devel rpm-build-java rpm-build-python rpm-build-ruby swig
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          qpid-proton-java
Version:       0.12.2
Release:       alt1_4jpp8
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
  examples/go examples/cpp CMakeLists.txt bin proton-c \
  tests/smoke tests/ruby tests/python tests/tools tests/javascript

%pom_remove_dep org.python:jython-standalone tests
rm tests/java/org/apache/qpid/proton/JythonTest.java

rm contrib/proton-hawtdispatch/src/test/java/org/apache/qpid/proton/hawtdispatch/api/SampleTest.java

%mvn_alias :proton-j org.apache.qpid:proton-api org.apache.qpid:proton-j-impl

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference proton-j/LICENSE
%doc examples/java/messenger/README.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference proton-j/LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_1jpp8
- new version

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_1jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1jpp8
- java8 mass update

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

