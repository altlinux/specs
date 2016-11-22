Serial: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
#global _check 1

Summary:    JavaScript minifier and checker
Name:       closure-compiler
#define commit ad29f06d581fb8c54ad031334b82a5c301b6ce0a
#define shorthash %(printf %%.7s %commit)
Version:    20141215
Release:    alt1_3jpp8
License:    ASL 2.0
URL:        https://developers.google.com/closure/compiler/
Source0:    https://github.com/google/closure-compiler/archive/maven-release-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    closure-compiler.xml
BuildArch:  noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires: maven-local
BuildRequires: jarjar
BuildRequires: args4j
BuildRequires: guava >= 15
BuildRequires: google-gson
BuildRequires: jsr-305
BuildRequires: junit
BuildRequires: protobuf-java
BuildRequires: rhino
BuildRequires: nekohtml
BuildRequires: plexus-classworlds
BuildRequires: plexus-component-api
BuildRequires: plexus-utils
BuildRequires: findbugs
%if 0%{?_check}
BuildRequires: mockito
%endif
BuildRequires: libxslt xsltproc
BuildRequires: docbook-style-xsl

Requires: javapackages-tools rpm-build-java
Requires:      args4j
Requires:      guava
Requires:      google-gson
Requires:      jsr-305
Requires:      junit
Requires:      protobuf-java
Requires:      rhino
Requires:      jarjar
Source44: import.info

%description
The Closure Compiler is a tool for making JavaScript download and run
faster. It is a true compiler for JavaScript. Instead of compiling
from a source language to machine code, it compiles from JavaScript to
better JavaScript. It parses your JavaScript, analyzes it, removes
dead code and rewrites and minimizes whata.'s left. It also checks
syntax, variable references, and types, and warns about common
JavaScript pitfalls.

%package javadoc
Group: Development/Documentation
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the %{summary}.

%prep
%setup -q -n %{name}-maven-release-v%{version}

rm -rf lib/*
build-jar-repository -s -p lib/ \
    jarjar \
    args4j \
    google-gson \
    jsr-305 \
    junit \
    protobuf \
    js \
    findbugs \
%if 0%{?_check}
    mockito \
%endif
    guava
ln -s android-json-org-java.jar lib/json.jar
%if 0%{?_check} == 0
%pom_remove_dep :mockito-core pom-main.xml
rm test/com/google/javascript/jscomp/fuzzing/FuzzerTest.java
%endif

%build
%mvn_build -- \
%if 0%{?_check} == 0
    -DskipTests
%endif

xsltproc \
        --nonet \
        --stringparam man.output.quietly 1 \
        --stringparam funcsynopsis.style ansi \
        --stringparam man.authors.section.enabled 0 \
        --stringparam man.copyright.section.enabled 0 \
        http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl %{SOURCE1}

%install
%mvn_install
%jpackage_script com.google.javascript.jscomp.CommandLineRunner "" "" jarjar:args4j:google-gson:jsr-305:junit:protobuf:js:guava:%{name} %{name} true

install -Dm0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%global _docdir_fmt %{name}

%files -f .mfiles
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%doc COPYING
%doc CONTRIBUTORS README.md

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:20141215-alt1_3jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:20141215-alt1_2jpp8
- java 8 mass update

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150218-alt1jpp7
- Initial build for Sisyphus

