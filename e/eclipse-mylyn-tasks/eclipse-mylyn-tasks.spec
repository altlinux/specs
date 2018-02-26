# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global eclipse_base        %{_libdir}/eclipse
%global install_loc         %{_datadir}/eclipse/dropins
# Taken from update site so we match upstream
#  http://download.eclipse.org/mylyn/archive/3.6.0/v20110608-1400/
%global qualifier           v20110908-0706

Name: eclipse-mylyn-tasks
Summary: Mylyn Bugzilla/Trac Tasks Connectors
Version: 3.6.4
Release: alt1_2jpp6
License: EPL
URL: http://www.eclipse.org/mylyn/tasks

BuildArch: noarch
%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%endif

# bash fetch-eclipse-mylyn-tasks.sh
Source0: eclipse-mylyn-tasks-R_3_6_4-fetched-src.tar.bz2
Source1: fetch-eclipse-mylyn-tasks.sh
# Red Hat bugzilla's custom transition file
Source2: redhat-bugzilla-custom-transitions.txt

# These patches are probably not suitable for upstream.
# They switch Import-Package for Bundle-Require in
# bugzilla.core and trac.core MANIFEST.MF
Patch0: %{name}-bugzilla-core-xmlrpc-import-package-manifest-fix.patch
Patch1: %{name}-trac-core-xmlrpc-import-package-manifest-fix.patch

BuildArch: noarch

BuildRequires: eclipse-platform >= 1:3.5.0
BuildRequires: eclipse-pde >= 1:3.5.0
BuildRequires: eclipse-mylyn >= 3.6.0
BuildRequires: eclipse-mylyn-commons >= 3.6.0
BuildRequires: eclipse-mylyn-context >= 3.6.0
# The following two are required for webtasks
BuildRequires: rome
BuildRequires: jdom
Source44: import.info

%description
Mylyn Tasks Connectors


# eclips-mylyn-tasks-bugzilla

%package bugzilla
Summary: Mylyn Tasks Connector: Bugzilla
Requires: eclipse-platform >= 1:3.5.0
Requires: eclipse-mylyn >= 3.6.0
Requires: eclipse-mylyn-commons >= 3.6.0
Provides: eclipse-mylyn-bugzilla = %{version}-%{release}
Obsoletes: eclipse-mylyn-bugzilla < %{version}-%{release}
Group: Development/Java

%description bugzilla
Provides Task List integration, offline support and rich editing for the
open source Bugzilla bug tracker.


# eclips-mylyn-tasks-trac

%package  trac
Summary: Mylyn Tasks Connector: Trac
Requires: eclipse-platform >= 1:3.5.0
Requires: eclipse-mylyn >= 3.6.0
Requires: eclipse-mylyn-commons >= 3.6.0
Requires: eclipse-mylyn-context >= 3.6.0
Group: Development/Java
Provides: eclipse-mylyn-trac = %{version}-%{release}
Obsoletes: eclipse-mylyn-trac < %{version}-%{release}

%description trac
Provides Task List integration, offline support and rich editing
for the open source Trac issue tracker.


# eclips-mylyn-tasks-web

%package  web
Summary: Mylyn Tasks Connector: Web Templates (Advanced) (Incubation)
Requires: eclipse-platform >= 1:3.5.0
Requires: eclipse-mylyn >= 3.6.0
Requires: eclipse-mylyn-commons >= 3.6.0
Requires: rome
Requires: jdom
Group: Development/Java
Provides: eclipse-mylyn-webtasks = %{version}-%{release}
Obsoletes: eclipse-mylyn-webtasks < %{version}-%{release}

%description web
Provides Task List integration for web-based issue trackers
and templates for example projects.


%prep
%setup -q -c
pushd eclipse-mylyn-tasks-R_3_6_4-fetched-src
%patch0
%patch1
rm -rf orbitDeps
mkdir orbitDeps
pushd orbitDeps
ln -s %{_javadir}/rome-0.9.jar
ln -s %{_javadir}/jdom.jar
popd

%build
pushd eclipse-mylyn-tasks-R_3_6_4-fetched-src
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.bugzilla_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -d "mylyn mylyn-commons"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.trac_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -d "mylyn mylyn-commons mylyn-context"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.web.tasks_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -d "mylyn mylyn-commons" -o `pwd`/orbitDeps
popd

%install
install -d -m 755 %{buildroot}%{_datadir}/eclipse
install -d -m 755 %{buildroot}%{install_loc}/mylyn-bugzilla
install -d -m 755 %{buildroot}%{install_loc}/mylyn-trac
install -d -m 755 %{buildroot}%{install_loc}/mylyn-webtasks
install %{SOURCE2} %{buildroot}%{install_loc}/mylyn-bugzilla/redhat-bugzilla-custom-transitions.txt

pushd eclipse-mylyn-tasks-R_3_6_4-fetched-src
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-bugzilla \
 build/rpmBuild/org.eclipse.mylyn.bugzilla_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-trac \
 build/rpmBuild/org.eclipse.mylyn.trac_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-webtasks \
 build/rpmBuild/org.eclipse.mylyn.web.tasks_feature.zip
popd
pushd %{buildroot}%{install_loc}/mylyn-webtasks/eclipse/plugins
# rome
rm com.sun.syndication*
# jdom
rm org.jdom*
# link to system files instead
ln -s %{_javadir}/rome-0.9.jar
ln -s %{_javadir}/jdom.jar
popd


# eclips-mylyn-tasks-bugzilla
%files bugzilla
%{install_loc}/mylyn-bugzilla
%doc eclipse-mylyn-tasks-R_3_6_4-fetched-src/org.eclipse.mylyn.bugzilla-feature/epl-v10.html
%doc eclipse-mylyn-tasks-R_3_6_4-fetched-src/org.eclipse.mylyn.bugzilla-feature/license.html

# eclips-mylyn-tasks-trac
%files trac
%{install_loc}/mylyn-trac
%doc eclipse-mylyn-tasks-R_3_6_4-fetched-src/org.eclipse.mylyn.trac-feature/epl-v10.html
%doc eclipse-mylyn-tasks-R_3_6_4-fetched-src/org.eclipse.mylyn.trac-feature/license.html

# eclips-mylyn-tasks-web
%files web
%{install_loc}/mylyn-webtasks
%doc eclipse-mylyn-tasks-R_3_6_4-fetched-src/org.eclipse.mylyn.web.tasks-feature/epl-v10.html
%doc eclipse-mylyn-tasks-R_3_6_4-fetched-src/org.eclipse.mylyn.web.tasks-feature/license.html


%changelog
* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.4-alt1_2jpp6
- new version

