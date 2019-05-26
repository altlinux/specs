Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          noggit
Version:       0.7
Release:       alt1_7jpp8
Summary:       JSON streaming parser
License:       ASL 2.0
URL:           http://noggit.org/
Source0:       https://github.com/yonik/noggit/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Fast streaming JSON parser for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find -name '*.class' -print -delete
find -name '*.jar' -print -delete

chmod 644 LICENSE.txt README.txt

%mvn_file : %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_7jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3jpp8
- new jpp release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_2jpp8
- new version

