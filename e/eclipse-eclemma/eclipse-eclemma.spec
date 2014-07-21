# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global install_loc  %{_datadir}/eclipse/dropins/eclemma

Name:      eclipse-eclemma
Version:   2.2.0
Release:   alt1_1jpp7
Summary:   Java code coverage tool plugin for Eclipse
Group:     Development/Java
License:   EPL and ASL 2.0
URL:       http://www.eclemma.org

Source0:   https://github.com/jacoco/eclemma/archive/v2.2.0.tar.gz

BuildArch:        noarch
BuildRequires:    jpackage-utils
BuildRequires:    eclipse-pde >= 1:4.2.0
BuildRequires:    jacoco >= 0.6.0
Requires:         jpackage-utils
Requires:         eclipse-jdt >= 1:4.2.0
Requires:         jacoco >= 0.6.0
Requires:         objectweb-asm4
Source44: import.info

%description
EclEmma is a Java code coverage tool for Eclipse based on the EMMA Java
code coverage tool.  Features include launching from within the IDE,
coverage analysis summaries, and highlighting in Java source code
editors.

%prep
%setup -q -n eclemma-%{version}

#git does not handle empty folders - but this one is necessary

mkdir -p com.mountainminds.eclemma.asm/src
rm -fr com.mountainminds.eclemma.debug.ui.compatibility/src/org/eclipse/debug/ui/actions/RelaunchLastAction.java
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

rm -rf orbitDeps
mkdir orbitDeps
pushd orbitDeps
ln -s %{_javadir}/jacoco/org.jacoco.core.jar
ln -s %{_javadir}/jacoco/org.jacoco.agent.jar
ln -s %{_javadir}/jacoco/org.jacoco.report.jar
ln -s %{_javadir}/objectweb-asm4/asm-all.jar
popd

%build
eclipse-pdebuild -o `pwd`/orbitDeps

%install
install -d -m 755 %{buildroot}/%{install_loc}
unzip -q -o -d %{buildroot}/%{install_loc} \
  build/rpmBuild/com.mountainminds.eclemma.feature.zip
pushd %{buildroot}/%{install_loc}/eclipse/plugins
rm -fr org.jacoco*
rm -fr org.objectweb.asm*
ln -s %{_javadir}/jacoco/org.jacoco.agent.jar 
ln -s %{_javadir}/jacoco/org.jacoco.core.jar 
ln -s %{_javadir}/jacoco/org.jacoco.report.jar
ln -s %{_javadir}/objectweb-asm4/asm-all.jar
popd

%files
%doc com.mountainminds.eclemma.doc/pages/faq.html
%doc com.mountainminds.eclemma.doc/pages/license.html
%doc com.mountainminds.eclemma.core/about.html
%{install_loc}

%changelog
* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp7
- new version

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.4-alt1_2jpp7
- new release

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_2jpp7
- new version

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_1jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_1jpp6
- new version

