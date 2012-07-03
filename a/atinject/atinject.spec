BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 1
%define name atinject
%bcond_without repolib

%global namedversion %{version}

Name:           atinject
Version:        1
Release:        alt3_8jpp6
Epoch:          0
Summary:        Dependency injection specification for Java (JSR-330)
Group:          Development/Java
License:        ASL 2.0
URL:            http://code.google.com/p/atinject/
# svn export -r 86 http://atinject.googlecode.com/svn/tags/1/ atinject-1 && tar cjf atinject-1.tar.bz2 atinject-1
%if 0
XXX: rather than take from
XXX: http://atinject.googlecode.com/svn/tags/javax.inject-tck-1/, we just patch
XXX: the current build, as this woudl rquire creating a separate RPM .spec
%endif
Source0:        %{name}-%{namedversion}.tar.bz2
Patch0:         atinject-tck.patch
Provides:       javax.inject = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
BuildRequires:  apache-commons-parent
BuildRequires:  junit
BuildRequires:  maven2
BuildRequires:  maven2-plugin-deploy
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-compiler
BuildArch:      noarch
Source44: import.info

%description
This package specifies a means for obtaining objects in such a way as
to maximize reusability, testability and maintainability compared to
traditional approaches such as constructors, factories, and service
locators (e.g., JNDI). This process, known as dependency injection, is
beneficial to most nontrivial applications.

%package tck
Summary:        TCK for javax.inject
Group:          Development/Java
Provides:       javax.inject-tck = %{epoch}:%{version}-%{release}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       junit

%description tck
TCK for javax.inject.

%package javadoc
Summary:        API documentation for javax.inject
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for javax.inject.

%package tck-javadoc
Summary:        API documentation for javax.inject-tck
Group:          Development/Java
Requires:       jpackage-utils

%description tck-javadoc
API documentation for javax.inject-tck.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q
%patch0 -p1 -b .sav0

%{__rm} -r lib/ javadoc/
%{__mkdir} lib
%{__ln_s} `%{_bindir}/build-classpath junit` lib/junit.jar

# fix insource
sed -i 's,javac -g,javac -source 1.5 -target 1.5 -g,' build.sh

%build
/bin/sh ./build.sh

%install

# jar files
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/maven/javax.inject-%{namedversion}.jar %{buildroot}%{_javadir}/javax.inject-%{namedversion}.jar
%{__cp} -p build/maven/javax.inject-%{namedversion}-javadoc.jar %{buildroot}%{_javadir}/javax.inject-%{namedversion}-javadoc.jar
%{__cp} -p build/maven/javax.inject-%{namedversion}-sources.jar %{buildroot}%{_javadir}/javax.inject-%{namedversion}-sources.jar
%{__cp} -p build/tck/dist/javax.inject-tck.jar %{buildroot}%{_javadir}/javax.inject-tck-%{namedversion}.jar
%{__cp} -p build/tck/dist/javax.inject-tck-javadoc.zip %{buildroot}%{_javadir}/javax.inject-tck-%{namedversion}-javadoc.jar
%{__cp} -p build/tck/dist/javax.inject-tck-src.zip %{buildroot}%{_javadir}/javax.inject-tck-%{namedversion}-sources.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{namedversion}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-javax.inject.pom
%{__cp} -p tck-pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-javax.inject-tck.pom
%add_to_maven_depmap javax.inject javax.inject %{namedversion} JPP javax.inject
%add_to_maven_depmap javax.inject javax.inject-tck %{namedversion} JPP javax.inject-tck

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/javax.inject-%{namedversion}
%{__cp} -pr build/javadoc/* %{buildroot}%{_javadocdir}/javax.inject-%{namedversion}
%{__ln_s} javax.inject-%{namedversion} %{buildroot}%{_javadocdir}/javax.inject
%{__mkdir_p} %{buildroot}%{_javadocdir}/javax.inject-tck-%{namedversion}
%{__unzip} -qqo build/tck/dist/javax.inject-tck-javadoc.zip -d %{buildroot}%{_javadocdir}/javax.inject-tck-%{namedversion}
%{__ln_s} javax.inject-tck-%{namedversion} %{buildroot}%{_javadocdir}/javax.inject-tck

%if %with repolib
export MAVEN_REPO_LOCAL=`pwd`/.m2/repository
export URL=file://%{buildroot}%{_javadir}/repository.jboss.com/maven2-brew/maven2-brew
export MAVEN_OPTS="-Xms1g -Xmx1g"
%{_bindir}/mvn-jpp deploy:deploy-file -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DpomFile=pom.xml -Dfile=build/maven/javax.inject-%{namedversion}.jar -Durl=${URL} -DrepositoryId=oss-releases
%{_bindir}/mvn-jpp deploy:deploy-file -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DpomFile=pom.xml -Dfile=build/maven/javax.inject-%{namedversion}-javadoc.jar -Dclassifier=javadoc -Durl=${URL} -DrepositoryId=oss-releases
%{_bindir}/mvn-jpp deploy:deploy-file -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DpomFile=pom.xml -Dfile=build/maven/javax.inject-%{namedversion}-sources.jar -Dclassifier=sources -Durl=${URL} -DrepositoryId=oss-releases
%{_bindir}/mvn-jpp deploy:deploy-file -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DpomFile=tck-pom.xml -Dfile=build/tck/dist/javax.inject-tck.jar -Durl=${URL} -DrepositoryId=oss-releases
%{_bindir}/mvn-jpp deploy:deploy-file -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DpomFile=tck-pom.xml -Dfile=build/tck/dist/javax.inject-tck-javadoc.zip -Dclassifier=javadoc -Dpackaing=jar -Durl=${URL} -DrepositoryId=oss-releases
%{_bindir}/mvn-jpp deploy:deploy-file -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DpomFile=tck-pom.xml -Dfile=build/tck/dist/javax.inject-tck-src.zip -Dclassifier=sources -Dpackaing=jar -Durl=${URL} -DrepositoryId=oss-releases
%endif

pushd %buildroot%{_javadir}
ln -s javax.inject.jar atinject.jar
popd

%files
%{_javadir}*/javax.inject-%{namedversion}.jar
%{_javadir}*/javax.inject.jar
%{_javadir}*/javax.inject-%{namedversion}-javadoc.jar
%{_javadir}*/javax.inject-javadoc.jar
%{_javadir}*/javax.inject-%{namedversion}-sources.jar
%{_javadir}*/javax.inject-sources.jar
%{_datadir}/maven2/poms/JPP-javax.inject.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/atinject.jar

%files tck
%{_javadir}*/javax.inject-tck-%{namedversion}.jar
%{_javadir}*/javax.inject-tck.jar
%{_javadir}*/javax.inject-tck-%{namedversion}-javadoc.jar
%{_javadir}*/javax.inject-tck-javadoc.jar
%{_javadir}*/javax.inject-tck-%{namedversion}-sources.jar
%{_javadir}*/javax.inject-tck-sources.jar
%{_datadir}/maven2/poms/JPP-javax.inject-tck.pom

%files javadoc
%{_javadocdir}/javax.inject-%{namedversion}
%{_javadocdir}/javax.inject

%files tck-javadoc
%{_javadocdir}/javax.inject-tck-%{namedversion}
%{_javadocdir}/javax.inject-tck

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt3_8jpp6
- added fc compat symlink %{_javadir}/atinject.jar

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt2_8jpp6
- target 5 build

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_8jpp6
- new jpp relase

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_2.20100611svn86jpp6
- fixed build

