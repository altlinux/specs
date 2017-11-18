Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}
%global _version 1_2_6
Name:          jibx
Version:       1.2.6
Release:       alt1_7jpp8
Summary:       Framework for binding XML data to Java objects
License:       BSD and ASL 1.1
URL:           http://sourceforge.net/projects/jibx/
Source0:       http://sourceforge.net/projects/jibx/files/jibx/jibx-%{version}/%{name}_%{_version}.zip
Patch0:        %{name}-classpath.patch
Patch1:        %{name}-1.2.6-poms.patch
Patch2:        %{name}-port-to-qdox-2.patch

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: objectweb-asm3
BuildRequires: bcel
BuildRequires: bea-stax-api
BuildRequires: eclipse-equinox-osgi >= 1:4.6.0
BuildRequires: eclipse-jdt >= 1:4.6.0
BuildRequires: eclipse-platform >= 1:4.6.0
BuildRequires: joda-time
BuildRequires: qdox
BuildRequires: dom4j
BuildRequires: jdom
BuildRequires: xpp3
BuildRequires: log4j12
BuildRequires: javapackages-local
Source44: import.info
BuildArch: noarch

%description
JiBX is a framework for binding XML data to Java objects. It lets you
work with data from XML documents using your own class structures. 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}
#Patch to add the bundled jar dependencies in the classpath
%patch0 -p1
#Patch to add maven poms
%patch1 -p1
%patch2 -p0

find -name '*.class' -delete
find -name '*.jar' -delete

rm -rf %{_builddir}/%{name}/build/docs/src/*


#Symlink the eclipse dependencies
# platform
plugin_file=`ls %{_javadir}/eclipse/core.contenttype*.jar`
ln -s "$plugin_file" lib/org.eclipse.core.contenttype.jar

plugin_file=`ls %{_javadir}/eclipse/core.jobs*.jar`
ln -s "$plugin_file" lib/org.eclipse.core.jobs.jar

plugin_file=`ls %{_javadir}/eclipse/core.runtime*.jar`
ln -s "$plugin_file" lib/org.eclipse.core.runtime.jar

plugin_file=`ls %{_javadir}/eclipse/core.resources*.jar`
ln -s "$plugin_file" lib/org.eclipse.core.resources.jar

plugin_file=`ls %{_javadir}/eclipse/equinox.common*.jar`
ln -s "$plugin_file" lib/org.eclipse.equinox.common.jar

plugin_file=`ls %{_javadir}/eclipse/equinox.preferences*.jar`
ln -s "$plugin_file" lib/org.eclipse.equinox.preferences.jar

plugin_file=`ls %{_javadir}/eclipse/text*.jar`
ln -s "$plugin_file" lib/org.eclipse.text.jar

# new location in eclipse 4.6.0-0.5.git201604261105
plugin_file=`ls %{_datadir}/eclipse/droplets/eclipse-jdt/eclipse/plugins/org.eclipse.jdt.core_*jar`
ln -s "$plugin_file" lib/org.eclipse.jdt.core.jar

# equinox-osgi
#plugin_file=`ls %%{_javadir}/eclipse/osgi_*.jar`
#ln -s "$plugin_file" lib/org.eclipse.osgi.jar
ln -s $(build-classpath eclipse/osgi) lib/org.eclipse.osgi.jar

# jdt
plugin_file=`ls %{_datadir}/eclipse/droplets/eclipse-jdt/eclipse/plugins/org.eclipse.jdt.core.manipulation_*.jar`
ln -s "$plugin_file" lib/org.eclipse.jdt.core.manipulation.jar


build-jar-repository -p lib \
bcel \
bea-stax-api \
dom4j \
jdom \
joda-time \
qdox \
xpp3 

ln -s $(build-classpath objectweb-asm3/asm) lib/
ln -s $(build-classpath objectweb-asm3/asm-commons) lib/
ln -s $(build-classpath log4j12-1.2.17) lib/

sed -i '/Class-Path/I d' %{_builddir}/%{name}/build/build.xml

%pom_change_dep :log4j ::1.2.17 build/maven/jibx-bind/pom.xml

%build

for sub_component in bind extras run schema tools; do
%mvn_file org.%{name}:%{name}-${sub_component} %{name}/${sub_component}
done

pushd build/
sed -i -e s:stax-api.jar:bea-stax-api.jar:g build.xml
# thanks to msrb@redhat.com
sed -i 's|version}" arg2="1.5"|version}" arg2="1.8"|g' build.xml
javac jenable/JEnable.java

export CLASSPATH=$(build-classpath junit)
ant current -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 devdoc #test-multiples test-singles test-extras basic-blackbox blackbox devdoc javadoc

%install
%mvn_artifact build/maven/pom.xml
for sub_component in bind extras run schema tools; do
%mvn_artifact build/maven/jibx-${sub_component}/pom.xml lib/%{name}-${sub_component}.jar
done

%mvn_install -J %{_builddir}/%{name}/build/api


%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2.6-alt1_7jpp8
- fixed build

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.6-alt1_5jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.5-alt1_5jpp7
- new release

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.5-alt1_2jpp7
- update

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.4-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.4-alt1_6jpp7
- new version

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt2_1jpp6
- applied repocop patches

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt1_1jpp6
- new version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6a-alt2_1jpp5
- selected java5 compiler explicitly

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6a-alt1_1jpp5
- new jpp release

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt1_1jpp1.7
- updated to new jpackage release

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.b3.1jpp1.7
- converted from JPackage by jppimport script

