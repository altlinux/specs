Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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
%global project         xtaci
%global repo            kcp-go
# https://github.com/xtaci/kcp-go
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          86eebd5cadb519b7c9306082c7eb3bcee2c49a7b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20170605

# commit 86eebd5cadb519b7c9306082c7eb3bcee2c49a7b == version 3.23


Name:           golang-%{provider}-%{project}-%{repo}
Version:        3.23
Release:        alt1_1
Summary:        Production-Grade Reliable-UDP Library for golang
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}/%{project}-%{repo}-%{version}.tar.gz

# Add a patch to disable a failing test.
# It tries to open more than 1024 sockets, which doesn't work on fedora.
# See https://github.com/xtaci/kcp-go/issues/40
Patch0:         00-disable-failing-test.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}


%if 0%{?with_devel}
%package        devel
Group: Development/Other
Summary:        %{summary}
BuildArch:      noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/klauspost/reedsolomon)
BuildRequires:  golang(github.com/templexxx/xor)
BuildRequires:  golang(github.com/tjfoc/gmsm/sm4)
BuildRequires:  golang(golang.org/x/crypto/blowfish)
BuildRequires:  golang(golang.org/x/crypto/cast5)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(golang.org/x/crypto/salsa20)
BuildRequires:  golang(golang.org/x/crypto/tea)
BuildRequires:  golang(golang.org/x/crypto/twofish)
BuildRequires:  golang(golang.org/x/crypto/xtea)
BuildRequires:  golang(golang.org/x/net/ipv4)
%endif

Requires:       golang(github.com/pkg/errors)
Requires:       golang(github.com/klauspost/reedsolomon)
Requires:       golang(github.com/templexxx/xor)
Requires:       golang(github.com/tjfoc/gmsm/sm4)
Requires:       golang(golang.org/x/crypto/blowfish)
Requires:       golang(golang.org/x/crypto/cast5)
Requires:       golang(golang.org/x/crypto/pbkdf2)
Requires:       golang(golang.org/x/crypto/salsa20)
Requires:       golang(golang.org/x/crypto/tea)
Requires:       golang(golang.org/x/crypto/twofish)
Requires:       golang(golang.org/x/crypto/xtea)
Requires:       golang(golang.org/x/net/ipv4)

Provides:       golang(%{import_path}) = %{version}-%{release}

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif


%if 0%{?with_unit_test} && 0%{?with_devel}
%package        unit-test-devel
Group: Development/Other
Summary:        Unit tests for %{name} package

# test subpackage tests code from devel subpackage

%description    unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif


%prep
%setup -q -n %{repo}-%{version}
%patch0 -p1


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
export GOPATH=%{buildroot}/%{go_path}:%{go_path}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}
%endif


#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%doc --no-dereference LICENSE
%doc README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif


%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc --no-dereference LICENSE
%doc README.md
%endif


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 3.23-alt1_1
- update to new release by fcimport

* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.22-alt1_1
- new version

