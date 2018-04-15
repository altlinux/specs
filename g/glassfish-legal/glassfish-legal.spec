Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          glassfish-legal
Version:       1.1
Release:       alt1_11jpp8
Summary:       Legal License for glassfish code
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/ glassfish-legal-1.1
# tar czf glassfish-legal-1.1-src-svn.tar.gz glassfish-legal-1.1
Source0:       %{name}-%{version}-src-svn.tar.gz

BuildRequires: glassfish-master-pom
BuildRequires: maven-local
BuildRequires: maven-remote-resources-plugin

Requires:      glassfish-master-pom
BuildArch:     noarch
Source44: import.info

%description
An archive which contains license files for glassfish code.

%prep
%setup -q -n %{name}-%{version}

sed -i 's/\r//' src/main/resources/META-INF/LICENSE.txt
cp -p src/main/resources/META-INF/LICENSE.txt .

%mvn_file :legal %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_11jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7jpp8
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp7
- new release

