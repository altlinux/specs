Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ perl(Digest.pm) perl(English.pm) perl(Error.pm) perl(Exception/Class.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Slurp.pm) perl(File/Spec/Unix.pm) perl(FindBin.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Moose.pm) perl(Moose/Role.pm) perl(Moose/Util/TypeConstraints.pm) perl(Params/Validate.pm) perl(Readonly.pm) perl(Switch.pm) perl(Test/Builder/Module.pm) perl(Test/Class/Load.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(UNIVERSAL.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(blib.pm) perl(overload.pm) perl-devel unzip
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global antlr_version 3.5.2
%global c_runtime_version 3.4
%global javascript_runtime_version 3.1
%global baserelease 11

Summary:            ANother Tool for Language Recognition
Name:               antlr3
Version:            %{antlr_version}
Release:            alt1_11jpp8
Epoch:              1
URL:                http://www.antlr3.org/
Source0:            https://github.com/antlr/antlr3/archive/%{antlr_version}.tar.gz
#Source2:            http://www.antlr3.org/download/Python/antlr_python_runtime-%{python_runtime_version}.tar.gz
Source3:            http://www.antlr3.org/download/antlr-javascript-runtime-%{javascript_runtime_version}.zip
Patch0:             0001-java8-fix.patch

# Generate OSGi metadata
Patch1:         osgi-manifest.patch

License:            BSD

BuildRequires:      maven-local
BuildRequires:      maven-plugin-bundle
BuildRequires:      maven-surefire-provider-junit
BuildRequires:      junit
BuildRequires:      tomcat-servlet-3.1-api
BuildRequires:      stringtemplate4
BuildRequires:      stringtemplate
BuildRequires:      antlr3-tool

BuildRequires:      autoconf-common
BuildRequires:      automake-common
BuildRequires:      libtool-common

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
Requires:    %{name}-java = %{epoch}:%{antlr_version}

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
Requires:  %{name}-C = %{epoch}:%{c_runtime_version}
Version:   %{c_runtime_version}


%description C-devel
Header files for the C bindings for ANTLR-generated parsers

%package        C-docs
Group: Development/Java
Summary:        API documentation for the C run-time support for ANTLR-generated parsers
BuildArch:      noarch
BuildRequires: graphviz libgraphviz
BuildRequires:  doxygen
Requires:       %{name}-C = %{epoch}:%{c_runtime_version}
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
%setup -q -n antlr3-%{antlr_version} -a 3
sed -i "s,\${buildNumber},`cat %{_sysconfdir}/fedora-release` `date`," tool/src/main/resources/org/antlr/antlr.properties
%patch0 -p1
%patch1

# remove pre-built artifacts
find -type f -a -name *.jar -delete
find -type f -a -name *.class -delete

%pom_disable_module antlr3-maven-archetype
%pom_disable_module gunit
%pom_disable_module gunit-maven-plugin
%pom_disable_module antlr-complete

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

# compile for target 1.6, see BZ#842572
sed -i 's/jsr14/1.6/' antlr3-maven-archetype/src/main/resources/archetype-resources/pom.xml \
                      antlr3-maven-plugin/pom.xml \
                                          gunit/pom.xml \
                                          gunit-maven-plugin/pom.xml \
                                          pom.xml \
                                          runtime/Java/pom.xml \
                                          tool/pom.xml

# workarounds bug in filtering (Mark invalid)
%pom_xpath_remove pom:resource/pom:filtering

%mvn_package :antlr-runtime java
%mvn_package : tool

%mvn_file :antlr antlr3
%mvn_file :antlr-runtime antlr3-runtime
%mvn_file :antlr-maven-plugin antlr3-maven-plugin

%build
%mvn_build -f

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
make %{?_smp_mflags}
doxygen -u # update doxygen configuration file
doxygen # build doxygen documentation
popd

# build ant task
pushd antlr-ant/main/antlr3-task/
export CLASSPATH=$(build-classpath ant)
javac -encoding ISO-8859-1 antlr3-src/org/apache/tools/ant/antlr/ANTLR3.java
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
%jpackage_script org.antlr.Tool '' '' 'stringtemplate4.jar:antlr3.jar:antlr3-runtime.jar' antlr3 true

# install C runtime
pushd runtime/C
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_libdir}/libantlr3c.{a,la}
pushd api/man/man3
for file in `ls -1 * | grep -vi "^antlr3"`; do
    mv $file antlr3-$file
done
sed -i -e 's,^\.so man3/pANTLR3,.so man3/antlr3-pANTLR3,' `grep -rl 'man3/pANTLR3' .`
gzip *
popd
mv api/man/man3 $RPM_BUILD_ROOT%{_mandir}/
rmdir api/man
popd

# install javascript runtime
pushd antlr-javascript-runtime-%{javascript_runtime_version}
install -pm 644 *.js $RPM_BUILD_ROOT%{_datadir}/antlr/
popd

# install C++ runtime (header only)
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/%{name}
install -pm 644 runtime/Cpp/include/* $RPM_BUILD_ROOT/%{_includedir}/

rm -f runtime/C/api/*.png

%files tool -f .mfiles-tool
%doc README.txt tool/{LICENSE.txt,CHANGES.txt}
%{_bindir}/antlr3
%{_javadir}/ant/ant-antlr3.jar
%config(noreplace) %{_sysconfdir}/ant.d/ant-antlr3

%files C
%doc tool/LICENSE.txt
%{_libdir}/libantlr3c.so

%files C-devel
%{_mandir}/man3/*
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

