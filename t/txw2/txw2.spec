Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: txw2
Version: 20110809
Release: alt2_16jpp8
Summary: Typed XML writer for Java
License: CDDL and GPLv2 with exceptions
URL: https://txw.dev.java.net

# svn export https://svn.java.net/svn/jaxb~version2/tags/txw2-project-20110809/ txw2-20110809
# tar -zcvf txw2-20110809.tar.gz txw2-20110809
Source0: %{name}-%{version}.tar.gz

# Remove the reference to the parent net.java:jvnet-parent, as no package
# contains that artifact:
Patch0: %{name}-%{version}-pom.patch

# Update to use the version of args4j available in the distribution:
Patch1: %{name}-%{version}-args4j.patch

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.sun.codemodel:codemodel)
BuildRequires:  mvn(com.sun.xsom:xsom)
BuildRequires:  mvn(javax.xml.stream:stax-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.kohsuke.rngom:rngom)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
Source44: import.info

%description
Typed XML writer for Java.

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 20110809-alt2_16jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 20110809-alt2_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 20110809-alt2_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 20110809-alt2_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 20110809-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 20110809-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 20110809-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 20110809-alt1_4jpp7
- new version

