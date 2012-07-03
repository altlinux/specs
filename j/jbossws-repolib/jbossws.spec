Packager: Igor Vlasenko <viy@altlinux.ru>
%define oldname jbossws
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%define _with_jdk6 1
%bcond_with jdk6

%define version_maj 2
%define version_min 0
%define version_rev 1
%define version_tag SP2
%define version_full %{version_maj}.%{version_min}.%{version_rev}.%{version_tag}

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jboss/jbossws/%{version_full}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define native_repodir %{_javadir}/repository.jboss.com/jboss/jbossws-native42/%{version_full}-brew
%define native_repodirlib %{native_repodir}/lib
%define native_repodirsrc %{native_repodir}/src

 
Summary:        JBoss Web Services
Name:           jbossws-repolib
Version:        %{version_maj}.%{version_min}.%{version_rev}
Release:        alt6_3.SP2.6jpp6
Epoch:          1
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com/jbossws/

BuildArch:      noarch

# svn export https://svn.jboss.org/repos/jbossws/stack/native/tags/jbossws-native-2.0.1.SP2 jbossws 
Source0:        %{oldname}-%{version}.%{version_tag}-src.tar.gz
Source1:        %{oldname}-component-info.xml
Source2:        jbossws-native42-component-info.xml
Source3:        %{oldname}-resources.zip
Source4:        %{oldname}-tp.tar.gz
Patch0:         jbossws-jpeg-image-encoder-exception.patch
Patch1:         jbossws-sun-ri-consumer-impl.patch
BuildRequires: ant
BuildRequires: bea-stax-api
BuildRequires: glassfish-jaf
BuildRequires: dom4j
BuildRequires: glassfish-javamail
BuildRequires: gnu-getopt
BuildRequires: javassist
BuildRequires: jaxbintros
BuildRequires: jbossas >= 4.2.2
BuildRequires: jboss-common
BuildRequires: jboss-remoting
BuildRequires: jbossws-common
BuildRequires: jbossws-framework
BuildRequires: jbossws-spi
BuildRequires: jbossxb
BuildRequires: jpackage-utils
BuildRequires: tomcat5-servlet-2.4-api
BuildRequires: ws-commons-policy
BuildRequires: wsdl4j
BuildRequires: wstx
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-security

Requires: bea-stax-api
Requires: glassfish-jaf
Requires: dom4j
Requires: glassfish-javamail
Requires: gnu-getopt
Requires: javassist
Requires: jbossas >= 4.2.2
Requires: jboss-common
Requires: jboss-remoting
Requires: jbossws-common
Requires: jbossws-framework
Requires: jbossws-spi
Requires: jbossxb
Requires: jpackage-utils
Requires: tomcat5-servlet-2.4-api
Requires: wsdl4j
Requires: wstx
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-security

%description
JBossWS an implementation of J2EE Web Services

%package     native42
Summary:     native42 component for jbossws
Group:       Development/Java

%description native42
native42 component for jbossws

%if %{with_repolib}
%package repolib
Summary:     Artifacts to be uploaded to a repository library
Group:       Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.

%package native42-repolib
Summary:     Artifacts to be uploaded to a repository library
Group:       Development/Java

%description native42-repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{oldname} 
%setup -q -n %{oldname} -D -T -a 4
%patch0 -p1
%if %with jdk6
%patch1 -p1
%endif

%build
export JBOSS_HOME=%{_datadir}/jbossas
mkdir thirdparty/

pushd thirdparty/
# Link available system jars
ln -s $(build-classpath activation) .
ln -s $(build-classpath ant) .
ln -s $(build-classpath dom4j) .
ln -s $(build-classpath gnu-getopt) getopt.jar
ln -s $(build-classpath javassist) .
ln -s $(build-classpath jboss-common/jboss-common) jboss-common-core.jar
ln -s $(build-classpath jbossas/jboss-j2ee) .
ln -s $(build-classpath jboss/jboss-jaxb-intros) .
ln -s $(build-classpath jboss-common/jboss-common) jboss-logging-spi.jar
ln -s $(build-classpath jboss-remoting) .
ln -s $(build-classpath jboss/jboss-xml-binding) .
ln -s $(build-classpath jbossas/jbosssx) .
ln -s $(build-classpath jbossws-common) .
ln -s $(build-classpath jbossws-framework) .
ln -s $(build-classpath jbossws-spi) .
ln -s $(build-classpath glassfish-javamail-monolithic) mail.jar
ln -s $(build-classpath ws-commons-policy) policy.jar
ln -s $(build-classpath tomcat5-servlet-2.4-api) servlet-api.jar
ln -s $(build-classpath bea-stax-api) stax-api.jar
ln -s $(build-classpath wsdl4j) .
ln -s $(build-classpath wstx/wstx-asl) wstx.jar
ln -s $(build-classpath xalan-j2) xalan.jar
ln -s $(build-classpath xalan-j2-serializer) .
ln -s $(build-classpath xmlsec) .
ln -s $(build-classpath xerces-j2) xercesImpl.jar
cp -a $JBOSS_HOME/server/all/deploy/ejb3.deployer .
ln -s $(build-classpath jbossas/jboss-ejb3x) ejb3.deployer/

# Copy pre-built files from tp
cp ../thirdpartyrepo/sun-jaxb/lib/jaxb-api.jar .
cp ../thirdpartyrepo/sun-jaxb/lib/jaxb-impl.jar .
cp ../thirdpartyrepo/sun-jaxb/lib/jaxb-xjc.jar .
cp ../thirdpartyrepo/sun-jaxws/lib/jaxws-tools.jar .
cp ../thirdpartyrepo/jboss/microcontainer/lib/jboss-dependency.jar .
cp ../thirdpartyrepo/jboss/microcontainer/lib/jboss-microcontainer.jar .

# Copy resources
cp -p %{SOURCE3} jbossws-jboss42-resources.zip
popd

mv ant.properties.example ant.properties

# Build jbossws
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djboss42.home=$JBOSS_HOME -Djboss.server.instance=all -Dchecksum.ok=true jars

%install

# Install to javadir
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{oldname}/native42/sar
unzip -q -d $RPM_BUILD_ROOT%{_javadir}/%{oldname}/native42/sar output/lib/%{oldname}-native42.sar
cp -p output/lib/jboss-jaxrpc.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}
cp -p output/lib/jboss-jaxws.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}
cp -p output/lib/jboss-saaj.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}
cp -p output/lib/jbossws-client.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}
cp -p output/lib/jbossws-core.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}
cp -p output/lib/jbossws-core-scripts.zip $RPM_BUILD_ROOT%{_javadir}/%{oldname}
cp -p output/lib/jbossws-core-src.zip $RPM_BUILD_ROOT%{_javadir}/%{oldname}

# -repolib
%if %{with_repolib}
    # jboss/jbossws
    install -d -m 755 $RPM_BUILD_ROOT%{repodir}
    install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
    install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml

    sed -i 's/@VERSION@/%{version}.%{version_tag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
    tag=`echo %{oldname}-%{version}-%{release} | sed 's|\.|_|g'`
    sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml

    install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
    install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}/jbossws-%{version_full}-src.tar.gz

    cp -p output/lib/jboss-jaxrpc.jar $RPM_BUILD_ROOT%{repodirlib}
    cp -p output/lib/jboss-jaxws.jar $RPM_BUILD_ROOT%{repodirlib}
    cp -p output/lib/jboss-saaj.jar $RPM_BUILD_ROOT%{repodirlib}
    cp -p output/lib/jbossws-client.jar $RPM_BUILD_ROOT%{repodirlib}
    cp -p output/lib/jbossws-core.jar $RPM_BUILD_ROOT%{repodirlib}
    cp -p output/lib/jbossws-core-scripts.zip $RPM_BUILD_ROOT%{repodirlib}
    cp -p output/lib/jbossws-core-src.zip $RPM_BUILD_ROOT%{repodirlib}

    # jboss/jbossws-native42
    install -d -m 755 $RPM_BUILD_ROOT%{native_repodir}
    install -d -m 755 $RPM_BUILD_ROOT%{native_repodirlib}
    install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{native_repodir}/component-info.xml
    sed -i 's/@VERSION@/%{version}.%{version_tag}-brew/g' $RPM_BUILD_ROOT%{native_repodir}/component-info.xml
    tag=`echo %{oldname}-%{version}-%{release} | sed 's|\.|_|g'`
    sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{native_repodir}/component-info.xml

    install -d -m 755 $RPM_BUILD_ROOT%{native_repodirsrc}
    install -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{native_repodirsrc}/jbossws-native42-%{version_full}-src.tar.gz

    cp -p output/lib/%{oldname}-native42.sar $RPM_BUILD_ROOT%{native_repodirlib}
%endif
%if %{with_repolib}


%files
%dir %{_javadir}/repository.jboss.com
%dir %{_javadir}/repository.jboss.com/jboss
%{_javadir}/repository.jboss.com/jboss/jbossws
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt6_3.SP2.6jpp6
- built with java 6 due to com.sun.image.codec.jpeg

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt5_3.SP2.6jpp6
- fixed build with glassfish-jaxws

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt4_3.SP2.6jpp6
- fixed components-info

* Mon Nov 01 2010 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt3_3.SP2.6jpp6
- build with wstx 3.2.8

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt2_3.SP2.6jpp6
- rebuild w/new xml-security

* Sun Mar 07 2010 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_3.SP2.6jpp5
- jboss repolib release

