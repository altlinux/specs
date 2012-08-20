Name: mojo-maven2-plugin-build-helper
Version: 17
Summary: Build helper plugin from mojo-maven2-plugins
License: ASL, MIT, GPL, LGPL
Url: http://mojo.codehaus.org
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: maven-plugin-build-helper

BuildArch: noarch
Group: Development/Java
Release: alt21_0jpp

%description
Build Helper plugin from mojo-maven2-plugins.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT

%files

%changelog
* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:17-alt21_0jpp
- empty package to satisfy dependencies

