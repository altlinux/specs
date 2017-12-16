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
%global repo            golex
# https://github.com/cznic/golex
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          4ab7c5e190e49208c823ce8ec803aa39e6a4b31a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20170803


Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.4.%{commitdate}.git%{shortcommit}
Summary:        Lex/Flex-like utility written in Go
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{project}-%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if 0%{?with_cli_tool}
Provides:       golex = %{version}-%{release}

BuildRequires:  golang(github.com/cznic/lex)
BuildRequires:  golang(github.com/cznic/lexer)
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
BuildRequires:  golang(github.com/cznic/lex)
BuildRequires:  golang(github.com/cznic/lexer)
%endif

Provides:       golang(%{import_path}/lex) = %{version}-%{release}

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
%gobuild -o bin/golex %{import_path}
%endif


%install
%if 0%{?with_cli_tool}
mkdir -p %{buildroot}/%{_bindir}
cp -pav ./bin/golex %{buildroot}/%{_bindir}/
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
%gotest %{import_path}/lex
%endif


#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_cli_tool}
%files
%doc LICENSE
%doc CONTRIBUTORS README AUTHORS
%{_bindir}/golex
%endif

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc CONTRIBUTORS README AUTHORS
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc CONTRIBUTORS README AUTHORS
%endif


%changelog
* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.4.20170803.git4ab7c5e
- new version

