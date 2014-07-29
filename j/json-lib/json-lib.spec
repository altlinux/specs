Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           json-lib
Version:        2.3
Release:        alt2_10jpp7
Summary:        JSON library for Java
License:        ASL 2.0
URL:            http://json-lib.sourceforge.net/
# A plain jarball with the source is provided by upstream.  We could use
# it, but we choose to build with maven for the sake of consistency.
# Therefore we pull the tree with maven metadata from VCS.
# cvs -d:pserver:anonymous@json-lib.cvs.sourceforge.net:/cvsroot/json-lib login
# cvs -z3 -d:pserver:anonymous@json-lib.cvs.sourceforge.net:/cvsroot/json-lib co -r REL_2_3 -d json-lib-2.3 -P json-lib
# tar czf json-lib-2.3.tar.gz --exclude CVS json-lib-2.3
Source0:        %{name}-%{version}.tar.gz
Patch0:         json-lib-2.3-pom.patch

BuildRequires:  jpackage-utils
BuildRequires:  antlr3-tool >= 3.2-7
BuildRequires:  asm2
BuildRequires:  ezmorph
BuildRequires:  groovy >= 1.7.2-2
BuildRequires:  jakarta-oro
BuildRequires:  junit
BuildRequires:  log4j
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-javadoc-plugin
BuildRequires:  dom4j
BuildRequires:  xom
BuildRequires:  jaxen
BuildRequires:  xmlunit
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
JSON-lib is a java library for transforming beans, maps, collections, java
arrays and XML to JSON and back again to beans and DynaBeans.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Requires:       %{name} = %{version}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .pom

%build
# Not strictly needed, but it makes no harm to be on the safe side
find -name '*.jar' -o -name '*.class' -delete

mvn-rpmbuild install javadoc:javadoc

%install
# Code
install -d $RPM_BUILD_ROOT%{_javadir}
install -m644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Documentation
install -d $RPM_BUILD_ROOT%{_javadocdir}
cp -ap target/site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Maven
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/*
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_10jpp7
- new release

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_8jpp7
- fc update

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_5jpp7
- fixed build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_5jpp7
- fc version

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1jpp6
- new version

