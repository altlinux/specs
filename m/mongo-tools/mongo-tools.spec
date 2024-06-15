# debuginfo extraction currently fails with
# "Failed to write file: invalid section alignment"
%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%global gopath %_libdir/golang
%global goroot %_libdir/golang

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
Version: 100.9.5
Release: alt1

Summary: Mongo client tools
License: Apache-2.0
Url: https://github.com/mongodb/mongo-tools
Group: Development/Databases

Source: %name-%version.tar
Source1: man.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.3
BuildRequires: libssl-devel libpcap-devel

Conflicts:      mongo < 3.0.0

%description
The MongoDB tools provides import, export, and diagnostic capabilities.

%prep
%setup
tar xf %SOURCE1

%build
# Temporary workaround to build with golang 1.16. Waiting for upstream to
# add go modules support.
export GO111MODULE=off
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"
%golang_prepare
rm -fr "$BUILDDIR/src/$IMPORT_PATH/vendor"
cp -alv -- vendor/* "$BUILDDIR/src"

mkdir bin
binaries=(bsondump mongostat mongofiles mongoexport mongoimport mongorestore mongodump mongotop)
for bin in "${binaries[@]}"; do
    go build -o bin/${bin} \-tags ssl $BUILDDIR/src/%{import_path}/${bin}/main/${bin}.go
done

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/* %{buildroot}%{_bindir}

# Mongo-tools does not contain man files yet
# - see https://groups.google.com/forum/#!topic/mongodb-dev/t6Sd2Bki12I
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/* %{buildroot}%{_man1dir}/

%files
%doc README.md CONTRIBUTING.md THIRD-PARTY-NOTICES LICENSE.md
%_bindir/*
%_man1dir/*.1*

%changelog
* Sat Jun 15 2024 Andrey Cherepanov <cas@altlinux.org> 100.9.5-alt1
- New version.

* Mon Feb 12 2024 Andrey Cherepanov <cas@altlinux.org> 100.9.4-alt1
- New version (ALT #49305).
- Fixed summary.

* Sat Feb 20 2021 Vladimir Didenko <cow@altlinux.org> 4.2.12-alt1
- 4.2.12
- fix build with golang 1.16

* Mon Jun 29 2020 Vladimir Didenko <cow@altlinux.org> 4.2.8-alt1
- 4.2.8

* Tue Apr 28 2020 Vladimir Didenko <cow@altlinux.org> 4.2.6-alt1
- 4.2.6

* Wed Feb 5 2020 Vladimir Didenko <cow@altlinux.org> 4.2.3-alt1
- 4.2.3
- update man pages
- fix license name

* Fri Oct 25 2019 Vladimir Didenko <cow@altlinux.org> 4.2.1-alt1
- 4.2.1

* Wed Sep 11 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Thu Aug 1 2019 Vladimir Didenko <cow@altlinux.org> 4.0.11-alt1
- 4.0.11

* Fri Apr 5 2019 Vladimir Didenko <cow@altlinux.org> 4.0.8-alt1
- 4.0.8 (closes: #36520)

* Tue Mar 26 2019 Vladimir Didenko <cow@altlinux.org> 4.0.7-alt1
- 4.0.7

* Fri Jan 25 2019 Vladimir Didenko <cow@altlinux.org> 4.0.5-alt2
- Remove golang-tools-devel from build reqs

* Thu Jan 17 2019 Vladimir Didenko <cow@altlinux.org> 4.0.5-alt1
- 4.0.5

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.org> 4.0.4-alt1
- 4.0.4

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1
- 4.0.0

* Tue Mar 13 2018 Vladimir Didenko <cow@altlinux.org> 3.6.3-alt1
- 3.6.3

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
