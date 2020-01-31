Name:       git-reveiw
Version:    1.24
Release:    alt2

Summary:    A Git helper for integration with Gerrit
License:    ASL 2.0
Group:      Development/Tools
URL:        https://github.com/openstack-infra/git-review

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

Source:     %name-%version.tar


%description
An extension for source control system Git that creates and manages
review requests in the patch management system Gerrit.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install
install -p -m 0644 -D git-review.1 %buildroot%_man1dir/git-review.1

%files
%doc README.rst LICENSE
%_bindir/git-review
%python3_sitelibdir_noarch/git_review*
%exclude %python3_sitelibdir_noarch/git_review/tests/
%_man1dir/*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.24-alt2
- Porting on Python3.

* Sun Mar 15 2015 Ivan A. Melnikov <iv@altlinux.org> 1.24-alt1
- Initial build for Sisyphus.
