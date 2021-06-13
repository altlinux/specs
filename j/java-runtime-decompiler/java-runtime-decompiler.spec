Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: Application for extraction and decompilation of JVM byte code
Name: java-runtime-decompiler
Version: 4.0
Release: alt1_3jpp11
License: GPLv3
URL: https://github.com/pmikova/java-runtime-decompiler
Source0: https://github.com/pmikova/%{name}/archive/%{name}-%{version}.tar.gz
Source1: java-runtime-decompiler
Source2: java-runtime-decompiler.1
Source3: jrd.desktop
Source4: java-runtime-decompiler8
Patch0: remove_rsyntaxtextarea.patch
Patch1: systemFernflower.patch
Patch2: systemProcyon.patch
Patch3: rsyntaxVersion.patch
BuildArch: noarch
BuildRequires: maven-local
BuildRequires: byteman
BuildRequires: rsyntaxtextarea
BuildRequires: junit5
BuildRequires: ant-junit5
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-clean-plugin
# depends on devel, not runtime (needs tools.jar, javap attach and manyn others)
BuildRequires: java-11-devel
BuildRequires: java-1.8.0-devel
BuildRequires: google-gson
BuildRequires: desktop-file-utils
Requires: fernflower
Requires: procyon-decompiler
Source44: import.info

%description
This application can access JVM memory at runtime,
extract byte code from the JVM and decompile it. 

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package jdk8
Group: Development/Java
Summary: jdk8 comaptible version of %{name}, may miss sme features
Requires: fernflower
Requires: procyon-decompiler

%description jdk8
jdk8 comaptible version of %{name}, may miss sme features.
Eg rich text area is missng or the agent need to be adjusted manually

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p0
sed -i 's,/usr/bin/bash,/bin/bash,;s,^run ,jvm_run ,' %{SOURCE1} %{SOURCE4}

%build
pushd runtime-decompiler
%pom_remove_plugin :maven-jar-plugin
popd

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
pushd runtime-decompiler
%pom_add_dep com.sun:tools
popd
%mvn_build -f --xmvn-javadoc --skip-javadoc --skip-install -- -Plegacy
find | grep .jar$
mv -v ./decompiler_agent/target/decompiler-agent-%{version}.0-SNAPSHOT.jar     ../decompiler-agent8.jarx  #to avoid being mvn installed
mv -v ./runtime-decompiler/target/runtime-decompiler-%{version}.0-SNAPSHOT.jar ../runtime-decompiler8.jarx #to avoid being mvn installed
xmvn clean

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
patch -p1 -R < %{PATCH0}
patch -p0 < %{PATCH3}
pushd runtime-decompiler
%pom_remove_dep com.sun:tools
popd
%mvn_build --xmvn-javadoc -f

%install
%mvn_install
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
install -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
cp -r %{_builddir}/%{name}-%{name}-%{version}/runtime-decompiler/src/plugins/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install                      \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE3}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/java/%{name}-jdk8
cp -v %{_builddir}/decompiler-agent8.jarx $RPM_BUILD_ROOT%{_datadir}/java/%{name}-jdk8/decompiler-agent8.jar
cp -v %{_builddir}/runtime-decompiler8.jarx  $RPM_BUILD_ROOT%{_datadir}/java/%{name}-jdk8/runtime-decompiler8.jar


%files -f .mfiles
%attr(755, root, -) %{_bindir}/java-runtime-decompiler
%{_mandir}/man1/java-runtime-decompiler.1*
# wrappers for decompilers shared with jdk8 subpackage
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/plugins
%config %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.json
%doc --no-dereference LICENSE

%{_datadir}/applications/jrd.desktop

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%files jdk8
%attr(755, root, -) %{_bindir}/java-runtime-decompiler8
%dir %{_datadir}/java/%{name}-jdk8
%{_datadir}/java/%{name}-jdk8/runtime-decompiler8.jar
%{_datadir}/java/%{name}-jdk8/decompiler-agent8.jar
# wrappers for decompilers shared with main
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/plugins
%config %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.json
%doc --no-dereference LICENSE

%changelog
* Sun Jun 13 2021 Igor Vlasenko <viy@altlinux.org> 4.0-alt1_3jpp11
- new version

* Mon Jun 07 2021 Igor Vlasenko <viy@altlinux.org> 3.0-alt2_9jpp9
- use jvm_run

* Mon Oct 12 2020 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_9jpp9
- new version

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_6jpp8
- new version

