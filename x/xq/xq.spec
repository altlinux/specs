%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name: xq
Version: 1.5.1
Release: alt1
Summary: Command-line XML and HTML beautifier and content extractor

Group: Development/Tools
License: MIT
Url: https://github.com/sibprogrammer/xq
Vcs: https://github.com/sibprogrammer/xq

Source0: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Command-line XML and HTML beautifier and content extractor

%prep
%setup

%build
go build -a -ldflags '-s -w -X main.version=%version -X main.revision=altlinux' -tags "" -o bin/%name

%install
mkdir -p %buildroot%_bindir
#install main binary
install -Dpm0755 bin/%name %buildroot%_bindir/

#install man pages
install -d -p %buildroot%_mandir/man1
install -Dpm0644 docs/%name.man %buildroot%_mandir/man1/%name.1

%files
%_bindir/%name
%_mandir/man1/%name.1*

%changelog
* Fri Sep 25 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1
- added VCS

* Fri Aug 21 2026 Vladimir Didenko <cow@altlinux.org> 1.5.0-alt1
- New version

* Tue Mar 3 2026 Vladimir Didenko <cow@altlinux.org> 1.4.0-alt1
- New version

* Tue Feb 10 2026 Vladimir Didenko <cow@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
