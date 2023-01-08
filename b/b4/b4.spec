Summary: A tool to work with public-inbox and patch archives
Name: b4
Version: 0.11.1
Release: alt1

Group: Development/Python
License: GPL-2.0-or-later
Url: https://git.kernel.org/pub/scm/utils/b4/b4.git/about/

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

%description
This is a helper utility to work with patches made available via a
public-inbox archive like lore.kernel.org. It is written to make it
easier to participate in a patch-based workflows, like those used in
the Linux kernel development.

%define _unpackaged_files_terminate_build 1

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/b4
%_man5dir/*
%python3_sitelibdir_noarch/b4
%python3_sitelibdir_noarch/b4*.egg-info

%changelog
* Sun Jan 08 2023 Alexey Gladkov <legion@altlinux.ru> 0.11.1-alt1
- New release (0.11.1).

* Sun Oct 16 2022 Alexey Gladkov <legion@altlinux.ru> 0.10.1-alt1
- New release (0.10.1).

* Sat Apr 23 2022 Alexey Gladkov <legion@altlinux.ru> 0.8.0-alt1
- New release (0.8.0).

* Thu Aug 12 2021 Alexey Gladkov <legion@altlinux.ru> 0.7.2.6.gf6071de-alt1
- Initial build.
