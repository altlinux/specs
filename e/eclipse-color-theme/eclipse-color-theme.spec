BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name eclipse-color-theme
%define version 0.11.1
%global install_loc     %{_datadir}/eclipse/dropins/%{name}
%global git_tag         598b755

Summary:        An Eclipse plugin which permits color theme switching
Name:           eclipse-color-theme
Version:        0.11.1
Release:        alt1_5jpp7
License:        EPL
Group:          Development/Java
URL:            http://www.eclipsecolorthemes.org/
# http://github.com/eclipse-color-theme/eclipse-color-theme/tarball/v%{version}
Source0:        %{name}-%{name}-v%{version}-0-g%{git_tag}.tar.gz

BuildRequires: eclipse-pde >= 1:3.4.0

Requires: eclipse-platform >= 3.4.0

BuildArch:     noarch
Source44: import.info

%description
The Eclipse Color Theme plugin makes it possible to switch color themes
conveniently and without side effects. It includes the most popular themes
from eclipsecolorthemes.org, but you can add any theme created on the site
by exporting it as XML.

%prep
%setup -q -n %{name}-%{name}-%{git_tag}

%build
/usr/bin/eclipse-pdebuild

%install
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}
%{__unzip} -q -d $RPM_BUILD_ROOT%{install_loc} \
     build/rpmBuild/com.github.eclipsecolortheme.feature.zip

%files
%doc README.md CHANGES.md COPYING
%{install_loc}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_5jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_4jpp7
- new version

