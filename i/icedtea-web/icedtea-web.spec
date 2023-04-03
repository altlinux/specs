%define _unpackaged_files_terminate_build 1

%define oldname icedtea-web
#can rust have debuginfo? Verify and fix! Likely issue in Makefile of itw.
%global debug_package %{nil}

# Version of java we run against
%define javaver 11
# Version of java we build by
%define buildjavaver 11

# Alternatives priority (rised by one number when jre bumped to 11 (as 11 < 18 :)
%define priority 110000
# jnlp prorocol gnome registry keys
%define gurlhandler    /desktop/gnome/url-handlers
%define jnlphandler    %{gurlhandler}/jnlp
%define jnlpshandler   %{gurlhandler}/jnlps

%define jredir         %{_jvmdir}/jre-%{javaver}-openjdk

%define preffered_jre  java-%{javaver}-openjdk
%define preffered_jdk  java-%{buildjavaver}-openjdk-devel

Name:		icedtea-web
Version:	2.0.0
Release:	alt3_pre.0.1.alpha26.patched1.3jpp11

Summary:	Additional Java components for OpenJDK - Java Web Start implementation
Group:      Networking/WWW
License:    LGPLv2+ and GPLv2 with exceptions
URL:        https://github.com/AdoptOpenJDK/IcedTea-Web

Source:     %name-%version.tar

Patch0:     patchOutDunce.patch
Patch1:     launchersPhase.patch
Patch33:    translation-desktop-files.patch

BuildRequires(pre): rpm-macros-java
BuildRequires:  /proc rpm-build-java
BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  %{preffered_jdk}
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:	rust
BuildRequires:	rust-cargo
BuildRequires:	libappstream-glib
BuildRequires:  junit
BuildRequires:  maven
BuildRequires:  hamcrest
BuildRequires:  tagsoup
BuildRequires:  maven-local
BuildRequires:  maven-source-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  exec-maven-plugin
BuildRequires:  hamcrest
BuildRequires:  hamcrest-core
BuildRequires:  rhino
BuildRequires:  IPAddress
#BuildRequires:  maven-javadoc-plugin

# For functionality and the OpenJDK dirs
Requires:      %{preffered_jre}
Requires:      javapackages-tools
Requires:      rhino
Requires:      IPAddress
Requires:      tagsoup

#maven fragments
Requires(post):      javapackages-tools
Requires(postun):    javapackages-tools

%description
The IcedTea-Web project provides a an implementation of Java Web Start
(originally based on the Netx project, now opensource part of OpenWebStart)
and a settings tool to manage deployment settings for the aforementioned 
Web Start implementations. 

%package javaws
Summary:    Java Web Start launcher
Group:      Networking/Other

Provides:   javaws = %{javaver}
Provides:   %{preffered_jre}-javaws = %{javaver}
Provides:   mozilla-plugin-java-1.8.0-openjdk
Obsoletes:  mozilla-plugin-java-1.7.0-openjdk
Obsoletes:  mozilla-plugin-java-1.8.0-openjdk

Requires:   %{name} = %{version}-%{release}
# Post requires alternatives to install tool alternatives.
# jnlp protocols support
Requires(post):   GConf libGConf
# Postun requires alternatives to uninstall tool alternatives.
# jnlp protocols support
Requires(postun):   GConf libGConf
Requires(post,preun): alternatives

%description javaws
Java Web Start is a deployment solution for Java-technology-based
applications. It is the plumbing between the computer and the Internet
that allows the user to launch and manage applications right off the
Web. Java Web Start provides easy, one-click activation of
applications, and guarantees that you are always running the latest
version of the application, eliminating complicated installation or
upgrade procedures.


%package javadoc
Group: Development/Java
Summary:    API documentation for IcedTea-Web
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description javadoc
This package contains Javadocs for the IcedTea-Web project.


%package devel
Group: Development/Java
Summary:    pure sources for debugging IcedTea-Web
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description devel
This package contains ziped sources of the IcedTea-Web project.

%prep
%setup -q
%patch0 -p1
dos2unix launchers/pom.xml
%patch1 -p0

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-surefire-plugin
%pom_add_plugin org.apache.maven.plugins:maven-install-plugin:2.5.2
%pom_remove_dep junit:junit common/pom.xml
%pom_remove_dep org.hamcrest:hamcrest common/pom.xml

%pom_remove_dep org.hamcrest:hamcrest test-extensions/pom.xml
%pom_remove_dep net.jcip:jcip-annotations test-extensions/pom.xml
%pom_remove_dep com.github.stefanbirkner:system-rules test-extensions/pom.xml

%pom_remove_dep com.github.vatbub:mslinks core/pom.xml
%pom_remove_dep org.hamcrest:hamcrest integration/pom.xml
%pom_remove_dep com.github.tomakehurst:wiremock-jre8 integration/pom.xml
%pom_remove_dep com.github.stefanbirkner:system-rules integration/pom.xml

# TODO: Add Javadoc support
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin common/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin core/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin test-extensions/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin xml-parser/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin pom.xml

rm -v core/src/main/java/net/sourceforge/jnlp/util/WindowsDesktopEntry.java
rm -r integration/src
%patch33 -p2

%build
rm -rf launchers/build.log
SPLASH_TARGET_DIR=%{_datadir}/%name \
ITW_TARGET_DIR=%{_datadir}/%name \
BIN_TARGET_DIR=%{_libexecdir}/%name \
ETC_TARGET_DIR=%{_sysconfdir}/java/%name \
ITW_LIBS=DISTRIBUTION \
JRE=%jredir \
%mvn_build --skip-javadoc -- -Plaunchers -Dmaven.test.skip=true -Dmaven.javadoc.skip=true || cat launchers/build.log

%install
%mvn_install

#not installing all, itw is comlex maven project, wfrom which we need onlythe finall jar, without system deps
#%mvn_artifact pom.xml launchers/target/usr/share/icedtea-web/javaws.jar

mkdir -p %buildroot%{_libexecdir}/%{name}
# build provides also .bat files, we do not want them
cp -v launchers/target/%{_libexecdir}/%{name}/javaws %buildroot%{_libexecdir}/%{name}/
cp -v launchers/target/%{_libexecdir}/%{name}/itweb-settings %buildroot%{_libexecdir}/%{name}/
cp -v launchers/target/%{_libexecdir}/%{name}/policyeditor %buildroot%{_libexecdir}/%{name}/
cp -v launchers/target/%{_libexecdir}/%{name}/javaws.sh %buildroot%{_libexecdir}/%{name}/
cp -v launchers/target/%{_libexecdir}/%{name}/itweb-settings.sh %buildroot%{_libexecdir}/%{name}/
cp -v launchers/target/%{_libexecdir}/%{name}/policyeditor.sh %buildroot%{_libexecdir}/%{name}/

mkdir -p %buildroot%{_sysconfdir}/java/%{name}/
cp -v launchers/target/%{_sysconfdir}/java/%{name}/itw-modularjdk.args %buildroot%{_sysconfdir}/java/%{name}/

mkdir -p %buildroot%{_datadir}/%{name}
cp -v launchers/target/%{_datadir}/%{name}/javaws_splash.png %buildroot%{_datadir}/%{name}/javaws_splash.png

mkdir -p %buildroot%{_datadir}/bash-completion/completions/
cp -v launchers/target/extensions/bash_completion.d/* %buildroot%{_datadir}/bash-completion/completions/

mkdir -p %buildroot/%{_mandir}/
cp -r launchers/target/icedtea-web-docs/%version-*/man/* %buildroot/%{_mandir}/
# rename javaws so it can coexists with other implementations
mv %buildroot/%{_mandir}/man1/javaws.1 %buildroot/%{_mandir}/man1/javaws.itweb.1
mv %buildroot/%{_mandir}/cs/man1/javaws.1 %buildroot/%{_mandir}/cs/man1/javaws.itweb.1
mv %buildroot/%{_mandir}/de/man1/javaws.1 %buildroot/%{_mandir}/de/man1/javaws.itweb.1
mv %buildroot/%{_mandir}/pl/man1/javaws.1 %buildroot/%{_mandir}/pl/man1/javaws.itweb.1

rm -rf %buildroot%_mandir/man1/%name-plugin.1
rm -rf %buildroot%_mandir/*/man1/%name-plugin.1

# Install desktop files.
install -d -m 755 %buildroot%{_datadir}/{applications,pixmaps}
desktop-file-install --vendor '' --dir %buildroot%{_datadir}/applications launchers/target/extensions/xdesktop/javaws.desktop
desktop-file-install --vendor '' --dir %buildroot%{_datadir}/applications launchers/target/extensions/xdesktop/itweb-settings.desktop
desktop-file-install --vendor '' --dir %buildroot%{_datadir}/applications launchers/target/extensions/xdesktop/policyeditor.desktop
cp launchers/target/libs/javaws.png %buildroot%{_datadir}/pixmaps

# install MetaInfo file for javaws
DESTDIR=%{buildroot} appstream-util install launchers/metadata/%{name}-javaws.appdata.xml

pushd %{buildroot}%{_datadir}/%{name}
ln -s ../java/%{name}/%{name}-all-dependencies.jar javaws.jar
popd

mkdir -p %{buildroot}%{_sysconfdir}/.java/deployment
echo "deployment.jre.dir=%{jredir}" > %{buildroot}%{_sysconfdir}/.java/deployment/deployment.properties

%find_lang %{name} --all-name --with-man


##################################################
# --- alt linux specific, shared with openjdk ---#
##################################################
install -d %buildroot%_altdir
%__cat <<EOF >>%buildroot%_altdir/%name-javaws
%_bindir/javaws	%_libexecdir/%name/javaws	10
%_man1dir/javaws.1.gz	%_man1dir/javaws.itweb.1.gz	10
%_bindir/itweb-settings	%_libexecdir/%name/itweb-settings 10
%_bindir/policyeditor	%_libexecdir/%name/policyeditor 10
EOF

##################################################
# - END alt linux specific, shared with openjdk -#
##################################################

%files
%{_mavenpomdir}/*
%{_datadir}/java/*
%{_datadir}/maven-metadata/*
%doc README.md CONTRIBUTING.md
%doc --no-dereference LICENSE LICENCE_DETAILS.md

%files javaws -f %{name}.lang
%{_datadir}/bash-completion/completions/*
%dir %{_sysconfdir}/java/%{name}
%config(noreplace) %{_sysconfdir}/java/%{name}/itw-modularjdk.args
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_sysconfdir}/.java/deployment/*
%{_datadir}/applications/*
%{_datadir}/man/man1/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.xml
%doc README.md CONTRIBUTING.md
%doc --no-dereference LICENSE LICENCE_DETAILS.md
# alt linux specific
%_altdir/%name-javaws

%changelog
* Tue Mar 28 2023 Andrey Limachko <liannnix@altlinux.org> 2.0.0-alt3_pre.0.1.alpha26.patched1.3jpp11
- new version
- spec file refactored
- package renamed

* Mon Jun 14 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt2_pre.0.3.alpha16.patched1.3jpp8
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1_pre.2.alpha13.patched1jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_3jpp8
- new version

* Tue Jun 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2jpp8
- restored Ivan Razzhivin patches

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_1jpp8
- new version

* Wed Jan 09 2019 Ivan Razzhivin <underwit@altlinux.org> 1.7.1-alt5_6jpp8
- fix russian translation

* Fri Dec 07 2018 Ivan Razzhivin <underwit@altlinux.org> 1.7.1-alt4_6jpp8
- add russian translation to desktop files

* Thu Nov 15 2018 Ivan Razzhivin <underwit@altlinux.org> 1.7.1-alt3_6jpp8
- add russian translation

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2_6jpp8
- fixed alternatives

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_6jpp8
- fixed icons in desktop files

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_5jpp8
- new version

* Sat Apr 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt3_1jpp8
- removed fedora-based alternative (closes: #32043)

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_1jpp8
- fixed requires

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1jpp8
- new version

