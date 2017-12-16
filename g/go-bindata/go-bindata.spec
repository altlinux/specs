Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora}
%global with_devel 1
%global with_bundled 0
%global with_debug 1
# Some tests fails and it takes a lot of time to investigate
# what is wrong
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

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**}; 
%endif

%global provider        github
%global provider_tld    com
%global project         jteeuwen
%global repo            go-bindata
# https://github.com/jteeuwen/go-bindata
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          a0ff2567cfb70903282db057e799fd826784d41d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           go-bindata
Version:        3.0.7
Release:        alt1_11.git%{shortcommit}
Summary:        A small utility which generates Go code from any file
License:        MIT
URL:		https://%{provider_prefix}
Source0:	https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}

This tool converts any file into managable Go source code. Useful for
embedding binary data into a go program. The file data is optionally gzip
compressed before being converted to a raw byte slice.

%prep
%setup -n go-bindata-%{commit}

%build
mkdir -p src/github.com/jteeuwen/
ln -s ../../../ src/github.com/jteeuwen/go-bindata

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{go_path}
%else
export GOPATH=$(pwd):$(pwd)/Godeps/_workspace:%{go_path}
%endif

%gobuild -o bin/go-bindata %{import_path}/go-bindata

%install
install -d -p %{buildroot}%{_bindir}
install -m 755 bin/go-bindata %{buildroot}%{_bindir}/go-bindata

%files
%doc LICENSE README.md
%{_bindir}/go-bindata

%changelog
* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.7-alt1_11.gita0ff256
- new version

