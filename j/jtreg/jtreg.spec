%define _unpackaged_files_terminate_build 1
%def_without check

Name: jtreg
Version: 8.1+1
Release: alt1

Summary: Regression Test Harness for the OpenJDK platform: jtreg
License: Apache-2.0
Group: Development/Java
Url: https://openjdk.org/projects/code-tools/jtreg
Vcs: https://github.com/openjdk/jtreg

ExcludeArch: i586

Source0: %name-%version.tar
# Temporary solution while bug: 57053 is open
Source1: junit-platform-console-standalone-6.0.1.jar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: ant
BuildRequires: openjdk-asmtools
BuildRequires: hamcrest
BuildRequires: jtharness
BuildRequires: testng
BuildRequires: java-21-openjdk-devel
BuildRequires: beust-jcommander
BuildRequires: google-guice
BuildRequires: apiguardian
BuildRequires: junit5
BuildRequires: make
BuildRequires: zip

%description
This framework is intended primarily for regression tests. It can also
be used for unit tests, functional tests, and even simple product tests
-- in other words, just about any type of test except a conformance
test, which belong in a TCK.

As well as API tests, jtreg is designed to be well suited for running
both positive and negative compiler tests, simple manual GUI tests, and
(when necessary) tests written in shell script. jtreg also takes care
of compiling tests as well as executing them, so there is no need to
precompile any test classes.

%prep
%setup
%autopatch -p1
install -m 0644 %SOURCE1 %_builddir/%name-%version/

%build
cd make
chmod +x build.sh
./build.sh

%install
find make/build/images/%name/lib/ -type f \
    -exec install -m 0644 -Dpvt %buildroot%_javadir/%name/lib/ {} \;

install -D -m 0755 -t %buildroot%_bindir/ make/build/images/%name/bin/{jtreg,jtdiff}

find make/build/images/%name/doc/%name -type f \
    -exec install -m 0644 -Dpvt %buildroot%_docdir/%name/ {} \;

mkdir -p %buildroot%_javadir/%name/{bin,doc}

%define install_tool_link() ln -sf ../../../%1 %buildroot%_javadir/%name/%2

%install_tool_link ../bin/jtreg bin/jtreg
%install_tool_link ../bin/jtdiff bin/jtdiff
%install_tool_link doc/jtreg/faq.html doc/faq.html
%install_tool_link doc/jtreg/tag-spec.html doc/tag-spec.html
%install_tool_link doc/jtreg/usage.txt doc/usage.txt

%check
export JDKHOME=/usr/lib/jvm/java
export JAVATEST_JAR=/usr/share/java/javatest.jar
export ASMTOOLS_JAR=/usr/share/java/openjdk-asmtools/asmtools.jar
export JUNIT_JARS=%SOURCE1
export TESTNG_JARS=/usr/share/java/testng.jar
export JCOMMANDER_JAR=/usr/share/java/beust-jcommander/jcommander.jar
export GOOGLE_GUICE_JAR=/usr/share/java/guice/google-guice.jar

cd ./make
make test

%files
%_bindir/jtreg
%_bindir/jtdiff
%_javadir/%name/
%_docdir/%name/faq.html
%_docdir/%name/tag-spec.html
%_docdir/%name/usage.txt
%doc LICENSE README.md

%changelog
* Mon Nov 17 2025 Timofei Fedotov <sovtouch@altlinux.org> 8.1+1-alt1
- Initial build for ALT Sisyphus.
