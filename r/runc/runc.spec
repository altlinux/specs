%global provider        github.com
%global project         opencontainers
%global repo            runc

%global provider_prefix %{provider}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1
%global commit      58aa9203c123022138b22cf96540c284876a7910
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:           runc
Version:        1.1.13
Release:        alt1
Summary:        CLI for running Open Containers
Group:          Development/Other
License:        Apache-2.0
URL:            https://%provider_prefix
ExclusiveArch:  %go_arches

Source0:        %name-%version.tar

Patch1:         runc-alt-loongarch64-support.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-md2man
BuildRequires: libseccomp-devel
Provides: oci-runtime
Provides: docker-runc = %version-%release
Obsoletes: docker-runc <= 1.0.0-alt2.gitb2567b3

%description
The runc command can be used to start containers which are packaged
in accordance with the Open Container Initiative's specifications,
and to manage containers running under runc.

%prep
%setup -q
sed -i 's/ -trimpath//g' Makefile
sed -i '/\#\!\/bin\/bash/d' contrib/completions/bash/%name
%patch1 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare
make COMMIT=%shortcommit BUILDTAGS="seccomp selinux" all

%install
mkdir -p -- %buildroot%_bindir
install -p -m 755 %name %buildroot%_bindir/%name

# generate man pages
man/md2man-all.sh

# install man pages
install -d -p %buildroot%_man8dir
install -p -m 0644 man/man8/*.8 %buildroot%_man8dir/
# install bash completion
install -d -p %buildroot%_datadir/bash-completion/completions
install -p -m 0644 contrib/completions/bash/%name %buildroot%_datadir/bash-completion/completions/

%files
%doc MAINTAINERS_GUIDE.md PRINCIPLES.md README.md CONTRIBUTING.md
%_bindir/*
%_man8dir/*
%_datadir/bash-completion/completions/%name

%changelog
* Fri Jun 14 2024 Vladimir Didenko <cow@altlinux.ru> 1.1.13-alt1
- New version

* Fri Feb 02 2024 Alexey Shabalin <shaba@altlinux.org> 1.1.12-alt1
- New version 1.1.12 (Fixes: CVE-2024-21626).
- Drop tmpfiles.d/runc.conf

* Wed Jan 10 2024 Vladimir Didenko <cow@altlinux.ru> 1.1.11-alt1
- New version

* Thu Nov 23 2023 Vladimir Didenko <cow@altlinux.ru> 1.1.10-alt1
- New version

* Thu Nov 02 2023 Ivan A. Melnikov <iv@altlinux.org> 1.1.9-alt1.1
- NMU: add patch for loongarch64 support

* Wed Sep 6 2023 Vladimir Didenko <cow@altlinux.ru> 1.1.9-alt1
- New version

* Wed Jul 26 2023 Vladimir Didenko <cow@altlinux.ru> 1.1.8-alt1
- New version

* Wed May 3 2023 Vladimir Didenko <cow@altlinux.ru> 1.1.7-alt1
- New version

* Wed Apr 19 2023 Vladimir Didenko <cow@altlinux.ru> 1.1.6-alt1
- New version

* Tue Apr 4 2023 Vladimir Didenko <cow@altlinux.ru> 1.1.5-alt1
- New version (Fixes: CVE-2023-25809, CVE-2023-27561, CVE-2023-28642)

* Mon Sep 12 2022 Vladimir Didenko <cow@altlinux.ru> 1.1.4-alt1
- New version

* Tue Jul 26 2022 Vladimir Didenko <cow@altlinux.ru> 1.1.3-alt1
- New version

* Thu May 12 2022 Vladimir Didenko <cow@altlinux.ru> 1.1.2-alt1
- New version (Fixes: CVE-2022-29162)

* Fri Mar 11 2022 Vladimir Didenko <cow@altlinux.ru> 1.1.0-alt1
- New version

* Wed Dec 22 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.3-alt2
- Define COMMIT as %%release
- Build and install man pages
- Package bash completion

* Fri Dec 17 2021 Vladimir Didenko <cow@altlinux.ru> 1.0.3-alt1
- New version (Fixes: CVE-2021-43784)

* Thu Sep 23 2021 Vladimir Didenko <cow@altlinux.ru> 1.0.2-alt1
- New version

* Thu Aug 5 2021 Vladimir Didenko <cow@altlinux.ru> 1.0.1-alt1
- New version

* Fri Jun 18 2021 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt17.rc95
- New version (Fixes: CVE-2021-30465)

* Sat Feb 20 2021 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt16.rc93
- Fix build with golang 1.16

* Tue Feb 9 2021 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt15.rc93
- New version

* Tue Sep 29 2020 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt14.rc92
- New version

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt13.rc91
- New version

* Mon Feb 17 2020 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt12.rc10
- New version
- Fixes CVE-2019-19921

* Tue Dec 10 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt11.rc9
- Print user friendly error on cgroups v2
- Fix license name

* Thu Oct 10 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt10.rc9
- New version
- fixes: CVE-2019-16884

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt9.rc8
- New version

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt8.rc7
- New version

* Wed Feb 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt7.git0a012df
- snapshot of master branch.
- Fixes CVE-2019-5736.

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt6.rc6
- New version (for docker 18.09.1-ce).

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt5.git69663f0
- New version (for docker 18.06.0-ce).

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt4.rc5
- New version (for docker 18.03.0-ce).

* Mon Feb 5 2018 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt3.git9f9c962
- New version (for docker 18.02.0-ce).

* Mon Jan 23 2017 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt2.gitc91b5be
- New version.
- Fixes CVE-2016-9962.

* Tue Aug 2 2016 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1.git04f275d
- New version.

* Thu May 12 2016 Vladimir Didenko <cow@altlinux.ru> 0.1.1-alt1.gitbaf6536
- New version.

* Wed Mar 16 2016 Alexey Gladkov <legion@altlinux.ru> 0.0.9-alt1.git69fe79d
- First build for Altlinux.
