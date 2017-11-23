BuildRequires: maven-project
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		port-allocator-maven-plugin
Version:	1.2
Release:	alt4_12jpp8
Summary:	Port Allocator Maven Plugin

Group:		Development/Other
License:	ASL 2.0
URL:		http://github.com/sonatype/port-allocator-maven-plugin

# git clone git://github.com/sonatype/port-allocator-maven-plugin.git
# git archive --format=tar --prefix=port-allocator-maven-plugin-1.2/ port-allocator-maven-plugin-1.2 | xz > port-allocator-maven-plugin-1.2.tar.xz
Source0:	%{name}-%{version}.tar.xz
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt

# Switch parent to sonatype-oss-parent - seems to work
Patch0:		%{name}-parent.patch

BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-enforcer-plugin
BuildRequires:	maven-plugin-plugin
BuildRequires:	maven-resources-plugin
BuildRequires:	maven-surefire-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-javadoc-plugin
BuildRequires:	sonatype-oss-parent
Source44: import.info

%description
Allocate ports to be used during maven build process.

%package javadoc
Group: Development/Java
Summary:	Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} .

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%patch0


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt


%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt4_12jpp8
- fixed build with new maven-reporting-impl

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_12jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_10jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_5jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

