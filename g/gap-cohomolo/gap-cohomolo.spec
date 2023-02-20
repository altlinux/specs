%define repo cohomolo

Name: gap-cohomolo
Version: 1.6.11
Release: alt1
Summary: GAP: Cohomology groups of finite groups on finite modules
License: GPL-2.0
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/cohomolo

Source: https://github.com/gap-packages/cohomolo/releases/download/v%version/%repo-%version.tar.gz

BuildPreReq: fdupes
BuildPreReq: rpm-macros-gap
BuildRequires: gap-devel
Requires: gap >= 4.7

%description
The cohomolo package is a GAP interface to some C programs for
computing Schur multipliers and covering groups of finite groups and
first and second cohomology groups of finite groups acting on finite
modules.

%prep
%setup -n cohomolo-%version
sed -i 's/FILE  *ip,*op;/extern FILE  *ip,*op;/' \
    standalone/progs.d/crp1.c \
    standalone/progs.d/testchb.c
sed -i 's/FILE *ip,*op;/extern FILE *ip,*op;/' \
    standalone/progs.d/{egp.c,exa.c,gpp.c,gppb.c,grp.c,matperm.c,mcp.c,normp1.c,"nq+chfns.c",nqmfns.c,nqmp.c,optp.c,pcp.c,permmat.c,pkp.c,slg.c,subdir.c,sylp.c,sylp2.c,testmf.c,testmfz.c,testpf.c,wreath.c}

%build
find standalone/{README,info.d} -type f -exec chmod a-x "{}" "+"
./configure "%gapdir"
%make_build CFLAGS="-O2 -g"

%install
%gappkg_simple_install
rm -Rf %buildroot/$moddir/standalone/progs.d
fdupes %buildroot%_prefix

%files -f %name.files
%dir %gap_sitearch/%repo-%version/
%gap_sitearch/%repo-%version/*

%changelog
* Mon Feb 20 2023 Leontiy Volodin <lvol@altlinux.org> 1.6.11-alt1
- 1.6.11.

* Tue May 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.6.10-alt1
- 1.6.10.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.9-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
