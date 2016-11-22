Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:           objectweb-asm3
Version:        3.3.1
Release:        alt1_13jpp8
Summary:        Java bytecode manipulation and analysis framework
License:        BSD
URL:            http://asm.ow2.org/
BuildArch:      noarch

Source0:        http://download.forge.ow2.org/asm/asm-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  ant
BuildRequires:  maven-local
# shade-jar utility used in this spec file needs this
BuildRequires:  objectweb-asm3
Source44: import.info

%description
ASM is an all purpose Java bytecode manipulation and analysis
framework.  It can be used to modify existing classes or dynamically
generate classes, directly in binary form.  Provided common
transformations and analysis algorithms allow to easily assemble
custom complex transformations and code analysis tools.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n asm-%{version}
find -name *.jar -delete

sed -i /Class-path/d archive/asm-xml.xml

# Our system version of asm always used BSN org.objectweb.asm for
# asm-all because that's what Eclipse bundle has.  Now upstream
# provides OSGi metadata with incompatible BSN, but we want to keep
# compatibility with existing Eclipse plugins, so we have to use the
# old BSN (org.objectweb.asm).
sed -i s/org.objectweb.asm.all/org.objectweb.asm/ archive/asm-all.xml

%build
%ant -Dobjectweb.ant.tasks.path= jar jdoc

mv output/dist/lib/all/* output/dist/lib/

# Fix artifactId in POMs for shaded artifacts
for m in asm asm-analysis asm-commons asm-tree asm-util asm-xml asm-all; do
    cp output/dist/lib/${m}-%{version}.pom output/dist/lib/${m}-distroshaded-%{version}.pom
    %pom_xpath_set "pom:project/pom:artifactId" "${m}-distroshaded" \
                   output/dist/lib/${m}-distroshaded-%{version}.pom
done

# Fix inter-module dependecies in POMs for shaded artifacts
%if 0%{?fedora} > 0
pushd output/dist/lib
for m in asm-analysis asm-commons asm-util; do
    %pom_remove_dep :asm-tree ${m}-distroshaded-%{version}.pom
    %pom_add_dep asm:asm-tree-distroshaded:3.3.1 ${m}-distroshaded-%{version}.pom
done
%pom_remove_dep :asm-util asm-xml-distroshaded-%{version}.pom
%pom_add_dep asm:asm-util-distroshaded:3.3.1 asm-xml-distroshaded-%{version}.pom

%pom_remove_dep :asm asm-tree-distroshaded-%{version}.pom
%pom_add_dep asm:asm-distroshaded:3.3.1 asm-tree-distroshaded-%{version}.pom
popd

for m in asm asm-analysis asm-commons asm-tree asm-util asm-xml asm-all; do
    shade-jar org.objectweb.asm org.objectweb.distroshaded.asm output/dist/lib/${m}-%{version}.jar \
              output/dist/lib/${m}-distroshaded-%{version}.jar
    jar xf output/dist/lib/${m}-distroshaded-%{version}.jar META-INF/MANIFEST.MF
    sed -i /Bundle-/d META-INF/MANIFEST.MF
    jar ufM output/dist/lib/${m}-distroshaded-%{version}.jar META-INF/MANIFEST.MF
done
%endif

%install
%mvn_artifact output/dist/lib/asm-parent-%{version}.pom

for m in asm asm-analysis asm-commons asm-tree asm-util asm-xml asm-all; do
%if 0%{?fedora} > 0
    %mvn_artifact output/dist/lib/${m}-distroshaded-%{version}.pom \
                  output/dist/lib/${m}-distroshaded-%{version}.jar
%endif
    %mvn_artifact output/dist/lib/${m}-%{version}.pom \
                  output/dist/lib/${m}-%{version}.jar
done
%mvn_install -J output/dist/doc/javadoc/user

%jpackage_script org.objectweb.asm.xml.Processor "" "" %{name}/asm:%{name}/asm-attrs:%{name}/asm-util:%{name}/asm-xml %{name}-processor true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc LICENSE.txt README.txt
%{_bindir}/%{name}-processor
%dir %{_javadir}/%{name}
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_13jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_12jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

