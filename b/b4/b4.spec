%define _unpackaged_files_terminate_build 1
%def_with check

Summary: A tool to work with public-inbox and patch archives
Name: b4
Version: 0.15.2
Release: alt1

Group: Development/Python
License: GPL-2.0-or-later
Url: https://git.kernel.org/pub/scm/utils/b4/b4.git/about/

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio

BuildRequires: python3(dkim)
BuildRequires: python3(git_filter_repo)
BuildRequires: python3(patatt)
BuildRequires: python3(requests)
BuildRequires: python3(textual)

BuildRequires: git
%endif

Requires: python3(dkim)
Requires: python3(git_filter_repo)
Requires: python3(patatt)

%description
This is a helper utility to work with patches made available via a
public-inbox archive like lore.kernel.org. It is written to make it
easier to participate in a patch-based workflows, like those used in
the Linux kernel development.

%define _unpackaged_files_terminate_build 1

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install
install -Dm644 src/b4/man/b4.1 %buildroot%_man1dir/b4.1

%check
%pyproject_run_pytest -vra \
  -k 'not test_trailers'

%files
%_bindir/b4
%_man1dir/b4*
%python3_sitelibdir_noarch/b4
%python3_sitelibdir_noarch/%{pyproject_distinfo b4}/

%changelog
* Thu Jul 23 2026 Ivan A. Melnikov <iv@altlinux.org> 0.15.2-alt1
- New release (0.15.2).
- Add requires for some optional dependencies (ALT#58355).
- Run unit tests during building.

* Sun Jan 08 2023 Alexey Gladkov <legion@altlinux.ru> 0.11.1-alt1
- New release (0.11.1).

* Sun Oct 16 2022 Alexey Gladkov <legion@altlinux.ru> 0.10.1-alt1
- New release (0.10.1).

* Sat Apr 23 2022 Alexey Gladkov <legion@altlinux.ru> 0.8.0-alt1
- New release (0.8.0).

* Thu Aug 12 2021 Alexey Gladkov <legion@altlinux.ru> 0.7.2.6.gf6071de-alt1
- Initial build.
