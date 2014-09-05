# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           olfs
Version:        1.9.5
Release:        alt1_3jpp7
Summary:        OPeNDAP Lightweight Frontend Servlet - client interface for Hyrax

Group:          System/Servers
License:        LGPLv2
URL:            http://opendap.org/download/hyrax?q=olfs
Source0:        http://www.opendap.org/pub/olfs/olfs-%{version}-src.tgz
Source1:        context.xml
# Patch to update to servlet3 api
Patch0:         olfs-servlet3.patch
BuildArch:      noarch
Patch33:	olfs-1.9.5-notest.patch

BuildRequires:  jpackage-utils
BuildRequires:  ant-junit
BuildRequires:  commons-codec
BuildRequires:  commons-httpclient
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  jdom
BuildRequires:  junit4
BuildRequires:  log4j
BuildRequires:  logback
BuildRequires:  saxon
BuildRequires:  slf4j
BuildRequires:  tomcat-lib
BuildRequires:  xalan-j2

Requires:       jpackage-utils
Requires:       tomcat
Requires:       commons-codec
Requires:       commons-httpclient
Requires:       apache-commons-cli
Requires:       apache-commons-lang
Requires:       apache-commons-logging
Requires:       jdom
Requires:       junit4
Requires:       log4j
Requires:       logback
Requires:       saxon
Requires:       slf4j
Requires:       xalan-j2
Source44: import.info


%description
The OPeNDAP Lightweight Frontend Servlet (OLFS) provides the public-
accessible client interface for Hyrax.  The OLFS communicates with the Back
End Server (BES) to provide data and catalog services to clients.  The OLFS
implements the DAP2 protocol and supports some of the new DAP4 features.  We
hope that other groups will develop new front end modules that will implement
other protocols.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1 -b .servlet3
find \( -name '*.class' -o -name '*.jar' \) -delete
# Fix FSF license
find -type f | xargs sed -i -e 's/[5]9 Temple Place,/51 Franklin Street,/' \
  -e 's/[S]uite 330,/Fifth Floor,/' -e 's/[0]2111-1307/02110-1301/'

#sed -i -e 's!target name="all" depends="clean,clients,check,server,soap-lib!target name="all" depends="clean,clients,server,soap-lib!;s!depends="clean,src-dist,doc-dist,server-dist,check"!depends="clean,src-dist,doc-dist,server-dist"!' build.xml
#patch33 -p1

%build
export CLASSPATH=`build-classpath commons-cli commons-codec commons-httpclient \
  commons-lang commons-logging jdom junit4 log4j logback saxon \
  servlet slf4j/api tomcat/catalina.jar xalan-j2 xalan-j2-serializer`
ant -Dbuild.sysclasspath=$CLASSPATH server


%install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/tomcat/webapps/opendap
#Explode the war file into webapps
unzip -d $RPM_BUILD_ROOT%{_datadir}/tomcat/webapps/opendap build/dist/opendap.war

#Allow symbolic links in the webapp
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/tomcat/webapps/opendap/META-INF/context.xml

#Move config to /etc/olfs
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/olfs
pushd $RPM_BUILD_ROOT%{_datadir}/tomcat/webapps/opendap/initialContent
for xml in *.xml
do
   mv $xml $RPM_BUILD_ROOT%{_sysconfdir}/olfs/
   ln -s ../../../../../../etc/olfs/$xml .
done

#Setup log directory
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/lib/tomcat/content/opendap
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/log/tomcat/opendap
ln -s ../../../../log/tomcat/opendap \
      $RPM_BUILD_ROOT%{_sharedstatedir}/lib/tomcat/content/opendap/logs

#Move javadocs out of webapp and into javadocdir
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
mv $RPM_BUILD_ROOT%{_datadir}/tomcat/webapps/opendap/docs \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc ChangeLog COPYRIGHT README
%dir %{_sysconfdir}/olfs
%config(noreplace) %{_sysconfdir}/olfs/*.xml
%{_datadir}/tomcat/webapps/opendap/
%attr(-,tomcat,tomcat) %{_sharedstatedir}/lib/tomcat/content/opendap
%attr(-,tomcat,tomcat) %{_sharedstatedir}/log/tomcat/opendap

%files javadoc
%doc COPYRIGHT
%{_javadocdir}/%{name}


%changelog
* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.5-alt1_3jpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.5-alt1_2jpp7
- new release

