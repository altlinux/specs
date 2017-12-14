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
# Cyclic deps among grpc, cloud and oauth2
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
%global project         grpc
%global repo            grpc-go
# https://github.com/grpc/grpc-go
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     google.golang.org/grpc
%global commit          8050b9cbc271307e5a716a9d782803d09b0d6f2d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.0.0
Release:        alt1_0.7.git%{shortcommit}
Summary:        The Go language implementation of gRPC. HTTP/2 based RPC
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

%if 0%{?with_check}
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/golang/mock/gomock)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/net/http2/hpack)
BuildRequires: golang(golang.org/x/net/trace)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/oauth2/jwt)
%endif

Requires:      golang(github.com/golang/glog)
Requires:      golang(github.com/golang/mock/gomock)
Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(golang.org/x/net/http2)
Requires:      golang(golang.org/x/net/http2/hpack)
Requires:      golang(golang.org/x/net/trace)
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)
Requires:      golang(golang.org/x/oauth2/jwt)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/benchmark) = %{version}-%{release}
Provides:      golang(%{import_path}/benchmark/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/benchmark/stats) = %{version}-%{release}
Provides:      golang(%{import_path}/codes) = %{version}-%{release}
Provides:      golang(%{import_path}/credentials) = %{version}-%{release}
Provides:      golang(%{import_path}/credentials/oauth) = %{version}-%{release}
Provides:      golang(%{import_path}/examples/helloworld/helloworld) = %{version}-%{release}
Provides:      golang(%{import_path}/examples/helloworld/mock/mock_helloworld) = %{version}-%{release}
Provides:      golang(%{import_path}/examples/route_guide/routeguide) = %{version}-%{release}
Provides:      golang(%{import_path}/grpclb) = %{version}-%{release}
Provides:      golang(%{import_path}/grpclb/grpc_lb_v1) = %{version}-%{release}
Provides:      golang(%{import_path}/grpclog) = %{version}-%{release}
Provides:      golang(%{import_path}/grpclog/glogger) = %{version}-%{release}
Provides:      golang(%{import_path}/health) = %{version}-%{release}
Provides:      golang(%{import_path}/health/grpc_health_v1) = %{version}-%{release}
Provides:      golang(%{import_path}/interop) = %{version}-%{release}
Provides:      golang(%{import_path}/interop/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/keepalive) = %{version}-%{release}
Provides:      golang(%{import_path}/metadata) = %{version}-%{release}
Provides:      golang(%{import_path}/naming) = %{version}-%{release}
Provides:      golang(%{import_path}/peer) = %{version}-%{release}
Provides:      golang(%{import_path}/reflection) = %{version}-%{release}
Provides:      golang(%{import_path}/reflection/grpc_reflection_v1alpha) = %{version}-%{release}
Provides:      golang(%{import_path}/reflection/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/stats) = %{version}-%{release}
Provides:      golang(%{import_path}/stats/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/stress/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/tap) = %{version}-%{release}
Provides:      golang(%{import_path}/test/codec_perf) = %{version}-%{release}
Provides:      golang(%{import_path}/test/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/transport) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
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
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate unit-test.file-list
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
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
chmod -x %{buildroot}%{go_path}/src/%{import_path}/interop/grpc_testing/test.pb.go
for ext in .pem .key .proto _test.go; do
    # find all files with $ext prefix and generate unit-test.file-list
    for file in $(find . -iname "*${ext}"); do
        echo "%%dir %%{go_path}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
        install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
        cp $file %{buildroot}/%{go_path}/src/%{import_path}/$file
        echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test.file-list
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

#%gotest %{import_path}
%gotest %{import_path}/benchmark
%gotest %{import_path}/metadata
# Leaked goroutine
#%%gotest %%{import_path}/test
%gotest %{import_path}/transport
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
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README.md CONTRIBUTING.md
%endif

%changelog
* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.7.git8050b9c
- new version

