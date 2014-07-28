Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           ezmorph
Version:        1.0.6
Release:        alt1_7jpp7
Summary:        Object transformation library for Java
License:        ASL 2.0
URL:            http://ezmorph.sourceforge.net/
# A plain jarball with the source is provided by upstream.  We could use
# it, but we choose to build with maven for the sake of consistency.
# Therefore we pull the tree with maven metadata from VCS.
# cvs -d:pserver:anonymous@ezmorph.cvs.sourceforge.net:/cvsroot/ezmorph login
# cvs -z3 -d:pserver:anonymous@ezmorph.cvs.sourceforge.net:/cvsroot/ezmorph co -r REL_1_0_6 -d ezmorph-1.0.6 -P ezmorph
# tar czf ezmorph-1.0.6.tar.gz --exclude CVS ezmorph-1.0.6
Source0:        %{name}-%{version}.tar.gz
Patch0:         ezmorph-1.0.6-maven.patch

BuildRequires:  jpackage-utils
BuildRequires:  jakarta-oro
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
Requires:       jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
EZMorph is simple java library for transforming an Object to another
Object. It supports transformations for primitives and Objects and
multidimensional arrays.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       %{name} = %{version}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .maven

%build
mvn-rpmbuild install javadoc:javadoc

%install
# Code
install -d $RPM_BUILD_ROOT%{_javadir}
# Bad version number, likely a typo
install -m644 target/%{name}-1.0.5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_7jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_5jpp7
- fc update

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_1jpp6
- new version

