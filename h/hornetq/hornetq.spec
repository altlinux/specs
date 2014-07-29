# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             hornetq
Version:          2.2.13
Release:          alt2_6jpp7
Summary:          High performance messaging system
Group:            Development/Java
License:          ASL 2.0
URL:              http://www.jboss.org/hornetq

# git clone git://github.com/hornetq/hornetq.git
# cd hornetq && git checkout HornetQ_2_2_13_AS7_Final && git checkout-index -f -a --prefix=hornetq-2.2.13/ 
# find hornetq-2.2.13/ -name '*.jar' -delete
# tar cafJ hornetq-2.2.13-CLEAN.tar.xz hornetq-2.2.13
Source0:          hornetq-%{version}-CLEAN.tar.xz

Patch0:           0001-Removed-maven-buildmagic-thirdparty-plugin-dependenc.patch
Patch1:           0002-Removed-spring-dependency.patch
Patch2:           0003-gui-aid-changes.patch
Patch3:           0004-JDK7-fix-for-FileChannel-constructor.patch
Patch4:           0005-Libraries-paths.patch
Patch5:           0006-Make-creation-of-pom-files-easier.patch
Patch6:           0007-Add-jdepend-dependency-to-run-javadoc-creation.patch
Patch7:           0008-Native-build-fixes.patch

BuildRequires:    jpackage-utils
BuildRequires:    ant

BuildRequires:    automake libtool autoconf
BuildRequires:    apiviz
BuildRequires:    apache-commons-logging
BuildRequires:    javacc
BuildRequires:    jboss-connector-1.6-api
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-ejb3-ext-api
BuildRequires:    jboss-jaspi-1.0-api
BuildRequires:    jboss-jms-1.1-api
BuildRequires:    jboss-jts
BuildRequires:    jboss-logging
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jboss-transaction-spi
BuildRequires:    jboss-logging
BuildRequires:    jdepend
BuildRequires:    libaio-devel
BuildRequires:    netty

Requires:         jpackage-utils

Requires:         apache-commons-logging
Requires:         jboss-connector-1.6-api
Requires:         jboss-ejb-3.1-api
Requires:         jboss-ejb3-ext-api
Requires:         jboss-jaspi-1.0-api
Requires:         jboss-jms-1.1-api
Requires:         jboss-jts
Requires:         jboss-logging
Requires:         jboss-servlet-3.0-api
Requires:         jboss-transaction-1.1-api
Requires:         jboss-transaction-spi
Requires:         jboss-logging
Requires:         jdepend
Requires:         netty
Source44: import.info

%description
HornetQ is an open source project to build a multi-protocol, embeddable,
very high performance, clustered, asynchronous messaging system.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package devel
Summary:          Native development files for %{name}
Group:            Development/Java
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the support files which can be used to
build applications using the HornetQ native library.

%prep
%setup -q -n hornetq-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

mkdir -p thirdparty/net/java/dev/javacc/lib/ thirdparty/org/jboss/apiviz/lib/

ln -s $(build-classpath javacc) thirdparty/net/java/dev/javacc/lib/javacc.jar
ln -s $(build-classpath apiviz) thirdparty/org/jboss/apiviz/lib/apiviz.jar
ln -s $(build-classpath jdepend) thirdparty/org/jboss/apiviz/lib/jdepend.jar

%build
# Build jars and javadocs
ant -Dnodownload=true -Dhornetq.run_script=true jar-core jar-core-client jar-jms jar-jms-client jar-ra javadoc

# Create POMs
ant -f build-maven.xml deploy

# Build native bits
export JAVA_HOME=/usr/lib/jvm/java

pushd native
# Generate C headers
pushd src
javah -classpath ../../build/jars/hornetq-core.jar org.hornetq.core.asyncio.impl.AsynchronousFileImpl
popd

autoreconf --install
%configure
make %{?_smp_mflags}
popd

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

for m in core-client core jms-client jms ra; do
  # JAR
  install -pm 644 build/jars/hornetq-${m}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar

  # POM
  install -pm 644 hornetq-${m}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom

  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# APIDOCS
cp -rp build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install native bits
pushd native
make install DESTDIR=$RPM_BUILD_ROOT
popd

# Remove static files
rm $RPM_BUILD_ROOT/%{_libdir}/*.la

# Rename the executable file by prefixing it
mv $RPM_BUILD_ROOT/%{_bindir}/disktest $RPM_BUILD_ROOT/%{_bindir}/%{name}-disktest

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%{_libdir}/libHornetQAIO.so.*
%{_bindir}/%{name}-disktest
%doc licenses/LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc licenses/LICENSE.txt

%files devel
%{_libdir}/libHornetQAIO.so
%doc licenses/LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt1_5jpp7
- new version

