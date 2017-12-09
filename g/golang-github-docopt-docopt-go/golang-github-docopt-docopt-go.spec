Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package	%{nil}
%global provider	github
%global provider_tld	com
%global project		docopt
%global repo		docopt.go
%global gorepo		docopt-go
%global github_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path	%{provider}.%{provider_tld}/%{project}/%{gorepo}
%global commit		854c423c810880e30b9fecdabb12d54f4a92f9bb
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

Name:		golang-github-docopt-docopt-go
Version:	0
Release:	alt1_0.8.git.%{shortcommit}
Summary:	Command-line interface description language in Go

License:	MIT
URL:		https://godoc.org/%{github_path}
Source0:	https://%{github_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source44: import.info


%description
Docopt helps you create beautiful command-line interfaces easily with Go


%package devel
Group: Development/Other
BuildRequires:	golang >= 1.2.1
Requires:	golang >= 1.2.1
Summary:	Command-line interface description language in Go
Provides:	golang(%{import_path}) = %{version}-%{release}

%description devel
Docopt helps you create beautiful command-line interfaces easily with Go

This package contains library source intended for building other packages
which use docopt/docopt-go.


%prep
%setup -q -n %{repo}-%{commit}


%build


%install
install -d %{buildroot}/%{go_path}/src/%{import_path}
cp -pav docopt.go docopt_test.go testcases.docopt test_golang.docopt \
  %{buildroot}/%{go_path}/src/%{import_path}/


%check
GOPATH=%{buildroot}/%{go_path} go test %{import_path}


%files devel
%doc LICENSE README.md example_test.go examples
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%{go_path}/src/%{import_path}


%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.8.git.854c423
- new version

