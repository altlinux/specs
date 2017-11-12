Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          thredds
Version:       4.6.2
Release:       alt1_6jpp8
Summary:       Thematic Realtime Environmental Distributed Data Services (TDS)
# GPLv3: opendap/src/main/java/opendap/dap/parsers/DapParser.java
# LGPLv3: opendap/src/main/java/opendap/servlet/AsciiWriter.java
#         visad/src/main/java/ucar/nc2/iosp/mcidas/V5DStruct.java
#         grib/src/main/java/ucar/jpeg
# ASL: tds/src/main/java/thredds/servlet/URLEncoder.java
License:       ASL 2.0 and BSD
URL:           http://www.unidata.ucar.edu/software/tds/
# sh thredds-create-tarball.sh < VERSION >
Source0:       %{name}-%{version}-clean.tar.xz
Source1:       %{name}-create-tarball.sh

Patch0:        thredds-4.6.2-use-proper-system-environment-variables.patch
# jj2000 is non free:
# https://www.redhat.com/archives/fedora-legal-list/2008-December/msg00004.html
Patch1:        thredds-4.6.2-remove-jj2000-support.patch

# Support for log4j 2.5
Patch2:        thredds-4.6.2-log4j.patch

BuildRequires: bison >= 3.0
BuildRequires: maven-local
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.protobuf:protobuf-java)
BuildRequires: mvn(com.sleepycat:je)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java.dev.jna:jna)
BuildRequires: mvn(net.jcip:jcip-annotations)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.httpcomponents:httpcore)
BuildRequires: mvn(org.apache.logging.log4j:log4j-api)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.logging.log4j:log4j-slf4j-impl)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-report-plugin)
BuildRequires: mvn(org.jdom:jdom2)
BuildRequires: mvn(org.jsoup:jsoup)
BuildRequires: mvn(org.quartz-scheduler.internal:quartz-core)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-jdk14)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-web)

# TODO: opendap, tds, and ... modules
%if 0
# https://github.com/coverity/coverity-security-library
BuildRequires: mvn(com.coverity.security:coverity-escapers:1.1.1)
# https://github.com/eclipsesource/restfuse
BuildRequires: mvn(com.restfuse:com.eclipsesource.restfuse:1.0.0)
BuildRequires: mvn(EDS:threddsIso)
BuildRequires: mvn(org.bounce:bounce)
BuildRequires: mvn(org.imgscalr:imgscalr-lib)
# https://github.com/52North/OX-Framework/
BuildRequires: mvn(org.n52.sensorweb:52n-oxf-xmlbeans)
# https://github.com/52North/common-xml/
BuildRequires: mvn(org.n52.sensorweb:52n-xml-gml-v321)
BuildRequires: mvn(org.n52.sensorweb:52n-xml-om-v20)
BuildRequires: mvn(org.n52.sensorweb:52n-xml-sampling-v20)
BuildRequires: mvn(org.n52.sensorweb:52n-xml-sweCommon-v20)
BuildRequires: mvn(org.n52.sensorweb:52n-xml-waterML-v20)
BuildRequires: mvn(org.opengis:geoapi-pending)
# https://github.com/Unidata/ncWMS/
BuildRequires: mvn(uk.ac.rdg.resc:ncwms)
# NON free
BuildRequires: mvn(edu.ucar:jj2000)
BuildRequires: mvn(edu.wisc.ssec:visad)
%endif

BuildArch:     noarch
Source44: import.info

%description
The THREDDS (Thematic Realtime Environmental Distributed
Data Services) project is developing middle-ware to bridge the
gap between data providers and data users. The goal is to
simplify the discovery and use of scientific data and to allow
scientific publications and educational materials to reference
scientific data. The mission of THREDDS is for students,
educators and researchers to publish, contribute, find, and
interact with data relating to the Earth system in a convenient,
effective, and integrated fashion. Just as the World Wide Web and
digital-library technologies have simplified the process of
publishing and accessing multimedia documents, THREDDS is building
infrastructure needed for publishing and accessing scientific data
in a similarly convenient fashion.

%package -n netcdf-java
Group: Development/Java
Summary:       Java interface to NetCDF files

%description -n netcdf-java
The NetCDF-Java Library is a Java interface to NetCDF files,
as well as to many other types of scientific data formats.

%package bufr
Group: Development/Java
Summary:       BUFR IOSP

%description bufr
Reading BUFR files with the NetCDF-java library.

%package clcommon
Group: Development/Java
Summary:       Client-side common library

%description clcommon
A collection of utilities needed client-side,
including java.awt dependencies and assorted IOSPs.

%package dap
Group: Development/Java
Summary:       THREDDS DAP4 Protocol Services

%description dap
THREDDS DAP4 Protocol Services.

%package grib
Group: Development/Java
Summary:       GRIB IOSP and Feature Collection

%description grib
Decoder for the GRIB format.

%package httpservices
Group: Development/Java
Summary:       THREDDS HttpClient Wrappers

%description httpservices
THREDDS HttpClient Wrappers.

%package netcdf
Group: Development/Java
Summary:       THREDDS netCDF-4 IOSP JNI connection to C library

%description netcdf
THREDDS netCDF-4 IOSP JNI connection to C library.

%package tdcommon
Group: Development/Java
Summary:       THREDDS Server Common Utilities

%description tdcommon
THREDDS Server Common Utilities.

%package tdm
Group: Development/Java
Summary:       THREDDS Data Manager (TDM)

%description tdm
THREDDS Data Manager (TDM).

%package -n java-udunits
Group: Development/Java
Summary:       Java package for decoding and encoding unit specifications

%description -n java-udunits
The ucar.units Java package is for decoding and encoding
formatted unit specifications (e.g. "m/s"), converting numeric values
between compatible units (e.g. between "m/s" and "knot"), and for
performing arithmetic operations on units (e.g. dividing one unit by
another, raising a unit to a power).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
rm -rf grib/src/main/java/ucar/nc2/grib/grib2/Grib2JpegDecoder.java
%patch2 -p1

sed -i 's/\r//' cdm/CHANGES.txt LICENSE.txt

# Disable unavailable build deps
%pom_disable_module cdm-test
%pom_disable_module dap4/d4tests
%pom_disable_module dap4/d4tswar
%pom_disable_module it
%pom_disable_module ncIdv
# thredds use customized opendap == 0.0.7 http://www.opendap.org/
%pom_disable_module opendap
%pom_disable_module opendap/dtswar
%pom_disable_module tds
%pom_disable_module ui
%pom_disable_module visad
%pom_disable_module waterml

%pom_remove_dep org.n52.sensorweb:
# waterml visadCdm opendap clcommon

#%% pom_xpath_set -r "pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:configuration/pom:archive/pom:manifest/pom:addClasspath" false

# fix for httpcore-4.4.5
sed -i '/org.apache.http.annotation/d' \
 httpservices/src/main/java/ucar/httpservices/HTTPAuthScope.java

%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_xpath_set "pom:properties/pom:org.quartz-scheduler.version" 2.2.1
%pom_change_dep -r org.quartz-scheduler:quartz org.quartz-scheduler.internal:quartz-core

%mvn_package ':d4*' dap

%mvn_package ':cdm::tests:' cdm 
%mvn_alias :cdm :netcdf

%build
# Regnerate java source code
(
 cd dap4/grammars
 make bison
)
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}-parent
%doc README.md
%doc LICENSE.txt

%files -n netcdf-java -f .mfiles-cdm
%doc cdm/CHANGES.txt
%doc LICENSE.txt

%files bufr -f .mfiles-bufr
%doc LICENSE.txt

%files clcommon -f .mfiles-clcommon
%doc LICENSE.txt

%files dap -f .mfiles-dap
%doc LICENSE.txt

%files grib -f .mfiles-grib
%doc LICENSE.txt

%files httpservices -f .mfiles-httpservices
%doc LICENSE.txt

%files netcdf -f .mfiles-netcdf4
%doc LICENSE.txt

%files tdcommon -f .mfiles-tdcommon
%doc LICENSE.txt

%files tdm -f .mfiles-tdm
%doc LICENSE.txt

%files -n java-udunits -f .mfiles-udunits
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 4.6.2-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 4.6.2-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 4.6.2-alt1_4jpp8
- new fc release

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 4.6.2-alt1_3jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 4.6.2-alt1_1jpp8
- new version

