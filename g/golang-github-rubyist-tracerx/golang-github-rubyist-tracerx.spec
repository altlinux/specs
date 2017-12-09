Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package   %{nil}

%global provider        github
%global provider_tld    com
%global project         rubyist
%global repo            tracerx
# https://github.com/rubyist/tracerx
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          d7bcc0bc315bed2a841841bee5dbecc8d7d7582f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_4.git%{shortcommit}
Summary:        Output tracing information in your Go app based on environment variables
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source44: import.info

%description
Tracerx is a simple tracing package that logs messages depending on environment
variables. It is very much inspired by git's GIT_TRACE mechanism.

%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}) = %{version}-%{release}

%description devel
Tracerx is a simple tracing package that logs messages depending on environment
variables. It is very much inspired by git's GIT_TRACE mechanism.

This package contains library source intended for building other packages which
use import path with %{import_path} prefix.

%prep
%setup -q -n %{repo}-%{commit}


%build

%install
install -Dpm0644 %{repo}.go %{buildroot}%{go_path}/src/%{import_path}/%{repo}.go

%files devel
%doc LICENSE
%doc README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%dir %{go_path}/src/%{import_path}
%{go_path}/src/%{import_path}/%{repo}.go

%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_4.gitd7bcc0b
- new version

