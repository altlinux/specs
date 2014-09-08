Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          guava
Version:       13.0
Release:       alt1_6jpp7
Summary:       Google Core Libraries for Java
License:       ASL 2.0 
URL:           http://code.google.com/p/guava-libraries
# git clone https://code.google.com/p/guava-libraries/
# (cd ./guava-libraries && git archive --format=tar --prefix=guava-%{version}/ v%{version}) | xz >guava-%{version}.tar.xz
Source0:       %{name}-%{version}.tar.xz

BuildRequires: mvn(org.sonatype.oss:oss-parent)

BuildRequires: maven-local
BuildRequires: maven-dependency-plugin

BuildRequires: mvn(com.google.code.findbugs:jsr305) >= 0-0.6.20090319svn
BuildRequires: ant

BuildArch:     noarch
Source44: import.info

%description
Guava is a suite of core and expanded libraries that include 
utility classes, Google's collections, io classes, and much 
much more.
This project is a complete packaging of all the Guava libraries
into a single jar.  Individual portions of Guava can be used
by downloading the appropriate module and its dependencies.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
find . -name '*.jar' -delete

%pom_disable_module guava-gwt
%pom_disable_module guava-testlib
%pom_disable_module guava-tests
%pom_remove_plugin :animal-sniffer-maven-plugin guava
%pom_remove_plugin :maven-gpg-plugin

%build

%mvn_file :%{name} %{name}
%mvn_alias :%{name} "com.google.collections:google-collections"
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS CONTRIBUTORS COPYING README*

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_3jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_1jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

