Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          glassfish-jaxws
Version:       2.2.7
Release:       alt1_2jpp7
Summary:       JAX-WS Reference Implementation (RI) Project
Group:         Development/Java
# ASL 2.0
# tools/wscompile/src/com/sun/tools/ws/ant/AnnotationProcessingTask.java
# tools/wscompile/src/com/sun/tools/ws/wsdl/parser/NamespaceContextImpl.java
# Public Domain rt/src/com/sun/xml/ws/util/NamespaceSupport.java
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0 and Public Domain
Url:           http://jax-ws.java.net/
# svn export https://svn.java.net/svn/jax-ws~sources/tags/JAXWS_2_2_7_03082012/jaxws-ri/ glassfish-jaxws-2.2.7
# find glassfish-jaxws-2.2.7/ -name '*.jar' -delete
# find glassfish-jaxws-2.2.7/ -name '*.zip' -delete
# find glassfish-jaxws-2.2.7/ -name '*.class' -delete
# tar cafJ glassfish-jaxws-2.2.7-src-svn.tar.xz glassfish-jaxws-2.2.7
Source0:       %{name}-%{version}-src-svn.tar.xz
# custom pom file
Source1:       %{name}-%{version}-httpspi-servlet.pom

# use system asm
Patch0:        %{name}-%{version}-asm.patch
# use system xml-resolver
Patch1:        %{name}-%{version}-resolver.patch
# build fix for glassfish-gmbal 3.2.0-b003
Patch2:        %{name}-%{version}-gmbal.patch
# disable ivy support, use system libraries
Patch4:        %{name}-%{version}-build-bundle.patch
# remove maven references and use istack-commons ant task for resgen. use system libraries
Patch5:        %{name}-%{version}-build.patch
Patch6:        %{name}-%{version}-remove-classpath-from-manifests.patch
# disable for now require eclipselink >= 2.4.0-RC2
Patch7:        %{name}-%{version}-disable-eclipselink-plugin.patch
# remove javax.jws jsr181-api 1.0-MR1
# add system jboss apis, asm, and xml-resolver
Patch8:        %{name}-%{version}-poms.patch
# use system libraries and fix async-client-transport build
Patch9:        glassfish-jaxws-2.2.7-transports-build.patch
# add some system libraries used for testing, fix koji build
Patch10:       glassfish-jaxws-2.2.7-test-deps.patch


BuildRequires: ant
BuildRequires: ant-findbugs
BuildRequires: ant-junit
BuildRequires: junit

BuildRequires: codemodel
BuildRequires: glassfish-fastinfoset
BuildRequires: glassfish-gmbal
BuildRequires: glassfish-ha-api
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxb-api
BuildRequires: glassfish-management-api
BuildRequires: glassfish-pfl
BuildRequires: glassfish-policy
BuildRequires: glassfish-saaj
BuildRequires: istack-commons >= 2.14
BuildRequires: jboss-annotations-1.1-api
BuildRequires: jboss-jaxws-2.2-api
BuildRequires: jboss-jsp-2.2-api
BuildRequires: jboss-saaj-1.3-api
BuildRequires: jboss-servlet-3.0-api
BuildRequires: mimepull
BuildRequires: objectweb-asm
BuildRequires: stax-ex
BuildRequires: stax2-api
BuildRequires: txw2
BuildRequires: woodstox-core
BuildRequires: xmlstreambuffer
BuildRequires: xml-commons-resolver
BuildRequires: xsom

Requires:      glassfish-fastinfoset
Requires:      glassfish-gmbal
Requires:      glassfish-ha-api
Requires:      glassfish-jaxb
Requires:      glassfish-jaxb-api
Requires:      glassfish-management-api
Requires:      glassfish-pfl
Requires:      glassfish-policy
Requires:      glassfish-saaj
Requires:      istack-commons
Requires:      jboss-annotations-1.1-api
Requires:      jboss-jaxws-2.2-api
Requires:      jboss-jsp-2.2-api
Requires:      jboss-saaj-1.3-api
Requires:      jboss-servlet-3.0-api
Requires:      mimepull
Requires:      objectweb-asm
Requires:      stax-ex
Requires:      stax2-api
Requires:      txw2
Requires:      woodstox-core
Requires:      xml-commons-resolver
Requires:      xmlstreambuffer
Requires:      xsom

BuildArch:     noarch
Source44: import.info

%description
This project provides the core of Metro project,
inside GlassFish community. This project develops and
evolves the code base for the reference implementation of
the Java API for XML Web Services (JAX-WS) specification.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package tools
Group:         Development/Java
Summary:       JAX-WS Reference Implementation Tools
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:      codemodel
Requires:      glassfish-jaxb
Requires:      glassfish-jaxb-api
Requires:      glassfish-policy
Requires:      istack-commons
Requires:      jboss-jaxws-2.2-api
Requires:      txw2
Requires:      xsom

%description tools
Open source Reference Implementation of
JSR-224: Java API for XML Web Services.

%package transports
Group:         Development/Java
Summary:       JAX-WS RI Transports Implementation
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:      istack-commons
Requires:      xmlstreambuffer

%description transports
This package provides Implementation of:
- Async-Client-Transport.
- Local-Transport (used mainly in tests)
for JAX-WS RI.

%package tools-javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}-tools

%description tools-javadoc
This package contains javadoc for %{name}-tools.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p1
sed -i "s|@VERSION@|%{version}|" etc/poms/*.pom
%patch9 -p1
%patch10 -p0
sed -i "s|@JAXWS_VERSION@|%{version}|" transports/*/*.pom

for d in CDDL+GPLv2.html CDDL+GPLv2.txt CDDL-1.0-license.txt LICENSE.txt README ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

# these tests fails
rm -r tools/wscompile/test/com/sun/tools/ws/ant/*.java

%build

%ant tools-build

for mod in local async-client-transport; do
(
 cd transports/${mod}
 %ant jar
)
done

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
install -m 644 build/lib/jaxws-rt.jar %{buildroot}%{_javadir}/%{name}/jaxws-rt.jar
install -m 644 build/lib/jaxws-tools.jar %{buildroot}%{_javadir}/%{name}/jaxws-tools.jar
install -m 644 httpspi-servlet/build/lib/jaxws-httpspi-servlet.jar %{buildroot}%{_javadir}/%{name}/jaxws-httpspi-servlet.jar
install -m 644 transports/async-client-transport/build/jaxws-async-client-transport.jar \
   %{buildroot}%{_javadir}/%{name}/jaxws-async-client-transport.jar
install -m 644 transports/local/build/jaxws-local-transport.jar \
   %{buildroot}%{_javadir}/%{name}/jaxws-local-transport.jar
   
# dirty hack
(
  cd %{buildroot}%{_javadir}/%{name}
  ln -sf jaxws-rt.jar jaxws-ri.jar
)

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 etc/poms/jaxws-ri.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxws-ri.pom
%add_maven_depmap JPP.%{name}-jaxws-ri.pom %{name}/jaxws-ri.jar
install -pm 644 etc/poms/jaxws-rt.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxws-rt.pom
%add_maven_depmap JPP.%{name}-jaxws-rt.pom %{name}/jaxws-rt.jar
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxws-httpspi-servlet.pom
%add_maven_depmap JPP.%{name}-jaxws-httpspi-servlet.pom %{name}/jaxws-httpspi-servlet.jar

install -pm 644 etc/poms/jaxws-tools.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxws-tools.pom
%add_maven_depmap JPP.%{name}-jaxws-tools.pom %{name}/jaxws-tools.jar -f tools

install -pm 644 transports/async-client-transport/jaxws-async-client-transport.pom \
   %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxws-async-client-transport.pom
install -pm 644 transports/local/jaxws-local-transport.pom \
   %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxws-local-transport.pom
%add_maven_depmap -f transports JPP.%{name}-jaxws-async-client-transport.pom %{name}/jaxws-async-client-transport.jar
%add_maven_depmap -f transports JPP.%{name}-jaxws-local-transport.pom %{name}/jaxws-local-transport.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/javadocs/rt/* %{buildroot}%{_javadocdir}/%{name}
mkdir -p %{buildroot}%{_javadocdir}/%{name}-tools
cp -rp build/javadocs/tools/* %{buildroot}%{_javadocdir}/%{name}-tools

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jaxws-ri.jar
%{_javadir}/%{name}/jaxws-rt.jar
%{_javadir}/%{name}/jaxws-httpspi-servlet.jar
%{_mavenpomdir}/JPP.%{name}-jaxws-ri.pom
%{_mavenpomdir}/JPP.%{name}-jaxws-rt.pom
%{_mavenpomdir}/JPP.%{name}-jaxws-httpspi-servlet.pom
%{_mavendepmapfragdir}/%{name}
%doc CDDL+GPLv2.html CDDL+GPLv2.txt CDDL-1.0-license.txt LICENSE.txt README

%files javadoc
%{_javadocdir}/%{name}
%doc CDDL+GPLv2.html CDDL+GPLv2.txt CDDL-1.0-license.txt LICENSE.txt README

%files tools
%{_javadir}/%{name}/jaxws-tools.jar
%{_mavenpomdir}/JPP.%{name}-jaxws-tools.pom
%{_mavendepmapfragdir}/%{name}-tools
%doc CDDL+GPLv2.html CDDL+GPLv2.txt CDDL-1.0-license.txt LICENSE.txt README

%files transports
%{_javadir}/%{name}/jaxws-*-transport.jar
%{_mavenpomdir}/JPP.%{name}-jaxws-*-transport.pom
%{_mavendepmapfragdir}/%{name}-transports
%doc CDDL+GPLv2.html CDDL+GPLv2.txt CDDL-1.0-license.txt LICENSE.txt README

%files tools-javadoc
%{_javadocdir}/%{name}-tools
%doc CDDL+GPLv2.html CDDL+GPLv2.txt CDDL-1.0-license.txt LICENSE.txt README

%changelog
* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.7-alt1_2jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt4_8jpp6
- build with new boss

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt3_8jpp6
- build with glassfish-jaxb21

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_8jpp6
- fixed components-info
- hack: added saaj-api/impl.jar though jaxws is built w/o them,
  for jbossas compatibility

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_8jpp6
- new version

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_4jpp5
- fixed components-info

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_4jpp5
- fixed repocop warnings

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_3jpp5.1
- NMU (by repocop): the following fixes applied:
 * windows-thumbnail-database-in-package for glassfish-jaxws-javadoc

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_3jpp5
- converted from JPackage by jppimport script

