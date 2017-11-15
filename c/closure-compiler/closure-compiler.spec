Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#global _check 1

Summary:    JavaScript minifier and checker
Name:       closure-compiler
#define commit ad29f06d581fb8c54ad031334b82a5c301b6ce0a
#define shorthash %(printf %%.7s %commit)
Version:    20160315
Release:    alt1_2jpp8
License:    ASL 2.0
URL:        https://developers.google.com/closure/compiler/
Source0:    https://github.com/google/closure-compiler/archive/maven-release-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    closure-compiler.xml
BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildRequires: libxslt xsltproc
BuildRequires: docbook-style-xsl
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

# Compatibility with more guava versions
sed -i -e 's/CharMatcher\.whitespace()/CharMatcher.WHITESPACE/' \
  src/com/google/javascript/jscomp/deps/*.java
sed -i -e 's/CharMatcher\.javaUpperCase()/CharMatcher.JAVA_UPPER_CASE/' -e 's/CharMatcher\.javaLetterOrDigit()/CharMatcher.JAVA_LETTER_OR_DIGIT/' \
  src/com/google/javascript/jscomp/parsing/JsDocInfoParser.java
sed -i -e 's/isSupertypeOf/isAssignableFrom/g' src/com/google/javascript/jscomp/ConformanceRules.java

# Don't build shaded jar because it bundles all deps
%pom_disable_module "pom-main-shaded.xml" pom-main.xml
%mvn_alias :closure-compiler-unshaded :closure-compiler

# Fix OSGi metadata
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']" \
"<configuration><instructions>
  <Bundle-SymbolicName>\${project.groupId}</Bundle-SymbolicName>
</instructions></configuration>" pom-main.xml

%build
%mvn_build -f

xsltproc \
        --nonet \
        --stringparam man.output.quietly 1 \
        --stringparam funcsynopsis.style ansi \
        --stringparam man.authors.section.enabled 0 \
        --stringparam man.copyright.section.enabled 0 \
        http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl %{SOURCE1}

%install
%mvn_install
%jpackage_script com.google.javascript.jscomp.CommandLineRunner "" "" args4j:google-gson:jsr-305:protobuf-java:js:guava:%{name} %{name} true

install -Dm0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%global _docdir_fmt %{name}

%files -f .mfiles
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%doc COPYING
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:20160315-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:20141215-alt1_7jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:20141215-alt1_3jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:20141215-alt1_2jpp8
- java 8 mass update

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150218-alt1jpp7
- Initial build for Sisyphus

