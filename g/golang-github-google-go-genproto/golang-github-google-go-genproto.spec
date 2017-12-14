Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
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
%global with_check 1
# Generate unit-test rpm
# no test files so far
%global with_unit_test 0

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif


%global provider        github
%global provider_tld    com
%global project         google
%global repo            go-genproto
# https://github.com/google/go-genproto
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     google.golang.org/genproto
%global commit          411e09b969b1170a9f0c467558eb4c4c110d9c77
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.2.git%{shortcommit}
Summary:        Go generated proto packages
# Detected licences
# - *No copyright* Apache (v2.0) GENERATED FILE at 'LICENSE'
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

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(github.com/golang/protobuf/ptypes/any)
BuildRequires: golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires: golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires: golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/grpc)
%endif

Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
Requires:      golang(github.com/golang/protobuf/ptypes/any)
Requires:      golang(github.com/golang/protobuf/ptypes/duration)
Requires:      golang(github.com/golang/protobuf/ptypes/empty)
Requires:      golang(github.com/golang/protobuf/ptypes/struct)
Requires:      golang(github.com/golang/protobuf/ptypes/timestamp)
Requires:      golang(github.com/golang/protobuf/ptypes/wrappers)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(google.golang.org/grpc)

Provides:      golang(%{import_path}/googleapis/api) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/annotations) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/configchange) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/distribution) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/httpbody) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/label) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/metric) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/monitoredres) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/serviceconfig) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/servicecontrol/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/api/servicemanagement/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/appengine/legacy) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/appengine/logging/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/appengine/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bigtable/admin/table/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bigtable/admin/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bigtable/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bigtable/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/bytestream) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/audit) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/billing/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/dataproc/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/functions/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/language/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/language/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/language/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/ml/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/ml/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/runtimeconfig/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/speech/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/speech/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/support/common) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/support/v1alpha1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/cloud/vision/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/container/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/datastore/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/datastore/v1beta3) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/cloudbuild/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/clouddebugger/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/clouderrorreporting/v1beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/cloudtrace/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/source/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/devtools/sourcerepo/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/example/library/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/genomics/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/genomics/v1alpha2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/iam/admin/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/iam/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/logging/type) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/logging/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/longrunning) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/monitoring/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/privacy/dlp/v2beta1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/pubsub/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/pubsub/v1beta2) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/rpc/code) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/rpc/errdetails) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/rpc/status) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/spanner/admin/database/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/spanner/admin/instance/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/spanner/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/storagetransfer/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/tracing/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/color) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/date) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/dayofweek) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/latlng) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/money) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/postaladdress) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/type/timeofday) = %{version}-%{release}
Provides:      golang(%{import_path}/googleapis/watcher/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/protobuf/api) = %{version}-%{release}
Provides:      golang(%{import_path}/protobuf/field_mask) = %{version}-%{release}
Provides:      golang(%{import_path}/protobuf/ptype) = %{version}-%{release}
Provides:      golang(%{import_path}/protobuf/source_context) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Group: Development/Other
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif


%description unit-test-devel
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
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
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

%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README.md CONTRIBUTING.md
%dir %{go_path}/src/google.golang.org
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc README.md CONTRIBUTING.md
%endif

%changelog
* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.2.git411e09b
- new version

