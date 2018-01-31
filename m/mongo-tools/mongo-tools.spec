# debuginfo extraction currently fails with
# "Failed to write file: invalid section alignment"
%global __find_debuginfo_files %nil

%global _unpackaged_files_terminate_build 1

%global gopath    %_libdir/golang
%global goroot    %_libdir/golang

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %goroot %_bindir
%brp_strip_none %_bindir/*

%global provider        github
%global provider_tld    com
%global project         mongodb
%global repo            mongo-tools
# https://github.com/mongodb/mongo-tools
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name: mongo-tools
Version: 3.6.2
Release: alt1
Summary: mongo client shell and tools
License: ASL 2.0
Url: https://github.com/mongodb/mongo-tools
Group: Development/Databases

Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar

BuildRequires: golang >= 1.3
BuildRequires: golang-tools-devel
BuildRequires: libssl-devel libpcap-devel

Conflicts:      mongo < 3.0.0

%description
The MongoDB tools provides import, export, and diagnostic capabilities.

%package devel
Group: Development/Other
Requires: golang
Summary: %{summary}
Provides:      golang(%{import_path}/bsondump) = %{version}-%{release}
Provides:      golang(%{import_path}/common) = %{version}-%{release}
Provides:      golang(%{import_path}/common/archive) = %{version}-%{release}
Provides:      golang(%{import_path}/common/auth) = %{version}-%{release}
Provides:      golang(%{import_path}/common/bsonutil) = %{version}-%{release}
Provides:      golang(%{import_path}/common/db) = %{version}-%{release}
Provides:      golang(%{import_path}/common/db/kerberos) = %{version}-%{release}
Provides:      golang(%{import_path}/common/db/openssl) = %{version}-%{release}
Provides:      golang(%{import_path}/common/intents) = %{version}-%{release}
Provides:      golang(%{import_path}/common/json) = %{version}-%{release}
Provides:      golang(%{import_path}/common/log) = %{version}-%{release}
Provides:      golang(%{import_path}/common/options) = %{version}-%{release}
Provides:      golang(%{import_path}/common/password) = %{version}-%{release}
Provides:      golang(%{import_path}/common/progress) = %{version}-%{release}
Provides:      golang(%{import_path}/common/signals) = %{version}-%{release}
Provides:      golang(%{import_path}/common/testutil) = %{version}-%{release}
Provides:      golang(%{import_path}/common/text) = %{version}-%{release}
Provides:      golang(%{import_path}/common/util) = %{version}-%{release}
Provides:      golang(%{import_path}/mongodump) = %{version}-%{release}
Provides:      golang(%{import_path}/mongoexport) = %{version}-%{release}
Provides:      golang(%{import_path}/mongofiles) = %{version}-%{release}
Provides:      golang(%{import_path}/mongoimport) = %{version}-%{release}
Provides:      golang(%{import_path}/mongoimport/csv) = %{version}-%{release}
Provides:      golang(%{import_path}/mongooplog) = %{version}-%{release}
Provides:      golang(%{import_path}/mongorestore) = %{version}-%{release}
Provides:      golang(%{import_path}/mongostat) = %{version}-%{release}
Provides:      golang(%{import_path}/mongotop) = %{version}-%{release}


%description devel
This is the source libraries for mongo-tools.

%prep
%setup

%build
mkdir -p src/github.com/mongodb

ln -s ../../../  src/github.com/mongodb/mongo-tools
export GOPATH=$(pwd):$(pwd)/vendor:%{gopath}

mkdir bin
binaries=(bsondump mongostat mongofiles mongoexport mongoimport mongorestore mongodump mongotop mongoreplay)
for bin in "${binaries[@]}"; do
    go build -o bin/${bin} \-tags ssl ${bin}/main/${bin}.go
done

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/* %{buildroot}%{_bindir}

# Mongo-tools does not contain man files yet
# - see https://groups.google.com/forum/#!topic/mongodb-dev/t6Sd2Bki12I
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/* %{buildroot}%{_mandir}/man1/

install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
sort -u -o devel.file-list devel.file-list

%files
%doc Godeps README.md CONTRIBUTING.md THIRD-PARTY-NOTICES LICENSE.md
%_bindir/*
%{_mandir}/man1/*

%files devel
%{gopath}/src/%{import_path}

%changelog
* Wed Jan 31 2018 Vladimir Didenko <cow@altlinux.org> 3.6.2-alt1
- 3.6.2

* Mon Apr 10 2017 Vladimir Didenko <cow@altlinux.org> 3.4.3-alt1
- 3.4.3

* Thu Dec 8 2016 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue May 17 2016 Vladimir Didenko <cow@altlinux.org> 3.2.5-alt1
- 3.2.5

* Wed Dec 2 2015 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1.rc5
- 3.2.0 rc5
