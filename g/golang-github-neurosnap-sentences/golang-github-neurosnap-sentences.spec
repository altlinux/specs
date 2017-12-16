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
%global with_debug 1
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
%global project         neurosnap
%global repo            sentences
# https://github.com/neurosnap/sentences
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global gopkgin_import_path     gopkg.in/%{project}/%{repo}.v1
# v1.0.6
%global commit          a7f18ead1433a139742a8b42ce7a059cfb484d60
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.0.6
Release:        alt1_2
Summary:        Multilingual command line sentence tokenizer in Golang
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if ! 0%{?with_bundled}
# _cmd/sentences/main.go
BuildRequires: golang(github.com/spf13/cobra)

# Remaining dependencies not included in main packages
%endif

# This is required to build data/english.go
BuildRequires: go-bindata

Provides: sentences = %{version}-%{release}
Source44: import.info

%description
%{summary}

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif


Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/data) = %{version}-%{release}
Provides:      golang(%{import_path}/english) = %{version}-%{release}
Provides:      golang(%{import_path}/utils) = %{version}-%{release}
# We also want to provide the gopkg.in path for this package
Provides:      golang(%{gopkgin_import_path}) = %{version}-%{release}
Provides:      golang(%{gopkgin_import_path}/data) = %{version}-%{release}
Provides:      golang(%{gopkgin_import_path}/english) = %{version}-%{release}
Provides:      golang(%{gopkgin_import_path}/utils) = %{version}-%{release}

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
# remove pre-compiled data file
rm -f data/english.go

%build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../ src/%{import_path}
# Also link the gopkg.in path
mkdir -p src/gopkg.in/%{project}
ln -s ../../../ src/%{gopkgin_import_path}

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{go_path}
%else
# No dependency directories so far
export GOPATH=$(pwd):%{go_path}
%endif

# build data/english.go
go-bindata -pkg="data" -o data/english.go data/english.json

%gobuild -o bin/_cmd/sentences %{import_path}/_cmd/sentences

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/_cmd/sentences %{buildroot}%{_bindir}

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
# install data used for tests
cp -rpav ./test_files %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%{go_path}/src/%%{import_path}/test_files" >> unit-test-devel.file-list
%endif

# link the gopkg.in path
mkdir -p %{buildroot}%{go_path}/src/gopkg.in/%{project}
ln -sT %{go_path}/src/%{import_path} %{buildroot}%{go_path}/src/%{gopkgin_import_path}

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
# The pwd is needed here, since the upstream package itself
# depends on both gopkg.in and github versions of itself
export GOPATH=%{buildroot}/%{go_path}:$(pwd):%{go_path}
%else
# No dependency directories so far

export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}
%gotest %{import_path}/english
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%doc LICENSE.md
%doc CHANGES.md README.md
%{_bindir}/sentences

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE.md
%doc CHANGES.md README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%dir %{go_path}/src/gopkg.in/%{project}
%{go_path}/src/%{gopkgin_import_path}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE.md
%doc CHANGES.md README.md
%endif

%changelog
* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt1_2
- new version

