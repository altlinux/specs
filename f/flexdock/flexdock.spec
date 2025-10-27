Name: flexdock
Version: 1.2.5
Release: alt1
Epoch: 1
Summary: Docking framework for Java Swing GUI apps

#Licence is MIT on their website
License: MIT 
Group: Development/Java
URL: http://forge.scilab.org/index.php/p/flexdock/
VCS: https://gitlab.com/scilab/forge/flexdock

Source0: %name-master.tar.gz
Patch0: flexdock-use-libraries.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc rpm-build-java
BuildRequires: java-devel
BuildRequires: ant
BuildRequires: jpackage-utils
BuildRequires: jgoodies-common
BuildRequires: jgoodies-looks
BuildRequires: skinlf

Requires: java
Requires: jpackage-utils
Requires: jgoodies-common
Requires: jgoodies-looks
Requires: skinlf

BuildArch: noarch

%description
FlexDock is a Java docking framework for use in cross-platform
Swing applications.

%prep
%setup -n %name-master
%patch0 -p1

#Override the build file's default hard-coded paths
echo "sdk.home=%{java_home}" > workingcopy.properties

#JAR "dependency" handling
find ./ -name \*.jar -exec rm {} \;
build-jar-repository -s -p lib skinlf jgoodies-looks jgoodies-common

#Remove the jmf-using demo files
rm src/java/demo/org/flexdock/demos/raw/jmf/MediaPanel.java
rm src/java/demo/org/flexdock/demos/raw/jmf/JMFDemo.java

#Endline convert Doc files
for i in "LICENSE.txt README release-notes.txt" ;
do
    sed -i 's/\r//' $i
done

# Set minimal version
subst 's|"1\.5"|"11"|g' build.xml

# Fix package version
subst 's|VERSION.*|VERSION = "%version";|' src/java/core/org/flexdock/util/Utilities.java

%build
ant jar

%install
mkdir -p %{buildroot}%{_javadir}
install -pm644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%doc LICENSE.txt README release-notes.txt
%{_javadir}/*

%changelog
* Tue Apr 22 2025 Andrey Cherepanov <cas@altlinux.org> 1:1.2.5-alt1
- New version.

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:1.2.4-alt1_14jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_11jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_9jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_8jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_6jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_3jpp8
- new version

* Fri Sep 19 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_1jpp7
- new release

* Wed Sep 17 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.4-alt1_0jpp7
- restored version 1.2.4

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.3-alt1_1jpp7
- new release

* Mon Apr 14 2014 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- New version

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_1jpp7
- fc update

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2jpp7
- new version

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt4
- resurrect

* Thu Aug 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt3
- Fix creation %%_libdir/%%name in working dir (ALT #21138)

* Mon Jul 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt2
- Move jar to %%_javadir

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1
- Initial from Fedora
