BuildArch: noarch
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define debug_package %{nil}

Name: jibx
Version:	1.2.4
Release:	alt2_6jpp7
Summary:	Framework for binding XML data to Java objects

Group:		Development/Java
License:	BSD and ASL 1.1
URL:		http://sourceforge.net/projects/jibx/
Source0:	http://sourceforge.net/projects/jibx/files/jibx/jibx-1.2.4/%{name}_1_2_4.zip
Patch0: %{name}-classpath.patch
Patch1: %{name}-%{version}-poms.patch

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: asm2
BuildRequires: bcel
BuildRequires: bea-stax-api
BuildRequires: eclipse-jdt
BuildRequires: eclipse-rcp
BuildRequires: eclipse-platform
BuildRequires: joda-time
BuildRequires: qdox
BuildRequires: dom4j
BuildRequires: jdom
BuildRequires: xpp3
	
Requires: jpackage-utils
Source44: import.info

%description
JiBX is a framework for binding XML data to Java objects. It lets you
work with data from XML documents using your own class structures. 

%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}
#Patch to add the bundled jar dependencies in the classpath
%patch0 -p1
#Patch to add maven poms
%patch1 -p0

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
rm -rf %{_builddir}/%{name}/build/docs/src/*


#Symlink the eclipse dependencies 
plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.core.contenttype_*.jar`
ln -s "$plugin_file" lib/org.eclipse.core.contenttype.jar

plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.core.jobs_*.jar`
ln -s "$plugin_file" lib/org.eclipse.core.jobs.jar

plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.core.runtime_*.jar`
ln -s "$plugin_file" lib/org.eclipse.core.runtime.jar

plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.core.resources_*.jar`
ln -s "$plugin_file" lib/org.eclipse.core.resources.jar

plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.common_*.jar`
ln -s "$plugin_file" lib/org.eclipse.equinox.common.jar

plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.preferences_*.jar`
ln -s "$plugin_file" lib/org.eclipse.equinox.preferences.jar

plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.text_*.jar`
ln -s "$plugin_file" lib/org.eclipse.text.jar

plugin_file=`ls %{_libdir}/eclipse/dropins/jdt/plugins/org.eclipse.jdt.core.manipulation_*.jar`
ln -s "$plugin_file" lib/org.eclipse.jdt.core.manipulation.jar

plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.osgi_*.jar`
ln -s "$plugin_file" lib/org.eclipse.osgi.jar

plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.jdt.core_*jar`
ln -s "$plugin_file" lib/org.eclipse.jdt.core.jar


build-jar-repository -p lib \
asm2/asm2 \
asm2/asm2-commons \
bcel \
bea-stax-api \
dom4j \
jdom \
joda-time \
log4j \
qdox \
xpp3 

sed -i '/Class-Path/I d' %{_builddir}/%{name}/build/build.xml


%build
pushd build/
sed -i -e s:stax-api.jar:bea-stax-api.jar:g build.xml

export CLASSPATH=$(build-classpath junit)
ant current #test-multiples test-singles test-extras basic-blackbox blackbox devdoc javadoc

%install
install -d -m 755 %{buildroot}/%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}

install -pm 644 build/maven/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-main-reactor.pom
%add_maven_depmap JPP.%{name}-main-reactor.pom

for sub_component in bind extras run schema tools; do
install -m 644 lib/%{name}-${sub_component}.jar \
%{buildroot}/%{_javadir}/%{name}/${sub_component}-%{version}.jar
# TODO unversioned jars
( cd %{buildroot}%{_javadir}/%{name} && ln -sf ${sub_component}-%{version}.jar ${sub_component}.jar )
install -m 644 build/maven/jibx-${sub_component}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${sub_component}.pom
%add_maven_depmap JPP.%{name}-${sub_component}.pom %{name}/${sub_component}.jar
done

mkdir -p %{buildroot}/%{_javadocdir}/%{name}
cp -rp %{_builddir}/%{name}/build/docs/* \
%{buildroot}/%{_javadocdir}/%{name}/


%files
%{_javadir}/%{name}/*.jar
%dir %{_javadir}/%{name}
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
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

