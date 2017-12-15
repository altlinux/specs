Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 1
%global with_bundled 0
%global with_debug 0
#  Error: nothing provides libboost_system.so.1.59.0()(64bit) needed by mongodb-3.2.1-2.fc24.x86_64.
%global with_check 0
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 0
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         go-mgo
%global repo            mgo
# https://github.com/go-mgo/mgo
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     gopkg.in/mgo.v2
%global commit          e30de8ac9ae3b30df7065f766c71f88bba7d4e49
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global import_path_sec gopkg.in/v2/mgo

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.9.git%{shortcommit}
Summary:        The MongoDB driver for Go
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
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
%if 0%{?fedora} >= 22
BuildRequires: supervisor
BuildRequires: mongo
BuildRequires: mongo-server-mongod mongo-server-mongos
BuildRequires: lsof
%endif
BuildRequires: golang(gopkg.in/check.v1)
BuildRequires: golang(gopkg.in/tomb.v2)
BuildRequires: golang(gopkg.in/yaml.v2)
%endif

Requires:      golang(gopkg.in/check.v1)
Requires:      golang(gopkg.in/tomb.v2)
Requires:      golang(gopkg.in/yaml.v2)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/bson) = %{version}-%{release}
Provides:      golang(%{import_path}/dbtest) = %{version}-%{release}
Provides:      golang(%{import_path}/testserver) = %{version}-%{release}
Provides:      golang(%{import_path}/txn) = %{version}-%{release}

Provides:      golang(%{import_path_sec}) = %{version}-%{release}
Provides:      golang(%{import_path_sec}/bson) = %{version}-%{release}
Provides:      golang(%{import_path_sec}/dbtest) = %{version}-%{release}
Provides:      golang(%{import_path_sec}/testserver) = %{version}-%{release}
Provides:      golang(%{import_path_sec}/txn) = %{version}-%{release}

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
# If go_arches not defined fall through to implicit golang archs
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

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
install -d -p %{buildroot}/%{go_path}/src/%{import_path_sec}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
echo "%%dir %%{go_path}/src/%%{import_path_sec}/." >> devel.file-list
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
    install -d -p %{buildroot}/%{go_path}/src/%{import_path_sec}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path_sec}/$file
    echo "%%{go_path}/src/%%{import_path_sec}/$file" >> devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path_sec}/$filedir" >> devel.file-list.dir
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

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%else
export GOPATH=$(pwd):%{buildroot}/%{go_path}:$(pwd)/Godeps/_workspace:%{go_path}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

export GOPATH=$(pwd):%{buildroot}/%{go_path}:%{go_path}
%if 0%{?fedora} >= 22
make startdb
%gotest -gocheck.v
make stopdb
%endif
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc %doc README.md
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README.md
%endif

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.9.gite30de8a
- new version

