Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name t-digest
%global url     https://github.com/tdunning/%{name}

Name:           t-digest
Version:        3.0
Release:        alt1_15jpp11
Summary:        A new data structure for on-line accumulation of statistics
License:        ASL 2.0
URL:            %{url}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
#grep -ir -e "<p/>"
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/TDigest.java
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/TreeDigest.java
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/ArrayDigest.java
Patch0:         jdk8-javadoc.patch

BuildArch:      noarch

BuildRequires:  maven-local

Requires:       java
Source44: import.info

%description
A new data structure for accurate on-line accumulation of rank-based statistics
eg. quantiles and trimmed means. The t-digest algorithm is also very parallel
friendly making it useful in map-reduce and parallel streaming applications.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0
# Useless tasks
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin

%build
#skipping tests, they requires currently unpacked depndences
%mvn_build --force

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE NOTICES

%files javadoc  -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICES

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.0-alt1_15jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_11jpp8
- fc update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_9jpp8
- explicit build with java8

* Mon Jan 28 2019 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_8jpp8
- new version

