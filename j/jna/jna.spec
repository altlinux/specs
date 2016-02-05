Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jna
Version:        4.1.0
Release:        alt1_9jpp8
Summary:        Pure Java access to native libraries
# Most of code is dual-licensed under either LGPL 2.1 only or Apache
# License 2.0.  WeakIdentityHashMap.java was taken from Apache CXF,
# which is pure Apache License 2.0.
License:        (LGPLv2 or ASL 2.0) and ASL 2.0
URL:            https://github.com/twall/jna
# ./generate-tarball.sh
Source0:        %{name}-%{version}-clean.tar.xz
Source1:        package-list
Source2:        generate-tarball.sh
Patch0:         jna-3.5.0-build.patch
# This patch is Fedora-specific for now until we get the huge
# JNI library location mess sorted upstream
Patch1:         jna-4.0.0-loadlibrary.patch
# The X11 tests currently segfault; overall I think the X11 JNA stuff is just a 
# Really Bad Idea, for relying on AWT internals, using the X11 API at all,
# and using a complex API like X11 through JNA just increases the potential
# for problems.
Patch2:         jna-4.0.0-tests-headless.patch
Patch6:         jna-4.0.0-ffi.patch
Patch7:         jna-4.0.0-fix-native-test.patch

# We manually require libffi because find-requires doesn't work
# inside jars.
Requires:       jpackage-utils libffi
BuildRequires:  jpackage-utils libffi-devel
BuildRequires:  ant ant-junit junit reflections
BuildRequires:  libX11-devel libXt-devel
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
License:        LGPLv2 or ASL 2.0
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}


%description    contrib
This package contains the contributed examples for %{name}.


%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} .
%patch0 -p1 -b .build
%patch1 -p1 -b .loadlib
%patch2 -p1 -b .tests-headless
%patch6 -p1 -b .ffi
%patch7 -p1

chmod -Rf a+rX,u+w,g-w,o-w .
sed -i 's|@LIBDIR@|%{_libdir}/%{name}|' src/com/sun/jna/Native.java

# clean LICENSE.txt
sed -i 's/\r//' LICENSE

chmod -c 0644 LICENSE OTHERS CHANGES.md

sed s,'<include name="junit.jar"/>,&<include name="reflections.jar"/>,' -i build.xml

build-jar-repository -s -p lib junit reflections
cp lib/native/aix-ppc64.jar lib/clover.jar

%build
# We pass -Ddynlink.native which comes from our patch because
# upstream doesn't want to default to dynamic linking.
#ant -Dcflags_extra.native="%{optflags}" -Ddynlink.native=true native compile javadoc jar contrib-jars
ant -Dcompatibility=1.6 -Dplatform.compatibility=1.6 -Dcflags_extra.native="%{optflags}" -Ddynlink.native=true native dist
# remove compiled contribs
find contrib -name build -exec rm -rf {} \; || :

%install
# jars
install -D -m 644 build/%{name}-min.jar %{buildroot}%{_javadir}/%{name}.jar
install -d -m 755 %{buildroot}%{_javadir}/%{name}
find contrib -name '*.jar' -exec cp {} %{buildroot}%{_javadir}/%{name}/ \;
# NOTE: JNA has highly custom code to look for native jars in this
# directory.  Since this roughly matches the jpackage guidelines,
# we'll leave it unchanged.
install -d -m 755 %{buildroot}%{_libdir}/%{name}
install -m 755 build/native*/libjnidispatch*.so %{buildroot}%{_libdir}/%{name}/

# install maven pom file
install -Dm 644 pom-%{name}.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -Dm 644 pom-%{name}-platform.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-platform.pom

# ... and maven depmap
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP.%{name}-%{name}-platform.pom -f platform %{name}/%{name}-platform.jar -a "net.java.dev.jna:platform"

# javadocs
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -a doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}


#%check
#ant -Dcflags_extra.native="%{optflags}" -Ddynlink.native=true -Dnomixedjar.native=true test


%files -f .mfiles
%doc OTHERS README.md CHANGES.md TODO
%doc LICENSE LGPL2.1 ASL2.0
%{_libdir}/%{name}


%files javadoc
%doc LICENSE LGPL2.1 ASL2.0
%{_javadocdir}/%{name}


%files contrib -f .mfiles-platform
%{_javadir}/%{name}


%changelog
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

