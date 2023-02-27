%define repo sophus

Name: gap-sophus
Version: 1.27
Release: alt1
Summary: Computing in nilpotent Lie algebras

License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/sophus/

Source: https://github.com/gap-packages/sophus/releases/download/v%version/%repo-%version.tar.gz
BuildArch: noarch

BuildRequires: rpm-macros-gap

Requires: gap
Requires: gap-autpgrp

%description
The Sophus package is written to compute with nilpotent Lie algebras
over finite prime fields.  Using this package, you can compute the
cover, the list of immediate descendants, and the automorphism group of
such Lie algebras.  You can also test if two such Lie algebras are
isomorphic.

The immediate descendant function of the package can be used to classify
small-dimensional nilpotent Lie algebras over a given field.  For
instance, the package author obtained a classification of nilpotent Lie
algebras with dimension at most 9 over F_2; see
http://www.sztaki.hu/~schneider/Research/SmallLie.

%prep
%setup -n %repo-%version

%build
%install
%gappkg_simple_install

%files -f %name.files
%dir %gap_sitelib/%repo-%version/
%gap_sitelib/%repo-%version/*

%changelog
* Mon Feb 27 2023 Leontiy Volodin <lvol@altlinux.org> 1.27-alt1
- New version.

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 1.24-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
