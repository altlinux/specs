BuildRequires: /proc
BuildRequires: jpackage-compat
# one of the sources is a zip file
BuildRequires: unzip
Name:           clojure
Epoch:		1
Version:     	1.3.0
Release:        alt1_1jpp6
Summary:        A dynamic programming language that targets the Java Virtual Machine

Group:          Development/Java
License:        EPL
URL:            http://clojure.org/
Source0:        http://repo1.maven.org/maven2/org/clojure/clojure/%{version}/clojure-%{version}.zip
Source1:        clojure.sh

BuildArch:      noarch

BuildRequires:  ant >= 1.6
BuildRequires:  jpackage-utils >= 1.5
BuildRequires:  objectweb-asm

Requires:       objectweb-asm
Source44: import.info

%description 
Clojure is a dynamic programming language that targets the Java
Virtual Machine. It is designed to be a general-purpose language,
combining the approachability and interactive development of a
scripting language with an efficient and robust infrastructure for
multithreaded programming. Clojure is a compiled language - it
compiles directly to JVM bytecode, yet remains completely
dynamic. Every feature supported by Clojure is supported at
runtime. Clojure provides easy access to the Java frameworks, with
optional type hints and type inference, to ensure that calls to Java
can avoid reflection.

%prep
%setup -q
rm -f *.jar

%build
ant

%install

# prefix install
install -p -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -ar src/clj/clojure/*  %{buildroot}%{_datadir}/%{name}/
rm -f %{buildroot}%{_datadir}/%{name}/xml/\#*

# jar - link to prefix'd jar so that java stuff knows where to look
install -d -m 755 %{buildroot}%{_javadir}
cp clojure.jar %{buildroot}%{_javadir}/%{name}.jar

# startup script
install -d -m 755 %{buildroot}%{_bindir}
cp %{SOURCE1} %{buildroot}%{_bindir}/clojure

install -d %{buildroot}%{_datadir}/maven2/poms
%add_to_maven_depmap clojure clojur-lang %{version} JPP/%{name} clojure-lang
install -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-clojure-lang.pom

%files
%doc readme.txt epl-v10.html

%attr(0755,root,root) %{_bindir}/clojure
%{_javadir}/%{name}.jar
%{_datadir}/%{name}
%{_bindir}/clojure
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}/*

%changelog
* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.3.0-alt1_1jpp6
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_1jpp6
- update to new release by jppimport

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.2.0-alt1_1jpp6
- new version (closes: #24726)

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 20080916-alt1_2jpp5
- first build

