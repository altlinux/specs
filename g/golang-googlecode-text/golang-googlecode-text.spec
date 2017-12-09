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

%global provider_tld    com 
%global provider        github
%global project         golang
%global repo            text
# https://github.com/golang/text
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     code.google.com/p/go.text
%global commit          3bd178b88a8180be2df394a1fbb81313916f0e7b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global x_provider      golang
%global x_provider_tld  org
%global x_repo          text
%global x_import_path   %{x_provider}.%{x_provider_tld}/x/%{x_repo}
%global x_name          golang-%{x_provider}%{x_provider_tld}-%{repo}

%global devel_main      %{x_name}-devel
%global devel_prefix    x

Name:       golang-googlecode-text
Version:    0
Release:    alt1_0.21.git%{shortcommit}
Summary:    Supplementary Go text libraries
License:    BSD
URL:        https://%{provider_prefix}
Source0:    https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

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
Summary:    Supplementary Go text libraries for code.google.com/p/ imports
BuildArch:  noarch

%if 0%{?with_check}
%endif

Provides:   golang(%{import_path}) = %{version}-%{release}
Provides:   golang(%{import_path}/cases) = %{version}-%{release}
Provides:   golang(%{import_path}/collate) = %{version}-%{release}
Provides:   golang(%{import_path}/collate/build) = %{version}-%{release}
Provides:   golang(%{import_path}/currency) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/charmap) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/htmlindex) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/ianaindex) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/japanese) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/korean) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/simplifiedchinese) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/traditionalchinese) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/unicode) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/unicode/utf32) = %{version}-%{release}
Provides:   golang(%{import_path}/feature/plural) = %{version}-%{release}
Provides:   golang(%{import_path}/language) = %{version}-%{release}
Provides:   golang(%{import_path}/language/display) = %{version}-%{release}
Provides:   golang(%{import_path}/message) = %{version}-%{release}
Provides:   golang(%{import_path}/message/catalog) = %{version}-%{release}
Provides:   golang(%{import_path}/runes) = %{version}-%{release}
Provides:   golang(%{import_path}/search) = %{version}-%{release}
Provides:   golang(%{import_path}/secure) = %{version}-%{release}
Provides:   golang(%{import_path}/secure/bidirule) = %{version}-%{release}
Provides:   golang(%{import_path}/secure/precis) = %{version}-%{release}
Provides:   golang(%{import_path}/transform) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/bidi) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/cldr) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/norm) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/rangetable) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/runenames) = %{version}-%{release}
Provides:   golang(%{import_path}/width) = %{version}-%{release}

%package -n %{x_name}-devel
Group: Development/Other
Summary:    Supplementary Go text libraries for golang.org/x/ imports
BuildArch:  noarch

%if 0%{?with_check}
%endif

Provides:   golang(%{x_import_path}) = %{version}-%{release}
Provides:   golang(%{x_import_path}/cases) = %{version}-%{release}
Provides:   golang(%{x_import_path}/collate) = %{version}-%{release}
Provides:   golang(%{x_import_path}/collate/build) = %{version}-%{release}
Provides:   golang(%{x_import_path}/currency) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/charmap) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/htmlindex) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/ianaindex) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/japanese) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/korean) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/simplifiedchinese) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/traditionalchinese) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/unicode) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/unicode/utf32) = %{version}-%{release}
Provides:   golang(%{x_import_path}/feature/plural) = %{version}-%{release}
Provides:   golang(%{x_import_path}/language) = %{version}-%{release}
Provides:   golang(%{x_import_path}/language/display) = %{version}-%{release}
Provides:   golang(%{x_import_path}/message) = %{version}-%{release}
Provides:   golang(%{x_import_path}/message/catalog) = %{version}-%{release}
Provides:   golang(%{x_import_path}/runes) = %{version}-%{release}
Provides:   golang(%{x_import_path}/search) = %{version}-%{release}
Provides:   golang(%{x_import_path}/secure) = %{version}-%{release}
Provides:   golang(%{x_import_path}/secure/bidirule) = %{version}-%{release}
Provides:   golang(%{x_import_path}/secure/precis) = %{version}-%{release}
Provides:   golang(%{x_import_path}/transform) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/bidi) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/cldr) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/norm) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/rangetable) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/runenames) = %{version}-%{release}
Provides:   golang(%{x_import_path}/width) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go text libraries with code.google.com/p/ imports.

%description -n %{x_name}-devel

This package contains library source intended for building other packages
which use the supplementary Go text libraries with golang.org/x/ imports.
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
providing packages with %{x_import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
install -d -p %{buildroot}%{go_path}/src/%{x_import_path}
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{x_import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{x_import_path}/$file
    echo "%%{go_path}/src/%%{x_import_path}/$file" >> x_devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        echo "%%dir %%{go_path}/src/%%{x_import_path}/$dirprefix" >> x_devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
pushd %{buildroot}/%{go_path}/src/%{import_path}
# from https://groups.google.com/forum/#!topic/golang-nuts/eD8dh3T9yyA, first post
sed -i 's/"golang\.org\/x\//"code\.google\.com\/p\/go\./g' \
        $(find . -name '*.go')
popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{x_import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{x_import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{x_import_path}/$file
    echo "%%{go_path}/src/%%{x_import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{x_import_path}/$dirprefix" >> x_devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
for file in $(find ./encoding/testdata -iname "*.txt"); do
    install -d -p %{buildroot}/%{go_path}/src/%{x_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{x_import_path}/$file
    echo "%%{go_path}/src/%%{x_import_path}/$file" >> unit-test-devel.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
sort -u -o x_devel.file-list x_devel.file-list
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

#%%gotest %%{x_import_path}/cases
%gotest %{x_import_path}/collate
%gotest %{x_import_path}/collate/build
%ifnarch s390x aarch64
%gotest %{x_import_path}/currency
%endif
%gotest %{x_import_path}/encoding
%gotest %{x_import_path}/encoding/charmap
%gotest %{x_import_path}/encoding/htmlindex
%gotest %{x_import_path}/encoding/ianaindex
%gotest %{x_import_path}/encoding/japanese
%gotest %{x_import_path}/encoding/korean
%gotest %{x_import_path}/encoding/simplifiedchinese
%gotest %{x_import_path}/encoding/traditionalchinese
%gotest %{x_import_path}/encoding/unicode
%gotest %{x_import_path}/internal
%gotest %{x_import_path}/internal/colltab
%gotest %{x_import_path}/internal/tag
%gotest %{x_import_path}/internal/triegen
%gotest %{x_import_path}/internal/ucd
%gotest %{x_import_path}/language
%gotest %{x_import_path}/language/display
%gotest %{x_import_path}/message
%gotest %{x_import_path}/runes
%gotest %{x_import_path}/search
#%%gotest %%{import_path}/secure/precis
%gotest %{x_import_path}/transform
%gotest %{x_import_path}/unicode/bidi
%gotest %{x_import_path}/unicode/cldr
#%gotest %{x_import_path}/unicode/norm
%gotest %{x_import_path}/unicode/rangetable
%gotest %{x_import_path}/width
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc AUTHORS CONTRIBUTORS PATENTS README

%files -n %{x_name}-devel -f x_devel.file-list
%doc LICENSE
%doc AUTHORS CONTRIBUTORS PATENTS README
%endif

%if 0%{?with_unit_test}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc CONTRIBUTORS
%endif

%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.21.git3bd178b
- new version

