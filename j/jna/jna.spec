Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Allow conditionally building without the reflections library
%bcond_without reflections

Name:           jna
Version:        5.6.0
Release:        alt1_4jpp11
Summary:        Pure Java access to native libraries
# Most of code is dual-licensed under either LGPL 2.1+ only or Apache
# License 2.0.  WeakIdentityHashMap.java was taken from Apache CXF,
# which is pure Apache License 2.0.
License:        (LGPLv2+ or ASL 2.0) and ASL 2.0

URL:            https://github.com/java-native-access/jna/
# ./generate-tarball.sh
Source0:        %{name}-%{version}-clean.tar.xz
Source1:        package-list
Source2:        generate-tarball.sh

Patch0:         0001-Adapt-build.patch
# This patch is Fedora-specific for now until we get the huge
# JNI library location mess sorted upstream
Patch1:         0002-Load-system-library.patch
# The X11 tests currently segfault; overall I think the X11 JNA stuff is just a
# Really Bad Idea, for relying on AWT internals, using the X11 API at all,
# and using a complex API like X11 through JNA just increases the potential
# for problems.
Patch2:         0003-Tests-headless.patch
# Adds --allow-script-in-comments arg to javadoc to avoid error
Patch3:         0004-Fix-javadoc-build.patch
# Avoid generating duplicate manifest entry
# See https://bugzilla.redhat.com/show_bug.cgi?id=1469022
Patch4:         0005-Fix-duplicate-manifest-entry.patch
# We don't want newly added warnings to break our build
Patch5:         0006-Remove-Werror.patch

# We manually require libffi because find-requires doesn't work
# inside jars.
Requires:       libffi
BuildRequires:  gcc
BuildRequires:  javapackages-local
BuildRequires:  libffi-devel
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
%if %{with reflections}
BuildRequires:  reflections
%endif
Source44: import.info

%description
JNA provides Java programs easy access to native shared libraries
(DLLs on Windows) without writing anything but Java code. JNA's
design aims to provide native access in a natural way with a
minimum of effort. No boilerplate or generated code is required.
While some attention is paid to performance, correctness and ease
of use take priority.

%package        javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch:      noarch

%description    javadoc
This package contains the javadocs for %{name}.

%package        contrib
Group: Development/Java
Summary:        Contrib for %{name}
License:        LGPLv2+ or ASL 2.0
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    contrib
This package contains the contributed examples for %{name}.


%prep
%setup -q
cp %{SOURCE1} .
%patch0 -p1 -b .build
%patch1 -p1 -b .loadlib
%patch2 -p1 -b .tests-headless
%patch3 -p1
%patch4 -p1
%patch5 -p1

chmod -Rf a+rX,u+w,g-w,o-w .
sed -i 's|@LIBDIR@|%{_libdir}/%{name}|' src/com/sun/jna/Native.java

# clean LICENSE.txt
sed -i 's/\r//' LICENSE

chmod -c 0644 LICENSE OTHERS CHANGES.md

%if %{with reflections}
sed s,'<include name="junit.jar"/>,&<include name="reflections.jar"/>,' -i build.xml
build-jar-repository -s -p lib junit reflections
%else
build-jar-repository -s -p lib junit
rm test/com/sun/jna/StructureFieldOrderInspector.java
rm test/com/sun/jna/StructureFieldOrderInspectorTest.java
%endif
ln -s $(xmvn-resolve ant:ant:1.10.5) lib/ant.jar

cp lib/native/aix-ppc64.jar lib/clover.jar

%pom_remove_plugin -r :maven-javadoc-plugin parent


%build
# We pass -Ddynlink.native which comes from our patch because
# upstream doesn't want to default to dynamic linking.
# -Drelease removes the .SNAPSHOT suffix from maven artifact names
#ant -Dcflags_extra.native="%{optflags}" -Ddynlink.native=true native compile javadoc jar contrib-jars
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Drelease -Dcompatibility=1.6 -Dplatform.compatibility=1.6\
 -Dcflags_extra.native="%{optflags}" -Ddynlink.native=true -DCC=gcc native dist
# remove compiled contribs
find contrib -name build -exec rm -rf {} \; || :


%install
# NOTE: JNA has highly custom code to look for native jars in this
# directory.  Since this roughly matches the jpackage guidelines,
# we'll leave it unchanged.
install -d -m 755 %{buildroot}%{_libdir}/%{name}
install -m 755 build/native*/libjnidispatch*.so %{buildroot}%{_libdir}/%{name}/

%mvn_file :jna jna jna/jna %{_javadir}/jna

%mvn_package :jna-platform contrib
%mvn_alias :jna-platform :platform

%mvn_artifact pom-jna.xml build/jna-min.jar
%mvn_artifact pom-jna-platform.xml contrib/platform/dist/jna-platform.jar

%mvn_install -J doc/javadoc


%files -f .mfiles
%doc OTHERS README.md CHANGES.md TODO
%doc --no-dereference LICENSE LGPL2.1 AL2.0
%{_libdir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE LGPL2.1 AL2.0

%files contrib -f .mfiles-contrib


%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 5.6.0-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 5.6.0-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 5.4.0-alt1_7jpp11
- update

* Mon Oct 12 2020 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_2jpp8
- new version

* Mon Aug 03 2020 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.5.1-alt2_6jpp8
- NMU: removed invalid parasitic dependency on libffi6 (#38781).

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt1_4jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt1_3jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt1_1jpp8
- new version

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 4.4.0-alt1_7jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 4.3.0-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_9jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.5.2-alt1_2jpp7
- new release

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1_2jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt1_5jpp7
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.2.7-alt1_12jpp6
- update to new release by jppimport

* Sun Aug 29 2010 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt2_3jpp5
- rebuild with new libffi

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt1_3jpp5
- new version

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_4jpp5
- jpp5 build

