Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          apache-commons-pool2
Version:       2.4.2
Release:       alt3_4jpp8
Summary:       Apache Commons Object Pooling Library 2.x series
License:       ASL 2.0
URL:           http://commons.apache.org/proper/commons-pool/
Source0:       http://www.apache.org/dist/commons/pool/source/commons-pool2-%{version}-src.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.ow2.asm:asm-util)

BuildArch:     noarch
Source44: import.info

%description
The Apache Commons Pool open source software library provides an
object pooling API and a number of object pool implementations.
Version 2 of Apache Commons Pool contains a completely re-written
pooling implementation compared to the 1.x series. In addition
to performance and scalability improvements, version 2 includes
robust instance tracking and pool monitoring.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n commons-pool2-%{version}-src

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

%mvn_file : %{name} commons-pool2

%build

%mvn_build -- -Dmaven.test.skip.exec=true

%install
%mvn_install

%files -f .mfiles
%doc README.txt RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt3_4jpp8
- fixed build

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_3jpp8
- new jpp release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_2jpp8
- fixed build

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_2jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_1jpp8
- new version

