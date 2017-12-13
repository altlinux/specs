Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 1
# package depends on kubernetes which atm does
# not provide complete source codes
%global with_bundled 1
%if 0%{?rhel} == 6
%global with_debug 0
%else
%global with_debug 1
%endif
# missing deps on kubernetes
%global with_check 0
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 1
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
%global project         appc
%global repo            spec
# https://github.com/appc/spec
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          37bef679148751952f169298fa0ea8171373d95c
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.5.1
Release:        alt1_11.git%{shortcommit}
Summary:        Schema defs and tools for app container specification
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

Provides:   actool = %{version}-%{release}
Provides:   ace-validator = %{version}-%{release}
Source44: import.info

%description
%{summary}

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
#BuildRequires: golang(github.com/GoogleCloudPlatform/kubernetes/pkg/api/resource)
BuildRequires: golang(github.com/coreos/go-semver/semver) >= 0
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)
%endif

#Requires: golang(github.com/GoogleCloudPlatform/kubernetes/pkg/api/resource)
Requires: golang(github.com/coreos/go-semver/semver) >= 0
Requires: golang(golang.org/x/net/html)
Requires: golang(golang.org/x/net/html/atom)

Provides:      golang(%{import_path}/aci) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/acirenderer) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/tarheader) = %{version}-%{release}
Provides:      golang(%{import_path}/schema) = %{version}-%{release}
Provides:      golang(%{import_path}/schema/types) = %{version}-%{release}

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
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
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
mkdir -p src/github.com/appc
ln -s ../../../ src/github.com/appc/spec

%if 0%{?with_bundled}
export GOPATH=$(pwd):$(pwd)/Godeps/_workspace:%{go_path}
%else
export GOPATH=$(pwd):%{go_path}
%endif

%if 0%{?with_debug}
function gobuild { go build -a -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -v -x "$@"; }
%else
function gobuild { go build -a "$@"; }
%endif

gobuild -o bin/actool %{import_path}/actool
gobuild -o bin/ace-validator -installsuffix ace %{import_path}/ace

find . -name "*.go" \
    -print |\
    xargs sed -i 's/github.com\/appc\/spec\/Godeps\/_workspace\/src\///g'

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 755 bin/actool %{buildroot}%{_bindir}
install -p -m 755 bin/ace-validator %{buildroot}%{_bindir}

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go" | grep -v "^./Godeps") ; do
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
sort -u devel.file-list.dir >> devel.file-list
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/discovery
echo "%%dir %%{go_path}/src/%%{import_path}/./discovery" >> devel.file-list
cp -pav discovery/myapp.html %{buildroot}/%{go_path}/src/%{import_path}/discovery/.
cp -pav discovery/myapp2.html %{buildroot}/%{go_path}/src/%{import_path}/discovery/.
echo "%%{go_path}/src/%%{import_path}/discovery/myapp.html" >> unit-test.file-list
echo "%%{go_path}/src/%%{import_path}/discovery/myapp2.html" >> unit-test.file-list
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go" | grep -v "^./Godeps"); do
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
sort -u unit-test.file-list.dir >> unit-test.file-list
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

%gotest %{import_path}/aci
%gotest %{import_path}/discovery
%gotest %{import_path}/pkg/acirenderer
%gotest %{import_path}/pkg/tarheader
%gotest %{import_path}/schema
%gotest %{import_path}/schema/types
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%doc LICENSE
%doc SPEC.md README.md OS-SPEC.md GUIDE.md CONTRIBUTING.md
%{_bindir}/actool
%{_bindir}/ace-validator

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc SPEC.md README.md OS-SPEC.md GUIDE.md CONTRIBUTING.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc SPEC.md README.md OS-SPEC.md GUIDE.md CONTRIBUTING.md
%endif

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_11.git37bef67
- new version

