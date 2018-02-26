BuildRequires: /proc
BuildRequires: jpackage-compat
# Upstream uses version-release.  Control the madness here.
%global upver 1.11
%global uprel 8
%global filever %{upver}-%{uprel}

Name:           automaton
Version:        %{upver}r%{uprel}
Release:        alt1_2jpp7
Summary:        A Java finite state automata/regular expression library

Group:          Development/Java
License:        BSD
URL:            http://www.brics.dk/automaton/
Source:         http://www.brics.dk/~amoeller/%{name}/%{name}-%{filever}.tar.gz

BuildRequires:  ant
BuildRequires:  jpackage-utils
Requires:       jpackage-utils

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
Summary:        A Java finite state automata/regular expression library
Group:          Development/Documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description javadoc
Javadoc documentation for automaton.

%prep
%setup -q -n %{name}-%{upver}
rm -f dist/%{name}.jar

%build
ant all

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
mv doc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc ChangeLog COPYING README
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_2jpp7
- fc build

