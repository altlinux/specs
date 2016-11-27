Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name objectweb-asm
%define version 5.0.4
%{?scl:%scl_package objectweb-asm}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}objectweb-asm
Version:        5.0.4
Release:        alt1_2jpp8
Summary:        Java bytecode manipulation and analysis framework
License:        BSD
URL:            http://asm.ow2.org/
BuildArch:      noarch

Source0:        http://download.forge.ow2.org/asm/asm-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  ant
BuildRequires:  aqute-bnd
BuildRequires:  maven-local
%{?scl:Requires: %scl_runtime}

Obsoletes:      %{?scl_prefix}objectweb-asm4 < 5
Provides:       %{?scl_prefix}objectweb-asm4 = %{version}-%{release}
Source44: import.info

%description
ASM is an all purpose Java bytecode manipulation and analysis
framework.  It can be used to modify existing classes or dynamically
generate classes, directly in binary form.  Provided common
transformations and analysis algorithms allow to easily assemble
custom complex transformations and code analysis tools.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{pkg_name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n asm-%{version}
find -name *.jar -delete

sed -i /Class-Path/d archive/*.bnd
sed -i "s/Import-Package:/&org.objectweb.asm,org.objectweb.asm.util,/" archive/asm-xml.bnd
sed -i "s|\${config}/biz.aQute.bnd.jar|`build-classpath aqute-bnd`|" archive/*.xml
sed -i -e '/kind="lib"/d' -e 's|output/eclipse|output/build|' .classpath

%build
%ant -Dobjectweb.ant.tasks.path= jar jdoc

%install
%{?scl:scl enable %{scl} - <<"EOF"}
%mvn_artifact output/dist/lib/asm-parent-%{version}.pom
for m in asm asm-analysis asm-commons asm-tree asm-util asm-xml all/asm-all all/asm-debug-all; do
    %mvn_artifact output/dist/lib/${m}-%{version}.pom \
                  output/dist/lib/${m}-%{version}.jar
done
%mvn_install -J output/dist/doc/javadoc/user
%{?scl:EOF}

%jpackage_script org.objectweb.asm.xml.Processor "" "" %{pkg_name}/asm:%{pkg_name}/asm-attrs:%{pkg_name}/asm-util:%{pkg_name}/asm-xml %{pkg_name}-processor true

%files -f .mfiles
%doc LICENSE.txt README.txt
%{_bindir}/%{pkg_name}-processor
%dir %{_javadir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.4-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt1_2jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_7jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp7
- update

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp6
- updated OSGi manifest to match version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt4_4jpp6
- added pom groupid asm

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt3_4jpp6
- fixed poms

* Fri Sep 16 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt2_4jpp6
- removed asm2 pom provides

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_4jpp6
- new version

* Sat Feb 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_2jpp6
- added osgi manifest

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt2_5jpp5
- added OSGi manifest

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Jan 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

