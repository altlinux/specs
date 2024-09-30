
%define _unpackaged_files_terminate_build 1
%define _customdocdir %_defaultdocdir/%name

Name:       git-review
Version:    2.4.0
Release:    alt1

Summary:    A Git helper for integration with Gerrit
License:    ASL 2.0
Group:      Development/Tools
URL:        https://github.com/openstack-infra/git-review

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pbr)
BuildRequires: python3(requests)

# I made a typo some many many years ago...
Provides:   git-reveiw = %EVR
Obsoletes:  git-reveiw < %EVR

Source:     %name-%version.tar
Patch:      %name-%version-%release.patch


%description
An extension for source control system Git that creates and manages
review requests in the patch management system Gerrit.

%prep
%setup -n %name-%version
%autopatch -p1

%build
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install
install -p -m 0644 -D git-review.1 %buildroot%_man1dir/git-review.1


%files
%doc README.rst LICENSE
%_bindir/git-review
%python3_sitelibdir_noarch/git_review*
%exclude %python3_sitelibdir_noarch/git_review/tests/
%_man1dir/*

%changelog
* Mon Sep 30 2024 Ivan A. Melnikov <iv@altlinux.org> 2.4.0-alt1
- 2.4.0;
- build from git
- fix typo in the package name (ALT#37977)

* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.24-alt2
- Porting on Python3.

* Sun Mar 15 2015 Ivan A. Melnikov <iv@altlinux.org> 1.24-alt1
- Initial build for Sisyphus.
