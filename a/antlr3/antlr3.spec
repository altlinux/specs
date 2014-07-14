# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: perl(Digest.pm) perl(English.pm) perl(Error.pm) perl(Exception/Class.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Slurp.pm) perl(File/Spec/Unix.pm) perl(FindBin.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Moose.pm) perl(Moose/Role.pm) perl(Moose/Util/TypeConstraints.pm) perl(Params/Validate.pm) perl(Readonly.pm) perl(Switch.pm) perl(Test/Builder/Module.pm) perl(Test/Class/Load.pm) perl(Test/More.pm) perl(UNIVERSAL.pm) perl(YAML/Tiny.pm) perl(blib.pm) perl(overload.pm) perl-devel perl-podlators python-devel unzip
# END SourceDeps(oneline)
BuildRequires: antlr3-java
BuildRequires: /proc
BuildRequires: jpackage-compat
#%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%global with_bootstrap 0

%global antlr_version 3.4
#%global python_runtime_version 3.1.3
%global javascript_runtime_version 3.1

Summary:            ANother Tool for Language Recognition
Name:               antlr3
Version:            %{antlr_version}
Release:            alt2_12jpp7
URL:                http://www.antlr.org/
Source0:            http://www.antlr.org/download/antlr-%{antlr_version}.tar.gz
Source1:            http://www.antlr.org/download/C/libantlr3c-%{antlr_version}.tar.gz
Source2:            http://www.antlr.org/download/Python/antlr_python_runtime-%{python_runtime_version}.tar.gz
Source3:            http://www.antlr.org/download/antlr-javascript-runtime-%{javascript_runtime_version}.zip
Source5:            antlr3
%if %{with_bootstrap}
Source6:            settings.xml
Source7:            http://www.antlr.org/download/antlr-%{antlr_version}.jar
Source8:            http://mirrors.ibiblio.org/pub/mirrors/maven2/org/antlr/antlr3-maven-plugin/%{antlr_version}/antlr3-maven-plugin-%{antlr_version}.jar
%endif
Source9:            antlr-runtime-MANIFEST.MF
License:            BSD
Group:              Development/Java
BuildRequires:      jpackage-utils
BuildRequires:      maven
BuildRequires:      maven-enforcer-plugin
BuildRequires:      maven-plugin-bundle
BuildRequires:      maven-assembly-plugin
BuildRequires:      maven-shared-reporting-impl
BuildRequires:      maven-surefire-provider-junit4
BuildRequires:      buildnumber-maven-plugin
BuildRequires:      junit
BuildRequires:      tomcat-servlet-3.0-api
BuildRequires:      stringtemplate4
BuildRequires:      stringtemplate
BuildRequires:      felix-parent
BuildRequires:      zip
%if ! %{with_bootstrap}
BuildRequires:      antlr3-tool >= 3.2
%endif

# we don't build it now
Obsoletes:       antlr3-gunit < 3.2-15
Source44: import.info

%description
ANother Tool for Language Recognition, is a language tool
that provides a framework for constructing recognizers,
interpreters, compilers, and translators from grammatical
descriptions containing actions in a variety of target languages.

%package     tool
Group:       Development/Java
Summary:     ANother Tool for Language Recognition
BuildArch:   noarch
Requires:    jpackage-utils
Provides:    %{name} = %{antlr_version}-%{release}
Obsoletes:   %{name} < %{antlr_version}-%{release}
Requires:    %{name}-java = %{antlr_version}-%{release}
Requires:    stringtemplate4

%description tool
ANother Tool for Language Recognition, is a language tool
that provides a framework for constructing recognizers,
interpreters, compilers, and translators from grammatical
descriptions containing actions in a variety of target languages.

%package     java
Group:       Development/Java
Summary:     Java run-time support for ANTLR-generated parsers
BuildArch:   noarch
Requires:    stringtemplate4
Requires:    stringtemplate
Requires:    jpackage-utils

%description java
Java run-time support for ANTLR-generated parsers

%package      javascript
Group:        Development/Java
Summary:      Javascript run-time support for ANTLR-generated parsers
Version:      %{javascript_runtime_version}
BuildArch:    noarch

%description  javascript
Javascript run-time support for ANTLR-generated parsers

%package   C
Group:     Development/Java
Summary:   C run-time support for ANTLR-generated parsers

%description C
C run-time support for ANTLR-generated parsers

%package   C-devel
Group:     Development/Java
Summary:   Header files for the C bindings for ANTLR-generated parsers
Requires:  %{name}-C = %{antlr_version}-%{release}

%description C-devel
Header files for the C bindings for ANTLR-generated parsers

%package        C-docs
Group:          Development/Java
Summary:        API documentation for the C run-time support for ANTLR-generated parsers
BuildArch:      noarch
BuildRequires:  graphviz
BuildRequires:  doxygen
Requires:       %{name}-C = %{antlr_version}-%{release}

%description    C-docs
This package contains doxygen documentation with instruction
on how to use the C target in ANTLR and complete API description of the
C run-time support for ANTLR-generated parsers.

#%package        python
#Group:          Development/Libraries
#Summary:        Python run-time support for ANTLR-generated parsers
#BuildRequires:  python-devel
#BuildRequires:  python-setuptools-devel
#BuildArch:      noarch
#Version:        %{python_runtime_version}
#
#%description    python
#Python run-time support for ANTLR-generated parsers

%prep
%setup -q -n antlr-%{antlr_version} -a 1 -a 2 -a 3
%if %{with_bootstrap}
cp %{SOURCE6} settings.xml
%endif
sed -i "s,\${buildNumber},`cat %{_sysconfdir}/fedora-release` `date`," tool/src/main/resources/org/antlr/antlr.properties

sed -i 's:<module>antlr3-maven-archetype</module>::' pom.xml
sed -i 's:<module>gunit</module>::' pom.xml
sed -i 's:<module>gunit-maven-plugin</module>::' pom.xml

# compile for target 1.6, see BZ#842572
sed -i 's/jsr14/1.6/' antlr3-maven-archetype/src/main/resources/archetype-resources/pom.xml \
                      antlr3-maven-plugin/pom.xml \
					  gunit/pom.xml \
					  gunit-maven-plugin/pom.xml \
					  pom.xml \
					  runtime/Java/pom.xml \
					  tool/pom.xml

# remove corrupted files:
rm antlr3-maven-plugin/src/main/java/org/antlr/mojo/antlr3/._*
rm gunit-maven-plugin/src/main/java/org/antlr/mojo/antlr3/._GUnitExecuteMojo.java


%build

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

%if %{with_bootstrap}
# we need antlr3-maven-plugin in place
sed -i -e \
"s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" \
  settings.xml
  sed -i -e \
  "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" \
  settings.xml
  sed -i -e \
  "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" \
  settings.xml
  sed -i -e \
  "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" \
  settings.xml

mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
mkdir -p $MAVEN_REPO_LOCAL/org.antlr/
cp antlr3-maven-plugin/pom.xml $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/JPP-antlr3-maven-plugin.pom
# install prebuilt antlr and antlr3-maven-plugin into repository
# Man, this is hackish. Hold your nose.
cp %{SOURCE7} $MAVEN_REPO_LOCAL/org.antlr/antlr.jar
cp %{SOURCE8} $MAVEN_REPO_LOCAL/org.antlr/antlr3-maven-plugin.jar
%endif

# Build antlr
%if %{with_bootstrap}
mvn-rpmbuild -s $(pwd)/settings.xml -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven.test.skip=true -Dmaven.compile.target=1.6 install
%else
mvn-rpmbuild -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven.test.skip=true -Dmaven.compile.target=1.6 install
%endif

# Build the plugin
pushd antlr3-maven-plugin
mvn-rpmbuild -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven.compile.target=1.6 install javadoc:javadoc
popd

## Build the python runtime
#pushd antlr_python_runtime-%{python_runtime_version}
#%{__python} setup.py build
#popd

# Build the C runtime
pushd libantlr3c-%{antlr_version}-beta4

%configure --disable-abiflags --enable-debuginfo \
%ifarch x86_64 ppc64 s390x sparc64
    --enable-64bit
%else
    %{nil}
%endif

sed -i "s/CFLAGS = .*/CFLAGS = $RPM_OPT_FLAGS/" Makefile
make %{?_smp_mflags}
doxygen -u # update doxygen configuration file
doxygen # build doxygen documentation
popd

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u runtime/Java/target/antlr-runtime-%{antlr_version}.jar META-INF/MANIFEST.MF

%install
mkdir -p $RPM_BUILD_ROOT{%{_javadir},%{_mavenpomdir},%{_bindir},%{_datadir}/antlr,%{_mandir}}

# install maven POMs
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-antlr3-master.pom
%add_maven_depmap JPP-antlr3-master.pom

install -pm 644 runtime/Java/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-antlr3-runtime.pom
install -pm 644 tool/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-antlr3.pom
install -pm 644 antlr3-maven-plugin/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-antlr3-maven-plugin.pom
install -pm 644 gunit-maven-plugin/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-maven-gunit-plugin.pom

# install jars
install -m 644 runtime/Java/target/antlr-runtime-*.jar \
        $RPM_BUILD_ROOT%{_datadir}/java/antlr3-runtime.jar
%add_maven_depmap JPP-antlr3-runtime.pom antlr3-runtime.jar

install -m 644 tool/target/antlr-*.jar \
        $RPM_BUILD_ROOT%{_datadir}/java/antlr3.jar
%add_maven_depmap JPP-antlr3.pom antlr3.jar

install -m 644 antlr3-maven-plugin/target/%{name}-maven-plugin-%{antlr_version}.jar \
        $RPM_BUILD_ROOT%{_datadir}/java/%{name}-maven-plugin.jar
%add_maven_depmap JPP-%{name}-maven-plugin.pom %{name}-maven-plugin.jar

# We disable gunit because it currently fails to build, maybe after upgrade?
#install gunit/target/gunit-%{antlr_version}.jar \
#        $RPM_BUILD_ROOT%{_datadir}/java/gunit.jar

#install -m 644 gunit-maven-plugin/target/maven-gunit-plugin-%{antlr_version}.jar \
#        $RPM_BUILD_ROOT%{_datadir}/java/maven-gunit-plugin.jar
#%%add_maven_depmap JPP-maven-gunit-plugin.pom maven-gunit.plugin.jar


# install wrapper script
install -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/antlr3

## install python runtime
#pushd antlr_python_runtime-%{python_runtime_version}
#%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
#chmod a+x $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/antlr_python_runtime-*
#popd

# install C runtime
pushd libantlr3c-%{antlr_version}-beta4
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

%files tool
%doc tool/{README.txt,LICENSE.txt,CHANGES.txt}
%{_javadir}/antlr3.jar
%{_javadir}/antlr3-maven*.jar
%{_bindir}/antlr3

#%files python
#%doc tool/LICENSE.txt
#%{python_sitelibdir_noarch}/antlr3/*
#%{python_sitelibdir_noarch}/antlr_python_runtime-*

%files C
%doc tool/LICENSE.txt
%{_libdir}/libantlr3c.so

%files C-devel
%{_includedir}/antlr3*
%{_mandir}/man3/*

%files C-docs
%doc libantlr3c-%{antlr_version}-beta4/api/

%files java
%doc tool/LICENSE.txt
%{_javadir}/*runtime*.jar
%{_mavenpomdir}/*.pom
%config %{_mavendepmapfragdir}/antlr3

%files javascript
%doc tool/LICENSE.txt
%{_datadir}/antlr/

%changelog
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

