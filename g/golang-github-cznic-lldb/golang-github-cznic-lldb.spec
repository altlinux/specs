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
%global project         cznic
%global repo            lldb
# https://github.com/cznic/lldb
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          bea8611dd5c407f3c5eab9f9c68e887a27dc6f0e
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

# commit bea8611dd5c407f3c5eab9f9c68e887a27dc6f0e == version 1.1.0


Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.1.0
Release:        alt1_3
Summary:        Low-level database engine implementation in Go
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/cznic-%{repo}-%{shortcommit}.tar.gz

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
BuildRequires:  golang(github.com/cznic/fileutil)
BuildRequires:  golang(github.com/cznic/internal/buffer)
BuildRequires:  golang(github.com/cznic/internal/file)
BuildRequires:  golang(github.com/cznic/mathutil)
BuildRequires:  golang(github.com/cznic/sortutil)
BuildRequires:  golang(github.com/cznic/zappy)
%endif

Requires:       golang(github.com/cznic/fileutil)
Requires:       golang(github.com/cznic/internal/buffer)
Requires:       golang(github.com/cznic/internal/file)
Requires:       golang(github.com/cznic/mathutil)
Requires:       golang(github.com/cznic/sortutil)
Requires:       golang(github.com/cznic/zappy)

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

# add test data for unit test subpackage
cp -pvr testdata %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%{go_path}/src/%%{import_path}/testdata" >> unit-test-devel.file-list

mkdir -p %{buildroot}/%{_licensedir}/%{name}-unit-test-devel
cp -pvr testdata/LICENSE %{buildroot}/%{_licensedir}/%{name}-unit-test-devel/LICENSE-testdata
echo "%%{_licensedir}/%%{name}-unit-test-devel" >> unit-test-devel.file-list
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif


%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?gotest:1}
%global gotest go test
%endif

# This go library uses an "internal" package (that's not really internal,
# since it's in the same prefix, but in another GOPATH), so ... copy
# everything to a common directory for running the tests.

# create temporary "test root"
mkdir -p testroot/src/github.com

# copy dependencies
cp -pavr %{go_path}/src/github.com/* testroot/src/github.com/

# copy sources
cp -pavr %{buildroot}/%{go_path}/src/%{import_path} testroot/src/%{import_path}

# run tests
export GOPATH=$(pwd)/testroot
%gotest %{import_path}

# remove temporary "test root"
rm -r ./testroot
%endif


#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc CONTRIBUTORS README.md AUTHORS
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif


%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc CONTRIBUTORS README.md AUTHORS
%endif


%changelog
* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_3
- new version

