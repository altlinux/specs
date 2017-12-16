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
%global with_debug 1
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1
# Build command line tool
%global with_cli_tool 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         cznic
%global repo            ql
# https://github.com/cznic/ql
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          3f53e147d722f949b627631bc771623ab9bdb396
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20171122


Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.1.0
Release:        alt1_2.%{commitdate}.git%{shortcommit}
Summary:        Embedded SQL database written in Go

# This package is BSD licensed, but the vendored go4.org/lock library is ASLv2.0
License:        BSD and ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{project}-%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if 0%{?with_cli_tool}
BuildRequires:  golang(github.com/cznic/b)
BuildRequires:  golang(github.com/cznic/golex/lex)
BuildRequires:  golang(github.com/cznic/lldb)
BuildRequires:  golang(github.com/cznic/mathutil)
BuildRequires:  golang(github.com/cznic/strutil)

Provides:       ql = %{version}-%{release}
%endif
Source44: import.info

%description
%{summary}


%if 0%{?with_devel}
%package        devel
Group: Development/Other
Summary:        %{summary}
BuildArch:      noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires:  golang(github.com/cznic/b)
BuildRequires:  golang(github.com/cznic/golex/lex)
BuildRequires:  golang(github.com/cznic/lldb)
BuildRequires:  golang(github.com/cznic/mathutil)
BuildRequires:  golang(github.com/cznic/strutil)
%endif

Requires:       golang(github.com/cznic/b)
Requires:       golang(github.com/cznic/golex/lex)
Requires:       golang(github.com/cznic/lldb)
Requires:       golang(github.com/cznic/mathutil)
Requires:       golang(github.com/cznic/strutil)

Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/design) = %{version}-%{release}
Provides:       golang(%{import_path}/driver) = %{version}-%{release}
Provides:       bundled(golang(github.com/camlistore/go4/lock))

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
%if 0%{?with_cli_tool}
# prepare build environment
mkdir -p ./_build/src/%{provider}.%{provider_tld}/%{project}
ln -s $(pwd) ./_build/src/%{import_path}

# run build and set version correctly
export GOPATH=$(pwd)/_build:%{go_path}
%gobuild -o bin/ql %{import_path}/ql
%endif


%install
%if 0%{?with_cli_tool}
mkdir -p %{buildroot}/%{_bindir}
cp -pav ./bin/ql %{buildroot}/%{_bindir}/
%endif

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
cp -pavr _testdata %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%{go_path}/src/%%{import_path}/_testdata" >> unit-test-devel.file-list

cp -pav testdata.ql %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%{go_path}/src/%%{import_path}/testdata.ql" >> unit-test-devel.file-list
%endif

# install license file for bundled go4.org/lock library
mkdir -p %{buildroot}%{_licensedir}/%{name}
cp -pav vendored/github.com/camlistore/LICENSE \
    %{buildroot}/%{_licensedir}/%{name}/LICENSE.camlistore-go4-lock

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
%gotest %{import_path}/driver
%gotest %{import_path}/vendored/github.com/camlistore/go4/lock

# Clean up test logs
rm %{buildroot}/%{go_path}/src/%{import_path}/testdata.log
%endif


#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_cli_tool}
%files
%doc LICENSE
%doc CONTRIBUTORS README.md AUTHORS
%{_bindir}/ql
%{_licensedir}/%{name}/LICENSE.camlistore-go4-lock
%endif

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc CONTRIBUTORS README.md AUTHORS
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%{_licensedir}/%{name}/LICENSE.camlistore-go4-lock
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc CONTRIBUTORS README.md AUTHORS
%{_licensedir}/%{name}/LICENSE.camlistore-go4-lock
%endif


%changelog
* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2.20171122.git3f53e14
- new version

