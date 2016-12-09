Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-java
BuildRequires: python3-devel
# END SourceDeps(oneline)
# optional dependencies of jpackage-utils
%filter_from_requires /^.usr.bin.jar/d
%filter_from_requires /^objectweb-asm/d
%define _unpackaged_files_terminate_build 1

BuildRequires: source-highlight python3-module-nose python3-module-setuptools-tests
%add_python3_path /usr/share/java-utils/
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# Don't generate requires on jpackage-utils and java-headless for
# provided pseudo-artifacts: com.sun:tools and sun.jdk:jconsole.
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}/maven-metadata/javapackages-metadata.xml$

# Avoid circular dependency on itself when bootstrapping
%{!?_with_bootstrap: %global bootstrap 0}

%bcond_with tests

Name:           javapackages-tools
Version:        4.6.0
Release:        alt10_14jpp8

Summary:        Macros and scripts for Java packaging support

License:        BSD
URL:            https://git.fedorahosted.org/git/javapackages.git
Source0:        https://fedorahosted.org/released/javapackages/javapackages-%{version}.tar.xz

Patch0:         0001-Initial-gradle_build-implementation.patch
Patch1:         0002-install-Move-mvn_build-and-builddep-from-maven-local.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires: asciidoc asciidoc-a2x
BuildRequires:  xmlto
BuildRequires:  dia
%if ! 0%{?bootstrap}
BuildRequires:  maven-local >= 4.0.0
BuildRequires:  xmvn-resolve >= 2
%endif

Requires:       coreutils
Requires:       findutils
Requires:       lua

Provides:       jpackage-utils = %{version}-%{release}
Source44: import.info
Source45: osgi-fc.prov.files
Source46: maven.prov.files
Source47: maven.env
Patch33: javapackages-tools-4.6.0-alt-use-enviroment.patch
Patch34: javapackages-tools-4.6.0-alt-req-headless-off.patch
Patch35: javapackages-tools-4.6.0-alt-shade-jar.patch
Patch36: macros.fjava-to-alt-rpm404.patch
Patch37: macros.jpackage-alt-script.patch

Conflicts:       jpackage-utils < 0:5.0.1
Obsoletes:       jpackage-utils < 0:5.0.1
Provides:       jpackage-utils = 1:5.0.0

%description
This package provides macros and scripts to support Java packaging.

%package -n rpm-macros-java
Summary: RPM helper macros to build Java packages
Group: Development/Java
Conflicts: rpm-build-java < 0:5.0.0-alt34
# comment if jnidir patch is used
BuildArch:      noarch

%description -n rpm-macros-java
These helper macros facilitate creation of RPM packages containing Java
bytecode archives and Javadoc documentation.

%package -n rpm-build-java
Summary: RPM build helpers for Java packages
Group: Development/Java
BuildArch:      noarch
Requires:       javapackages-tools = %{epoch}:%{version}-%{release}
Requires: 	rpm-macros-java >= %{epoch}:%{version}-%{release}
#Requires: rpm-build-java-osgi >= %{epoch}:%{version}-%{release}
# moved from main package; not for runtime
Requires:       python3-module-javapackages = %{epoch}:%{version}-%{release}
Requires:       python3

%description -n rpm-build-java
RPM build helpers for Java packages.



%package -n maven-local
Group: Development/Java
Summary:        Macros and scripts for Maven packaging support
Requires:       maven-local = %{version}
Requires:       javapackages-local = %{version}
Requires:       maven
Requires:       xmvn >= 2
Requires:       xmvn-mojo >= 2
Requires:       xmvn-connector-aether >= 2
# POM files needed by maven itself
Requires:       apache-commons-parent
Requires:       apache-parent
Requires:       geronimo-parent-poms
Requires:       httpcomponents-project
Requires:       jboss-parent
Requires:       jvnet-parent
Requires:       maven-parent
Requires:       maven-plugins-pom
Requires:       mojo-parent
Requires:       objectweb-pom
Requires:       plexus-components-pom
Requires:       plexus-pom
Requires:       sonatype-oss-parent
Requires:       weld-parent
# Common Maven plugins required by almost every build. It wouldn't make
# sense to explicitly require them in every package built with Maven.
Requires:       maven-assembly-plugin
Requires:       maven-compiler-plugin
Requires:       maven-enforcer-plugin
Requires:       maven-jar-plugin
Requires:       maven-javadoc-plugin
Requires:       maven-resources-plugin
Requires:       maven-surefire-plugin
# Tests based on JUnit are very common and JUnit itself is small.
# Include JUnit provider for Surefire just for convenience.
Requires:       maven-surefire-provider-junit
# testng is quite common as well
Requires:       maven-surefire-provider-testng

%description -n maven-local
This package provides macros and scripts to support packaging Maven artifacts.

%package -n gradle-local
Group: Development/Java
Summary:        Local mode for Gradle
Requires:       maven-local = %{version}
Requires:       javapackages-local = %{version}
Requires:       gradle >= 2.2.1
Requires:       xmvn-connector-gradle >= 2

%description -n gradle-local
This package implements local mode for Gradle, which allows artifact
resolution using XMvn resolver.

%package -n ivy-local
Group: Development/Java
Summary:        Local mode for Apache Ivy
Requires:       maven-local = %{version}
Requires:       javapackages-local = %{version}
Requires:       apache-ivy >= 2.3.0
Requires:       xmvn-connector-ivy >= 2

%description -n ivy-local
This package implements local mode for Apache Ivy, which allows
artifact resolution using XMvn resolver.

%package -n python3-module-javapackages
Group: Development/Java
Summary:        Module for handling various files for Java packaging
Requires:       python3-module-lxml
Requires:       python3-module-six
Obsoletes:      python-javapackages < %{version}-%{release}

%description -n python3-module-javapackages
Module for handling, querying and manipulating of various files for Java
packaging in Linux distributions

%package doc
Group: Development/Java
Summary:        Guide for Java packaging

%description doc
User guide for Java packaging and using utilities from javapackages-tools

%package -n javapackages-local
Group: Development/Java
Summary:        Non-essential macros and scripts for Java packaging support
Requires:       maven-local = %{version}
Requires:       xmvn-install >= 2
Requires:       xmvn-subst >= 2
Requires:       xmvn-resolve >= 2
# Java build systems don't have hard requirement on java-devel, so it should be there

%description -n javapackages-local
This package provides non-essential macros and scripts to support Java packaging.

%prep
%setup -q -n javapackages-%{version}
%patch0 -p1
%patch1 -p1

sed -i '/fedora-review/d' install
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1

# alt specific shabang
sed -i -e 1,1s,/bin/bash,/bin/sh, java-utils/java-wrapper bin/*


%build
%configure --pyinterpreter=%{__python3}
./build

%install
./install
sed -e 's/.[17]$/&.*/' -e 's/.py$/&*/' -i files-*

pushd python
  %{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd

install -m755 -D %{SOURCE46} %buildroot/usr/lib/rpm/maven.prov.files
install -m755 -D %{SOURCE46} %buildroot/usr/lib/rpm/maven.req.files

install -m755 -D %{SOURCE46} %buildroot/usr/lib/rpm/javadoc.req.files
sed -i -e s,/usr/share/maven-metadata/,/usr/share/javadoc/, %buildroot/usr/lib/rpm/javadoc.req.files

install -m755 -D %{SOURCE45} %buildroot/usr/lib/rpm/osgi-fc.prov.files
install -m755 -D %{SOURCE45} %buildroot/usr/lib/rpm/osgi-fc.req.files

chmod 755 %buildroot/usr/lib/rpm/*.req* %buildroot/usr/lib/rpm/*.prov*
sed -i -e 's,^#!python,#!/usr/bin/python,' %buildroot/usr/lib/rpm/*.req* %buildroot/usr/lib/rpm/*.prov*

install -m755 -D %{SOURCE47} %buildroot%_rpmmacrosdir/maven.env

# in rpm-build-java
sed -i -e '/usr\/lib\/rpm/d' files-common
# move /usr/share/xmvn/* to maven-local
grep /usr/share/xmvn files-common >> files-maven
sed -i -e '/usr\/share\/xmvn/d' files-common
sed -i -e '/usr\/share\/java-utils\/.*\.py/d' files-common
sed -i -e '/usr\/bin\/xmvn-builddep/d' files-common

rm -rf %buildroot/usr/lib/rpm/fileattrs

pushd %buildroot%_rpmmacrosdir/
mv macros.fjava javapackages-fjava
mv macros.jpackage javapackages-jpackage
popd

pushd %buildroot/usr/lib/rpm/
mv osgi.prov osgi-fc.prov
mv osgi.req osgi-fc.req
popd



%if %{with tests}
%check
./check
%endif

%files -f files-common

%files -n javapackages-local -f files-local

%_datadir/java-utils/__pycache__
%exclude %_datadir/java-utils/__pycache__/maven_depmap.*
%exclude %_datadir/java-utils/__pycache__/pom_editor.*
%exclude %_datadir/java-utils/__pycache__/request-artifact.*


%files -n maven-local -f files-maven

%files -n gradle-local -f files-gradle

%files -n ivy-local -f files-ivy

%files -n python3-module-javapackages
%doc LICENSE
%{python3_sitelibdir_noarch}/javapackages*

%files doc -f files-doc
%doc LICENSE

%files -n rpm-macros-java
%_rpmmacrosdir/javapackages-fjava
%_rpmmacrosdir/javapackages-jpackage

%files -n rpm-build-java
/usr/lib/rpm/maven.*
/usr/lib/rpm/javadoc.*
/usr/lib/rpm/osgi-fc.*
%_rpmmacrosdir/maven.env
%_datadir/java-utils/maven_depmap.py
%_datadir/java-utils/pom_editor.py
%_datadir/java-utils/request-artifact.py
%_bindir/xmvn-builddep
%_datadir/java-utils/__pycache__/maven_depmap.*
%_datadir/java-utils/__pycache__/pom_editor.*
%_datadir/java-utils/__pycache__/request-artifact.*


%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt10_14jpp8
- update

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.6.0-alt9_12jpp8.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.6.0-alt9_12jpp8.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt9_12jpp8
- temporatily disabled gradle patch

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt8_12jpp8
- %%_jnidir set to /usr/lib/java

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt7_12jpp8
- fixes in shade-jar (javapackages-tools-4.6.0-alt-shade-jar.patch)

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt6_12jpp8
- enabled gradle-local

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt5_12jpp8
- fixes in fjava macros

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt4_12jpp8
- fixes in script patch

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt3_12jpp8
- fixes in script macro

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt2_12jpp8
- explicitly cleaned jar dependency
- moved python to rpm-build-java

* Thu Jan 14 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt1_12jpp8
- new version

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.6.0-alt1_11jpp7
- new version

