Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#in noarch? why...
%define debug_package %{nil}
%global remove_tests 1

Name:       procyon
Version:    0.5.36
Release:    alt1_0.1jpp8
Summary:    procyon java decompiler and other tools
License:    ASL 2.0 
URL:        https://bitbucket.org/mstrobel/procyon/
Source0:    https://bitbucket.org/mstrobel/procyon/get/v0.5.36.tar.gz
Source1:    procyon-decompiler
# main removal is not upstream-able, and is enforced by fedora policy
# signature is touching online world, necessary for packaging, not usptream able
Patch0:     removeSigningAndIfDecompilerAndMain.patch
# fat jar do not have much sense for fedora packagin. not upstream-able
Patch1:     disableFatJar.patch
# patch should be proposed to upstream.
Patch2:     adaptToNewerJcommander.patch
Patch3:     madeToPasXlint.patch
Patch4:     newJcommander.patch
BuildArch:  noarch
BuildRequires:  javapackages-tools
BuildRequires:  dos2unix
BuildRequires:  beust-jcommander
Requires:      javapackages-tools
# main package is just meta package for all subprojects andtheirs artifacts
Requires:   %{name}-compilertools = %{version}-%{release}
Requires:   %{name}-core = %{version}-%{release}
Requires:   %{name}-expressions = %{version}-%{release}
Requires:   %{name}-reflection = %{version}-%{release}
Requires:   %{name}-decompiler = %{version}-%{release}
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


%prep
%setup -q -n mstrobel-procyon-9f7822463e41
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
%patch1 -p1
%patch2 -p1
dos2unix Procyon.CompilerTools/src/main/java/com/strobel/assembler/metadata/MethodBinder.java
%patch3 -p1
%patch4 -p1


%build

mkdir -p build/Procyon.CompilerTools/{libs,classes}
mkdir -p build/Procyon.Core/{libs,classes}
mkdir -p build/Procyon.Decompiler/{libs,classes}
mkdir -p build/Procyon.Expressions/{libs,classes}
mkdir -p build/Procyon.Reflection/{libs,classes}

javac -d build/Procyon.Core/classes/ ` find Procyon.Core/src/main/java -type f | grep  "\.java"`
javac -d build/Procyon.Reflection/classes/    -cp build/Procyon.Core/classes/ ` find Procyon.Reflection/src/main/java -type f | grep  "\.java"`
javac -d build/Procyon.Expressions/classes/   -cp build/Procyon.Core/classes/:build/Procyon.Reflection/classes/ ` find Procyon.Expressions/src/main/java -type f | grep  "\.java"`
javac -d build/Procyon.CompilerTools/classes/ -cp build/Procyon.Core/classes/ ` find Procyon.CompilerTools/src/main/java -type f | grep  "\.java"`

# pack the jars
for x in Procyon.CompilerTools Procyon.Core Procyon.Reflection Procyon.Expressions ; do
  pushd build/$x/classes/
    project=`echo $x | sed -e "s/Procyon.//"  | sed -e 's/\(.*\)/\L\1/'`
    jar -cf ../../../build/$x/libs/%{name}-$project-%{version}.jar com
  popd
done

# create just launcher jar to be used in fedora
mkdir build/launcher-minimal
mkdir build/launcher-minimal/classes
javac -cp  build/Procyon.Core/classes/:build/Procyon.CompilerTools/classes/:%{_javadir}/beust-jcommander.jar  -d build/launcher-minimal/classes ` find Procyon.Decompiler/src/main/java -type f | grep  "\.java"`
# pack the minimal jar
pushd build/launcher-minimal/classes/
jar -cf ../../../build/Procyon.Decompiler/libs/%{name}-decompiler-%{version}.jar com
popd

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE1}  $RPM_BUILD_ROOT/%{_bindir}/ # cusotm launcher for main method in main jar
mkdir -p $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.CompilerTools/libs/%{name}-compilertools-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Core/libs/%{name}-core-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Decompiler/libs/%{name}-decompiler-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Expressions/libs/%{name}-expressions-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/
cp  build/Procyon.Reflection/libs/%{name}-reflection-%{version}.jar  $RPM_BUILD_ROOT/%{_javadir}/%{name}/

pushd   $RPM_BUILD_ROOT/%{_javadir}/%{name}/
ln -s %{name}-compilertools-%{version}.jar %{name}-compilertools.jar
ln -s %{name}-core-%{version}.jar %{name}-core.jar
ln -s %{name}-decompiler-%{version}.jar %{name}-decompiler.jar
ln -s %{name}-expressions-%{version}.jar %{name}-expressions.jar
ln -s %{name}-reflection-%{version}.jar %{name}-reflection.jar
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

%files reflection
%dir %{_javadir}/%{name}/
%{_javadir}/%{name}/%{name}-reflection-%{version}.jar
%{_javadir}/%{name}/%{name}-reflection.jar
%doc --no-dereference License.txt
%doc README.md


%changelog
* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0.5.36-alt1_0.1jpp8
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.5.33-alt1_0.3.pre02jpp8
- fc update

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.5.33-alt1_0.2.pre02jpp8
- new version

