BuildArch: noarch
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-cmake rpm-macros-fedora-compat rpm-macros-golang rpm-build-mono
BuildRequires: java-devel-default python3-module-setuptools rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# NOTE: The JavaScript runtime library includes a bundled copy of an obsolete
# version of Torben Hasse's require.js.  If somebody who knows about JavaScript
# will do something about that, we can include that runtime as well.  For now,
# it is omitted.
#
# NOTE: A PHP runtime is available as a separate project:
# https://github.com/antlr/antlr-php-runtime/

%global swiftarches x86_64 aarch64
%global swiftarches %nil
%global swiftdir    %{_prefix}/lib/swift/linux

Name:           antlr4-project
Version:        4.8
Release:        alt1_5jpp8
Summary:        Parser generator (ANother Tool for Language Recognition)

License:        BSD
URL:            http://www.antlr.org/
Source0:        https://github.com/antlr/antlr4/archive/%{version}/antlr4-%{version}.tar.gz
# Work around a "code too large" error while compiling a generated file
# https://github.com/antlr/antlr4/pull/2739
Patch0:         antlr4-unicode-properties.patch
# Fix mono errors due to ambiguous references
# Upstream is not yet ready to move to newer mono versions.
Patch1:         antlr4-mono-ambiguous.patch
# Fix some javadoc problems
Patch2:         antlr4-javadoc.patch

BuildRequires:  ctest cmake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  maven-local
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(com.webguys:string-template-maven-plugin)
BuildRequires:  mvn(org.abego.treelayout:org.abego.treelayout.core)
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin)
BuildRequires:  mvn(org.antlr:antlr4-maven-plugin)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.glassfish:javax.json)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  python3-devel
BuildRequires:  python3-module-setuptools

%global _desc \
ANTLR (ANother Tool for Language Recognition) is a powerful parser \
generator for reading, processing, executing, or translating structured \
text or binary files.  It is widely used to build languages, tools, and \
frameworks.  From a grammar, ANTLR generates a parser that can build \
and walk parse trees.
Source44: import.info

%description 

%_desc
%package     -n antlr4-runtime-test-annotations
Group: Development/Java
Summary:        ANTLR runtime test annotations
BuildArch:      noarch

%description -n antlr4-runtime-test-annotations 

This package provides runtime library test annotations used by Java
ANTLR parsers.

%_desc
%package     -n antlr4-runtime-test-annotation-processors
Group: Development/Java
Summary:        ANTLR runtime test annotation processors
BuildArch:      noarch
Requires:       antlr4-runtime-test-annotations = %{version}-%{release}

%description -n antlr4-runtime-test-annotation-processors 

This package provides runtime library test annotation processors used by
Java ANTLR parsers.

%_desc
%package     -n antlr4-runtime
Group: Development/Java
Summary:        ANTLR runtime
BuildArch:      noarch

%description -n antlr4-runtime 

This package provides the runtime library used by Java ANTLR parsers.

%_desc
%package     -n antlr4
Group: Development/Java
Summary:        Parser generator (ANother Tool for Language Recognition)
BuildArch:      noarch
Requires:       antlr4-runtime = %{version}-%{release}
Requires:       mvn(com.sun:tools)

%description -n antlr4 

This package provides the ANTLR parser generator.

%_desc
%package     -n antlr4-maven-plugin
Group: Development/Java
Summary:        ANTLR plugin for Apache Maven
BuildArch:      noarch
Requires:       antlr4 = %{version}-%{release}

%description -n antlr4-maven-plugin 

This package provides a plugin for Apache Maven which can be used to
generate ANTLR parsers during project build.

%_desc
%package     -n antlr4-javadoc
Group: Development/Java
Summary:        Java API documentation for antlr4
BuildArch:      noarch

%description -n antlr4-javadoc 

This package contains Java API documentation for antlr4.

%_desc
%package     -n antlr4-doc
Group: Development/Java
Summary:        ANTLR4 documentation
BuildArch:      noarch

%description -n antlr4-doc 

This package contains ANTLR4 documentation.

%_desc
%package     -n antlr4-cpp-runtime
Group: Development/Java
Summary:        ANTLR runtime for C++

%description -n antlr4-cpp-runtime 

This package provides the runtime library used by C++ ANTLR parsers.

%_desc
%package     -n antlr4-cpp-runtime-devel
Group: Development/Java
Summary:        Header files for programs that use C++ ANTLR parsers
Requires:       antlr4-cpp-runtime = %{version}-%{release}

%description -n antlr4-cpp-runtime-devel 

This package provides header files for programs that use C++ ANTLR
parsers.

%ifarch %go_arches
%global goipath github.com/antlr/antlr4/runtime/Go/antlr

%_desc
%package     -n golang-antlr4-runtime-devel
Group: Development/Java
Summary:        ANTLR runtime for Go
BuildArch:      noarch
BuildRequires:  rpm-macros-golang

%description -n golang-antlr4-runtime-devel 

This package provides the runtime library used by Go ANTLR parsers.
%endif

%ifarch %mono_arches
%_desc
%package     -n mono-antlr4-runtime
Group: Development/Java
Summary:        ANTLR runtime for C\# (mono)
License:        MIT
BuildArch:      noarch
BuildRequires:  mono-core mono-devel mono-mono2-compat mono-mono2-compat-devel mono-web

%description -n mono-antlr4-runtime 

This package provides the runtime library used by C\# (mono) ANTLR
parsers.
%endif

%_desc
%package     -n python3-module-antlr4
Group: Development/Java
Summary:        ANTLR runtime for Python 3
BuildArch:      noarch

%description -n python3-module-antlr4 

This package provides the runtime library used by Python 3 ANTLR parsers.

%ifarch %swiftarches
%_desc
%package     -n swift-antlr4-runtime
Group: Development/Java
Summary:        ANTLR runtime for swift
BuildRequires:  swift-lang

%description -n swift-antlr4-runtime 

This package provides the runtime library used by swift ANTLR parsers.
%endif

%_desc
%prep
%setup -q -n antlr4-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

find -name \*.jar -delete

# Update for recent stringtemplate versions
sed -i 's,\\>,>,g' tool/resources/org/antlr/v4/tool/templates/unicodedata.st

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# Xmvn javadoc mojo is in use
%pom_remove_plugin -r :maven-javadoc-plugin

# Missing test deps: org.seleniumhq.selenium:selenium-java
%pom_disable_module runtime-testsuite
%pom_disable_module tool-testsuite

# Missing test dep:
# io.takari.maven.plugins:takari-plugin-testing
%pom_remove_dep -r :takari-plugin-testing

# Missing plugin
# io.takari.maven.plugins:takari-lifecycle-plugin
%pom_remove_plugin -r :takari-lifecycle-plugin

# Don't bundle dependencies
%pom_remove_plugin :maven-shade-plugin tool

# Need some javax.json classes
%pom_add_dep javax.json:javax.json-api tool

# Replace dep on deprecated maven-project with maven-core
%pom_change_dep org.apache.maven:maven-project:2.2.1 org.apache.maven:maven-core:3.6.1 antlr4-maven-plugin

# Replace dep on maven-jdk-tools-wrapper with dep on tools.jar
%pom_change_dep :maven-jdk-tools-wrapper com.sun:tools runtime-testsuite/processors

%mvn_package :antlr4-master antlr4-runtime

# Change library install directory on 64-bit platforms
if [ "%{_lib}" != "lib" ]; then
  sed -i 's/DESTINATION lib/&64/' runtime/Cpp/runtime/CMakeLists.txt
fi

%build
# Ensure we get the jit on arm
#ifarch %{arm}
#export JAVA_HOME=$(ls -1d %{_jvmdir}/java-1.8.0-openjdk-aarch32*)
#else
#export JAVA_HOME=%{_jvmdir}/java
#endif

# Build for Java
# Due to the missing takari packages, we cannot run the tests
%mvn_build -s -f -- -Dsource=1.7

%if 0
# Build the C++ runtime
cd runtime/Cpp
%{fedora_v2_cmake} -DCMAKE_BUILD_TYPE=RelWithDebInfo .
%fedora_v2_cmake_build
cd -

# Build the Mono runtime
%ifarch %mono_arches
cd runtime/CSharp/runtime/CSharp
xbuild Antlr4.mono.sln
cd -
%endif

# Build the Python 3 runtime
cd runtime/Python3
%python3_build
cd -

%ifarch %swiftarches
# Build the Swift runtime
cd runtime/Swift
# Swift insists on a space between -j and the number, so cannot use _smp_mflags
swift build -c release %{?_smp_build_ncpus:-j %_smp_build_ncpus} \
  -Xlinker --build-id -Xlinker --as-needed -Xlinker -z -Xlinker relro \
  -Xlinker -z -Xlinker now
cd -
%endif
%endif

%install
# Install for Java; cannot use %%mvn_install as it passes %%name to -n
xmvn-install -R .xmvn-reactor -n antlr4 -d %{buildroot}
jdir=target/site/apidocs
[ -d .xmvn/apidocs ] && jdir=.xmvn/apidocs
mkdir -p %{buildroot}%{_licensedir}
if [ -d "${jdir}" ]; then
   install -dm755 %{buildroot}%{_javadocdir}/antlr4
   cp -pr "${jdir}"/* %{buildroot}%{_javadocdir}/antlr4
   echo '%{_javadocdir}/antlr4' >>.mfiles-javadoc
fi

%jpackage_script org.antlr.v4.Tool "" "" antlr4/antlr4:antlr3-runtime:antlr4/antlr4-runtime:stringtemplate4:treelayout antlr4 true

%if 0
# Install the C++ runtime
cd runtime/Cpp
%fedora_v2_cmake_install
rm -f %{buildroot}%{_libdir}/libantlr4-runtime.a
cd -

# Install the Go runtime
%ifarch %go_arches
mkdir -p %{buildroot}%{go_path}/src/%{goipath}
cp -p runtime/Go/antlr/* %{buildroot}%{go_path}/src/%{goipath}
cat > %{buildroot}%{go_path}/src/%{goipath}/.goipath << EOF
version:%{version}-%{release}
excluderegex:.*example.*
EOF
%endif

# Install the Mono runtime
#ifarch %mono_arches
%if 0
mkdir -p %{buildroot}%{_monogacdir}
gacutil -i runtime/CSharp/runtime/CSharp/Antlr4.Runtime/lib/Debug/Antlr4.Runtime.Standard.dll -f -package antlr4 -root %{buildroot}%{_prefix}/lib
%endif

# Install the Python 3 runtime
cd runtime/Python3
%python3_install
sed 's,#!python,#!%{__python3},' bin/pygrun > %{buildroot}%{_bindir}/pygrun
touch -r bin/pygrun %{buildroot}%{_bindir}/pygrun
chmod 0755 %{buildroot}%{_bindir}/pygrun
cd -

%ifarch %swiftarches
# Install the Swift runtime
cd runtime/Swift
mkdir -p %{buildroot}%{swiftdir}/%{_arch}
cp -p .build/release/libAntlr4.so %{buildroot}%{swiftdir}
cp -p .build/release/Antlr4.swift{doc,module} %{buildroot}%{swiftdir}/%{_arch}
cd -
%endif
%endif

# Create man pages
export PYTHONPATH=%{buildroot}%{python3_sitelibdir_noarch}
mkdir -p %{buildroot}%{_mandir}/man1
cd %{buildroot}%{_bindir}
help2man -N --version-string=4.8 -h '' ./antlr4 > \
  %{buildroot}%{_mandir}/man1/antlr4.1
#help2man -N --version-string=4.8 ./pygrun > \
#  %{buildroot}%{_mandir}/man1/pygrun.1
cd -

# Clean up bits we do not want
rm -fr %{buildroot}%{_docdir}/libantlr4

%files -n antlr4-runtime-test-annotations -f .mfiles-antlr4-runtime-test-annotations
%doc --no-dereference LICENSE.txt

%files -n antlr4-runtime-test-annotation-processors -f .mfiles-antlr4-runtime-test-annotation-processors

%files -n antlr4-runtime -f .mfiles-antlr4-runtime
%doc README.md
%doc --no-dereference LICENSE.txt

%files -n antlr4 -f .mfiles-antlr4
%doc CHANGES.txt contributors.txt
%{_bindir}/antlr4
%{_mandir}/man1/antlr4.1*

%files -n antlr4-maven-plugin -f .mfiles-antlr4-maven-plugin

%files -n antlr4-javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%if 0
%files -n antlr4-doc
%doc doc
%doc --no-dereference LICENSE.txt

%files -n antlr4-cpp-runtime
%doc runtime/Cpp/README.md
%doc --no-dereference LICENSE.txt
%{_libdir}/libantlr4-runtime.so.%{version}

%files -n antlr4-cpp-runtime-devel
%doc runtime/Cpp/cmake/Antlr4Package.md runtime/Cpp/cmake/README.md
%{_includedir}/antlr4-runtime/
%{_libdir}/libantlr4-runtime.so

%ifarch %go_arches
%files -n golang-antlr4-runtime-devel
%doc --no-dereference LICENSE.txt
%{go_path}/src/github.com/
%endif

#ifarch %mono_arches
%if 0
%files -n mono-antlr4-runtime
%doc runtime/CSharp/README.md
%doc --no-dereference LICENSE.txt
%{_monodir}/antlr4/
%{_monogacdir}/Antlr4.Runtime.Standard/
%endif

%files -n python3-module-antlr4
%doc runtime/Python3/README.txt
%doc --no-dereference LICENSE.txt
%{_bindir}/pygrun
%{_mandir}/man1/pygrun.1*
%python3_sitelibdir_noarch/antlr4/
%python3_sitelibdir_noarch/antlr4*.egg-info/

%ifarch %swiftarches
%files -n swift-antlr4-runtime
%doc --no-dereference LICENSE.txt
%{swiftdir}/libAntlr4.so
%{swiftdir}/%{_arch}/Antlr4.swiftdoc
%{swiftdir}/%{_arch}/Antlr4.swiftmodule
%endif
%endif

%changelog
* Thu Nov 12 2020 Igor Vlasenko <viy@altlinux.ru> 4.8-alt1_5jpp8
- new version (closes: #39185)

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.2-alt1_7jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.2-alt1_5jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 4.5.2-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 4.5.2-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 4.5.2-alt1_2jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.2-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.5-alt1_4jpp8
- unbootsrap build

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 4.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

