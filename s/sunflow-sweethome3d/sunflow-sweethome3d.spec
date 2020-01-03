BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# (daviddavid)
# Please do not update this pkg because it is the forked SunFlow needed
# for Sweet Home 3D and the only one who need it (release 0.07.3i).
# As explained in THIRDPARTY-LICENSE-SUNFLOW.TXT, Sweet Home 3D is built
# with a version forked from SunFlow 0.07.3.
# https://github.com/rpax/sunflow

%define up_name	sunflow

Name:		sunflow-sweethome3d
Version:	0.07.3i
Release:	alt1_1jpp8
Summary:	A rendering system for photo-realistic image synthesis
License:	MIT
Group:		Development/Java
URL:		https://github.com/rpax/sunflow
Source0:	https://github.com/rpax/sunflow/archive/%{up_name}-%{version}.tar.gz
Patch0:		sunflow-0.07.3i-mga-fix-SunflowGUI.patch
BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix
BuildRequires:	maven-local
BuildRequires:	janino

# Explicit requires for javapackages-tools since sunflow script
# uses /usr/share/java-utils/java-functions
Requires:	javapackages-tools
Source44: import.info


%description
Sunflow is an open source rendering system for photo-realistic image synthesis.
It is written in Java and built around a flexible ray tracing core and
an extensible object-oriented design.

** Warning **
This is the sunflow version forked for Sweet Home 3D.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{up_name}-%{up_name}-%{version}
%patch0 -p1


dos2unix -k README.md

%pom_remove_plugin :maven-source-plugin

%mvn_compat_version : %{version}
%mvn_file  : %{up_name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc



%changelog
* Fri Jan 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.07.3i-alt1_1jpp8
- new version

