# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global eclipse_base        %{_libdir}/eclipse
%global install_loc         %{_datadir}/eclipse/dropins
# Taken from update site so we match upstream
#  http://download.eclipse.org/mylyn/archive/3.6.3/v20110608-1400/
%global qualifier           v20110908-0706

# Builds the following upstream features:
# - org.eclipse.mylyn.team-feature
# - org.eclipse.mylyn.cdt-feature
# - org.eclipse.mylyn.java-feature
# - org.eclipse.mylyn.pde-feature
# - org.eclipse.mylyn.context-feature

Name: eclipse-mylyn-context
Summary: Eclipse Mylyn context specific features
Version: 3.6.4
Release: alt1_2jpp6
License: EPL
URL: http://www.eclipse.org/mylyn

BuildArch: noarch
%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%endif

Source0: http://git.eclipse.org/c/mylyn/org.eclipse.mylyn.context.git/snapshot/R_3_6_4.tar.bz2

BuildArch: noarch

BuildRequires: eclipse-platform >= 1:3.5.0
BuildRequires: eclipse-pde >= 1:3.5.0
BuildRequires: eclipse-jdt >= 1:3.5.0
BuildRequires: eclipse-cdt
BuildRequires: eclipse-mylyn >= 3.6.0


# eclipse-mylyn-context

Requires: eclipse-platform >= 1:3.5.0
Requires: eclipse-mylyn >= 3.6.0
Group: Development/Java
Source44: import.info

%description
Provides the Eclipse Mylyn Task-Focused Interface.


# eclipse-mylyn-context-java

%package java
Summary:  Mylyn Bridge:  Java Development
Requires: eclipse-jdt
Requires: %{name} = %{version}-%{release}
Provides: eclipse-mylyn-java = %{version}-%{release}
Obsoletes: eclipse-mylyn-java < %{version}-%{release}
Group: Development/Java

%description java
Mylyn Task-Focused UI extensions for JDT.  Provides focusing of Java
element views and editors.


# eclipse-mylyn-context-pde

%package pde
Summary:  Mylyn Bridge:  Plug-in Development
Requires: eclipse-pde
Requires: %{name}-java = %{version}-%{release}
Provides: eclipse-mylyn-pde = %{version}-%{release}
Obsoletes: eclipse-mylyn-pde < %{version}-%{release}
Group: Development/Java

%description pde
Mylyn Task-Focused UI extensions for PDE, Ant, Team Support and CVS.


# eclipse-mylyn-context-cdt

%package cdt
Summary:  Mylyn Bridge:  C/C++ Development
Requires: %{name} = %{version}-%{release}
Requires: eclipse-cdt
Group: Development/Java
Provides: eclipse-cdt-mylyn = 2:1.0.0-1.fc12
Provides: eclipse-mylyn-cdt = %{version}-%{release}
Obsoletes: eclipse-mylyn-cdt < %{version}-%{release}
Obsoletes: eclipse-cdt-mylyn < 2:1.0.0

%description cdt
Mylyn Task-Focused UI extensions for CDT.  Provides focusing of C/C++
element views and editors.


# eclipse-mylyn-context-team

%package team
Summary:  Mylyn Context Connector: Team Support
Requires: %{name} = %{version}-%{release}
Group: Development/Java

%description team
Mylyn Task-Focused UI extensions for Team version control.


%prep
%setup -q -n R_3_6_4
# remove unneeded sources
ls -1 | grep -vE 'org.eclipse.mylyn.team.ui|org.eclipse.mylyn.context.ui|org.eclipse.mylyn.resources.ui|org.eclipse.mylyn.team-feature|org.eclipse.mylyn.cdt-feature|org.eclipse.mylyn.cdt.ui|org.eclipse.mylyn.java-feature|org.eclipse.mylyn.java.ui|org.eclipse.mylyn.ide.ant|org.eclipse.mylyn.ide.ui|org.eclipse.mylyn.java.tasks|org.eclipse.mylyn.pde-feature|org.eclipse.mylyn.pde.ui|org.eclipse.mylyn.context-feature' | xargs rm -rf


%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.context_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar -d "mylyn-commons mylyn"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.team_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.java_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar -d "jdt"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.pde_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar -d "sdk jdt"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.cdt.mylyn \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar -d "cdt"


%install
install -d -m 755 %{buildroot}%{_datadir}/eclipse
install -d -m 755 %{buildroot}%{install_loc}/mylyn-context
install -d -m 755 %{buildroot}%{install_loc}/mylyn-context-team
install -d -m 755 %{buildroot}%{install_loc}/mylyn-java
install -d -m 755 %{buildroot}%{install_loc}/mylyn-pde
install -d -m 755 %{buildroot}%{install_loc}/mylyn-cdt

unzip -q -o -d %{buildroot}%{install_loc}/mylyn-context \
 build/rpmBuild/org.eclipse.mylyn.context_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-context-team \
 build/rpmBuild/org.eclipse.mylyn.team_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-java \
 build/rpmBuild/org.eclipse.mylyn.java_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-pde \
 build/rpmBuild/org.eclipse.mylyn.pde_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-cdt \
 build/rpmBuild/org.eclipse.cdt.mylyn.zip


# eclipse-mylyn-context
%files
%{install_loc}/mylyn-context
%doc org.eclipse.mylyn.context-feature/license.html
%doc org.eclipse.mylyn.context-feature/epl-v10.html

# eclipse-mylyn-context-java
%files java
%{install_loc}/mylyn-java
%doc org.eclipse.mylyn.java-feature/license.html
%doc org.eclipse.mylyn.java-feature/epl-v10.html

# eclipse-mylyn-context-pde
%files pde
%{install_loc}/mylyn-pde
%doc org.eclipse.mylyn.pde-feature/license.html
%doc org.eclipse.mylyn.pde-feature/epl-v10.html

# eclipse-mylyn-context-cdt
%files cdt
%{install_loc}/mylyn-cdt
%doc org.eclipse.mylyn.cdt-feature/license.html
%doc org.eclipse.mylyn.cdt-feature/epl-v10.html

# eclipse-mylyn-context-team
%files team
%{install_loc}/mylyn-context-team
%doc org.eclipse.mylyn.team-feature/license.html
%doc org.eclipse.mylyn.team-feature/epl-v10.html

%changelog
* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.4-alt1_2jpp6
- new version

