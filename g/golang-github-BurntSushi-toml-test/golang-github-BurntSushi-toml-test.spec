Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora}
%global with_devel 0
%global with_bundled 0
%global with_debug 1
%global with_check 1
%else
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%global with_check 0
%endif

%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         BurntSushi
%global repo            toml-test
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          85f50d0991feaca39fd7c3ad1047acbf9df90859
%global shortcommit     %(c=%{commit}; echo ${c:0:7})


Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.2.0
Release:        alt1_0.12.git%{shortcommit}
Summary:        Language agnostic test suite for TOML
License:        WTFPL
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{commit}.tar.gz
Provides:       toml-test = %{version}-%{release}
BuildRequires:  golang >= 1.2.1
Source44: import.info

%description
toml-test is a higher-order program that tests other TOML decoders or
encoders. Tests are divided into two groups: invalid TOML data and valid TOML
data. Decoders that reject invalid TOML data pass invalid TOML tests. Decoders
that accept valid TOML data and output precisely what is expected pass valid
tests.



%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:        Language agnostic test suite for TOML devel package
BuildArch:      noarch

%description devel
toml-test is a higher-order program that tests other TOML decoders or
encoders. Tests are divided into two groups: invalid TOML data and valid TOML
data. Decoders that reject invalid TOML data pass invalid TOML tests. Decoders
that accept valid TOML data and output precisely what is expected pass valid
tests.

Devel package.
%endif


%prep
%setup -q -n %{repo}-%{commit}


%build
mkdir -p _build/src/github.com/BurntSushi
ln -sf $(pwd) _build/src/github.com/BurntSushi/toml-test
export GOPATH=$(pwd)/_build:%{go_path}
mkdir bin

%if 0%{?with_debug}
function gobuild { go build -a -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -v -x "$@"; }
%else
function gobuild { go build -a "$@"; }
%endif

gobuild -o bin/%{repo} %{import_path}


%install
install -D -p -m 0755 bin/%{repo} %{buildroot}%{_bindir}/%{repo}
mkdir -p  %{buildroot}%{_datadir}/%{repo}/
cp -a tests %{buildroot}%{_datadir}/%{repo}/

%if 0%{?with_devel}
# install devel source codes
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
%endif


%files
%if 0%{?fedora}
%doc COPYING
%else
%doc COPYING
%endif
%doc README.md
%{_bindir}/%{repo}
%{_datadir}/%{repo}/

%if 0%{?with_devel}
%files devel
%if 0%{?fedora}
%doc COPYING
%else
%doc README.md COPYING
%endif
%doc README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%{go_path}/src/%{import_path}
%endif


%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_0.12.git85f50d0
- new version

