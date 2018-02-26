Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with jdk6

%define version_maj 3
%define version_min 0
%define version_rev 1
%define version_tag GA
%define version_full %{version_maj}.%{version_min}.%{version_rev}.%{version_tag}
%define version_full_real %{version_maj}.%{version_min}.%{version_rev}-native-2.0.4.%{version_tag}

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jboss/jbossws/3.0.1-native-2.0.4.GA-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

Name:           jbossws-native
Version:        %{version_maj}.%{version_min}.%{version_rev}
Release:        alt9_1jpp6
Epoch:          1
Summary:        JBoss Web Services
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com/jbossws/
# svn export http://anonsvn.jboss.org/repos/jbossws/stack/native/tags/jbossws-native-3.0.1.GA/
# tar cjf jbossws-native-3.0.1.GA.tar.bz2 jbossws-native-3.0.1.GA
Source0:        %{name}-%{version_full}.tar.bz2
Source1:        %{name}-component-info.xml
Source2:        http://anonsvn.jboss.org/repos/repository.jboss.org/jboss/jbossws-jboss42/4.2.1.GA/lib/jbossws-jboss42-resources.zip
Patch0:         jbossws-native-jpeg-image-encoder-exception.patch
Patch1:         jbossws-native-no-classpath-in-manifest.patch
Provides:       jbossws = %{epoch}:%{version}-%{release}
Obsoletes:      jbossws < %{epoch}:%{version}-%{release}
Requires: annotation_1_0_api
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
Requires: ws-commons-policy
Requires: wsdl4j16
Requires: wstx
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-security
Requires: glassfish-jaxb
Requires: glassfish-jaxws
Requires: jboss-microcontainer
Requires: jettison
Requires: sun-fi
Requires: jaxbintros
BuildRequires: annotation_1_0_api
BuildRequires: ant
BuildRequires: bea-stax-api
BuildRequires: glassfish-jaf
BuildRequires: dom4j
BuildRequires: glassfish-javamail
BuildRequires: gnu-getopt
BuildRequires: javassist
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
BuildRequires: wsdl4j16
BuildRequires: wstx
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-security
%if 0
jboss-jaxrpc.jar jboss-saaj.jar
%endif
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxws
BuildRequires: jboss-microcontainer
#BuildRequires:  jbossws-native
BuildRequires: jettison
BuildRequires: sun-fi
BuildRequires: jaxbintros
BuildArch:      noarch

%description
JBossWS an implementation of J2EE Web Services

%if %{with_repolib}
%package repolib
Summary:     Artifacts to be uploaded to a repository library
Group:       Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}-%{version_full} 
%{_bindir}/find -type f -name '*.?ar' | %{_bindir}/xargs -t %{__rm}
%patch0 -p1
%if %with jdk6
%patch1 -p1
%endif

%{__mkdir_p} thirdparty

export JBOSS_HOME=%{_datadir}/jbossas

pushd thirdparty
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
ln -s $(build-classpath wsdl4j/wsdl4j16) wsdl4j.jar
ln -s $(build-classpath wstx/wstx-asl) wstx.jar
ln -s $(build-classpath xalan-j2) xalan.jar
ln -s $(build-classpath xalan-j2-serializer) .
ln -s $(build-classpath xmlsec) .
ln -s $(build-classpath xerces-j2) xercesImpl.jar
%{__cp} -a $JBOSS_HOME/server/all/deploy/ejb3.deployer .
ln -s $(build-classpath jbossas/jboss-ejb3x) ejb3.deployer/

# Copy pre-built files from tp
ln -s $(build-classpath glassfish-jaxb/jaxb-api) .
ln -s $(build-classpath glassfish-jaxb/jaxb-impl) .
ln -s $(build-classpath glassfish-jaxb/jaxb-xjc) .
ln -s $(build-classpath sun-jaxws/jaxws-tools) .
ln -s $(build-classpath jboss-microcontainer/jboss-dependency) .
ln -s $(build-classpath jboss-microcontainer/jboss-microcontainer) .

ln -s $(build-classpath jbossws/jbossws-client) .
ln -s $(build-classpath jettison) .
ln -s $(build-classpath sun-fi) FastInfoset.jar

%{__cp} -p %{SOURCE2} jbossws-jboss42-resources.zip
popd

%{__cp} -p ant.properties.example ant.properties

%build
export CLASSPATH=$(build-classpath annotation_1_0_api)
export OPT_JAR_LIST=:
export JBOSS_HOME=%{_datadir}/jbossas
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djboss42.home=$JBOSS_HOME -Djboss.server.instance=all -Dchecksum.ok=true jars

%install

%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_javadir}/jbossws
%{__mkdir_p} %{buildroot}%{_sysconfdir}/jbossws

%{__cp} -p output/lib/jbossws-client.jar %{buildroot}%{_javadir}/jbossws
%{__cp} -p output/lib/jbossws-core.jar %{buildroot}%{_javadir}/jbossws
%{__cp} -p output/lib/jboss-jaxrpc.jar %{buildroot}%{_javadir}/jbossws
%{__cp} -p output/lib/jboss-jaxws.jar %{buildroot}%{_javadir}/jbossws
%{__cp} -p output/lib/jboss-jaxws-ext.jar %{buildroot}%{_javadir}/jbossws
%{__cp} -p output/lib/jboss-saaj.jar %{buildroot}%{_javadir}/jbossws
%{__cp} -p output/lib/jbossws-core-src.zip %{buildroot}%{_javadir}/jbossws
%{__cp} -p output/lib/jbossws-context.war %{buildroot}%{_javadir}/jbossws
%{__cp} -p output/etc/wsrunclient.sh %{buildroot}%{_bindir}/jbossws-wsrunclient
%{__cp} -p output/etc/wstools.sh %{buildroot}%{_bindir}/jbossws-wstools
%{__cp} -p output/resources/standard-jaxrpc-client-config.xml %{buildroot}%{_sysconfdir}/jbossws
%{__cp} -p output/resources/standard-jaxrpc-endpoint-config.xml %{buildroot}%{_sysconfdir}/jbossws
%{__cp} -p output/resources/standard-jaxws-client-config.xml %{buildroot}%{_sysconfdir}/jbossws
%{__cp} -p output/resources/standard-jaxws-endpoint-config.xml %{buildroot}%{_sysconfdir}/jbossws
%{__cp} -p output/resources/jbossws-native42-beans.xml %{buildroot}%{_sysconfdir}/jbossws
%{__cp} -p output/resources/jbossws-native50-beans.xml %{buildroot}%{_sysconfdir}/jbossws
%{__cp} -p ant-import/jbossws-deploy-macros.xml %{buildroot}%{_sysconfdir}/jbossws
%{__cp} -p ant-import/jbossws-default-deploy.conf %{buildroot}%{_sysconfdir}/jbossws/jbossws-deploy.conf

%if %{with_repolib}
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodir}/bin
%{__mkdir_p} %{buildroot}%{repodir}/resources
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__mkdir_p} %{buildroot}%{repodirsrc}

%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i 's/@VERSION@/%{version_full_real}-brew/g' %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml

%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{PATCH1} %{buildroot}%{repodirsrc}

%{__install} -p -m 0644 output/lib/jbossws-client.jar %{buildroot}%{repodirlib}
%{__install} -p -m 0644 output/lib/jbossws-core.jar %{buildroot}%{repodirlib}
%{__install} -p -m 0644 output/lib/jboss-jaxrpc.jar %{buildroot}%{repodirlib}
%{__install} -p -m 0644 output/lib/jboss-jaxws.jar %{buildroot}%{repodirlib}
%{__install} -p -m 0644 output/lib/jboss-jaxws-ext.jar %{buildroot}%{repodirlib}
%{__install} -p -m 0644 output/lib/jboss-saaj.jar %{buildroot}%{repodirlib}
%{__install} -p -m 0644 output/lib/jbossws-core-src.zip %{buildroot}%{repodirlib}
%{__install} -p -m 0644 output/lib/jbossws-context.war %{buildroot}%{repodirlib}
%{__install} -p -m 0755 output/etc/wsrunclient.bat %{buildroot}%{repodir}/bin
%{__install} -p -m 0755 output/etc/wsrunclient.sh %{buildroot}%{repodir}/bin
%{__install} -p -m 0755 output/etc/wstools.bat %{buildroot}%{repodir}/bin
%{__install} -p -m 0755 output/etc/wstools.sh %{buildroot}%{repodir}/bin
%{__install} -p -m 0644 output/resources/standard-jaxrpc-client-config.xml %{buildroot}%{repodir}/resources
%{__install} -p -m 0644 output/resources/standard-jaxrpc-endpoint-config.xml %{buildroot}%{repodir}/resources
%{__install} -p -m 0644 output/resources/standard-jaxws-client-config.xml %{buildroot}%{repodir}/resources
%{__install} -p -m 0644 output/resources/standard-jaxws-endpoint-config.xml %{buildroot}%{repodir}/resources
%{__install} -p -m 0644 output/resources/jbossws-native42-beans.xml %{buildroot}%{repodir}/resources
%{__install} -p -m 0644 output/resources/jbossws-native50-beans.xml %{buildroot}%{repodir}/resources
%{__install} -p -m 0644 ant-import/jbossws-deploy-macros.xml %{buildroot}%{repodir}/resources
%{__install} -p -m 0644 ant-import/jbossws-default-deploy.conf %{buildroot}%{repodir}/bin/jbossws-deploy.conf
%endif

%files
%attr(0755,root,root) %{_bindir}/jbossws-wsrunclient
%attr(0755,root,root) %{_bindir}/jbossws-wstools
%{_javadir}/jbossws
%dir %{_sysconfdir}/jbossws
%config(noreplace) %{_sysconfdir}/jbossws/standard-jaxrpc-client-config.xml
%config(noreplace) %{_sysconfdir}/jbossws/standard-jaxrpc-endpoint-config.xml
%config(noreplace) %{_sysconfdir}/jbossws/standard-jaxws-client-config.xml
%config(noreplace) %{_sysconfdir}/jbossws/standard-jaxws-endpoint-config.xml
%config(noreplace) %{_sysconfdir}/jbossws/jbossws-native42-beans.xml
%config(noreplace) %{_sysconfdir}/jbossws/jbossws-native50-beans.xml
%config(noreplace) %{_sysconfdir}/jbossws/jbossws-deploy-macros.xml
%config(noreplace) %{_sysconfdir}/jbossws/jbossws-deploy.conf

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt9_1jpp6
- built with java 6 due to com.sun.image.codec.jpeg

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt8_1jpp6
- support for jboss-remoting 2.5.1

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt7_1jpp6
- fixed build with new glassfish-jaxb

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt6_1jpp6
- fixed build with glassfish-jaxws

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt5_1jpp6
- fixed components-info

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt4_1jpp6
- fixed jaxbintros version in repolib

* Mon Nov 01 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt3_1jpp6
- build with wstx 3.2.8

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt2_1jpp6
- rebuild with new xml-security

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt1_1jpp5
- full version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt0.1jpp
- bootstrap for jbossas

