Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Upstream uses version-release.  Control the madness here.
%global upver 1.11
%global uprel 8
%global filever %{upver}-%{uprel}

Name:           automaton
Version:        %{upver}r%{uprel}
Release:        alt1_13jpp8
Summary:        A Java finite state automata/regular expression library

License:        BSD
URL:            http://www.brics.dk/automaton/
Source0:        http://www.brics.dk/~amoeller/%{name}/%{name}-%{filever}.tar.gz
Source1:        https://repo1.maven.org/maven2/dk/brics/%{name}/%{name}/%{filever}/%{name}-%{filever}.pom
# Fix javadoc errors
Patch0:         %{name}-javadoc.patch

BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  java-javadoc

BuildArch:      noarch
Source44: import.info

%description
This Java package contains a DFA/NFA (finite-state automata) implementation
with Unicode alphabet (UTF-16) and support for the standard regular expression
operations (concatenation, union, Kleene star) and a number of non-standard
ones (intersection, complement, etc.).

In contrast to many other automaton/regexp packages, this package is fast,
compact, and implements real, unrestricted regular operations.  It uses a
symbolic representation based on intervals of Unicode characters.

%package javadoc
Group: Development/Documentation
Summary:        A Java finite state automata/regular expression library
BuildArch:      noarch

%description javadoc
Javadoc documentation for automaton.

%prep
%setup -q -n %{name}-%{upver}
%patch0

# Remove prebuilt artifacts
rm -fr dist/%{name}.jar doc/*

# Build for newer Java versions
sed -i 's/="1.5"/="1.6"/g' build.xml

# Link to offline javadocs
sed -i 's,http.*api/,file://%{_javadocdir}/java/,' build.xml

%build
ant all

%install
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}.jar %{buildroot}%{_javadir}

mkdir -p %{buildroot}%{_javadocdir}
cp -a doc %{buildroot}%{_javadocdir}/%{name}

# Install the POM
mkdir -p %{buildroot}%{_mavenpomdir}
cp -p %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom

# Add Maven metadata
%add_maven_depmap %{name}.pom %{name}.jar

%files -f .mfiles
%doc ChangeLog README
%doc COPYING

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_11jpp8
- new version

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_5jpp7
- update to new release by jppimport

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_4jpp7
- update to new release by jppimport

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_3jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_2jpp7
- fc build

