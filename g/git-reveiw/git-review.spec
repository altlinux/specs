Name: git-reveiw
Version: 1.24
Release: alt1
Summary: A Git helper for integration with Gerrit

Group: Development/Tools
License: ASL 2.0
URL: https://github.com/openstack-infra/git-review

BuildArch: noarch

Requires: python = %_python_version
BuildPreReq: python-devel = %_python_version
BuildPreReq: rpm-build-python >= 0.8

BuildRequires: python-module-pbr

Source: %name-%version.tar

%description
An extension for source control system Git that creates and manages
review requests in the patch management system Gerrit.

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install
install -p -m 0644 -D git-review.1 %buildroot%_man1dir/git-review.1

%files
%doc README.rst LICENSE
%_bindir/git-review
%python_sitelibdir_noarch/git_review*
%exclude %python_sitelibdir_noarch/git_review/tests/
%_man1dir/*

%changelog
* Sun Mar 15 2015 Ivan A. Melnikov <iv@altlinux.org> 1.24-alt1
- Initial build for Sisyphus.
