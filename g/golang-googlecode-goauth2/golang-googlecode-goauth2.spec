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
# Cyclic deps among cloud, grpc and oauth2
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
%global project         golang
%global repo            oauth2
# https://github.com/golang/oauth2
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/oauth2
%global commit          5432cc9688e6250a0dd8f5a5f4c781d92b398be6
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global gc_rev             afe77d958c701557ec5dc56f6936fcc194d15520
%global gc_shortrev        %(r=%{gc_rev}; echo ${r:0:12})
%global gc_provider        google
%global gc_provider_sub    code
%global gc_provider_tld    com
%global gc_repo            goauth2
%global gc_import_path     %{gc_provider_sub}.%{gc_provider}.%{gc_provider_tld}/p/%{gc_repo}
%global gc_name            golang-%{gc_provider}%{gc_provider_sub}-%{gc_repo}

%global x_name          golang-golangorg-oauth2
%global devel_main      %{x_name}-devel

Name:           golang-googlecode-goauth2
Version:        0
Release:        alt1_0.22.git%{shortcommit}
Summary:        OAuth 2.0 for Go clients
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:        https://%{gc_repo}.%{gc_provider}%{gc_provider_sub}.%{gc_provider_tld}/archive/%{gc_rev}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}

%if 0%{?with_devel}
%package -n %{x_name}-devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/appengine)
BuildRequires: golang(google.golang.org/appengine/urlfetch)
%endif

Requires:      golang(golang.org/x/net/context)
Requires:      golang(google.golang.org/appengine)
Requires:      golang(google.golang.org/appengine/urlfetch)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/amazon) = %{version}-%{release}
Provides:      golang(%{import_path}/bitbucket) = %{version}-%{release}
Provides:      golang(%{import_path}/clientcredentials) = %{version}-%{release}
Provides:      golang(%{import_path}/facebook) = %{version}-%{release}
Provides:      golang(%{import_path}/fitbit) = %{version}-%{release}
Provides:      golang(%{import_path}/foursquare) = %{version}-%{release}
Provides:      golang(%{import_path}/github) = %{version}-%{release}
Provides:      golang(%{import_path}/google) = %{version}-%{release}
Provides:      golang(%{import_path}/heroku) = %{version}-%{release}
Provides:      golang(%{import_path}/hipchat) = %{version}-%{release}
Provides:      golang(%{import_path}/jws) = %{version}-%{release}
Provides:      golang(%{import_path}/jwt) = %{version}-%{release}
Provides:      golang(%{import_path}/linkedin) = %{version}-%{release}
Provides:      golang(%{import_path}/mediamath) = %{version}-%{release}
Provides:      golang(%{import_path}/microsoft) = %{version}-%{release}
Provides:      golang(%{import_path}/odnoklassniki) = %{version}-%{release}
Provides:      golang(%{import_path}/paypal) = %{version}-%{release}
Provides:      golang(%{import_path}/slack) = %{version}-%{release}
Provides:      golang(%{import_path}/uber) = %{version}-%{release}
Provides:      golang(%{import_path}/vk) = %{version}-%{release}
Provides:      golang(%{import_path}/yandex) = %{version}-%{release}

%description -n %{x_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package -n %{gc_name}-devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{gc_import_path}/appengine/serviceaccount) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/compute/serviceaccount) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/oauth) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/oauth/jwt) = %{version}-%{release}

%description -n %{gc_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gc_import_path} prefix.
%endif

%if 0%{?with_unit_test}
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
%setup -q -n %{gc_repo}-%{gc_shortrev} -T -b 1
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
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
done
[ -s devel.file-list.dir ] && sort -u devel.file-list.dir >> devel.file-list

install -d -p %{buildroot}/%{go_path}/src/%{gc_import_path}/
pushd ../%{gc_repo}-%{gc_shortrev}
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{gc_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{gc_import_path}/$file
    echo "%%{go_path}/src/%%{gc_import_path}/$file" >> ../%{repo}-%{commit}/gc_devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{gc_import_path}/$filedir" >> ../%{repo}-%{commit}/gc_devel.file-list.dir
    done
done
[ -s ../%{repo}-%{commit}/gc_devel.file-list.dir ] && sort -u ../%{repo}-%{commit}/gc_devel.file-list.dir >> ../%{repo}-%{commit}/gc_devel.file-list
popd

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

%gotest %{import_path}
%gotest %{import_path}/clientcredentials
# open testdata/gcloud/credentials: no such file or directory
#%gotest %{import_path}/google
%gotest %{import_path}/internal
%gotest %{import_path}/jws
%gotest %{import_path}/jwt
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files -n %{x_name}-devel -f devel.file-list
%doc LICENSE
%doc README.md CONTRIBUTING.md AUTHORS CONTRIBUTORS
%dir %{go_path}/src/%{import_path}

%files -n %{gc_name}-devel -f gc_devel.file-list
%doc LICENSE
%doc README.md CONTRIBUTING.md AUTHORS CONTRIBUTORS
%dir %{go_path}/src/%{gc_import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README.md CONTRIBUTING.md AUTHORS CONTRIBUTORS
%endif

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.22.git5432cc9
- new version

