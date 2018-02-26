BuildRequires: icu4j
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global parent	jena
%global subname	iri

Name:		%{parent}-%{subname}
Version:	0.8
Release:	alt1_5jpp7
BuildArch:	noarch
Summary:	The Jena IRI Library

# License is contained in the file Copyright.txt
License:	BSD
URL:		http://jena.sourceforge.net/%{subname}
# cvs -z3 -d:pserver:anonymous@jena.cvs.sourceforge.net:/cvsroot/jena export -r IRI_0_8 iri
# tar caf jena-iri-0.8.tar.xz iri
Source0:	%{name}-%{version}.tar.xz
# Assembly id was commented out
Patch0:		%{name}-fixed-assembly-id.patch

BuildRequires:	jpackage-utils
BuildRequires:	maven
BuildRequires:	maven-shared
BuildRequires:	maven-shared-file-management
BuildRequires:	maven-assembly-plugin
BuildRequires:	maven-surefire-provider-junit4

Requires:	jpackage-utils
Source44: import.info

%description
The Jena IRI Library is an implementation of RFC 3987 (IRI) and 
RFC 3986 (URI), and a partial implementation of other related standards. 

It is incomplete. 

%package javadoc
Summary:	API documentation for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
The API documentation of %{name}.


%prep
%setup -qn %{subname}
%patch0 -p1
rm -rf doc lib lib-build Patches

%build
# 14 out of 1313 tests fail on parsing URLs.
# This happens only with mvn-rpmbuild, not mvn3. I'm investingating this.
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.failure.ignore


%install
# JAR
install -Dpm 644 target/%{subname}-%{version}.jar %{buildroot}%{_javadir}/%{parent}/%{subname}.jar

# POM
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom
%add_maven_depmap JPP.%{name}.pom %{parent}/%{subname}.jar

# JavaDoc
install -Ddm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc Copyright.txt Jena-IRI-changes.txt RELEASE_NOTES.txt TODO.txt dependencies.txt
%{_javadir}/%{parent}/%{subname}.jar
%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc Copyright.txt 
%doc %{_javadocdir}/%{name}



%changelog
* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_5jpp7
- new version

