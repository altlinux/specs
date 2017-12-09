Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global provider	github
%global provider_tld	com
%global project		influxdb
%global repo		go-cache
%global commit		7d1d6d6ae935664bc8b80ab2b1fc7ab77a7e46da

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{project}-%{repo}
Version:	0
Release:	alt1_0.6.git%{shortcommit}
Summary:	An in-memory key:value store/cache library for Go
License:	MIT
URL:		http://%{import_path}
Source0:	https://github.com/%{project}/%{repo}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
BuildArch:	noarch
Source44: import.info

%description
An in-memory key:value store/cache (similar to Memcached) library for Go,
suitable for single-machine applications


%package devel
Group: Development/Other
BuildRequires:	golang >= 1.2.1
Requires:	golang >= 1.2.1
Summary:	An in-memory key:value store/cache library for Go
Provides:	golang(%{import_path}) = %{version}-%{release}

%description devel
An in-memory key:value store/cache (similar to Memcached) library for Go,
suitable for single-machine applications

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{go_path}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{go_path}:%{go_path} go test %{import_path}

%files devel
%doc LICENSE README CONTRIBUTORS
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%dir %{go_path}/src/%{import_path}
%{go_path}/src/%{import_path}/*.go

%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.6.git7d1d6d6
- new version

