Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat rpm-macros-java
BuildRequires: gcc-c++ perl(Digest.pm) perl(English.pm) perl(Error.pm) perl(Exception/Class.pm) perl(Exception/Class/Base.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Slurp.pm) perl(File/Spec/Unix.pm) perl(FindBin.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Moose.pm) perl(Moose/Object.pm) perl(Moose/Role.pm) perl(Moose/Util/TypeConstraints.pm) perl(Params/Validate.pm) perl(Readonly.pm) perl(Switch.pm) perl(Test/Builder/Module.pm) perl(Test/Class/Load.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(UNIVERSAL.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(blib.pm) perl(overload.pm) perl-devel unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global antlr_version 3.5.2
%global c_runtime_version 3.4
%global javascript_runtime_version 3.1
%global baserelease 33

# This package needs itself to build.  Use this to bootstrap on a new system.
%bcond_with bootstrap

# Component versions to use when bootstrapping
%global antlr2_version 2.7.7
%global bootstrap_version 3.5
%global ST4ver1 4.0.7
%global ST4ver2 4.0.8
%global stringtemplatever 3.2.1

Summary:            ANother Tool for Language Recognition
Name:               antlr3
Epoch:              1
Version:            %{antlr_version}
Release:            alt1_33jpp11
License:            BSD
URL:                http://www.antlr3.org/

Source0:            https://github.com/antlr/antlr3/archive/%{antlr_version}/%{name}-%{antlr_version}.tar.gz
Source1:            http://www.antlr3.org/download/antlr-javascript-runtime-%{javascript_runtime_version}.zip
%if %{with bootstrap}
# Get prebuilt versions to bootstrap
Source2:            https://repo1.maven.org/maven2/org/antlr/ST4/%{ST4ver1}/ST4-%{ST4ver1}.jar
Source3:            https://repo1.maven.org/maven2/org/antlr/ST4/%{ST4ver1}/ST4-%{ST4ver1}.pom
Source4:            https://repo1.maven.org/maven2/org/antlr/ST4/%{ST4ver2}/ST4-%{ST4ver2}.jar
Source5:            https://repo1.maven.org/maven2/org/antlr/ST4/%{ST4ver2}/ST4-%{ST4ver2}.pom
Source6:            https://repo1.maven.org/maven2/org/antlr/antlr/%{bootstrap_version}/antlr-%{bootstrap_version}.jar
Source7:            https://repo1.maven.org/maven2/org/antlr/antlr/%{bootstrap_version}/antlr-%{bootstrap_version}.pom
Source8:            https://repo1.maven.org/maven2/org/antlr/antlr-master/%{bootstrap_version}/antlr-master-%{bootstrap_version}.pom
Source9:            https://repo1.maven.org/maven2/org/antlr/antlr-runtime/%{bootstrap_version}/antlr-runtime-%{bootstrap_version}.jar
Source10:           https://repo1.maven.org/maven2/org/antlr/antlr-runtime/%{bootstrap_version}/antlr-runtime-%{bootstrap_version}.pom
Source11:           https://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}/antlr3-maven-plugin-%{bootstrap_version}.jar
Source12:           https://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}/antlr3-maven-plugin-%{bootstrap_version}.pom
Source13:           https://repo1.maven.org/maven2/org/antlr/stringtemplate/%{stringtemplatever}/stringtemplate-%{stringtemplatever}.jar
Source14:           https://repo1.maven.org/maven2/org/antlr/stringtemplate/%{stringtemplatever}/stringtemplate-%{stringtemplatever}.pom
Source15:           https://repo1.maven.org/maven2/antlr/antlr/%{antlr2_version}/antlr-%{antlr2_version}.jar
Source16:           https://repo1.maven.org/maven2/antlr/antlr/%{antlr2_version}/antlr-%{antlr2_version}.pom
%endif

Patch0:         0001-java8-fix.patch
# Generate OSGi metadata
Patch1:         osgi-manifest.patch
# Increase the default conversion timeout to avoid build failures when complex
# grammars are processed on slow architectures.  Patch from Debian.
Patch2:         0002-conversion-timeout.patch
# Fix problems with the C template.  Patch from Debian.
Patch3:         0003-fix-c-template.patch
# Keep Token.EOF_TOKEN for backwards compatibility.  Patch from Debian.
Patch4:         0004-eof-token.patch
# Make parsers reproducible.  Patch from Debian.
Patch5:         0005-reproducible-parsers.patch
# Fix for C++20
Patch6:         0006-antlr3memory.hpp-fix-for-C-20-mode.patch
# Compile for target 1.8 to fix build with JDK 11
Patch7:         0007-update-java-target.patch

BuildRequires:  ant
BuildRequires:  maven-local
%if %{without bootstrap}
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin)
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.antlr:stringtemplate)
%endif
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)

BuildRequires:      autoconf
BuildRequires:      automake
BuildRequires:      libtool

# we don't build it now
Obsoletes:       antlr3-gunit < 3.2-15
Source44: import.info

%description
ANother Tool for Language Recognition, is a language tool
that provides a framework for constructing recognizers,
interpreters, compilers, and translators from grammatical
descriptions containing actions in a variety of target languages.

%package     tool
Group: Development/Java
Summary:     ANother Tool for Language Recognition
BuildArch:   noarch
Provides:    %{name} = %{epoch}:%{antlr_version}-%{release}
Obsoletes:   %{name} < %{epoch}:%{antlr_version}-%{release}
Requires:    %{name}-java = %{epoch}:%{antlr_version}-%{release}
# Explicit requires for javapackages-tools since antlr3-script
# uses /usr/share/java-utils/java-functions
Requires:    javapackages-tools


Provides:    ant-antlr3 = %{epoch}:%{antlr_version}-%{release}
Obsoletes:   ant-antlr3 < %{epoch}:%{antlr_version}-%{release}

%description tool
ANother Tool for Language Recognition, is a language tool
that provides a framework for constructing recognizers,
interpreters, compilers, and translators from grammatical
descriptions containing actions in a variety of target languages.

%package     java
Group: Development/Java
Summary:     Java run-time support for ANTLR-generated parsers
BuildArch:   noarch

%description java
Java run-time support for ANTLR-generated parsers

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch:      noarch

%description javadoc
%{summary}.

%package      javascript
Group: Development/Java
Summary:      Javascript run-time support for ANTLR-generated parsers
Version:      %{javascript_runtime_version}
BuildArch:    noarch

%description  javascript
Javascript run-time support for ANTLR-generated parsers

%package   C
Group: Development/Java
Summary:   C run-time support for ANTLR-generated parsers
Version:   %{c_runtime_version}

%description C
C run-time support for ANTLR-generated parsers

%package   C-devel
Group: Development/Java
Summary:   Header files for the C bindings for ANTLR-generated parsers
Requires:  %{name}-C = %{epoch}:%{c_runtime_version}-%{release}
Version:   %{c_runtime_version}


%description C-devel
Header files for the C bindings for ANTLR-generated parsers

%package        C-docs
Group: Development/Java
Summary:        API documentation for the C run-time support for ANTLR-generated parsers
BuildArch:      noarch
BuildRequires:  graphviz libgraphviz
BuildRequires:  doxygen
Requires:       %{name}-C = %{epoch}:%{c_runtime_version}-%{release}
Version:   %{c_runtime_version}

%description    C-docs
This package contains doxygen documentation with instruction
on how to use the C target in ANTLR and complete API description of the
C run-time support for ANTLR-generated parsers.

%package C++-devel
Group: Development/Java
Summary:        C++ runtime support for ANTLR-generated parsers

%description C++-devel
C++ runtime support for ANTLR-generated parsers.

%prep
%setup -q -n antlr3-%{antlr_version} -a 1
sed -i "s,\${buildNumber},`cat %{_sysconfdir}/fedora-release` `date`," tool/src/main/resources/org/antlr/antlr.properties
%patch0 -p1
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# remove pre-built artifacts
find -type f -a -name *.jar -delete
find -type f -a -name *.class -delete

%pom_remove_parent

%pom_disable_module antlr3-maven-archetype
%pom_disable_module gunit
%pom_disable_module gunit-maven-plugin
%pom_disable_module antlr-complete

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

# workarounds bug in filtering (Mark invalid)
%pom_xpath_remove pom:resource/pom:filtering

%mvn_package :antlr-runtime java
%mvn_package : tool

%mvn_file :antlr antlr3
%mvn_file :antlr-runtime antlr3-runtime
%mvn_file :antlr-maven-plugin antlr3-maven-plugin

%if %{with bootstrap}
# Make the bootstrap JARs and POMs available
mkdir -p .m2/org/antlr/ST4/%{ST4ver1}
cp -p %{SOURCE2} %{SOURCE3} .m2/org/antlr/ST4/%{ST4ver1}
mkdir -p .m2/org/antlr/ST4/%{ST4ver2}
cp -p %{SOURCE4} %{SOURCE5} .m2/org/antlr/ST4/%{ST4ver2}
mkdir -p .m2/org/antlr/antlr/%{bootstrap_version}
cp -p %{SOURCE6} %{SOURCE7} .m2/org/antlr/antlr/%{bootstrap_version}
mkdir -p .m2/org/antlr/antlr-master/%{bootstrap_version}
cp -p %{SOURCE8} .m2/org/antlr/antlr-master/%{bootstrap_version}
mkdir -p .m2/org/antlr/antlr-runtime/%{bootstrap_version}
cp -p %{SOURCE9} %{SOURCE10} .m2/org/antlr/antlr-runtime/%{bootstrap_version}
mkdir -p .m2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}
cp -p %{SOURCE11} %{SOURCE12} .m2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}
mkdir -p .m2/org/antlr/stringtemplate/%{stringtemplatever}
cp -p %{SOURCE13} %{SOURCE14} .m2/org/antlr/stringtemplate/%{stringtemplatever}
mkdir -p .m2/antlr/antlr/%{antlr2_version}
cp -p %{SOURCE15} %{SOURCE16} .m2/antlr/antlr/%{antlr2_version}

# We don't need the parent POM
%pom_remove_parent .m2/org/antlr/ST4/%{ST4ver1}/ST4-%{ST4ver1}.pom
%pom_remove_parent .m2/org/antlr/ST4/%{ST4ver2}/ST4-%{ST4ver2}.pom
%pom_remove_parent .m2/org/antlr/antlr-master/%{bootstrap_version}/antlr-master-%{bootstrap_version}.pom
%endif

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

# Build the C runtime
pushd runtime/C
autoreconf -i
%configure --disable-abiflags --enable-debuginfo \
%if 0%{?__isa_bits} == 64
    --enable-64bit
%else
    %{nil}
%endif

sed -i "s#CFLAGS = .*#CFLAGS = $RPM_OPT_FLAGS#" Makefile
%make_build
doxygen -u # update doxygen configuration file
doxygen # build doxygen documentation
popd

# build ant task
pushd antlr-ant/main/antlr3-task/
export CLASSPATH=$(build-classpath ant)
javac  -encoding ISO-8859-1 -source 1.8 -target 1.8 \
  antlr3-src/org/apache/tools/ant/antlr/ANTLR3.java
jar cvf ant-antlr3.jar \
  -C antlr3-src org/apache/tools/ant/antlr/antlib.xml \
  -C antlr3-src org/apache/tools/ant/antlr/ANTLR3.class
popd

%install
mkdir -p $RPM_BUILD_ROOT/%{_mandir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/antlr

%mvn_install

# install ant task
install -m 644 antlr-ant/main/antlr3-task/ant-antlr3.jar -D $RPM_BUILD_ROOT%{_javadir}/ant/ant-antlr3.jar
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/ant-antlr3 << EOF
ant/ant-antlr3 antlr3
EOF

# install wrapper script
%jpackage_script org.antlr.Tool '' '' 'stringtemplate4/ST4.jar:antlr3.jar:antlr3-runtime.jar' antlr3 true

# install C runtime
pushd runtime/C
%makeinstall_std
rm $RPM_BUILD_ROOT%{_libdir}/libantlr3c.{a,la}
pushd api/man/man3
for file in `ls -1 * | grep -vi "^antlr3"`; do
    mv $file antlr3-$file
done
sed -i -e 's,^\.so man3/pANTLR3,.so man3/antlr3-pANTLR3,' `grep -rl 'man3/pANTLR3' .`
gzip *
popd
#mv api/man/man3 $RPM_BUILD_ROOT%{_mandir}/
#rmdir api/man
popd

# install javascript runtime
pushd antlr-javascript-runtime-%{javascript_runtime_version}
install -pm 644 *.js $RPM_BUILD_ROOT%{_datadir}/antlr/
popd

# install C++ runtime (header only)
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/%{name}
install -pm 644 runtime/Cpp/include/* $RPM_BUILD_ROOT/%{_includedir}/

%files tool -f .mfiles-tool
%doc README.txt tool/LICENSE.txt
%doc README.txt tool/CHANGES.txt
%{_bindir}/antlr3
%{_javadir}/ant/ant-antlr3.jar
%config(noreplace) %{_sysconfdir}/ant.d/ant-antlr3

%files C
%doc tool/LICENSE.txt
%{_libdir}/libantlr3c.so

%files C-devel
#%{_mandir}/man3/*
%{_includedir}/*.h

%files C-docs
%doc runtime/C/api

%files C++-devel
%doc tool/LICENSE.txt
%{_includedir}/*.hpp
%{_includedir}/*.inl

%files java -f .mfiles-java
%doc tool/LICENSE.txt

%files javascript
%doc tool/LICENSE.txt
%{_datadir}/antlr/

%files javadoc -f .mfiles-javadoc
%doc tool/LICENSE.txt

%changelog
* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 1:3.5.2-alt1_33jpp11
- update

* Mon Jun 07 2021 Igor Vlasenko <viy@altlinux.org> 1:3.5.2-alt1_31jpp11
- use jvm_run

* Sun Oct 11 2020 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_30jpp8
- fc update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_22jpp8
- build with java 8

* Tue Jun 18 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_19jpp8
- fc update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_17jpp8
- regenerated to fix __isa_bits definition

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_16jpp8
- fixed build

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_11jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_9jpp8
- full-fledged build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt0_9jpp8
- java 8 mass update (bootstrap)

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 3.4-alt3_14jpp7
- new release

* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.4-alt3_12jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.4-alt2_12jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1_12jpp7
- fixed requires for antlr3-java

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1_11jpp7
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_10jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_9jpp6
- new version

