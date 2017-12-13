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
%global project         keybase
%global repo            go-crypto
# https://github.com/keybase/go-crypto
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          433e2f3d43ef1bd31387582a899389b2fbe2005e
%global commitdate      20170628
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.1.%{commitdate}git%{shortcommit}
Summary:        Supplementary Go cryptography libraries (Keybase fork)
# Detected licences
# - BSD (3 clause) at 'LICENSE'
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

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
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif


Provides:      golang(%{import_path}/bcrypt) = %{version}-%{release}
Provides:      golang(%{import_path}/blowfish) = %{version}-%{release}
Provides:      golang(%{import_path}/bn256) = %{version}-%{release}
Provides:      golang(%{import_path}/brainpool) = %{version}-%{release}
Provides:      golang(%{import_path}/cast5) = %{version}-%{release}
Provides:      golang(%{import_path}/curve25519) = %{version}-%{release}
Provides:      golang(%{import_path}/ed25519) = %{version}-%{release}
Provides:      golang(%{import_path}/hkdf) = %{version}-%{release}
Provides:      golang(%{import_path}/md4) = %{version}-%{release}
Provides:      golang(%{import_path}/nacl/box) = %{version}-%{release}
Provides:      golang(%{import_path}/nacl/secretbox) = %{version}-%{release}
Provides:      golang(%{import_path}/ocsp) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/armor) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/clearsign) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/ecdh) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/elgamal) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/errors) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/packet) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/s2k) = %{version}-%{release}
Provides:      golang(%{import_path}/otr) = %{version}-%{release}
Provides:      golang(%{import_path}/pbkdf2) = %{version}-%{release}
Provides:      golang(%{import_path}/pkcs12) = %{version}-%{release}
Provides:      golang(%{import_path}/poly1305) = %{version}-%{release}
Provides:      golang(%{import_path}/ripemd160) = %{version}-%{release}
Provides:      golang(%{import_path}/rsa) = %{version}-%{release}
Provides:      golang(%{import_path}/salsa20) = %{version}-%{release}
Provides:      golang(%{import_path}/salsa20/salsa) = %{version}-%{release}
Provides:      golang(%{import_path}/scrypt) = %{version}-%{release}
Provides:      golang(%{import_path}/sha3) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/agent) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/terminal) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/test) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/testdata) = %{version}-%{release}
Provides:      golang(%{import_path}/tea) = %{version}-%{release}
Provides:      golang(%{import_path}/twofish) = %{version}-%{release}
Provides:      golang(%{import_path}/xtea) = %{version}-%{release}
Provides:      golang(%{import_path}/xts) = %{version}-%{release}

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

%build
%install
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
for file in $(find . -iname "*_test.go" -o -wholename "*/testdata/*") ; do
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
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%else
# No dependency directories so far

export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/bcrypt
%gotest %{import_path}/blowfish
%gotest %{import_path}/bn256
%gotest %{import_path}/brainpool
%gotest %{import_path}/cast5
%gotest %{import_path}/curve25519
%gotest %{import_path}/ed25519
%gotest %{import_path}/hkdf
%gotest %{import_path}/md4
%gotest %{import_path}/nacl/box
%gotest %{import_path}/nacl/secretbox
%gotest %{import_path}/ocsp
%gotest %{import_path}/openpgp
%gotest %{import_path}/openpgp/armor
%gotest %{import_path}/openpgp/clearsign
%gotest %{import_path}/openpgp/elgamal
%gotest %{import_path}/openpgp/packet
%gotest %{import_path}/openpgp/s2k
%gotest %{import_path}/otr
%gotest %{import_path}/pbkdf2
%gotest %{import_path}/pkcs12
%gotest %{import_path}/pkcs12/internal/rc2
%gotest %{import_path}/poly1305
%gotest %{import_path}/ripemd160
%gotest %{import_path}/rsa
%gotest %{import_path}/salsa20
%gotest %{import_path}/salsa20/salsa
%gotest %{import_path}/scrypt
%gotest %{import_path}/sha3
%gotest %{import_path}/ssh
%gotest %{import_path}/ssh/agent
%gotest %{import_path}/ssh/terminal
%gotest %{import_path}/ssh/test
%gotest %{import_path}/tea
%gotest %{import_path}/twofish
%gotest %{import_path}/xtea
%gotest %{import_path}/xts
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README PATENTS AUTHORS CONTRIBUTING.md CONTRIBUTORS
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc README PATENTS AUTHORS CONTRIBUTING.md CONTRIBUTORS
%endif

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.1.20170628git433e2f3
- new version

