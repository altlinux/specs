Name: gradle
Version: 1.0
Summary: Groovy based build system
License: ASL 2.0
Url: http://www.gradle.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/bash
Requires: /bin/sh
Requires: /bin/sh
Requires: /bin/sh
Requires: /bin/sh
Requires: aether
Requires: ant
Requires: ant-antlr
Requires: antlr
Requires: antlr-tool
Requires: apache-commons-beanutils
Requires: apache-commons-cli
Requires: apache-commons-codec
Requires: apache-commons-collections
Requires: apache-commons-io
Requires: apache-commons-lang
Requires: apache-ivy
Requires: aqute-bnd
Requires: aqute-bndlib
Requires: beust-jcommander
Requires: bouncycastle
Requires: bouncycastle-pg
Requires: bsh
Requires: checkstyle
Requires: dom4j
Requires: findbugs
Requires: findbugs-bcel
Requires: groovy
Requires: guava
Requires: hamcrest
Requires: httpcomponents-client
Requires: httpcomponents-core
Requires: jaffl
Requires: jansi
Requires: java-devel
Requires: jaxen
Requires: jcifs
Requires: jcip-annotations
Requires: jna
Requires: jnr-constants
Requires: jnr-ffi
Requires: jnr-posix
Requires: jpackage-utils
Requires: jsch
Requires: junit
Requires: logback
Requires: maven
Requires: maven-ant-tasks
Requires: objectweb-asm
Requires: plexus-classworlds
Requires: plexus-component-api
Requires: plexus-container-default
Requires: plexus-containers-component-annotations
Requires: plexus-interpolation
Requires: plexus-utils
Requires: slf4j
Requires: snakeyaml
Requires: testng

BuildArch: noarch
Group: Development/Java
Release: alt1_9jpp
Source: gradle-1.0-13.fc19.cpio

%description
Gradle is a build system written in Groovy. It uses Groovy
also as the language for its build scripts. It has a powerful
multi-project build support. It has a layer on top of Ivy
that provides a build-by-convention integration for Ivy. It
gives you always the choice between the flexibility of Ant
and the convenience of a build-by-convention behavior.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done

%post
/bin/touch --no-create /usr/share/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create /usr/share/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi


%files -f %name-list

%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8%(echo  | tr - . )jpp7
- fc update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7%(echo  | tr - . )jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_0.4.20091127gitjpp7
- new version

