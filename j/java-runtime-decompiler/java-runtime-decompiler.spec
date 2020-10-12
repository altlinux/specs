Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: Application for extraction and decompilation of JVM byte code
Name: java-runtime-decompiler
Version: 3.0
Release: alt1_9jpp9
License: GPLv3
URL: https://github.com/pmikova/java-runtime-decompiler
Source0: https://github.com/pmikova/%{name}/archive/%{name}-%{version}.tar.gz
Source1: java-runtime-decompiler
Source2: java-runtime-decompiler.1
Source3: jrd.desktop
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
# depends on devel, not runtime (needs tools.jar)
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
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch1 -p0
%patch2 -p0
%patch3 -p0
sed -i s,/usr/bin/bash,/bin/bash, %SOURCE1

# requires /sys/kernel
rm runtime-decompiler/src/test/java/org/jrd/frontend/PluginMangerFrame/FileSelectorArrayRowTest.java

%build
pushd runtime-decompiler
%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools
%pom_remove_plugin :maven-jar-plugin
popd
%mvn_build --xmvn-javadoc

%install
%mvn_install
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
cp -r %{_builddir}/%{name}-%{name}-%{version}/runtime-decompiler/src/plugins/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install                      \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE3}

%files -f .mfiles
%attr(755, root, -) %{_bindir}/java-runtime-decompiler
%{_mandir}/man1/java-runtime-decompiler.1*

# wrappers for decompilers
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

%changelog
* Mon Oct 12 2020 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_9jpp9
- new version

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_6jpp8
- new version

