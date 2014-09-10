Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global debug_package %{nil}

Name:          jibx
Version:       1.2.5
Release:       alt1_5jpp7
Summary:       Framework for binding XML data to Java objects
License:       BSD and ASL 1.1
URL:           http://sourceforge.net/projects/jibx/
Source0:       http://sourceforge.net/projects/jibx/files/jibx/jibx-1.2.5/%{name}_1_2_5.zip
Patch0:        %{name}-classpath.patch
Patch1:        %{name}-%{version}-poms.patch

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: objectweb-asm
BuildRequires: bcel
BuildRequires: bea-stax-api
BuildRequires: eclipse-equinox-osgi
BuildRequires: eclipse-jdt
BuildRequires: eclipse-platform
BuildRequires: joda-time
BuildRequires: qdox
BuildRequires: dom4j
BuildRequires: jdom
BuildRequires: xpp3

Requires:      jpackage-utils
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
%patch1 -p0

find -name '*.class' -delete
find -name '*.jar' -delete

rm -rf %{_builddir}/%{name}/build/docs/src/*


#Symlink the eclipse dependencies
# platform
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

plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.jdt.core_*jar`
ln -s "$plugin_file" lib/org.eclipse.jdt.core.jar

# equinox-osgi
#plugin_file=`ls %%{_libdir}/eclipse/plugins/org.eclipse.osgi_*.jar`
#ln -s "$plugin_file" lib/org.eclipse.osgi.jar
ln -s $(build-classpath eclipse/osgi) lib/org.eclipse.osgi.jar

# jdt
plugin_file=`ls %{_libdir}/eclipse/dropins/jdt/plugins/org.eclipse.jdt.core.manipulation_*.jar`
ln -s "$plugin_file" lib/org.eclipse.jdt.core.manipulation.jar


build-jar-repository -p lib \
bcel \
bea-stax-api \
dom4j \
jdom \
joda-time \
log4j \
qdox \
xpp3 

ln -s $(build-classpath objectweb-asm/asm) lib/
ln -s $(build-classpath objectweb-asm/asm-commons) lib/

sed -i '/Class-Path/I d' %{_builddir}/%{name}/build/build.xml


%build
pushd build/
sed -i -e s:stax-api.jar:bea-stax-api.jar:g build.xml

export CLASSPATH=$(build-classpath junit)
ant current -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 #test-multiples test-singles test-extras basic-blackbox blackbox devdoc javadoc

%install
install -d -m 755 %{buildroot}/%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}

install -pm 644 build/maven/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-main-reactor.pom
%add_maven_depmap JPP.%{name}-main-reactor.pom

for sub_component in bind extras run schema tools; do
install -m 644 lib/%{name}-${sub_component}.jar \
%{buildroot}/%{_javadir}/%{name}/${sub_component}.jar
install -pm 644 build/maven/jibx-${sub_component}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${sub_component}.pom
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

