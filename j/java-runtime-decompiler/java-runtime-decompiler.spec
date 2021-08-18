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
Version: 5.1
Release: alt1_1jpp11
License: GPLv3
URL: https://github.com/pmikova/java-runtime-decompiler
Source0: https://github.com/pmikova/%{name}/archive/%{name}-%{version}.tar.gz
Source1: java-runtime-decompiler
Source3: jrd.desktop
Patch1: systemFernflower.patch
Patch2: systemProcyon.patch
Patch3: rsyntaxVersion.patch
Patch4: systemCfr.patch
Patch5: systemJasm.patch
Patch6: systemJcoder.patch


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
BuildRequires: java-11-devel
BuildRequires: google-gson
BuildRequires: desktop-file-utils
BuildRequires: classpathless-compiler
Requires: java
Requires: classpathless-compiler
Requires: fernflower
Requires: procyon-decompiler
Requires: CFR
Requires: openjdk-asmtools
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
%patch4 -p0
%patch5 -p0
%patch6 -p0
sed -i 's,/usr/bin/bash,/bin/bash,;s,^run ,jvm_run ,' %{SOURCE1}

%build
pushd runtime-decompiler
%pom_remove_plugin :maven-jar-plugin
popd

%mvn_build --xmvn-javadoc -f
java -cp /usr/share/java/classpathless-compiler/classpathless-compiler.jar:runtime-decompiler/target/runtime-decompiler-%{version}.jar org.jrd.backend.data.Help > %{name}.1

%install
%mvn_install
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/

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
%config %{_sysconfdir}/%{name}/plugins/CfrDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/CfrDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/JasmDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/JasmDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/JcoderDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/JcoderDecompilerWrapper.json
%doc --no-dereference LICENSE

%{_datadir}/applications/jrd.desktop

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 5.1-alt1_1jpp11
- new version

* Sun Jun 13 2021 Igor Vlasenko <viy@altlinux.org> 4.0-alt1_3jpp11
- new version

* Mon Jun 07 2021 Igor Vlasenko <viy@altlinux.org> 3.0-alt2_9jpp9
- use jvm_run

* Mon Oct 12 2020 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_9jpp9
- new version

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_6jpp8
- new version

