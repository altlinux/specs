Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package   %{nil}

%global provider        github
%global provider_tld    com
%global project         ThomsonReutersEikon
%global repo            go-ntlm
# https://github.com/ThomsonReutersEikon/go-ntlm
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          2a7c173f9e18233a4ae29891da6a0a63637e2d8d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20171030

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.5.%{commitdate}git%{shortcommit}
Summary:        Native implementation of NTLM for Go
License:        BSD with advertising
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
# https://github.com/ThomsonReutersEikon/go-ntlm/pull/11
Patch0001:      fix-go110.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}.

%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}/ntlm) = %{version}-%{release}
Provides:      golang(%{import_path}/ntlm/md4) = %{version}-%{release}

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package unit-test-devel
Group: Development/Other
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage

%description unit-test-devel
%{summary}.

This package contains unit tests for project
providing packages with %{import_path} prefix.

%prep
%setup -q -n %{repo}-%{commit}
%patch1 -p1

%build

%install
# source codes for building projects
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
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
rm -f devel.file-list.dir

# testing files for this project
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> unit-test-devel.file-list.dir
    done
done
[ -s unit-test-devel.file-list.dir ] && sort -u unit-test-devel.file-list.dir >> unit-test-devel.file-list
rm -f unit-test-devel.file-list.dir

sort -u -o devel.file-list devel.file-list

%check
export GOPATH=%{buildroot}/%{go_path}:%{go_path}

%gotest %{import_path}/ntlm
%gotest %{import_path}/ntlm/md4

%files devel -f devel.file-list
%doc --no-dereference License
%doc README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}

%files unit-test-devel -f unit-test-devel.file-list
%doc --no-dereference License
%doc README.md

%changelog
* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.5.20171030git2a7c173
- fc update

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.3.20151029gitb00ec39
- new version

