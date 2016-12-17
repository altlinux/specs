Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: swig
# END SourceDeps(oneline)
BuildRequires: /usr/bin/pod2man
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
Name:          jets3t
Version:       0.9.3
Release:       alt1_4jpp8
Summary:       Java interface to Amazon S3 and CloudFront services
# nuvola theme is under LGPL 2.1
# src/org/jets3t/gui/TableSorter.java BSD
License:       ASL 2.0 and BSD and LGPLv2+
Url:           http://jets3t.s3.amazonaws.com/index.html
# hg clone https://bitbucket.org/jmurty/jets3t -r Release-0.9.3 jets3t-0.9.3
# find jets3t-0.9.3/ -name "*.class" -delete
# find jets3t-0.9.3/ -name "*.jar" -delete
# find jets3t-0.9.3/ -name "*.bat" -delete
# tar cJf jets3t-0.9.3.tar.xz jets3t-0.9.3
Source0:       %{name}-%{version}.tar.xz
# from Debian
Source5:       %{name}-cockpit.pod
Source6:       %{name}-cockpitlite.pod
Source7:       %{name}-synchronize.pod
Source8:       %{name}-uploader.pod

# fix java.home, jets3t.home, add system libraries refs
Patch0:        %{name}-0.9.3-scripts.patch
# fix license fsf-address
Patch1:        %{name}-0.9.0-nuvola-fsf-address.patch

Patch2:        %{name}-0.9.3-dist-build.patch

BuildRequires: ant
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-logging
BuildRequires: BareBonesBrowserLaunch
BuildRequires: bouncycastle
BuildRequires: dos2unix
BuildRequires: httpcomponents-client
BuildRequires: httpcomponents-core
BuildRequires: jackson
BuildRequires: java-base64
BuildRequires: java-xmlbuilder
BuildRequires: javamail
BuildRequires: junit
%if %{?fedora} >= 21
BuildRequires: log4j12
%else
BuildRequires: log4j
%endif
BuildRequires: maven-local
BuildRequires: mx4j
# pod2man
BuildRequires: %{_bindir}/pod2man
BuildRequires: sonatype-oss-parent
BuildRequires: glassfish-servlet-api

BuildArch:     noarch
Source44: import.info

%description
The JetS3t toolkit provides Java programmers with an API for interacting and
managing data stored in Amazon Simple Storage Service and Amazon CloudFront
content delivery network.

%package app
Group: Development/Java
Summary:       Graphical and command-line tools for Amazon S3 and CloudFront
Requires:      %{name} = %{version}
Requires:      apache-commons-codec
Requires:      apache-commons-logging
Requires:      avalon-framework
Requires:      avalon-logkit
Requires:      BareBonesBrowserLaunch
Requires:      base64
Requires:      bouncycastle
Requires:      geronimo-jms
Requires:      glassfish-servlet-api
Requires:      httpcomponents-client
Requires:      httpcomponents-core
Requires:      java
Requires:      java-xmlbuilder
Requires:      jpackage-utils
%if %{?fedora} >= 21
Requires:      log4j12
%else
Requires:      log4j
%endif

%description app
The JetS3t toolkit provides Java programmers with an API for interacting and
managing data stored in Amazon Simple Storage Service and Amazon CloudFront
content delivery network.

Features:
- jets3t-cockpitlite: A graphical application that Service Providers with S3
  accounts may provide to clients or customers without S3 accounts.
  jets3t-cockpitlite allows users to manage the content of an S3 account to
  upload files, download files, delete S3 objects and make objects publicly
  accessible. All these operations are mediated by a Gatekeeper service.
- jets3t-cockpit: graphical application for transferring files, viewing and
  managing the contents of an Amazon S3 account.
- jets3t-synchronize: A command-line application for synchronizing
  directories on your computer with an Amazon S3 account. Ideal for
  performing back-ups or synchronizing files between different computers.
- jets3t-uploader: A graphical application that Service Providers with S3
  accounts may provide to clients or customers without S3 accounts.
  jets3t-uploader allows users to upload files to S3 using a simple
  wizard-based work-flow, but all uploads must first be authorized by a
  Gatekeeper service
- gatekeeper: A servlet that acts as an authorization service running on a
  Service Provider's server to mediate access to S3 accounts.
  It processes requests from client applications such as JetS3t Uploader &
  CockpitLite, and authorizes the client application to perform operations
  such as uploads, downloads and deletes.

%package javadoc
Group: Development/Documentation
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
dos2unix dist-build.xml
%patch0 -p1
%if %{?fedora} < 21
sed -i "s|log4j12-1.2.17.jar|log4j.jar|" scripts/*.sh
sed -i "s|bcprov-jdk15on|bcprov-jdk16|" pom.xml
%else
sed -i "s|log4j.jar|log4j12-1.2.17.jar|" dist-build.xml
%endif
%patch1 -p0
%patch2 -p0



rm -rf src/contribs/com/centerkey/utils/BareBonesBrowserLaunch.java
sed -i "s|contribs.com.centerkey.utils.BareBonesBrowserLaunch|com.centerkey.utils.BareBonesBrowserLaunch|" \
 src/org/jets3t/apps/cockpit/Cockpit.java \
 src/org/jets3t/apps/cockpit/gui/StartupDialog.java \
 src/org/jets3t/apps/cockpitlite/CockpitLite.java \
 src/org/jets3t/apps/uploader/Uploader.java \
 src/org/jets3t/apps/cockpit/Cockpit.java \
 src/org/jets3t/apps/cockpit/gui/StartupDialog.java \
 src/org/jets3t/apps/cockpitlite/CockpitLite.java \
 src/org/jets3t/apps/uploader/Uploader.java

find . -name "*.war" -delete

# fix non ASCII chars
for s in test/org/jets3t/service/BaseStorageServiceTests.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

sed -i 's/\r//' LICENSE-2.0.txt NOTICE.txt resources/images/nuvola/license.txt

cp -p %{SOURCE5} .
cp -p %{SOURCE6} .
cp -p %{SOURCE7} .
cp -p %{SOURCE8} .

%pom_remove_plugin org.apache.maven.plugins:maven-jarsigner-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
# https://gil.fedorapeople.org/appassembler-1.9-1.fc20.src.rpm
%pom_remove_plugin org.codehaus.mojo:appassembler-maven-plugin
%pom_remove_plugin org.codehaus.mojo:sonar-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

%pom_remove_dep javax.activation:activation
%pom_add_dep com.centerkey.utils:BareBonesBrowserLaunch:3.1

#%% pom_remove_dep javax.servlet:javax.servlet-api
#%% pom_add_dep org.apache.tomcat:tomcat-servlet-api::provided

%mvn_alias net.java.dev.%{name}:%{name} ":cockpit"
%mvn_alias net.java.dev.%{name}:%{name} ":cockpitlite"
%mvn_alias net.java.dev.%{name}:%{name} ":%{name}-gui"
%mvn_alias net.java.dev.%{name}:%{name} ":synchronize"
%mvn_alias net.java.dev.%{name}:%{name} ":uploader"

%build

# test use web access
%mvn_build -f

ant -f dist-build.xml -Ddir.servlets=$PWD/servlet rebuild-gatekeeper

for m in cockpitlite cockpit synchronize uploader; do
  %{_bindir}/pod2man -c '' -r '' %{name}-${m}.pod > %{name}-${m}.1 ;
done

%install
%mvn_install

mkdir -p %{buildroot}%{_datadir}/%{name}/jars
(
  cd %{buildroot}%{_javadir}
  ln -sf ../../java/%{name}/%{name}.jar %{buildroot}%{_datadir}/%{name}/jars/%{name}-%{version}.jar
  ln -sf ../../java/%{name}/%{name}.jar %{buildroot}%{_datadir}/%{name}/jars/%{name}-gui-%{version}.jar
)

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/bin
for TOOL in cockpit cockpitlite synchronize uploader
do
  install -pm 755 scripts/$TOOL.sh %{buildroot}%{_bindir}/%{name}-$TOOL
  ln -sf ../../../bin/%{name}-$TOOL %{buildroot}%{_datadir}/%{name}/bin/$TOOL.sh

(
  cd %{buildroot}%{_javadir}
  ln -sf ../../java/%{name}/%{name}.jar %{buildroot}%{_datadir}/%{name}/jars/%{name}-$TOOL-%{version}.jar
)

done

chmod 0755  %{buildroot}%{_datadir}/%{name}/bin/*

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 %{name}-*.1 %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_sysconfdir}/%{name} %{buildroot}%{_datadir}/%{name}/configs
sed -i "s|{jets3t-version}|%{version}|" configs/cockpitlite.properties
cp -pr configs/* %{buildroot}%{_sysconfdir}/%{name}/
ln  -sf ../../../../etc/%{name}/cockpitlite.properties %{buildroot}%{_datadir}/%{name}/configs/
ln  -sf ../../../../etc/%{name}/commons-logging.properties %{buildroot}%{_datadir}/%{name}/configs/
ln  -sf ../../../../etc/%{name}/devpay_products.properties %{buildroot}%{_datadir}/%{name}/configs/
ln  -sf ../../../../etc/%{name}/%{name}.properties %{buildroot}%{_datadir}/%{name}/configs/
ln  -sf ../../../../etc/%{name}/log4j.properties %{buildroot}%{_datadir}/%{name}/configs/
ln  -sf ../../../../etc/%{name}/mime.types %{buildroot}%{_datadir}/%{name}/configs/
ln  -sf ../../../../etc/%{name}/simplelog.properties %{buildroot}%{_datadir}/%{name}/configs/
ln  -sf ../../../../etc/%{name}/synchronize.properties %{buildroot}%{_datadir}/%{name}/configs/
ln  -sf ../../../../etc/%{name}/test.properties %{buildroot}%{_datadir}/%{name}/configs/
ln  -sf ../../../../etc/%{name}/uploader.properties %{buildroot}%{_datadir}/%{name}/configs/

mkdir -p %{buildroot}%{_datadir}/%{name}/resources
cp -pr resources/* %{buildroot}%{_datadir}/%{name}/resources/
cp -pr servlets %{buildroot}%{_datadir}/%{name}/

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README.markdown RELEASE_NOTES.markdown
%doc LICENSE-2.0.txt NOTICE.txt

%files app
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/%{name}-*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/configs
%dir %{_datadir}/%{name}/jars
%dir %{_datadir}/%{name}/resources
%dir %{_datadir}/%{name}/servlets
%{_datadir}/%{name}/jars/*
%{_datadir}/%{name}/bin/*
%{_datadir}/%{name}/configs/*
%{_datadir}/%{name}/resources/*
%{_datadir}/%{name}/servlets/*
%{_mandir}/man1/*
%doc LICENSE-2.0.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt NOTICE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.3-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.3-alt1_3jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.3-alt1_2jpp8
- java 8 mass update

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt2_1jpp6
- fixed build with java 7

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt1_1jpp6
- new version

