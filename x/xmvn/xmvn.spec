Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# XMvn uses OSGi environment provided by Tycho, it shouldn't require
# any additional bundles.


# Integration tests are disabled by default, but you can run them by
# adding "--with its" to rpmbuild or mock invocation.
#def_with its
%bcond_with its

Name:           xmvn
Version:        2.5.0
Release:        alt1_6jpp8
Summary:        Local Extensions for Apache Maven
License:        ASL 2.0
URL:            http://mizdebsk.fedorapeople.org/xmvn
BuildArch:      noarch

Source0:        https://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.xz

Patch0:         0001-Copy-core-dependencies-to-lib-core-in-assembly.patch
Patch1:         0002-Try-to-procect-builddep-MOJO-against-patological-cas.patch

BuildRequires:  maven >= 3.3.9
BuildRequires:  maven-local
BuildRequires:  beust-jcommander
BuildRequires:  cglib
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-plugin-build-helper
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  objectweb-asm
BuildRequires:  modello
BuildRequires:  xmlunit
BuildRequires:  apache-ivy
BuildRequires:  sisu-mojos
BuildRequires:  junit
BuildRequires:  gradle >= 2.5

Requires:       maven >= 3.2.5
Requires:       xmvn-api = %{version}
Requires:       xmvn-connector-aether = %{version}
Requires:       xmvn-core = %{version}
Source44: import.info
%filter_from_requires /^osgi\\($/d

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

%package        parent-pom
Group: Development/Java
Summary:        XMvn Parent POM

%description    parent-pom
This package provides XMvn parent POM.

%package        api
Group: Development/Java
Summary:        XMvn API

%description    api
This package provides XMvn API module which contains public interface
for functionality implemented by XMvn Core.

%package        launcher
Group: Development/Java
Summary:        XMvn Launcher

%description    launcher
This package provides XMvn Launcher module, which provides a way of
launching XMvn running in isolated class realm and locating XMVn
services.

%package        core
Group: Development/Java
Summary:        XMvn Core

%description    core
This package provides XMvn Core module, which implements the essential
functionality of XMvn such as resolution of artifacts from system
repository.

%package        connector-aether
Group: Development/Java
Summary:        XMvn Connector for Eclipse Aether

%description    connector-aether
This package provides XMvn Connector for Eclipse Aether, which
provides integration of Eclipse Aether with XMvn.  It provides an
adapter which allows XMvn resolver to be used as Aether workspace
reader.

%package        connector-gradle
Group: Development/Java
Summary:        XMvn Connector for Gradle

%description    connector-gradle
This package provides XMvn Connector for Gradle, which provides
integration of Gradle with XMvn.  It provides an adapter which allows
XMvn resolver to be used as Gradle resolver.

%package        connector-ivy
Group: Development/Java
Summary:        XMvn Connector for Apache Ivy

%description    connector-ivy
This package provides XMvn Connector for Apache Ivy, which provides
integration of Apache Ivy with XMvn.  It provides an adapter which
allows XMvn resolver to be used as Ivy resolver.

%package        mojo
Group: Development/Java
Summary:        XMvn MOJO

%description    mojo
This package provides XMvn MOJO, which is a Maven plugin that consists
of several MOJOs.  Some goals of these MOJOs are intended to be
attached to default Maven lifecycle when building packages, others can
be called directly from Maven command line.

%package        tools-pom
Group: Development/Java
Summary:        XMvn Tools POM

%description    tools-pom
This package provides XMvn Tools parent POM.

%package        resolve
Group: Development/Java
Summary:        XMvn Resolver

%description    resolve
This package provides XMvn Resolver, which is a very simple
commald-line tool to resolve Maven artifacts from system repositories.
Basically it's just an interface to artifact resolution mechanism
implemented by XMvn Core.  The primary intended use case of XMvn
Resolver is debugging local artifact repositories.

%package        bisect
Group: Development/Java
Summary:        XMvn Bisect

%description    bisect
This package provides XMvn Bisect, which is a debugging tool that can
diagnose build failures by using bisection method.

%package        subst
Group: Development/Java
Summary:        XMvn Subst

%description    subst
This package provides XMvn Subst, which is a tool that can substitute
Maven artifact files with symbolic links to corresponding files in
artifact repository.

%package        install
Group: Development/Java
Summary:        XMvn Install

%description    install
This package provides XMvn Install, which is a command-line interface
to XMvn installer.  The installer reads reactor metadata and performs
artifact installation according to specified configuration.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%mvn_package ":xmvn{,-it}" __noinstall

%if %{without its}
%pom_disable_module xmvn-it
%endif

# remove dependency plugin maven-binaries execution
# we provide apache-maven by symlink
%pom_xpath_remove "pom:executions/pom:execution[pom:id[text()='maven-binaries']]"

# get mavenVersion that is expected
mver=$(sed -n '/<mavenVersion>/{s/.*>\(.*\)<.*/\1/;p}' \
           xmvn-parent/pom.xml)
mkdir -p target/dependency/
cp -aL %{_datadir}/maven target/dependency/apache-maven-$mver

%build
# ITs require artifacts to be insalled in local repo
%mvn_build -s -j -g install

tar --delay-directory-restore -xvf target/*tar.bz2
chmod -R +rwX %{name}-%{version}*
# These are installed as doc
rm -Rf %{name}-%{version}*/{AUTHORS,README,LICENSE,NOTICE}


%install
%mvn_install

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -r %{name}-%{version}*/* %{buildroot}%{_datadir}/%{name}/
ln -sf %{_datadir}/maven/bin/mvn %{buildroot}%{_datadir}/%{name}/bin/mvn
ln -sf %{_datadir}/maven/bin/mvnDebug %{buildroot}%{_datadir}/%{name}/bin/mvnDebug
ln -sf %{_datadir}/maven/bin/mvnyjp %{buildroot}%{_datadir}/%{name}/bin/mvnyjp

# helper scripts
install -d -m 755 %{buildroot}%{_bindir}
for tool in subst resolve bisect install;do
    cat <<EOF >%{buildroot}%{_bindir}/%{name}-$tool
#!/bin/sh -e
exec %{_datadir}/%{name}/bin/%{name}-$tool "\${@}"
EOF
    chmod +x %{buildroot}%{_bindir}/%{name}-$tool
done

# copy over maven lib directory
cp -r %{_datadir}/maven/lib/* %{buildroot}%{_datadir}/%{name}/lib/

# possibly recreate symlinks that can be automated with xmvn-subst
%{name}-subst %{buildroot}%{_datadir}/%{name}/

# /usr/bin/xmvn script
cat <<EOF >%{buildroot}%{_bindir}/%{name}
#!/bin/sh -e
export M2_HOME="\${M2_HOME:-%{_datadir}/%{name}}"
exec mvn "\${@}"
EOF

# mvn-local symlink
ln -s %{name} %{buildroot}%{_bindir}/mvn-local

# make sure our conf is identical to maven so yum won't freak out
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf/
cp -P %{_datadir}/maven/conf/settings.xml %{buildroot}%{_datadir}/%{name}/conf/
cp -P %{_datadir}/maven/bin/m2.conf %{buildroot}%{_datadir}/%{name}/bin/
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

%files
%attr(755,-,-) %{_bindir}/%{name}
%attr(755,-,-) %{_bindir}/mvn-local
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/*.jar
%{_datadir}/%{name}/lib/ext
%{_datadir}/%{name}/bin/m2.conf
%{_datadir}/%{name}/bin/mvn
%{_datadir}/%{name}/bin/mvnDebug
%{_datadir}/%{name}/bin/mvnyjp
%{_datadir}/%{name}/bin/xmvn
%{_datadir}/%{name}/boot
%{_datadir}/%{name}/conf

%files parent-pom -f .mfiles-xmvn-parent
%doc LICENSE NOTICE

%files launcher -f .mfiles-xmvn-launcher
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/core

%files core -f .mfiles-xmvn-core

%files api -f .mfiles-xmvn-api
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE
%doc AUTHORS README

%files connector-aether -f .mfiles-xmvn-connector-aether

%files connector-gradle -f .mfiles-xmvn-connector-gradle

%files connector-ivy -f .mfiles-xmvn-connector-ivy
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/ivy

%files mojo -f .mfiles-xmvn-mojo

%files tools-pom -f .mfiles-xmvn-tools

%files resolve -f .mfiles-xmvn-resolve
%attr(755,-,-) %{_bindir}/%{name}-resolve
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/bin/%{name}-resolve
%{_datadir}/%{name}/lib/resolver

%files bisect -f .mfiles-xmvn-bisect
%attr(755,-,-) %{_bindir}/%{name}-bisect
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/bin/%{name}-bisect
%{_datadir}/%{name}/lib/bisect

%files subst -f .mfiles-xmvn-subst
%attr(755,-,-) %{_bindir}/%{name}-subst
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/bin/%{name}-subst
%{_datadir}/%{name}/lib/subst

%files install -f .mfiles-xmvn-install
%attr(755,-,-) %{_bindir}/%{name}-install
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/bin/%{name}-install
%{_datadir}/%{name}/lib/installer

%files javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_6jpp8
- unbootstrup build

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_5jpp8
- unbootsrap build

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt4_4jpp7
- rebuild to update symlinks

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt3_4jpp7
- fixed bin
- nobootstrap build

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_5jpp7
- nobootstrap build

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

