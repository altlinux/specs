Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: jetty6 servlet_2_5_api
BuildRequires: /proc rpm-build-java

%define servletspec 2.5

Name:           jetty6-servlet-2.5-api
Version:        6.1.22
Release:        alt1_0jpp6
Epoch:          0
Summary:        jetty6 servlet 2.5 api compatibility package
Group:          Development/Java
License:        ASL 2.0
URL:            http://www.mortbay.org/
#BuildRequires: servlet_2_5_api

BuildArch: noarch

%description
jetty6 servlet 2.5 api compatibility package.

%install
install -d -m 755 %{buildroot}%{_mavendepmapfragdir}

%add_to_maven_depmap org.mortbay.jetty servlet-api 2.5-20081211 JPP servlet_2_5_api

%files
%{_mavendepmapfragdir}/%{name}

%changelog
* Wed Nov 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.1.22-alt1_0jpp6
- jetty6 servlet 2.5 api compatibility package
