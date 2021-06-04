
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: clojure
Version: 1.10.1
Summary: A dynamic programming language that targets the Java Virtual Machine
License: EPL-1.0
Url: http://clojure.org/
Group: Development/Java
Release: alt0.1jpp

Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.org>
Provides: mvn(org.clojure:clojure) = 1.10.1
Provides: mvn(org.clojure:clojure:pom:) = 1.10.1
Requires: mvn(org.clojure:core.specs.alpha)
Requires: mvn(org.clojure:spec.alpha)

BuildArch: noarch
Source: clojure-1.10.1-5.fc33.cpio


%description
Clojure is a dynamic programming language that targets the Java
Virtual Machine. It is designed to be a general-purpose language,
combining the approachability and interactive development of a
scripting language with an efficient and robust infrastructure for
multithreaded programming. Clojure is a compiled language - it
compiles directly to JVM bytecode, yet remains completely
dynamic. Every feature supported by Clojure is supported at
runtime. Clojure provides easy access to the Java frameworks, with
optional type hints and type inference, to ensure that calls to Java
can avoid reflection.

%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list
sed -i 1s,/usr/bin/bash,/bin/bash, usr/bin/*
mkdir -p etc/java
touch etc/java/clojure.conf

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list
/etc/java/clojure.conf

%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1:1.10.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0-alt1_1jpp8
- new version

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.7.0-alt2_1jpp8
- fixed build

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7.0-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.5.1-alt1_2jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.5.1-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_3jpp7
- new release

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.3.0-alt1_1jpp6
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_1jpp6
- update to new release by jppimport

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.2.0-alt1_1jpp6
- new version (closes: #24726)

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 20080916-alt1_2jpp5
- first build

