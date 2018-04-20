Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           sequence-library
Version:        1.0.3
Release:        alt1_1jpp8
Summary:        Textual diff and merge library

License:        Sequence     
URL:            http://svn.svnkit.com/repos/3rdparty/de.regnis.q.sequence/

# Tarball generated with:
#  svn export http://svn.svnkit.com/repos/3rdparty/de.regnis.q.sequence/tags/1.0.3/ sequence-library-1.0.3 && \
#      tar caf sequence-library-1.0.3.tar.gz sequence-library-1.0.3/
Source0:        %{name}-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/de/regnis/q/sequence/sequence-library/%{version}/sequence-library-%{version}.pom
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
Source44: import.info

%description
A textual diff and merge library.

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.jar' -o -name '*.class' -delete

cp -pr %{SOURCE1} pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt


%changelog
* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1jpp8
- new version

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_10jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_10jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp7
- new release

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- replaced by fc package

