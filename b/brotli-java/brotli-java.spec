Name: brotli-java
Version: 1.2.0
Release: alt1

Summary: Pure Java decoder for the Brotli compression format

License: MIT
Group: Development/Java
Url: https://github.com/google/brotli
BuildArch: noarch
ExcludeArch: %ix86

# GitHub tag archives exclude java/ (export-ignore), the sources are imported
# from git: https://github.com/google/brotli.git tag v%version
Source: %name-%version.tar

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: java-25-openjdk-devel
BuildRequires: mvn(junit:junit)

%description
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling (RFC 7932).

This package contains the pure Java Brotli decoder (Maven artifact
org.brotli:dec).

%javadoc_package

%prep
%setup
cd java/org/brotli
%pom_xpath_set pom:project/pom:version %version
%pom_xpath_set pom:project/pom:parent/pom:version %version dec
%pom_xpath_set pom:project/pom:version %version dec
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin dec
%pom_remove_plugin :maven-javadoc-plugin dec
# OSGi manifest is not needed; without Automatic-Module-Name the jar keeps
# the module name "dec" of the Maven Central org.brotli:dec 0.1.2 artifact
# that consumers (sambox) require.
%pom_remove_plugin :maven-bundle-plugin dec
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:archive' dec
%mvn_file org.brotli:dec brotli/dec
# Upstream compiles from the shared source root with includes; XMvn javadoc
# would process the whole tree (JNI wrapper, tests), so use a standard layout.
pushd dec
mkdir -p src/main/java/org/brotli/dec src/test/java/org/brotli/dec
cp -p $(ls *.java | grep -v Test) src/main/java/org/brotli/dec/
cp -p *Test*.java src/test/java/org/brotli/dec/
# excluded by upstream pom (testExcludes)
rm -v src/test/java/org/brotli/dec/SetDictionaryTest.java
%pom_xpath_remove pom:build/pom:sourceDirectory
%pom_xpath_remove pom:build/pom:testSourceDirectory
%pom_remove_plugin :maven-compiler-plugin
popd

%build
cd java/org/brotli
%mvn_build

%install
cd java/org/brotli
%mvn_install
mv .mfiles* ../../../

%files -f .mfiles
%doc README.md CHANGELOG.md
%doc --no-dereference LICENSE

%changelog
* Sun Oct 18 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for Sisyphus
