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
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif


%global provider        github
%global provider_tld    com
%global project         grpc-ecosystem
%global repo            grpc-gateway
# https://github.com/grpc-ecosystem/grpc-gateway
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          18d159699f2e83fc5bb9ef2f79465ca3f3122676
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.0.0
Release:        alt1_0.7.git%{shortcommit}
Summary:        GRPC to JSON proxy generator
# Detected licences
# - BSD (3 clause) at 'LICENSE.txt'
License:        BSD
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
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/golang/protobuf/jsonpb)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/generator)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/plugin)
BuildRequires: golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/annotations)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/metadata)
%endif

Requires:      golang(github.com/golang/glog)
Requires:      golang(github.com/golang/protobuf/jsonpb)
Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
Requires:      golang(github.com/golang/protobuf/protoc-gen-go/generator)
Requires:      golang(github.com/golang/protobuf/protoc-gen-go/plugin)
Requires:      golang(github.com/golang/protobuf/ptypes/empty)
Requires:      golang(github.com/golang/protobuf/ptypes/timestamp)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(google.golang.org/genproto/googleapis/api/annotations)
Requires:      golang(google.golang.org/grpc)
Requires:      golang(google.golang.org/grpc/codes)
Requires:      golang(google.golang.org/grpc/grpclog)
Requires:      golang(google.golang.org/grpc/metadata)

Provides:      golang(%{import_path}/protoc-gen-grpc-gateway/descriptor) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-grpc-gateway/generator) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-grpc-gateway/gengateway) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-grpc-gateway/httprule) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-swagger/genswagger) = %{version}-%{release}
Provides:      golang(%{import_path}/runtime) = %{version}-%{release}
Provides:      golang(%{import_path}/utilities) = %{version}-%{release}

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
BuildRequires: golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires: golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/golang/protobuf/ptypes/wrappers)
%endif

Requires:      golang(github.com/golang/protobuf/ptypes/duration)
Requires:      golang(github.com/golang/protobuf/ptypes/struct)
Requires:      golang(github.com/golang/protobuf/ptypes/timestamp)
Requires:      golang(github.com/golang/protobuf/ptypes/wrappers)

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
for file in $(find . -iname "*.go" \! -iname "*_test.go" | grep -v "Godeps/_workspace") ; do
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
for file in $(find . -iname "*_test.go" | grep -v "Godeps/_workspace") ; do
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
export GOPATH=%{buildroot}/%{go_path}:$(pwd)/Godeps/_workspace:%{go_path}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/protoc-gen-grpc-gateway/descriptor
%gotest %{import_path}/protoc-gen-grpc-gateway/gengateway
%gotest %{import_path}/protoc-gen-grpc-gateway/httprule
%gotest %{import_path}/protoc-gen-swagger/genswagger
#%gotest %{import_path}/runtime
%gotest %{import_path}/utilities
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE.txt
%doc README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE.txt
%doc README.md
%endif

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.7.git18d1596
- new version

