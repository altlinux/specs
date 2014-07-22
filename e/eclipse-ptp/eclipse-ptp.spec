# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libslurm-devel maven perl(Exporter.pm) perl(FindBin.pm) perl(Storable.pm) perl(Switch.pm) perl(Text/ParseWords.pm) perl(Time/HiRes.pm) perl(Time/Local.pm) perl(XML/Parser.pm) unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global ptpver                  6.0.5
%global photranver              8.0.5
%global eclipse_base            %{_datadir}/eclipse
%global cdtreq                  1:8.1.0
%global pdereq                  1:4.2.0
%global rsereq                  3.2
%global pdebuild                %{_bindir}/eclipse-pdebuild
%global ptp_build_id            201303141502
#global ptp_git_tag             PTP_6_0_2
%global ptp_git_tag             7b02da97811f7eb9b57083da04da78a71e94cf5e
%global photran_build_id        201303141447
#global photran_git_tag         PTP_6_0_2
%global photran_git_tag         a3b657517fd448af21dbcfa9bf05e0e2cb36fbbb

Summary:        Eclipse Parallel Tools Platform
Name:           eclipse-ptp
# Be sure to update photran version if needed
Version:        %{ptpver}
Release:        alt1_2jpp7
License:        EPL
Group:          Development/Java
URL:            http://www.eclipse.org/ptp

# The following tarballs were downloaded from the git repositories
Source0:        http://git.eclipse.org/c/ptp/org.eclipse.ptp.git/snapshot/org.eclipse.ptp-%{ptp_git_tag}.tar.gz
Source1:        http://git.eclipse.org/c/ptp/org.eclipse.photran.git/snapshot/org.eclipse.photran-%{photran_git_tag}.tar.gz
# These are made with makesource.sh
#Source0:        org.eclipse.ptp-%{ptp_git_tag}.tar.xz
#Source1:        org.eclipse.photran-%{photran_git_tag}.tar.xz
Source2:        makesource.sh
# To help generate the needed Requires
Source3:        finddeps.sh

# Remove dependency specifications on ant-trax
Patch0:         eclipse-ptp-notrax.patch
# Remove rdt.remotetools from ptp feature
Patch1:         eclipse-ptp-noremote.patch
# Fix gridengine NPE
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=405024
Patch2:         eclipse-ptp-gridengine.patch

# Remove some unneeded dependencies
BuildRequires:  maven-local
BuildRequires:  tycho
BuildRequires:  eclipse-cdt-parsers >= %{cdtreq}
#BuildRequires: eclipse-cdt-tests
# >= 1:6.0.2
BuildRequires:  eclipse-jgit
BuildRequires:  eclipse-rse >= %{rsereq}
BuildRequires:  lpg-java-compat = 1.1.0

BuildArch:      noarch

Requires:       eclipse-cdt >= %{cdtreq}
# Pulled in by rdt.remotetools being in ptp main
Requires:       %{name}-rdt = %{version}-%{release}
Provides:       %{name}-cdt-compilers = %{version}-%{release}
Obsoletes:      %{name}-cdt-compilers < %{version}-%{release}
Provides:       %{name}-pldt = %{version}-%{release}
Obsoletes:      %{name}-pldt < %{version}-%{release}
Provides:       %{name}-pldt-openacc = %{version}-%{release}
Obsoletes:      %{name}-pldt-openacc < %{version}-%{release}
Provides:       %{name}-rdt-remotetools = %{version}-%{release}
Obsoletes:      %{name}-rdt-remotetools < %{version}-%{release}
Provides:       %{name}-rdt-sdk = %{version}-%{release}
Obsoletes:      %{name}-rdt-sdk < %{version}-%{release}
Provides:       %{name}-rdt-sync = %{version}-%{release}
Obsoletes:      %{name}-rdt-sync < %{version}-%{release}
Provides:       %{name}-rdt-xlc-sdk = %{version}-%{release}
Obsoletes:      %{name}-rdt-xlc-sdk < %{version}-%{release}
Source44: import.info

%description
The aim of the parallel tools platform project is to produce an open-source
industry-strength platform that provides a highly integrated environment
specifically designed for parallel application development. The project will
provide:

 - a standard, portable parallel IDE that supports a wide range of parallel
   architectures and run-time systems
 - a scalable parallel debugger
 - support for the integration of a wide range of parallel tools
 - an environment that simplifies the end-user interaction with parallel
   systems

This package contains the main PTP run-time features.


%package        master
Summary:        Complete PTP package
Group:          Development/Java
Requires:       eclipse-cdt >= %{cdtreq}
Requires:       %{name} = %{version}-%{release}

#master package is a virtual package that requires all of the components
Requires:       %{name}-etfw-ppw = %{version}-%{release}
Requires:       %{name}-etfw-tau = %{version}-%{release}
Requires:       %{name}-etfw-tau-fortran = %{version}-%{release}
Requires:       %{name}-fortran = %{version}-%{release}
Requires:       %{name}-gem = %{version}-%{release}
Requires:       %{name}-pldt-fortran = %{version}-%{release}
Requires:       %{name}-pldt-upc = %{version}-%{release}
Requires:       %{name}-rdt = %{version}-%{release}
Requires:       %{name}-rdt-xlc = %{version}-%{release}
Requires:       %{name}-remote-rse = %{version}-%{release}
Requires:       %{name}-rm-contrib = %{version}-%{release}
Requires:       %{name}-sci = %{version}-%{release}
Requires:       %{name}-sdk = %{version}-%{release}
Requires:       eclipse-photran = %{photranver}-%{release}
Requires:       eclipse-photran-intel = %{photranver}-%{release}
Requires:       eclipse-photran-xlf = %{photranver}-%{release}

%description    master
The package will bring in all of the PTP components.


%package        etfw-ppw
Summary:        PTP Parallel Performance Wizard (PPW)
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description    etfw-ppw
Adds support for Parallel Performance Wizard (PPW).


%package        etfw-tau
Summary:        PTP External Tools Framework TAU Support
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description    etfw-tau
Extends the external tools framework with capabilities specific
to the TAU performance analysis system.


%package        etfw-tau-fortran
Summary:        PTP External Tools Framework: TAU Fortran Enabler
Group:          Development/Java
Requires:       %{name}-etfw-tau = %{version}-%{release}
Requires:       eclipse-photran = %{photranver}-%{release}

%description    etfw-tau-fortran
Adds selective instrumentation functionality for Fortran via the
Photran project.


%package        fortran
Summary:        PTP Fortran Support
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-etfw-tau-fortran = %{version}-%{release}
Requires:       %{name}-pldt-fortran = %{version}-%{release}
Requires:       %{name}-rdt-sync-fortran = %{version}-%{release}
Requires:       eclipse-photran = %{photranver}-%{release}
Requires:       eclipse-photran-intel = %{photranver}-%{release}
Requires:       eclipse-photran-xlf = %{photranver}-%{release}

%description    fortran
Adds Fortran support to PTP.


%package        gem
Summary:        PTP Graphical Explorer of MPI Programs (GEM)
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description    gem
GEM serves as a graphical front end for In-situ Partial Order (ISP), a
dynamic formal verification tool for MPI developed at the School of
Computing, University of Utah.

Whether you are new to MPI or are an advanced user, GEM will help you debug
your MPI programs, and graphically show many valuable facts, including all
the possible send/receive matches, and synchronizations. GEM also includes
features to help users understand and debug the program across all platforms
on which it may be run (e.g. highlighting deadlocks that may occur due to
differing communication buffer allocations). For a given test harness, GEM
will allow you to explore only the relevant process interleavings, which are
much smaller than the number of total feasible interleavings. GEM also
guarantees to discover and explore all non-deterministic matches at run-time. 


%package        pldt-fortran
Summary:        PTP Parallel Language Development Tools Fortran Support
Group:          Development/Java
Requires:       eclipse-cdt-parsers >= %{cdtreq}
Requires:       %{name} = %{version}-%{release}
Requires:       eclipse-photran = %{photranver}-%{release}

%description    pldt-fortran
Adds a range of static analysis and programming assistance tools for Fortran.


%package        pldt-upc
Summary:        PTP Parallel Language Development Tools UPC Support
Group:          Development/Java
Requires:       eclipse-cdt-parsers >= %{cdtreq}
Requires:       %{name} = %{version}-%{release}

%description    pldt-upc
Adds a range of static analysis and programming assistance tools for UPC.  
Note: this is separated from the rest of PLDT since it requires the UPC
feature of CDT, which is sometimes not installed with CDT.


%package        rdt
Summary:        PTP Remote Development Tools
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       eclipse-jgit
Requires:       eclipse-rse >= %{rsereq}

%description    rdt
PTP components for supporting Remote Development Tools.


%package        rdt-sync-fortran
Summary:        PTP Fortran Synchronization Support
Group:          Development/Java
Requires:       %{name}-rdt-sync = %{version}-%{release}

%description    rdt-sync-fortran
Adds the ability to remotely synchronize Fortran projects.


%package        rdt-xlc
Summary:        PTP Remote Development Tools XL C/C++ Compiler Support
Group:          Development/Java
Requires:       %{name}-rdt = %{version}-%{release}
Requires:       eclipse-cdt-parsers >= %{cdtreq}

%description    rdt-xlc
Remote support for the IBM XL C/C++ compilers.


%package        rm-contrib
Summary:        PTP Contributed Resource Manager Definitions
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description    rm-contrib
Adds resource managers for a number of different systems.


%package        sci
Summary:        PTP Scalable Communication Infrastructure (SCI)
Group:          Development/Java

%description    sci
Parallel Tools Platform components that implements the Scalable Communication
Infrastructure (SCI).


%package        sdk
Summary:        Parallel Tools Platform SDK 
Group:          Development/Java

%description    sdk
Eclipse Parallel Tools Platform. Software development kit including source
code and developer documentation.


%package -n     eclipse-photran
Version:        %{photranver}
Summary:        Photran End-User Runtime
Group:          Development/Java
Requires:       eclipse-cdt >= %{cdtreq}

%description -n eclipse-photran
An Eclipse-based Integrated Development Environment for Fortran.


%package -n     eclipse-photran-intel
Version:        %{photranver}
Summary:        Intel Fortran compiler support for Photran
Group:          Development/Java
Requires:       eclipse-photran = %{photranver}-%{release}

%description -n eclipse-photran-intel
This feature packages the plugins required to support
the Intel Fortran compiler in Photran/FDT.


%package -n     eclipse-photran-xlf
Version:        %{photranver}
Summary:        IBM XLF Compiler Support
Group:          Development/Java
Requires:       eclipse-photran = %{photranver}-%{release}

%description -n eclipse-photran-xlf
Error parser and managed build tool chain for the IBM XLF compiler.

%package        remote-rse
#Kludge to work around http://rpm.org/ticket/124
Version:        %{ptpver}
Summary:        PTP RSE Enabler
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description    remote-rse
Provides support for remote services using RSE.


%prep
%setup -q -c -T -a 0 -a 1
# Fix tycho version
tychover=$(sed -ne '/<version>/{s/.*>\(.*\)<.*/\1/;p;q}' < /usr/share/maven-fragments/tycho)
sed -i -e "/tycho-version/s/>.*</>${tychover}</" */pom.xml
pushd org.eclipse.ptp-%{ptp_git_tag}
%patch0 -p1 -b .notrax
%patch1 -p2 -b .noremote
%patch2 -p2 -b .gridengine
# Copy into place for %doc
cp releng/org.eclipse.ptp-feature/epl-v10.html ..
popd
pushd org.eclipse.photran-%{photran_git_tag}

# We need to rebuild this jar from the sources within it
pwd
mkdir cdtdb-4.0.3-eclipse
pushd cdtdb-4.0.3-eclipse
unzip -q ../org.eclipse.rephraserengine.core/cdtdb-4.0.3-eclipse.jar
find -name \*.class -exec rm {} +
popd
# Delete any other jars in the project
find -name \*.jar -exec rm {} +
# This prevents the Photran Intel feature from building
sed -i -e 's/os="linux"//' org.eclipse.photran.intel-feature/feature.xml
#Fix line endings, causes problems with pdebuild link names
find -name MANIFEST.MF -exec sed -i -e 's|\r||' {} +
popd
pushd org.eclipse.ptp-%{ptp_git_tag}
# Remotejars requires a bunch of downloaded prebuilt stuff
%pom_disable_module rdt/org.eclipse.ptp.rdt.core.remotejars
%pom_disable_module releng/org.eclipse.ptp.rdt.remotejars-feature
# This depends on remotejars
%pom_disable_module rdt/org.eclipse.ptp.rdt.server.dstore
# This depends on rdt.server.dstor
%pom_disable_module releng/org.eclipse.ptp.rdt.remotetools-feature
popd


%build
export JAVA_HOME=%{java_home}
export PATH=/usr/bin:$PATH
# Build the helper jar first
pushd org.eclipse.photran-%{photran_git_tag}/cdtdb-4.0.3-eclipse
classpath=$(echo /usr/lib*/eclipse/plugins/org.eclipse.equinox.common_*.jar | sed -e 's/ /:/g')
find -name \*java -exec javac -classpath $classpath '{}' +
jar cf ../org.eclipse.rephraserengine.core/cdtdb-4.0.3-eclipse.jar *
popd
#Interferes with feature build
rm -rf cdtdb-4.0.3-eclipse
# Build the projects
pushd org.eclipse.photran-%{photran_git_tag}
mvn-rpmbuild -Dmaven.repo.local=../.m2 -DforceContextQualifier=%{photran_build_id} install
popd
pushd org.eclipse.ptp-%{ptp_git_tag}
mvn-rpmbuild -Dmaven.repo.local=../.m2 -DforceContextQualifier=%{ptp_build_id} install
popd


%install
mkdir -p %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/{features,plugins}

# ptp
for jar in org.eclipse.ptp-%{ptp_git_tag}/releng/org.eclipse.ptp.repo/target/repository/features/*.jar
do
  name=$(basename $jar .jar)
  unzip -u -d %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/$name $jar
  if [ $name == org.eclipse.ptp_%{version}.%{ptp_build_id} ]
  then
    # Group the core features
    sed -ne '/id=/s#.*"\(.*\)"#%{eclipse_base}/dropins/ptp/eclipse/features/\1_*#gp' %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/$name/feature.xml | tail -n +2 > files.$name
    # Add the plugins for those features
    sed -ne '/id=/s#.*"\(.*\)"#\1#gp' %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/$name/feature.xml | tail -n +2 | while read f
    do
      [ $f == org.eclipse.ptp ] && continue
      sed -ne '/id=/s#.*"\(.*\)"#%{eclipse_base}/dropins/ptp/eclipse/plugins/\1_*.jar#gp' %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/${f}_*/feature.xml | tail -n +2 >> files.$name
    done
    sort -u -o files.$name files.$name
  else
    sed -ne '/id=/s#.*"\(.*\)"#%{eclipse_base}/dropins/ptp/eclipse/plugins/\1_*.jar#gp' %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/$name/feature.xml | tail -n +2 > files.$name
  fi
done
cp -u org.eclipse.ptp-%{ptp_git_tag}/releng/org.eclipse.ptp.repo/target/repository/plugins/*.jar \
   %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/plugins/

# special case for rephraserengine feature included in photran
sed -i -e '/org.eclipse.rephraserengine_/d' files.org.eclipse.photran_%{photranver}.%{photran_build_id}
# multiple -f flags in %files: merging -f files.org.eclipse.ptp.rdt.editor_%{version}.%{ptp_build_id} into -f files.org.eclipse.ptp.rdt_%{version}.%{ptp_build_id}
cat files.org.eclipse.ptp.rdt.editor_%{version}.%{ptp_build_id} >> files.org.eclipse.ptp.rdt_%{version}.%{ptp_build_id}
# multiple -f flags in %files: merging -f files.org.eclipse.rephraserengine_%{photranver}.%{photran_build_id} into -f files.org.eclipse.photran_%{photranver}.%{photran_build_id}
cat files.org.eclipse.rephraserengine_%{photranver}.%{photran_build_id} >> files.org.eclipse.photran_%{photranver}.%{photran_build_id}


%files -f files.org.eclipse.ptp_%{version}.%{ptp_build_id}
%doc epl-v10.html
%dir %{eclipse_base}/dropins/ptp
%dir %{eclipse_base}/dropins/ptp/eclipse
%dir %{eclipse_base}/dropins/ptp/eclipse/features
%dir %{eclipse_base}/dropins/ptp/eclipse/plugins

%files master
%doc epl-v10.html

%files etfw-ppw -f files.org.eclipse.ptp.etfw.ppw_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.etfw.ppw_*

%files etfw-tau -f files.org.eclipse.ptp.etfw.tau_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.etfw.tau_*

%files etfw-tau-fortran -f files.org.eclipse.ptp.etfw.tau.fortran_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.etfw.tau.fortran_*

%files fortran
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.fortran_*

%files gem -f files.org.eclipse.ptp.gem_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.gem_*

%files pldt-fortran -f files.org.eclipse.ptp.pldt.fortran_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.pldt.fortran_*

%files pldt-upc -f files.org.eclipse.ptp.pldt.upc_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.pldt.upc_*

%files rdt -f files.org.eclipse.ptp.rdt_%{version}.%{ptp_build_id} 
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rdt_*
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rdt.editor_*

%files rdt-sync-fortran -f files.org.eclipse.ptp.rdt.sync.fortran_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rdt.sync.fortran_*

%files rdt-xlc -f files.org.eclipse.ptp.rdt.xlc_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rdt.xlc_*

%files remote-rse -f files.org.eclipse.ptp.remote.rse_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.remote.rse_*

%files rm-contrib -f files.org.eclipse.ptp.rm.jaxb.contrib_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rm.jaxb.contrib_*

%files sci -f files.org.eclipse.ptp.sci_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.sci_*

%files sdk -f files.org.eclipse.ptp.sdk_%{version}.%{ptp_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.sdk_*

%files -n eclipse-photran -f files.org.eclipse.photran_%{photranver}.%{photran_build_id} 
%doc epl-v10.html
%dir %{eclipse_base}/dropins/ptp
%dir %{eclipse_base}/dropins/ptp/eclipse
%dir %{eclipse_base}/dropins/ptp/eclipse/features
%dir %{eclipse_base}/dropins/ptp/eclipse/plugins
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.photran_*
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.rephraserengine_*

%files -n eclipse-photran-intel -f files.org.eclipse.photran.intel_%{photranver}.%{photran_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.photran.intel_*

%files -n eclipse-photran-xlf -f files.org.eclipse.photran.xlf_%{photranver}.%{photran_build_id}
%doc epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.photran.xlf_*


%changelog
* Tue Jul 22 2014 Igor Vlasenko <viy@altlinux.ru> 6.0.5-alt1_2jpp7
- update

