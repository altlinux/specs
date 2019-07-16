Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#in noarch? why...
%define debug_package %{nil}
# assembled single-jar decompiler can not be currently packed in fedora, but can be build locally
%global enable_fat_jar 0
%global remove_tests 1

Name:       procyon
Version:    0.5.33
Release:    alt1_0.2.pre02jpp8
Summary:    procyon java decompiler and other tools
License:    ASL 2.0 
URL:        https://bitbucket.org/mstrobel/procyon/
#Source0:   https://bitbucket.org/mstrobel/procyon/get/ee404caa9a29.zip
Source0:    mstrobel-procyon-ee404caa9a29.zip
Source1:    procyon-decompiler
# main removal is not upstream-able, and is enforced by fedora policy
# signature is touching online world, necessary for packaging, not usptream able
Patch0:     removeSigningAndIfDecompilerAndMain.patch
# fat jar do not have much sense for fedora packagin. not upstream-able
Patch1:     disableFatJar.patch
# patch should be proposed to upstream.
Patch2:     adaptToNewerJcommander.patch
BuildArch:  noarch
BuildRequires:  javapackages-tools
%if %{enable_fat_jar}
BuildRequires:  gradle
%else
BuildRequires:  gradle-local
%endif
BuildRequires:  dos2unix
BuildRequires:  beust-jcommander
Requires:      javapackages-tools
# main package is just meta package for all subprojects andtheirs artifacts
Requires:   %{name}-compilertools = %{version}-%{release}
Requires:   %{name}-core = %{version}-%{release}
Requires:   %{name}-expressions = %{version}-%{release}
Requires:   %{name}-reflection = %{version}-%{release}
Requires:   %{name}-decompiler = %{version}-%{release}
%if %{enable_fat_jar}
Requires:   %{name}-decompiler-all = %{version}-%{release}
%endif
Requires:   %{name}-compilertools-javadoc = %{version}-%{release}
Requires:   %{name}-core-javadoc = %{version}-%{release}
Requires:   %{name}-expressions-javadoc = %{version}-%{release}
Requires:   %{name}-reflection-javadoc = %{version}-%{release}
Requires:   %{name}-decompiler-javadoc = %{version}-%{release}
Requires:   %{name}-compilertools-srcs = %{version}-%{release}
Requires:   %{name}-core-srcs = %{version}-%{release}
Requires:   %{name}-expressions-srcs = %{version}-%{release}
Requires:   %{name}-reflection-srcs = %{version}-%{release}
Requires:   %{name}-decompiler-srcs = %{version}-%{release}
Source44: import.info

%description
Procyon is a suite of Java metaprogramming tools focused on code generation and analysis.
It includes the following libraries: Core Framework, Reflection Framework,
Expressions Framework, Compiler Toolset (Experimental), Java Decompiler.
The Procyon libraries are available from Maven Central under group ID org.bitbucket.mstrobel.

%package compilertools
Group: Development/Java
Summary:    The procyon-compilertools project
BuildArch:  noarch
Requires:      javapackages-tools

%description compilertools
The procyon-compilertools project is a work in progress that includes:
Class metadata and bytecode inspection/manipulation facilities based on Mono.Cecil and 
An optimization and decompiler framework based on ILSpy
The Compiler Toolset is still early in development and subject to change.

%package core
Group: Development/Java
Summary:    The procyon-core framework contains common support classes
BuildArch:  noarch
Requires:      javapackages-tools

%description core
The procyon-core framework contains common support classes used by the other
Procyon APIs. Its facilities include string manipulation, collection extensions,
filesystem/path utilities, freezable objects and collections, attached data stores,
and some runtime type helpers.

%package expressions
Group: Development/Java
Summary:    The procyon-expressions framework provides a more natural form of Linq-like code generation
BuildArch:  noarch
Requires:      javapackages-tools

%description expressions
The procyon-expressions framework provides a more natural form of code generation.
Rather than requiring bytecode to be emitted directly, as with procyon-reflection
and other popular libraries like ASM, procyon-expressions enables code composition
using declarative expression trees. These expression trees may then be compiled directly
into callbacks or coupled with a MethodBuilder. The procyon-expressions API is
almost a direct port of System.Linq.Expressions from .NET's Dynamic Language Runtime,
minus the dynamic callsite support (and with more relaxed rules regarding type conversions).

%package decompiler
Group: Development/Java
Summary:    procyon-decompiler is a front-end for the Java decompiler
BuildArch:  noarch
Requires:   %{name}-core
Requires:   %{name}-compilertools
Requires:   beust-jcommander
Requires:      javapackages-tools

%description decompiler
procyon-decompiler is a front-end for the Java decompiler included in procyon-compilertools.
For more information about the decompiler, see the Java Decompiler wiki page - 
https://bitbucket.org/mstrobel/procyon/wiki/Java%%20Decompiler

%if %{enable_fat_jar}
%package decompiler-all
Group: Development/Java
Summary:    procyon-decompiler-all is library with assembled core and compiler-tools together with cli
BuildArch:  noarch
Requires:      javapackages-tools

%description decompiler-all
procyon-decompiler is a front-end for the Java decompiler with all depndencies packed
For more information about the decompiler, see the Java Decompiler wiki page - 
https://bitbucket.org/mstrobel/procyon/wiki/Java%%20Decompiler
%endif

%package reflection
Group: Development/Java
Summary:    The procyon-reflection framework provides a rich reflection and code generation API
BuildArch:  noarch
Requires:      javapackages-tools

%description reflection
The procyon-reflection framework provides a rich reflection and code generation API with full support for generics,
wildcards, and other high-level Java type concepts. It is based on .NET's System.Reflection and System.Reflection.
Emit APIs and is meant to address many of the shortcomings of the core Java reflection API, which offers rather
limited and cumbersome support for generic type inspection. Its code generation facilities include a TypeBuilder,
MethodBuilder, and a bytecode emitter.

%package compilertools-javadoc
Group: Development/Java
Summary:    The procyon-compilertools project javadoc
BuildArch:  noarch

%description compilertools-javadoc
javadoc

%package core-javadoc
Group: Development/Java
Summary:    The procyon-core framework javadoc
BuildArch:  noarch

%description core-javadoc
javadoc

%package expressions-javadoc
Group: Development/Java
Summary:    The procyon-expressions framework provides javadoc
BuildArch:  noarch

%description expressions-javadoc
javadoc

%package decompiler-javadoc
Group: Development/Java
Summary:    procyon-decompiler javadoc
BuildArch:  noarch

%description decompiler-javadoc
javadoc

%package reflection-javadoc
Group: Development/Java
Summary:    The procyon-reflection framework javadoc
BuildArch:  noarch

%description reflection-javadoc
javadoc

%package compilertools-srcs
Group: Development/Java
Summary:    The procyon-compilertools project sources
BuildArch:  noarch
Requires:      javapackages-tools

%description compilertools-srcs
sources

%package core-srcs
Group: Development/Java
Summary:    The procyon-core framework sources
BuildArch:  noarch
Requires:      javapackages-tools

%description core-srcs
sources

%package expressions-srcs
Group: Development/Java
Summary:    The procyon-expressions framework provides sources
BuildArch:  noarch
Requires:      javapackages-tools

%description expressions-srcs
sources

%package decompiler-srcs
Group: Development/Java
Summary:    procyon-decompiler sources
BuildArch:  noarch
Requires:      javapackages-tools

%description decompiler-srcs
sources

%package reflection-srcs
Group: Development/Java
Summary:    The procyon-reflection framework sources
BuildArch:  noarch
Requires:      javapackages-tools

%description reflection-srcs
sources

%prep
%setup -q -n mstrobel-procyon-ee404caa9a29
%if %{remove_tests}
find | grep "\\.class$"
#find | grep "\\.jar$"
rm -rvf Procyon.CompilerTools/src/test/
find | grep "\\.class$" && exit 1
find | grep "\\.jar$"   && exit 1
%endif
#to allow smooth patching
dos2unix Procyon.Decompiler/build.gradle
dos2unix build.gradle
dos2unix README.md
# also removing main method from enter point jar
%patch0 -p1
%if %{enable_fat_jar}
echo "not applying patch1, enabeld fat jar"
%else
%patch1 -p1
%endif
%patch2 -p1

%build
#gradle build -x test
%gradle_build -f
# create just launcher jar to be used in fedora
mkdir launcher-minimal
mkdir launcher-minimal/classes
javac -cp  build/Procyon.Core/libs/%{name}-core-%{version}.jar:build/Procyon.CompilerTools/libs/%{name}-compilertools-%{version}.jar:%{_javadir}/beust-jcommander.jar  -d launcher-minimal/classes ` find Procyon.Decompiler/src/main/java -type f | grep  "\.java"`
%if %{enable_fat_jar}
# some dependent packages depnds on this assembeld decompiler jar (we build without its main in manifest (good idea?), see patch0
gradle fatjar -x test
# rename
mv build/Procyon.Decompiler/libs/%{name}-decompiler-%{version}.jar build/Procyon.Decompiler/libs/%{name}-decompiler-all-%{version}.jar
%endif
# pack the minimal jar
pushd launcher-minimal/classes/
jar -cf ../../build/Procyon.Decompiler/libs/%{name}-decompiler-%{version}.jar com
popd

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE1}  $RPM_BUILD_ROOT/%{_bindir}/ # cusotm launcher for main method in main jar
mkdir -p $RPM_BUILD_ROOT/%{_javadir}/%{name}/
mkdir -p $RPM_BUILD_ROOT/%{_javadir}/%{name}/srcs
mkdir -p $RPM_BUILD_ROOT/%{_javadocdir}/%{name}/
cp  build/Procyon.CompilerTools/libs/%{name}-compilertools-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Core/libs/%{name}-core-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Decompiler/libs/%{name}-decompiler-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
%if %{enable_fat_jar}
cp  build/Procyon.Decompiler/libs/%{name}-decompiler-all-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
%endif
cp  build/Procyon.Expressions/libs/%{name}-expressions-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Reflection/libs/%{name}-reflection-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/

cp  build/Procyon.CompilerTools/libs/%{name}-compilertools-%{version}-javadoc.jar  $RPM_BUILD_ROOT/%{_javadocdir}/%{name}/
cp  build/Procyon.Core/libs/%{name}-core-%{version}-javadoc.jar  $RPM_BUILD_ROOT/%{_javadocdir}/%{name}/
cp  build/Procyon.Decompiler/libs/%{name}-decompiler-%{version}-javadoc.jar  $RPM_BUILD_ROOT/%{_javadocdir}/%{name}/
cp  build/Procyon.Expressions/libs/%{name}-expressions-%{version}-javadoc.jar  $RPM_BUILD_ROOT/%{_javadocdir}/%{name}/
cp  build/Procyon.Reflection/libs/%{name}-reflection-%{version}-javadoc.jar  $RPM_BUILD_ROOT/%{_javadocdir}/%{name}/

cp  build/Procyon.CompilerTools/libs/%{name}-compilertools-%{version}-sources.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/srcs/
cp  build/Procyon.Core/libs/%{name}-core-%{version}-sources.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/srcs/
cp  build/Procyon.Decompiler/libs/%{name}-decompiler-%{version}-sources.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/srcs/
cp  build/Procyon.Expressions/libs/%{name}-expressions-%{version}-sources.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/srcs/
cp  build/Procyon.Reflection/libs/%{name}-reflection-%{version}-sources.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/srcs/
pushd   $RPM_BUILD_ROOT/%{_javadir}/%{name}/
ln -s %{name}-compilertools-%{version}.jar %{name}-compilertools.jar
ln -s %{name}-core-%{version}.jar %{name}-core.jar
ln -s %{name}-decompiler-%{version}.jar %{name}-decompiler.jar
%if %{enable_fat_jar}
ln -s %{name}-decompiler-all-%{version}.jar %{name}-decompiler-all.jar
%endif
ln -s %{name}-expressions-%{version}.jar %{name}-expressions.jar
ln -s %{name}-reflection-%{version}.jar %{name}-reflection.jar
popd
pushd   $RPM_BUILD_ROOT/%{_javadocdir}/%{name}/
ln -s %{name}-compilertools-%{version}-javadoc.jar %{name}-compilertools-javadoc.jar
ln -s %{name}-core-%{version}-javadoc.jar %{name}-core-javadoc.jar
ln -s %{name}-decompiler-%{version}-javadoc.jar %{name}-decompiler-javadoc.jar
ln -s %{name}-expressions-%{version}-javadoc.jar %{name}-expressions-javadoc.jar
ln -s %{name}-reflection-%{version}-javadoc.jar %{name}-reflection-javadoc.jar
popd
pushd   $RPM_BUILD_ROOT/%{_javadir}/%{name}/srcs
ln -s %{name}-compilertools-%{version}-sources.jar %{name}-compilertools-sources.jar
ln -s %{name}-core-%{version}-sources.jar %{name}-core-sources.jar
ln -s %{name}-decompiler-%{version}-sources.jar %{name}-decompiler-sources.jar
ln -s %{name}-expressions-%{version}-sources.jar %{name}-expressions-sources.jar
ln -s %{name}-reflection-%{version}-sources.jar %{name}-reflection-sources.jar
popd

%files
%doc --no-dereference License.txt
%doc README.md

%files compilertools
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-compilertools-%{version}.jar
%{_javadir}/%{name}/%{name}-compilertools.jar
%doc --no-dereference License.txt
%doc README.md

%files core
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-core-%{version}.jar
%{_javadir}/%{name}/%{name}-core.jar
%doc --no-dereference License.txt
%doc README.md

%files expressions
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-expressions-%{version}.jar
%{_javadir}/%{name}/%{name}-expressions.jar
%doc --no-dereference License.txt
%doc README.md

%files decompiler
%dir %{_javadir}/%{name}
%{_bindir}/%{name}-decompiler
%{_javadir}/%{name}/%{name}-decompiler-%{version}.jar
%{_javadir}/%{name}/%{name}-decompiler.jar
%doc --no-dereference License.txt
%doc README.md

%if %{enable_fat_jar}
%files decompiler-all
%dir %{_javadir}/%{name}
%{_bindir}/%{name}-decompiler
%{_javadir}/%{name}/%{name}-decompiler-all-%{version}.jar
%{_javadir}/%{name}/%{name}-decompiler-all.jar
%doc --no-dereference License.txt
%doc README.md
%endif

%files reflection
%dir %{_javadir}/%{name}/
%{_javadir}/%{name}/%{name}-reflection-%{version}.jar
%{_javadir}/%{name}/%{name}-reflection.jar
%doc --no-dereference License.txt
%doc README.md

%files compilertools-javadoc
%dir %{_javadocdir}/%{name}/
%{_javadocdir}/%{name}/%{name}-compilertools-%{version}-javadoc.jar
%{_javadocdir}/%{name}/%{name}-compilertools-javadoc.jar
%doc --no-dereference License.txt
%doc README.md

%files core-javadoc
%dir %{_javadocdir}/%{name}/
%{_javadocdir}/%{name}/%{name}-core-%{version}-javadoc.jar
%{_javadocdir}/%{name}/%{name}-core-javadoc.jar
%doc --no-dereference License.txt
%doc README.md

%files expressions-javadoc
%dir %{_javadocdir}/%{name}/
%{_javadocdir}/%{name}/%{name}-expressions-%{version}-javadoc.jar
%{_javadocdir}/%{name}/%{name}-expressions-javadoc.jar
%doc --no-dereference License.txt
%doc README.md

%files decompiler-javadoc
%dir %{_javadocdir}/%{name}/
%{_bindir}/%{name}-decompiler
%{_javadocdir}/%{name}/%{name}-decompiler-%{version}-javadoc.jar
%{_javadocdir}/%{name}/%{name}-decompiler-javadoc.jar
%doc --no-dereference License.txt
%doc README.md

%files reflection-javadoc
%dir %{_javadocdir}/%{name}/
%{_javadocdir}/%{name}/%{name}-reflection-%{version}-javadoc.jar
%{_javadocdir}/%{name}/%{name}-reflection-javadoc.jar
%doc --no-dereference License.txt
%doc README.md

%files compilertools-srcs
%dir %{_javadir}/%{name}
%dir %{_javadir}/%{name}/srcs
%{_javadir}/%{name}/srcs/%{name}-compilertools-%{version}-sources.jar
%{_javadir}/%{name}/srcs/%{name}-compilertools-sources.jar
%doc --no-dereference License.txt
%doc README.md

%files core-srcs
%dir %{_javadir}/%{name}
%dir %{_javadir}/%{name}/srcs
%{_javadir}/%{name}/srcs/%{name}-core-%{version}-sources.jar
%{_javadir}/%{name}/srcs/%{name}-core-sources.jar
%doc --no-dereference License.txt
%doc README.md

%files expressions-srcs
%dir %{_javadir}/%{name}
%dir %{_javadir}/%{name}/srcs
%{_javadir}/%{name}/srcs/%{name}-expressions-%{version}-sources.jar
%{_javadir}/%{name}/srcs/%{name}-expressions-sources.jar
%doc --no-dereference License.txt
%doc README.md

%files decompiler-srcs
%dir %{_javadir}/%{name}
%dir %{_javadir}/%{name}/srcs
%{_bindir}/%{name}-decompiler
%{_javadir}/%{name}/srcs/%{name}-decompiler-%{version}-sources.jar
%{_javadir}/%{name}/srcs/%{name}-decompiler-sources.jar
%doc --no-dereference License.txt
%doc README.md

%files reflection-srcs
%dir %{_javadir}/%{name}
%dir %{_javadir}/%{name}/srcs
%{_javadir}/%{name}/srcs/%{name}-reflection-%{version}-sources.jar
%{_javadir}/%{name}/srcs/%{name}-reflection-sources.jar
%doc --no-dereference License.txt
%doc README.md

%changelog
* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.5.33-alt1_0.2.pre02jpp8
- new version

