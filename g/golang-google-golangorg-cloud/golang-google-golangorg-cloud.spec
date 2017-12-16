Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
# Cyclic deps among cloud, grpc and oauth2
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         GoogleCloudPlatform
%global repo            google-cloud-go
# https://github.com/GoogleCloudPlatform/google-cloud-go
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     google.golang.org/cloud
%global commit          872c736f496c2ba12786bedbb8325576bbdb33cf
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-google-golangorg-cloud
Version:        0
Release:        alt1_0.13.git%{shortcommit}
Summary:        Google Cloud Platform APIs related types and common functions
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(golang.org/x/net/context)
# cyclic deps among cloud, grpc and oauth2
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(google.golang.org/api/bigquery/v2)
BuildRequires: golang(google.golang.org/api/container/v1)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/logging/v1beta3)
BuildRequires: golang(google.golang.org/api/pubsub/v1)
BuildRequires: golang(google.golang.org/api/storage/v1)
BuildRequires: golang(google.golang.org/appengine)
BuildRequires: golang(google.golang.org/appengine/file)
BuildRequires: golang(google.golang.org/appengine/log)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/credentials/oauth)
%endif

Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(golang.org/x/net/context)
# cyclic deps among cloud, grpc and oauth2
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)
Requires:      golang(google.golang.org/api/bigquery/v2)
Requires:      golang(google.golang.org/api/container/v1)
Requires:      golang(google.golang.org/api/googleapi)
Requires:      golang(google.golang.org/api/logging/v1beta3)
Requires:      golang(google.golang.org/api/pubsub/v1)
Requires:      golang(google.golang.org/api/storage/v1)
Requires:      golang(google.golang.org/appengine)
Requires:      golang(google.golang.org/appengine/file)
Requires:      golang(google.golang.org/appengine/log)
Requires:      golang(google.golang.org/grpc)
Requires:      golang(google.golang.org/grpc/credentials)
Requires:      golang(google.golang.org/grpc/credentials/oauth)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/bigquery) = %{version}-%{release}
Provides:      golang(%{import_path}/bigtable) = %{version}-%{release}
Provides:      golang(%{import_path}/bigtable/bttest) = %{version}-%{release}
Provides:      golang(%{import_path}/compute/metadata) = %{version}-%{release}
Provides:      golang(%{import_path}/container) = %{version}-%{release}
Provides:      golang(%{import_path}/datastore) = %{version}-%{release}
Provides:      golang(%{import_path}/examples/storage/appengine) = %{version}-%{release}
Provides:      golang(%{import_path}/logging) = %{version}-%{release}
Provides:      golang(%{import_path}/pubsub) = %{version}-%{release}
Provides:      golang(%{import_path}/storage) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test
Group: Development/Other
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> devel.file-list.dir
    done
done
[ -s devel.file-list.dir ] && sort -u devel.file-list.dir >> devel.file-list
rm -f devel.file-list.dir
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> unit-test.file-list.dir
    done
done
[ -s unit-test.file-list.dir ] && sort -u unit-test.file-list.dir >> unit-test.file-list
rm -f unit-test.file-list.dir
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%else
# No dependency directories so far

export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

gotest %{import_path}
gotest %{import_path}/bigquery
gotest %{import_path}/bigtable
gotest %{import_path}/datastore
gotest %{import_path}/pubsub
gotest %{import_path}/storage
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README.md CONTRIBUTING.md AUTHORS CONTRIBUTORS
%dir %{go_path}/src/google.golang.org
%dir %{go_path}/src/%{import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README.md CONTRIBUTING.md AUTHORS CONTRIBUTORS
%endif

%changelog
* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.13.git872c736
- new version

