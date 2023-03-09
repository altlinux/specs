%define repo primgrp

Name: gap-primgrp
Version: 3.4.4
Release: alt1
Summary: GAP: Primitive Permutation Groups Library
License: GPL-2.0
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/primgrp/

Source: https://github.com/gap-packages/primgrp/releases/download/v%version/primgrp-%version.tar.gz

BuildArch: noarch
BuildRequires: rpm-macros-gap
Requires: gap >= 4.9
Requires: gap-gapdoc >= 1.5

%description
The PrimGrp package provides the library of primitive permutation
groups which includes, up to permutation isomorphism (i.e., up to
conjugacy in the corresponding symmetric group), all primitive
permutation groups of degree < 4096.

%prep
%setup -n primgrp-%version

%build
perl -i -pe 's{#!%_bindir/env }{#!/bin/}' scripts/*

%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Thu Mar 09 2023 Leontiy Volodin <lvol@altlinux.org> 3.4.4-alt1
- New version (3.4.4).

* Mon Jul 25 2022 Leontiy Volodin <lvol@altlinux.org> 3.4.2-alt1
- New version (3.4.2).

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
