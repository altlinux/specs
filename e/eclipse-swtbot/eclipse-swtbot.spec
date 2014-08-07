Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven-local
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global install_loc   %{_datadir}/eclipse/dropins/swtbot

Name:           eclipse-swtbot
Version:        2.1.0
Release:        alt2_1jpp7
Summary:        UI and functional testing tool for SWT and Eclipse based applications

License:        EPL
URL:            http://www.eclipse.org/swtbot/
Source0:        http://git.eclipse.org/c/swtbot/org.eclipse.swtbot.git/snapshot/org.eclipse.swtbot-%{version}.tar.bz2
BuildRequires:  tycho
BuildRequires:  eclipse-gef
BuildRequires:  eclipse-pde
BuildRequires:  jacoco-maven-plugin
BuildArch:      noarch
Source44: import.info

%description
SWTBot is a Java based UI/functional testing tool for testing SWT and Eclipse
based applications. SWTBot provides APIs that are simple to read and write.
The APIs also hide the complexities involved with SWT and Eclipse. This makes
it suitable for UI/functional testing by everyone, not just developers.

%prep
%setup -q -n org.eclipse.swtbot-%{version}

for j in $(find -name \*.jar); do
if [ ! -L $j ] ; then
rm -fr $j
fi
done

sed -i -e "s|1.2.13.v200903072027|0.0.0|g" org.eclipse.swtbot/feature.xml


%build
mvn-rpmbuild clean install -Dmaven.test.skip=true -DskipTychoVersionCheck=true

%install
install -d -m 755 %{buildroot}%{install_loc}

cp -R org.eclipse.swtbot.updatesite/target/repository/plugins/ %{buildroot}%{install_loc}
cp -R org.eclipse.swtbot.updatesite/target/repository/features/ %{buildroot}%{install_loc}

pushd %{buildroot}%{install_loc}/plugins
    rm -fr org.apache.log4j*
    ln -s %{_javadir}/log4j.jar .
    rm -fr org.hamcrest*
    ln -s %{_javadir}/hamcrest/core.jar hamcrest-core.jar
    ln -s %{_javadir}/hamcrest/integration.jar hamcrest-integration.jar
    ln -s %{_javadir}/hamcrest/library.jar hamcrest-library.jar
    ln -s %{_javadir}/hamcrest/text.jar hamcrest-text.jar
popd

%files
%{install_loc}
%doc org.eclipse.swtbot/epl-v10.html 
%doc org.eclipse.swtbot/license.html

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2_1jpp7
- rebuild with maven-local

* Tue Jul 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_1jpp7
- update

