Name: gnulib
Version: 0.1.6840.3f463
Release: alt1

Summary: GNU Portability Library
# assorted licenses, see the source
License: GPL-3.0-or-later and LGPL-2.1-or-later and GFDL-1.3-or-later
Group: Development/C
BuildArch: noarch
Url: https://www.gnu.org/software/gnulib/
Source: %name-%version.tar
# git://git.altlinux.org/people/ldv/packages/gnulib refs/heads/po-current
Source1: po-%version-%release.tar
Patch1: gnulib-alt-utimens.patch
Patch2: gnulib-alt-mktime-internal.patch
AutoReqProv: no
BuildRequires: gnu-config makeinfo

%description
Gnulib is intended to be the canonical source for most of the important
"portability" and/or common files for GNU projects.  These are files
intended to be shared at the source level; Gnulib is not a typical
library meant to be installed and linked against.  Thus, unlike most
projects, Gnulib does not normally generate a source tarball
distribution; instead, developers grab modules directly from the
source repository.

%prep
%setup -a1
%patch1 -p1
%patch2 -p1

install -pm755 %_datadir/gnu-config/config.{guess,sub} build-aux/

%build
# Generate LINGUAS file.
ls build-aux/po/*.po | sed 's|.*/||; s|\.po$||' > build-aux/po/LINGUAS

make info

%install
rm -rf build-check
mkdir -p %buildroot{%_bindir,%_infodir,%_datadir/%name}
cp -a * %buildroot%_datadir/%name/
for f in check-module gnulib-tool; do
	ln -s $(relative %_datadir/%name/$f %_bindir/) %buildroot%_bindir/
done
mv %buildroot%_datadir/%name/doc/*.info %buildroot%_infodir/

%check
./gnulib-tool --create-testdir --dir build-check regex
cd build-check
%add_optflags -DDEBUG
%configure
%make_build -k check VERBOSE=1

%files
%_bindir/*
%_infodir/*
%_datadir/%name/

%changelog
* Wed Dec 06 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.6840.3f463-alt1
- v0.1-6734-gfbd3fbba93 -> v0.1-6840-g3f463202bd.

* Wed Sep 13 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.6734.fbd3f-alt1
- v0.1-5208-gc8b8f3bbcd -> v0.1-6734-gfbd3fbba93.
- Fixed the License: tag (Freely distributable -> GPL-3.0-or-later and
  LGPL-2.1-or-later and GFDL-1.3-or-later).

* Fri Apr 22 2022 Dmitry V. Levin <ldv@altlinux.org> 0.1.5208.c8b8f-alt1
- v0.1-4724-g7e3a9c5bd -> v0.1-5208-gc8b8f3bbcd.

* Tue Jun 22 2021 Dmitry V. Levin <ldv@altlinux.org> 0.1.4724.7e3a9-alt1
- v0.1-4683-g4480dd39f -> v0.1-4724-g7e3a9c5bd.

* Wed Jun 09 2021 Dmitry V. Levin <ldv@altlinux.org> 0.1.4683.4480d-alt1
- v0.1-4669-gfed6ffdbb -> v0.1-4683-g4480dd39f.

* Sun Jun 06 2021 Dmitry V. Levin <ldv@altlinux.org> 0.1.4669.fed6f-alt1
- v0.1-4550-g2a7948aad -> v0.1-4669-gfed6ffdbb.

* Wed Apr 07 2021 Dmitry V. Levin <ldv@altlinux.org> 0.1.4550.2a794-alt1
- v0.1-2433-g3043e43a7 -> v0.1-4550-g2a7948aad.

* Tue Jun 11 2019 Nikita Ermakov <arei@altlinux.org> 0.1.2433.3043e-alt2
- Ensure nproc(NPROC_ALL) >= nproc(NPROC_CURRENT) with glibc >= 2.26.

* Sat Feb 02 2019 Dmitry V. Levin <ldv@altlinux.org> 0.1.2433.3043e-alt1
- v0.1-2313-g4652c7baf -> v0.1-2433-g3043e43a7 (closes: ##35859).

* Wed Jan 02 2019 Dmitry V. Levin <ldv@altlinux.org> 0.1.2313.4652c-alt1
- v0.1-2305-g95c96b6dd -> v0.1-2313-g4652c7baf.

* Fri Dec 21 2018 Dmitry V. Levin <ldv@altlinux.org> 0.1.2305.95c96-alt1
- v0.1-1213-g683b60789 -> v0.1-2305-g95c96b6dd.

* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1213.683b6-alt2
- Fixed includes for new toolchain

* Sun Mar 26 2017 Dmitry V. Levin <ldv@altlinux.org> 0.1.1213.683b6-alt1
- v0.1-1209-g24b3216 -> v0.1-1213-g683b607.

* Mon Mar 20 2017 Dmitry V. Levin <ldv@altlinux.org> 0.1.1209.24b32-alt1
- v0.1-585-g2fda85e -> v0.1-1209-g24b3216.

* Wed Oct 07 2015 Dmitry V. Levin <ldv@altlinux.org> 0.1.585.2fda85-alt2
- Hacked forced mktime replacement out of mktime-internal module.

* Tue Oct 06 2015 Dmitry V. Levin <ldv@altlinux.org> 0.1.585.2fda85-alt1
- Updated to gnulib snapshot v0.1-585-g2fda85e.

* Mon May 25 2015 Dmitry V. Levin <ldv@altlinux.org> 0.1.443.875ec93-alt1
- Updated to gnulib snapshot v0.1-443-g875ec93.

* Fri Feb 21 2014 Dmitry V. Levin <ldv@altlinux.org> 0.1.114.caf1b31-alt2
- Adjusted link rules to link tests with -lpthread in --no-as-needed mode.

* Wed Feb 19 2014 Dmitry V. Levin <ldv@altlinux.org> 0.1.114.caf1b31-alt1
- Updated to gnulib snapshot v0.1-114-gcaf1b31.

* Sat Jan 04 2014 Dmitry V. Levin <ldv@altlinux.org> 0.1.58.0f3a662-alt1
- Updated to gnulib snapshot v0.1-58-g0f3a662.

* Mon Oct 28 2013 Dmitry V. Levin <ldv@altlinux.org> 0.0.8061.5191b35-alt1
- Updated to gnulib snapshot v0.0-8061-g5191b35.

* Thu Apr 11 2013 Dmitry V. Levin <ldv@altlinux.org> 0.0.7902.92f3a4c-alt1
- Updated to gnulib snapshot v0.0-7902-g92f3a4c.

* Sun Apr 07 2013 Dmitry V. Levin <ldv@altlinux.org> 0.0.7901.076ac82-alt1
- Updated to gnulib snapshot v0.0-7901-g076ac82.

* Tue Nov 20 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7696.fd9f1ac-alt1
- Updated to gnulib snapshot v0.0-7696-gfd9f1ac.

* Mon Oct 29 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7677.4027785-alt2
- Updated to gnulib snapshot v0.0-7677-g4027785.

* Mon Aug 20 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7591.898f143-alt1
- Updated to gnulib snapshot v0.0-7591-g898f143.
- Use config.{guess,sub} from gnu-config.

* Mon Aug 13 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7575.d22f151-alt1
- Updated to gnulib snapshot v0.0-7575-gd22f151.

* Fri Aug 03 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7557.ee60576-alt1
- Updated to gnulib snapshot v0.0-7557-gee60576.

* Wed Apr 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7312.7995834-alt1
- Updated to gnulib snapshot v0.0-7312-g7995834.

* Wed Jan 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.6780.bfacc22-alt1
- Updated to gnulib snapshot v0.0-6780-gbfacc22.
- Applied patches originally made for coreutils.

* Thu Sep 15 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.6125.da1717b-alt1
- Updated to gnulib snapshot v0.0-6125-gda1717b.

* Tue Jun 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.5864.0f247f9-alt1
- Updated to gnulib snapshot v0.0-5864-g0f247f9.

* Wed Feb 02 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.4800.a036b76-alt1
- Gnulib snapshot v0.0-4800-ga036b76.
