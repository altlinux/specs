# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name eclipse-dtp
%define version 1.10.2
%global eclipse_base     %{_libdir}/eclipse
%global eclipse_dropin   %{_datadir}/eclipse/dropins

%global tag DTP_1_10_2_Release_201302061842
# Match the context qualifier with the upstream p2 repo
# 
# eclipse -consolelog -nosplash -application org.eclipse.equinox.p2.director \
#  -repository http://download.eclipse.org/datatools/updates -list | \
#  grep org.eclipse.datatools.sdk.feature.feature.group | grep %%{version} | \
#  sed "s/org.eclipse.datatools.sdk.feature.feature.group=//" | \
#  sed "s/%%{version}.//" | \
#  sed "s/-.*//"

# For 1.10 M6, use this zip
# http://www.eclipse.org/downloads/download.php?file=/datatools/downloads/drops/N_DTP_1.10/dtp-p2repo-1.10.0M6-201203160500.zip
# and get the IU list as above
%global qualifier v201302061842

Name:      eclipse-dtp
Version:   1.10.2
Release:   alt1_1jpp7
Summary:   Eclipse Data Tools Platform
Group:     System/Libraries
License:   EPL
URL:       http://www.eclipse.org/datatools/

# get-dtp.sh will download all these tarballs
Source0:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.build.git/snapshot/org.eclipse.datatools.build-%{tag}.tar.bz2
Source1:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.connectivity.git/snapshot/org.eclipse.datatools.connectivity-%{tag}.tar.bz2
Source2:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.doc.git/snapshot/org.eclipse.datatools.doc-%{tag}.tar.bz2
Source3:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.general.git/snapshot/org.eclipse.datatools.enablement.general-%{tag}.tar.bz2
Source4:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.hsqldb.git/snapshot/org.eclipse.datatools.enablement.hsqldb-%{tag}.tar.bz2
Source5:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.ibm.git/snapshot/org.eclipse.datatools.enablement.ibm-%{tag}.tar.bz2
Source6:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.ingres.git/snapshot/org.eclipse.datatools.enablement.ingres-%{tag}.tar.bz2
Source7:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.msft.git/snapshot/org.eclipse.datatools.enablement.msft-%{tag}.tar.bz2
Source8:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.mysql.git/snapshot/org.eclipse.datatools.enablement.mysql-%{tag}.tar.bz2
Source9:   http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.oda.git/snapshot/org.eclipse.datatools.enablement.oda-%{tag}.tar.bz2
Source10:  http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.oracle.git/snapshot/org.eclipse.datatools.enablement.oracle-%{tag}.tar.bz2
Source11:  http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.postgresql.git/snapshot/org.eclipse.datatools.enablement.postgresql-%{tag}.tar.bz2
Source12:  http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.sap.git/snapshot/org.eclipse.datatools.enablement.sap-%{tag}.tar.bz2
Source13:  http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.sqlite.git/snapshot/org.eclipse.datatools.enablement.sqlite-%{tag}.tar.bz2
Source14:  http://git.eclipse.org/c/datatools/org.eclipse.datatools.enablement.sybase.git/snapshot/org.eclipse.datatools.enablement.sybase-%{tag}.tar.bz2
Source15:  http://git.eclipse.org/c/datatools/org.eclipse.datatools.incubator.git/snapshot/org.eclipse.datatools.incubator-%{tag}.tar.bz2
Source16:  http://git.eclipse.org/c/datatools/org.eclipse.datatools.modelbase.git/snapshot/org.eclipse.datatools.modelbase-%{tag}.tar.bz2
Source17:  http://git.eclipse.org/c/datatools/org.eclipse.datatools.sqltools.git/snapshot/org.eclipse.datatools.sqltools-%{tag}.tar.bz2
Source18:  get-dtp.sh

# Build with Java 7 SQL interfaces
Patch0:    %{name}-java7.patch

# remove duplicate plugin from sqltools features (it's actually built in the
# connectivity feature)
Patch1:    %{name}-remove-duplicate-plugin.patch

Patch6:    %{name}-enable-newer-javax.wsdl.patch
Patch7:    %{name}-remove-javaxxml.patch 

%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%else
BuildArch:        noarch
%endif 

BuildRequires:    jpackage-utils
BuildRequires:    eclipse-pde >= 1:4.2.0-0.4
BuildRequires:    eclipse-emf-core >= 2.6.0
BuildRequires:    eclipse-emf
BuildRequires:    eclipse-gef >= 3.6.1
BuildRequires:    wsdl4j >= 1.5.2-6.6
BuildRequires:    xerces-j2 >= 2.7.1-10.3
BuildRequires:    xml-commons-resolver12 >= 1.1-2.15
BuildRequires:    xalan-j2 >= 2.7.0-7.5
BuildRequires:    xml-commons-apis >= 1.3.04-1.4
BuildRequires:    lpg-java-compat = 1.1.0

Requires:         jpackage-utils
Requires:         eclipse-platform >= 1:3.4.2
Requires:         eclipse-emf-core
Requires:         eclipse-emf
Requires:         eclipse-gef
Requires:         wsdl4j >= 1.5.2-6.6
Requires:         xerces-j2 >= 2.7.1-10.3
Requires:         xml-commons-resolver12 >= 1.1-2.15
Requires:         xalan-j2 >= 2.7.0-7.5
Requires:         xml-commons-apis >= 1.3.04-1.4
Requires:         lpg-java-compat = 1.1.0
Source44: import.info

%description
The Eclipse Data Tools Platform provides extensible frameworks and exemplary 
tools, enabling a diverse set of plug-in offerings specific to particular 
data-centric technologies and supported by the DTP ecosystem.

%prep
%setup -q -c dtp-%{version} -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17

# apply patches
pushd org.eclipse.datatools.connectivity-%{tag}/plugins/org.eclipse.datatools.connectivity.sqm.core
%patch0 -p3
popd
pushd org.eclipse.datatools.build-%{tag}
%patch1 -p1
popd

pushd org.eclipse.datatools.enablement.oda-%{tag}
%patch6 -p1
popd

pushd org.eclipse.datatools.build-%{tag}/
%patch7 -p2
popd

pushd org.eclipse.datatools.build-%{tag}/features
# Use any xerces version
sed -i -e "s|2.9.0.qualifier|0.0.0|g" \
  org.eclipse.datatools.enablement.oda.feature/feature.xml
popd

pushd org.eclipse.datatools.doc-%{tag}/packaged_jars
rm -rf *.jar
popd

# make sure upstream hasn't snuck in any jars we don't know about
JARS=""
for j in `find -name "*.jar"`; do
  if [ ! -L $j ]; then
    JARS="$JARS $j"
  fi
done
if [ ! -z "$JARS" ]; then
   echo "These jars should be deleted and symlinked to system jars: $JARS"
   # There are some test JARs that can remain
   #exit 1
fi

mkdir orbitDeps
pushd orbitDeps
ln -s %{_javadir}/lucene.jar lucene.jar
ln -s %{_javadir}/xerces-j2.jar org.apache.xerces_2.9.0.jar
ln -s %{_javadir}/xalan-j2-serializer.jar org.apache.xml.serializer_2.7.1.jar
ln -s %{_javadir}/xml-commons-resolver.jar org.apache.xml.resolver_1.2.0.jar
ln -s %{_javadir}/wsdl4j.jar javax.wsdl_1.5.1.jar
ln -s %{_javadir}/lpgjavaruntime.jar net.sourceforge.lpg.lpgjavaruntime_1.1.0.jar
ln -s %{_javadir}/emf/eclipse/plugins/org.eclipse.emf* .
popd

%build
OPTIONS="-DjavacTarget=1.5 -DjavacSource=1.5 -DforceContextQualifier=%{qualifier}"

# build all features except for documentation and SDK features TODO: build everything
eclipse-pdebuild -f org.eclipse.datatools.modelbase.feature \
  -d "emf gef" -o `pwd`/orbitDeps -a "$OPTIONS"
eclipse-pdebuild -f org.eclipse.datatools.connectivity.feature \
  -d "emf gef" -o `pwd`/orbitDeps -a "$OPTIONS"
eclipse-pdebuild -f org.eclipse.datatools.sqldevtools.feature \
  -d "emf gef" -o `pwd`/orbitDeps -a "$OPTIONS"
eclipse-pdebuild -f org.eclipse.datatools.enablement.feature \
  -d "emf gef" -o `pwd`/orbitDeps -a "$OPTIONS"

%install
install -d -m 755 %{buildroot}%{eclipse_dropin}
unzip -q -d %{buildroot}%{eclipse_dropin}/dtp-modelbase build/rpmBuild/org.eclipse.datatools.modelbase.feature.zip
unzip -q -d %{buildroot}%{eclipse_dropin}/dtp-connectivity build/rpmBuild/org.eclipse.datatools.connectivity.feature.zip
unzip -q -d %{buildroot}%{eclipse_dropin}/dtp-sqldevtools build/rpmBuild/org.eclipse.datatools.sqldevtools.feature.zip
unzip -q -d %{buildroot}%{eclipse_dropin}/dtp-enablement build/rpmBuild/org.eclipse.datatools.enablement.feature.zip

# use system bundles
pushd %{buildroot}%{eclipse_dropin}/dtp-enablement/eclipse/plugins
rm org.apache.xerces_*.jar
rm org.apache.xml.serializer_*.jar
ln -s ../../../../../java/xalan-j2-serializer.jar org.apache.xml.serializer_2.7.1.jar
rm org.apache.xml.resolver_*.jar
ln -s ../../../../../java/xml-commons-resolver.jar org.apache.xml.resolver_1.2.0.jar
rm javax.wsdl_*.jar
ln -s ../../../../../java/wsdl4j.jar javax.wsdl_1.5.1.jar
popd
pushd %{buildroot}%{eclipse_dropin}/dtp-sqldevtools/eclipse/plugins
rm net.sourceforge.lpg.lpgjavaruntime_*.jar
ln -s ../../../../../java/lpgjavaruntime.jar net.sourceforge.lpg.lpgjavaruntime_1.1.0.jar
popd

%files
%{eclipse_dropin}/dtp-modelbase
%{eclipse_dropin}/dtp-connectivity
%{eclipse_dropin}/dtp-sqldevtools
%{eclipse_dropin}/dtp-enablement
%doc org.eclipse.datatools.build-%{tag}/features/org.eclipse.datatools.sdk-all.feature/rootfiles/*

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1jpp7
- new version

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_2jpp7
- build with lucene3

* Fri Sep 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2_2jpp6
- built with java 6

* Thu Sep 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_2jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_1jpp6
- new version

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.7.2-alt1_1jpp6
- new version

