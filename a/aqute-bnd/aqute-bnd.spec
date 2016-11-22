Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           aqute-bnd
Version:        2.4.1
Release:        alt2_3jpp8
Summary:        BND Tool
License:        ASL 2.0
URL:            http://www.aqute.biz/Bnd/Bnd
BuildArch:      noarch

Source0:        https://github.com/bndtools/bnd/archive/%{version}.REL.tar.gz
# Auxiliary parent pom, packager-written
Source1:        parent.pom
Source2:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/%{version}/biz.aQute.bnd-%{version}.pom
Source3:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/%{version}/biz.aQute.bndlib-%{version}.pom

Patch0:         0001-Port-to-Java-8.patch
Patch1:         0002-Inline-namespace-constants.patch
Patch2:         0003-Use-equinox-s-annotations.patch

BuildRequires:  maven-local
BuildRequires:  mvn(ant:ant)
BuildRequires:  mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires:  mvn(org.eclipse.osgi:org.eclipse.osgi.services)
Source44: import.info

%description
The bnd tool helps you create and diagnose OSGi bundles.
The key functions are:
- Show the manifest and JAR contents of a bundle
- Wrap a JAR so that it becomes a bundle
- Create a Bundle from a specification and a class path
- Verify the validity of the manifest entries
The tool is capable of acting as:
- Command line tool
- File format
- Directives
- Use of macros

%package -n aqute-bndlib
Group: Development/Java
Summary:        BND library

%description -n aqute-bndlib
%{summary}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n bnd-%{version}.REL

rm gradlew*
find -name '*.jar' -delete
find -name '*.class' -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1

# reference to Base64 is ambiguous
find -name '*.java' -not -name 'Base64.java' | xargs sed -i 's/\<Base64\>/aQute.lib.base64.Base64/g'

cp -p %{SOURCE1} pom.xml

build_section='
<build>
    <sourceDirectory>src</sourceDirectory>
    <resources>
        <resource>
            <directory>src/</directory>
            <excludes>
                <exclude>**/*.java</exclude>
                <exclude>**/packageinfo</exclude>
            </excludes>
        </resource>
    </resources>
</build>'

pushd biz.aQute.bnd
cp -p %{SOURCE2} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_xpath_inject /pom:project "$build_section"

%pom_add_dep ant:ant
%pom_add_dep biz.aQute.bnd:biz.aQute.bndlib:%{version}
%pom_add_dep org.eclipse.osgi:org.eclipse.osgi
%pom_add_dep org.eclipse.osgi:org.eclipse.osgi.services
# The common library is expected to be included in all artifacts
cp -r ../aQute.libg/src/* src/
popd

pushd biz.aQute.bndlib
cp -p %{SOURCE3} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_xpath_inject /pom:project "$build_section"

%pom_add_dep org.eclipse.osgi:org.eclipse.osgi
%pom_add_dep org.eclipse.osgi:org.eclipse.osgi.services
# The common library is expected to be included in all artifacts
cp -r ../aQute.libg/src/* src/

sed -i 's|${Bundle-Version}|%{version}|' src/aQute/bnd/osgi/bnd.info

# We don't have metatype-annotations and I haven't found any proper release of it
rm -r src/aQute/bnd/metatype

popd

%mvn_alias biz.aQute.bnd:biz.aQute.bnd :bnd biz.aQute:bnd
%mvn_alias biz.aQute.bnd:biz.aQute.bndlib :bndlib biz.aQute:bndlib

%mvn_package biz.aQute.bnd:biz.aQute.bndlib bndlib
%mvn_package biz.aQute.bnd:parent __noinstall

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%jpackage_script bnd "" "" aqute-bnd bnd 1

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc biz.aQute.bnd/LICENSE
%{_bindir}/bnd
%config(noreplace,missingok) /etc/java/%{name}.conf

%files -n aqute-bndlib -f .mfiles-bndlib
%doc biz.aQute.bnd/LICENSE

%files javadoc -f .mfiles-javadoc
%doc biz.aQute.bnd/LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_3jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_2jpp8
- new versio

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt0.2jpp
- removed compatibility symlink

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt1_7jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

