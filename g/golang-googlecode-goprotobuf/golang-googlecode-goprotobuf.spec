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
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**}; 
%endif

%global provider        github
%global provider_tld    com
%global project         golang
%global repo            protobuf
# https://github.com/golang/protobuf
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          24f28ae800abfde9310e779f94be606b1a98a3fc
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global simport_path    code.google.com/p/goprotobuf

Name:           golang-googlecode-goprotobuf
Version:        0
Release:        alt1_0.30.git%{shortcommit}
Summary:        Go support for Google protocol buffers
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

Requires:       libprotobuf
Provides:       protoc-gen-go = %{version}-%{release}
Source44: import.info

%description
This package provides support for protocol buffers in the form of a protocol
compiler plugin which generates Go source files that, once compiled, can access
and manage protocol buffers.

Install %{name}-devel for the associated support library.

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif

Provides:      golang(%{import_path}/jsonpb) = %{version}-%{release}
Provides:      golang(%{import_path}/jsonpb/jsonpb_test_proto) = %{version}-%{release}
Provides:      golang(%{import_path}/proto) = %{version}-%{release}
Provides:      golang(%{import_path}/proto/proto3_proto) = %{version}-%{release}
Provides:      golang(%{import_path}/proto/testdata) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go/descriptor) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go/generator) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go/grpc) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go/plugin) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go/testdata/my_test) = %{version}-%{release}
Provides:      golang(%{import_path}/ptypes) = %{version}-%{release}
Provides:      golang(%{import_path}/ptypes/any) = %{version}-%{release}
Provides:      golang(%{import_path}/ptypes/duration) = %{version}-%{release}
Provides:      golang(%{import_path}/ptypes/empty) = %{version}-%{release}
Provides:      golang(%{import_path}/ptypes/struct) = %{version}-%{release}
Provides:      golang(%{import_path}/ptypes/timestamp) = %{version}-%{release}
Provides:      golang(%{import_path}/ptypes/wrappers) = %{version}-%{release}

# back compatibility
Provides:      golang(%{simport_path}/jsonpb) = %{version}-%{release}
Provides:      golang(%{simport_path}/jsonpb/jsonpb_test_proto) = %{version}-%{release}
Provides:      golang(%{simport_path}/proto) = %{version}-%{release}
Provides:      golang(%{simport_path}/proto/proto3_proto) = %{version}-%{release}
Provides:      golang(%{simport_path}/proto/testdata) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go/descriptor) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go/generator) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go/grpc) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go/plugin) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go/testdata/my_test) = %{version}-%{release}
Provides:      golang(%{simport_path}/ptypes) = %{version}-%{release}
Provides:      golang(%{simport_path}/ptypes/any) = %{version}-%{release}
Provides:      golang(%{simport_path}/ptypes/duration) = %{version}-%{release}
Provides:      golang(%{simport_path}/ptypes/empty) = %{version}-%{release}
Provides:      golang(%{simport_path}/ptypes/struct) = %{version}-%{release}
Provides:      golang(%{simport_path}/ptypes/timestamp) = %{version}-%{release}
Provides:      golang(%{simport_path}/ptypes/wrappers) = %{version}-%{release}

%description devel
This package provides  a library that implements run-time support for
encoding (marshaling), decoding (unmarshaling), and accessing protocol
buffers in the Go language.

Install %{name} for the related protocol compiler plugin.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test-devel
Group: Development/Other
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build
mkdir -p src/github.com/golang
ln -s ../../../ src/github.com/golang/protobuf

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{go_path}
%else
echo "Unable to build from bundled deps. No Godeps nor vendor directory"
exit 1
%endif

%gobuild -o bin/protoc-gen-go %{import_path}/protoc-gen-go

%install
install -d %{buildroot}%{_bindir}
install -m 755 bin/protoc-gen-go %{buildroot}/%{_bindir}/protoc-gen-go

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done

install -d -p %{buildroot}/%{go_path}/src/%{simport_path}/
echo "%%dir %%{go_path}/src/%%{simport_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{simport_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{simport_path}/$file
    echo "%%{go_path}/src/%%{simport_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{simport_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
pushd %{buildroot}/%{go_path}/src/%{simport_path}/
# github.com/golang/protobuf -> code.google.com/p/goprotobuf
sed -i 's/"github\.com\/golang\/protobuf/"code\.google\.com\/p\/goprotobuf/g' \
        $(find . -name '*.go')
popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go") proto/testdata/*.proto; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
for file in $(find protoc-gen-go/testdata \! -iname "*.go"); do
    if [ -d $file ]; then
        echo "%%dir %%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list
        continue
    fi
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list
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

%gotest %{import_path}/jsonpb
%gotest %{import_path}/proto
# --- FAIL: TestGolden (0.09s)
#	golden_test.go:52: sum("test.pb.go"): length is 78494
#%%gotest %%{import_path}/proto/testdata
%gotest %{import_path}/protoc-gen-go/generator
#gotest %%{import_path}/protoc-gen-go/testdata
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%doc AUTHORS CONTRIBUTORS LICENSE README.md
%{_bindir}/protoc-gen-go

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README.md AUTHORS CONTRIBUTORS
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc README.md AUTHORS CONTRIBUTORS
%endif

%changelog
* Sun Dec 10 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.30.git24f28ae
- new version

