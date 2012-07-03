BuildRequires: /proc
BuildRequires: jpackage-compat
%define name            objectweb-deploysched
%define version         0.2
%define release         1jpp

# -----------------------------------------------------------------------------

Summary:        ObjectWeb scheduling framework
Name:           %{name}
Version:        %{version}
Release:        alt2_1jpp1.7
Epoch:		0
Group:          Development/Java
License:        LGPL
URL:            http://forge.objectweb.org/
BuildArch:      noarch
Source0:        http://mail-archive.objectweb.org/fractal/2004-08/zip00000.tar.bz2
BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: objectweb-anttask
Provides:	owdeploysched

%description
ObjectWeb scheduling framework

%prep
%setup -q -n deployment
find . -name "*.jar" -exec rm {} \;

%build
export LANG=en_US.ISO8859-1
echo objectweb.ant.tasks.path $(build-classpath objectweb-anttask) > build.config
echo xerces.path $(build-classpath xerces-j2) >> build.config
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
export CLASSPATH=
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.compiler=modern jar

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 output/dist/lib/ow_bean.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_bean-%{version}.jar
install -m 644 output/dist/lib/ow_deployment_scheduling.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_deployment_scheduling-%{version}.jar
install -m 644 output/dist/lib/ow_deployment_scheduling_component.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_deployment_scheduling_component-%{version}.jar
install -m 644 output/dist/lib/ow_deployment_scheduling_component_api.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_deployment_scheduling_component_api-%{version}.jar
install -m 644 output/dist/lib/ow_deployment_scheduling_component_lib.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_deployment_scheduling_component_lib-%{version}.jar
install -m 644 output/dist/lib/ow_deployment_scheduling_core.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_deployment_scheduling_core-%{version}.jar
install -m 644 output/dist/lib/ow_deployment_scheduling_core_api.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_deployment_scheduling_core_api-%{version}.jar
install -m 644 output/dist/lib/ow_deployment_scheduling_core_lib.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_deployment_scheduling_core_lib-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
  for jar in *-%{version}.jar; do ln -sf $jar $(echo $jar | sed -e 's/-%{version}//'); done
popd

%files
%{_javadir}/%{name}/*

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt2_1jpp1.7
- fixed build with java 7

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

