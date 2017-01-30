%global provider        github.com
%global project         opencontainers
%global repo            runc

%global provider_prefix %{provider}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          c91b5bea4830a57eac7882d7455d59518cdf70ec
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:           runc
Version:        1.0.0
Release:        alt2.git%shortcommit
Summary:        CLI for running Open Containers
Group:          Development/Other
License:        Apache 2.0
URL:            https://%provider_prefix
ExclusiveArch:  %go_arches

Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libseccomp-devel

%description
The runc command can be used to start containers which are packaged
in accordance with the Open Container Initiative's specifications,
and to manage containers running under runc.

%prep
%setup -q

%build
export GOPATH="%go_path"
make

%install
mkdir -p -- %buildroot/%_bindir
install -p -m 755 runc %buildroot/%_bindir

mkdir -p -- %buildroot/lib/tmpfiles.d
cat > %buildroot/lib/tmpfiles.d/runc.conf <<EOF
d /run/runc 0700 root root -
EOF

%files
%doc MAINTAINERS_GUIDE.md PRINCIPLES.md README.md CONTRIBUTING.md
%_bindir/*
/lib/tmpfiles.d/runc.conf

%changelog
* Mon Jan 23 2017 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt2.gitc91b5be
- New version.
- Fixes CVE-2016-9962.

* Tue Aug 2 2016 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1.git04f275d
- New version.

* Thu May 12 2016 Vladimir Didenko <cow@altlinux.ru> 0.1.1-alt1.gitbaf6536
- New version.

* Wed Mar 16 2016 Alexey Gladkov <legion@altlinux.ru> 0.0.9-alt1.git69fe79d
- First build for Altlinux.
