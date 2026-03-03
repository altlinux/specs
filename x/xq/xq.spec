%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:		xq
Version:	1.4.0
Release:	alt1
Summary:	Command-line XML and HTML beautifier and content extractor

Group:		Development/Tools
License:	MIT
URL:		https://github.com/sibprogrammer/xq

Packager:	Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Command-line XML and HTML beautifier and content extractor 

%prep
%setup -q

%build
go build -a -ldflags '-s -w -X main.version=%version -X main.revision=altlinux' -tags "" -o bin/%name

%install
mkdir -p %buildroot%_bindir
#install main binary
install -Dpm0755 bin/%name %{buildroot}%{_bindir}/

#install man pages
install -d -p %{buildroot}%{_mandir}/man1
install -Dpm0644 docs/%name.man %{buildroot}%{_mandir}/man1/%name.1

%files
%_bindir/%name
%_mandir/man1/%name.1*

%changelog
* Tue Mar 3 2026 Vladimir Didenko <cow@altlinux.org> 1.4.0-alt1
- New version

* Tue Feb 10 2026 Vladimir Didenko <cow@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
