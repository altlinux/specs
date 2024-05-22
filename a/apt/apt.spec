%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

Name: apt
Version: 0.5.15lorg2
Release: alt88

Summary: Debian's Advanced Packaging Tool with RPM support
Summary(ru_RU.UTF-8): Debian APT - Усовершенствованное средство управления пакетами с поддержкой RPM
License: GPL-2.0-or-later
Group: System/Configuration/Packaging
URL: http://apt-rpm.org
# Known upstream "apt-rpm" Git repos:
# -----------------------------------
#
# * http://apt-rpm.org/scm/apt.git -- I've named this remote "apt-rpm";
# * https://gitlab.com/apt-rpm/apt-rpm.git -- "apt-rpm@gitlab"
#   (and its clone on Github: https://github.com/arelixlinux/apt
#    -- "apt-rpm@github").
#
# "apt-rpm@gitlab" has a few more recent commits than "apt-rpm", a deeper
# history (into the past), and some better formatted commit headers (Author).
# (Compare like this: git range-diff apt-rpm/master...apt-rpm@gitlab/master)
#
# To graft it (the deeper "apt-rpm@gitlab" history) to ALT's history locally for yourself:
#
# git replace --graft 0.5.15lorg2-alt3 49dff175fb8ea3cd3ef47d45836f3089838246d6 0.5.15cnc6-alt18
#
# Then git blame on the source code gives more interesting information.
# If the two parents are in this order, git blame --first-parent -w shows more
# intersting individual commits from Conectiva's history, and not ALT's one.
# (Make sure that the grafted source code is identical to ours:
#
# git tag apt-rpm@gitlab/apt-0.5.15lorg2 49dff175fb8ea3cd3ef47d45836f3089838246d6
# git diff apt-rpm@gitlab/apt-0.5.15lorg2..0.5.15lorg2-alt3 --stat | fgrep -v ' => '
#
# The only reported difference is that they added a contributed script.)
#
# The upstream Debian repo:
# -------------------------
#
# https://salsa.debian.org/apt-team/apt.git -- "Debian"
#
# To attach it to Conectiva's history (locally for yourself):
#
# git tag apt-rpm@gitlab/MERGED-0.5.4.9 b780834d0d29cca5b0af1b544d3ff7b2a3d1a7a8
# git tag Debian/0.5.4.9-MERGED-into-apt-rpm 4968036c93552ff78c1f857a91c685f0f3bcb794
# git replace --graft apt-rpm@gitlab/MERGED-0.5.4.9 Debian/0.5.4.9-MERGED-into-apt-rpm apt-rpm@gitlab/MERGED-0.5.4.9^
#
# The parent with the richer history is 1st for git blame --first-parent -w.
#
# Grafting the most recent merge of Debian into apt-rpm:
#
# git replace --graft c5f4905b15ac022e6b18cf8acf59a4961210f3f9 725581a78ed5b222f7290321917199fb7fbc4c79 c5f4905b15ac022e6b18cf8acf59a4961210f3f9^
# git tag Debian/0.5.15 725581a78ed5b222f7290321917199fb7fbc4c79
# git tag apt-rpm@gitlab/MERGED-0.5.15 c5f4905b15ac022e6b18cf8acf59a4961210f3f9
#
# Enhanced apt-rpm history
# ------------------------
#
# I've enhanced the apt-rpm history (for future rebases and cherry-picks
# into ALT) and put it into the "next" remote (apt-rpm_next repo); branches:
#
# 0.5.15sisyphus0/apt-rpm -- brings the apt-repomd branch into the linear history;
# 0.5.15sisyphus1/apt-rpm -- fixes whitespace issues.
#
# It makes sense to graft it into our history (so that merges are hopefully
# simpler):
#
# git replace --graft 00dc7947063a474cafd29c6c1fb1185609eb0c6b 00dc7947063a474cafd29c6c1fb1185609eb0c6b^ next/0.5.15sisyphus1/fix-whitespace
#
Vcs: git://git.altlinux.org/gears/a/apt.git
Source0: %name-%version-%release.tar

Requires: libapt = %EVR
Requires: rpm >= 4.13.0.1-alt2, /etc/apt/pkgpriorities, apt-conf
Requires: librpmio(PGPHASHALGO_BLAKE2B)%{?_is_libsuff:(%{_libsuff}bit)} = 100
# We need (lib)rpm which finds pkgs by labels in N-E:V-R@T format:
Requires: RPMQ(EPOCH)
Requires: RPMQ(BUILDTIME)
Requires: RPMQ(DISTTAG)
# for methods.
Requires: gzip, bzip2, xz
Requires: gnupg, alt-gpgkeys

# Older versions of update-kernel misunderstood the @-postfix (with buildtime
# and disttag), which is now added by APT to verstrs and the names of
# allow-duplicated pkgs. (Epoch was also treated differently before, but that
# was not important until we added disttags, which are also separated by :.)
Conflicts: update-kernel < 0.9.14-alt1
# Older versions of apt-scripts-nvidia relied on a certain format of the APT ids
# of allow-duplicated packages, which changed (due to appending buildtime).
Conflicts: apt-scripts-nvidia < 0.5.0-alt1

# for apt-pipe.
BuildPreReq: setproctitle-devel

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

# should be same version in rpm.spec
BuildPreReq: liblua5.3-devel

BuildRequires: docbook-utils gcc-c++ libreadline-devel librpm-devel setproctitle-devel
BuildRequires: libgnutls-devel

%package -n libapt
Summary: APT's core libraries
Group: System/Libraries
# RPMTAG_AUTOINSTALLED is supported since 4.13.0.1-alt2.
Requires: librpm7 >= 4.13.0.1-alt2

%package -n libapt-devel
Summary: Development files and documentation for APT's core libs
Summary(ru_RU.UTF-8): Файлы и документация для разработчиков, использующих библиотеки APT
Group: Development/C
Requires: libapt = %EVR, librpm-devel >= 4.13.0.1-alt2

%package -n libapt-devel-static
Summary: Development static library for APT's libs
Summary(ru_RU.UTF-8): Статическая библиотека APT для разработчиков, использующих библиотеки APT
Group: Development/C
Requires: libapt-devel = %EVR, librpm-devel-static >= 4.13.0.1-alt2

%package rsync
Summary: rsync method support for APT
Summary(ru_RU.UTF-8): Поддержка метода rsync для APT
Group: Development/Other
Requires: %name = %EVR, rsync >= 2.5.5-alt3

%package https
Summary: https method support for APT
Summary(ru_RU.UTF-8): Поддержка метода https для APT
Group: Other
Requires: %name = %EVR

%package tests
Summary: Test suite for APT
Summary(ru_RU.UTF-8): Набор тестов для APT
Group: Other
BuildArch: noarch
Requires: %name = %EVR
Requires: rpm-build
Requires: /usr/bin/genbasedir
# optional
%global complete_reqs_of_tests %name-https /usr/sbin/nginx /usr/bin/openssl
%global reqs_of_tests_to_filter_out \\(%name-https\\|/usr/sbin/nginx\\|nginx\\|/usr/bin/openssl\\|openssl\\)
%filter_from_requires \,^%reqs_of_tests_to_filter_out\($\|[[:blank:]]\),d

# {{{ descriptions
%define risk_usage_en This package is still under development.

%description
A port of Debian's APT tools for RPM based distributions,
or at least for Conectiva. It provides the apt-get utility that
provides a simpler, safer way to install and upgrade packages.
APT features complete installation ordering, multiple source
capability and several other unique features.

%risk_usage_en

%define risk_usage Данный пакет пока еще находится в стадии разработки.

%description -l ru_RU.UTF-8
Перенесенные из Debian средства управления пакетами APT, включающие
в себя поддержку RPM, выполненную компанией Conectiva (Бразилия).
Этот пакет содержит утилиту apt-get для простой и надежной установки
и обновления пакетов. APT умеет автоматически разрешать зависимости
при установке, обеспечивает установку из нескольких источников и
целый ряд других уникальных возможностей.

%risk_usage

%description -n libapt
This package contains APT's package manipulation library,
modified for RPM.

%risk_usage_en

%description -n libapt-devel
This package contains the header files and libraries for developing with
APT's package manipulation library, modified for RPM.

%risk_usage_en

%description -n libapt-devel-static
This package contains static libraries for developing with APT's
package manipulation library, modified for RPM.

%risk_usage_en

%description rsync
This package contains method 'rsync' for APT.

%risk_usage_en

%description https
This package contains method 'https' for APT.

%risk_usage_en

%description tests
This package contains test suite for APT.

%description -n libapt -l ru_RU.UTF-8
В этом пакете находится библиотеки управления пакетами
из комплекта APT. В отличие от оригинальной версии для Debian, этот
пакет содержит поддержку для формата RPM.

%risk_usage

%description -n libapt-devel -l ru_RU.UTF-8
В этом пакете находятся заголовочные файлы и библиотеки для разработки
программ, использующих библиотеки управления пакетами
из комплекта APT. В отличие от оригинальной версии для Debian, этот
пакет содержит поддержку для формата RPM.

%risk_usage

%description -n libapt-devel-static -l ru_RU.UTF-8
В этом пакете находятся статические библиотеки для разработки программ,
использующих библиотеки управления пакетами из
комплекта APT. В отличие от оригинальной версии для Debian, этот пакет
содержит поддержку для формата RPM.

%risk_usage

%description rsync -l ru_RU.UTF-8
В этом пакете находится метод 'rsync' для APT

%risk_usage

%description https -l ru_RU.UTF-8
В этом пакете находится метод 'https' для APT

%risk_usage

%description tests -l ru_RU.UTF-8
В этом пакете находится набор тестов для APT.

# }}}

%prep
%setup -n %name-%version-%release

./verify-src.sh

# Fix url.
sed -i 's,/usr/share/common-licenses/GPL,/usr/share/license/GPL,' COPYING

# Unhide potential cc/c++ errors.
sed -i 's, > /dev/null 2>&1,,' buildlib/tools.m4

# Add trivial arch translation.
printf '%_target_cpu\t%_target_cpu' >> buildlib/archtable

%build
gettextize --force --quiet --no-changelog --symlink
%autoreconf

# std::optional support
# (We set a GNU dialect in -std= in order to minimally diverge
# from GCC's default, which is also -std=gnu++NN.)
%ifnarch %e2k
%add_optflags -std=gnu++17
%else
%remove_optflags -Wno-error
%add_optflags -std=gnu++14
find -type f -'(' -name '*.cc' -or -name '*.h' -')' -print0 \
| xargs -0 sed -i -re \
's,(std::)(optional|nullopt),\1experimental::\2,g;
 s,^(#[[:blank:]]*include[[:blank:]]*<)(optional>),\1experimental/\2,'
find -type f -'(' -name '*.cc' -or -name '*.h' -')' -print0 \
| xargs -0 sed -i -re \
's,(std::)(is_unsigned_v),\1experimental::\2,g;
 s,^(#[[:blank:]]*include[[:blank:]]*<)(type_traits>),\1experimental/\2,'
# [[fallthrough]] attribute is not yet known to lcc:
%add_optflags -Wno-error=attributes
%endif

%configure --includedir=%_includedir/apt-pkg --enable-Werror %{subst_enable static}
echo '#define APTRPM_ID "%name-%{?epoch:%epoch:}%version-%release%{?disttag::%disttag}.%_target_cpu"' \
	>> include/config.h

# Probably this obsolete now?
find -type f -print0 |
	xargs -r0 grep -EZl '/var(/lib)?/state/apt' -- |
	xargs -r0 %__subst -p 's,/var\(/lib\)\?/state/apt,%_localstatedir/%name,g' --
%make_build

%install
mkdir -p %buildroot%_sysconfdir/%name/{%name.conf,sources.list,vendors.list,preferences}.d
mkdir -p %buildroot%_libdir/%name/scripts
mkdir -p %buildroot%_localstatedir/%name/{lists/partial,prefetch}
mkdir -p %buildroot%_cachedir/%name/{archives/partial,gen{pkg,src}list}
mkdir -p %buildroot%_libdir/%name/tests

%makeinstall includedir=%buildroot%_includedir/apt-pkg

install -pm644 apt.conf %buildroot%_sysconfdir/%name/

# This is still needed.
ln -sf rsh %buildroot%_libdir/%name/methods/ssh
ln -sf gzip %buildroot%_libdir/%name/methods/bzip2
ln -sf gzip %buildroot%_libdir/%name/methods/xz

# Cleanup
rm %buildroot%_libdir/*.la

bzip2 -9fk ChangeLog-rpm.old

find %buildroot%_includedir -type f -name '*.h' |while read f; do
	cat >>"$f" <<EOF

#include <stdint.h>
#if __WORDSIZE == 32 && !defined(__USE_FILE_OFFSET64)
# error "<${f#%buildroot%_includedir/}> cannot be used without -D_FILE_OFFSET_BITS=64"
#endif
EOF
done

mkdir -p %buildroot%_datadir/%name
cp -r test/integration -T %buildroot%_datadir/%name/tests

install -m0755 run-tests-dir -t %buildroot%_datadir/%name/
cp -r tests-under-pkdirect -t %buildroot%_datadir/%name/

%find_lang %name

unset RPM_PYTHON

%package basic-checkinstall
Summary: Immediately test %name when installing this package (only basic tests)
Group: Other
BuildArch: noarch
Requires(pre): %name-tests

%description basic-checkinstall
Immediately test %name when installing this package.

The set of testcases is limited (just to the file method).

%files basic-checkinstall

%pre basic-checkinstall -p %_sbindir/sh-safely
set -o pipefail

# Check that %name-tests has no unwanted extra reqs:
found_unwanted_reqs_of_tests="$(rpm -q %name-tests -R |
				    { grep -e '%{reqs_of_tests_to_filter_out}' ||
				      [ $? -eq 1 ]; })"
if [ -n "$found_unwanted_reqs_of_tests" ]; then
    printf >&2 'These are unwanted extra reqs of %name-tests:\n%%s\n' \
	       "$found_unwanted_reqs_of_tests"
    exit 1
fi

pushd %_datadir/%name/tests/

# force the target arch for the tests
#
# By default, the packages would be built for the arch detected by rpm-build
# (rpmbuild --eval %%_arch). On installation, they would be compared
# by rpm for compatibility with the arch detected by rpm. Currently,
# the mismatch in the detection between rpm and rpm-build can lead to problems,
# at least, on armh. So, we set the target by force to a value that must work.
system_arch="$(rpm -q rpm --qf='%%{ARCH}')"
export APT_TEST_TARGET="$system_arch"

# this macro can be prefixed (e.g., by environment assignments),
# therefore the extra backslash in the first line
%global runtests \\\
		./run-tests -v

# A quick test with just one method for the case without APT_TEST_GPGPUBKEY.
APT_TEST_METHODS='file' %runtests

# The same tests, but just via cdrom with a missing release:
#APT_TEST_METHODS=cdrom_missing_release %%runtests

%package checkinstall
Summary: Immediately test %name when installing this package (complete set of tests)
Group: Other
BuildArch: noarch
Requires(pre): %name-tests
Requires(pre): %complete_reqs_of_tests
Requires(pre): gpg-keygen

%description checkinstall
Immediately test %name when installing this package.

The set of testcases is complete (all the methods that are tested by default
and some additional peculiarities are tested).

%files checkinstall

%pre checkinstall -p %_sbindir/sh-safely
set -o pipefail
pushd %_datadir/%name/tests/

# force the target arch for the tests
#
# By default, the packages would be built for the arch detected by rpm-build
# (rpmbuild --eval %%_arch). On installation, they would be compared
# by rpm for compatibility with the arch detected by rpm. Currently,
# the mismatch in the detection between rpm and rpm-build can lead to problems,
# at least, on armh. So, we set the target by force to a value that must work.
system_arch="$(rpm -q rpm --qf='%%{ARCH}')"
export APT_TEST_TARGET="$system_arch"

# prepare data for rpm --import
APT_TEST_GPGPUBKEY="$PWD"/example-pubkey.asc
gpg-keygen --passphrase '' \
	--name-real 'Some One' --name-email someone@example.com \
	/dev/null "$APT_TEST_GPGPUBKEY"

export APT_TEST_GPGPUBKEY

%runtests

# Everything has been tested by now.

%package xxtra-heavy-load-checkinstall
Summary: Immediately test %name when installing this package (many times under heavy load)
Group: Other
BuildArch: noarch
Requires(pre): %name-tests
Requires(pre): %complete_reqs_of_tests
Requires(pre): gpg-keygen

%description xxtra-heavy-load-checkinstall
Immediately test %name when installing this package.

The tests are run many times and under simulated heavy load (namely,
in parallel) in order to possibly detect races
(to make sure no tests are randomly succeeding).

%files xxtra-heavy-load-checkinstall

%pre xxtra-heavy-load-checkinstall -p %_sbindir/sh-safely
set -o pipefail
pushd %_datadir/%name/tests/

# force the target arch for the tests
#
# By default, the packages would be built for the arch detected by rpm-build
# (rpmbuild --eval %%_arch). On installation, they would be compared
# by rpm for compatibility with the arch detected by rpm. Currently,
# the mismatch in the detection between rpm and rpm-build can lead to problems,
# at least, on armh. So, we set the target by force to a value that must work.
system_arch="$(rpm -q rpm --qf='%%{ARCH}')"
export APT_TEST_TARGET="$system_arch"

# prepare data for rpm --import
APT_TEST_GPGPUBKEY="$PWD"/example-pubkey.asc
gpg-keygen --passphrase '' \
	--name-real 'Some One' --name-email someone@example.com \
	/dev/null "$APT_TEST_GPGPUBKEY"

export APT_TEST_GPGPUBKEY

# Below we run the same tests many times in order to possibly catch
# bad races. (It's more probable to catch a race under heavy load;
# therefore, of the total specified number of tries, we do
# simultaneously as many as reasonable and possibly even more than TRIES.)

# To not run in parallel, build the pkg with --define 'nprocs_for_check %%nil'
# Consider multiplying `nproc` by 2 for heavier load.
NPROCS=`nproc`
if ! [ "$NPROCS" -gt 0 ] 2>/dev/null; then
	NPROCS=1
fi
%{?nprocs_for_check:NPROCS=%nprocs_for_check}
TRIES=2
if [ $TRIES -lt ${NPROCS:-0} ]; then
	TRIES=$NPROCS
fi

already_once=0
for (( try = 0; try < TRIES; )); do
    # all methods (you might want to update the list if there are new ones)
    for method in file cdrom http https; do
	# do the same method several times in parallel (to provoke races)
	for (( repeat = 0; repeat < 2; ++repeat )); do
	    echo "$((try++)):$method"
	    if (( already_once && (try >= TRIES) )); then
		break 2
	    fi
	done
    done
    already_once=1
done |
    xargs -d'\n' -I'{}' ${NPROCS:+-P$NPROCS --process-slot-var=PARALLEL_SLOT} \
	  -- sh -efuo pipefail \
	  -c 'APT_TEST_METHODS={}
              APT_TEST_METHODS="${APT_TEST_METHODS#*:}"
              export APT_TEST_METHODS
              %runtests '${NPROCS:+'|& sed --unbuffered -e "s/^/[$PARALLEL_SLOT {}] /"'}

%package under-pkdirect-checkinstall
Summary: Immediately test %name+PK when installing this package (via packagekit-direct)
Group: Other
BuildArch: noarch
Requires(pre): packagekit

%description under-pkdirect-checkinstall
Immediately test PackageKit (which is supposed to use %name as the backend)
when installing this package.

The testing is done via %_libexecdir/packagekit-direct (which works
without relying on any daemons, DBus, etc.)

Some of the bugs (from the past) which are being tested for by these
tests could only be seen with APT indices that were big and/or
acquired from "external" sources (like the real Sisyphus repo). So,
having just the "internal" system RPM db diminishes the potential
of these few tests to find interesting bugs. One should set up
"external" sources for APT (in a real system or in hasher with network).

%files under-pkdirect-checkinstall
%dir %_datadir/%name
%_datadir/%name/run-tests-dir
%_datadir/%name/tests-under-pkdirect

%post under-pkdirect-checkinstall
# so that the two outputs are not out of sync
exec 1>&2

%_datadir/%name/run-tests-dir %_datadir/%name/tests-under-pkdirect

# * * *
#
# Note that git-bisect(1) expects an "exit with a code between 1 and
# 127 (inclusive), except 125, if the current source code is bad".
# Therefore, I suggest to use this test script (or the wrapper
# ./test-pk-in-hsh.sh) like this:
#
#   cd apt
#   git bisect start --no-checkout PK-BAD PK-GOOD
#   git bisect run /bin/sh -exc './gear-build-pair-in-hsh.sh . BISECT_HEAD ../packagekit/ revert-apt-API ~/hasher/; hsh-install ~/hasher/ apt-under-pkdirect-checkinstall || { echo BAD: $?; exit 1; }'


%files -f %name.lang
%_bindir/apt-*
%_libexecdir/apt
%_libdir/%name
%exclude %_libdir/%name/methods/rsync
%exclude %_libdir/%name/methods/https
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%dir %_sysconfdir/%name/*.d
%_mandir/man?/*
%doc README* TODO COPYING AUTHORS* ChangeLog-rpm.old.bz2 doc/examples contrib

%defattr(2770,root,rpm,2770)
%_cachedir/%name/archives

%files -n libapt
%_libdir/*.so.*
%_localstatedir/%name

%defattr(2770,root,rpm,2770)
%dir %_cachedir/%name

%files -n libapt-devel
%_libdir/*.so
%_includedir/*

%if_enabled static
%files -n libapt-devel-static
%_libdir/*.a
%endif

%files rsync
%dir %_libdir/%name
%dir %_libdir/%name/methods
%_libdir/%name/methods/rsync
# Probably %%doc with README.rsync?

%files https
%dir %_libdir/%name
%dir %_libdir/%name/methods
%_libdir/%name/methods/https

%files tests
%dir %_datadir/%name
%_datadir/%name/tests/

%changelog
* Tue May 21 2024 Ivan A. Melnikov <iv@altlinux.org> 0.5.15lorg2-alt88
- Backport columnar output for apt-get from Debian.

* Fri Mar 15 2024 Andrey Cherepanov <cas@altlinux.org> 0.5.15lorg2-alt87
- Ignore check reason-phrase element in HTTP header (ALT #49694).

* Mon Jul 24 2023 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt86
- To make future API changes easier, extended a class so that it is suitable
  for aptitude and to untie aptitude and libapt. (Aptitude depended on its
  details, because it reimplemented it.) (Picked from Debian apt 0.6.42.4.)
- Dropped a compat API, which could have still been relied on by libapt clients
  not aware of the support (since 0.5.15lorg2-alt73) for multiple hash types.

* Wed Jul 05 2023 Andrey Limachko <liannnix@altlinux.org> 0.5.15lorg2-alt85
- Added loongarch64 to archtable (thx Alexey Sheplyakov)

* Fri Jun 02 2023 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt84
- Fixed the display of descriptions in aptitude and packagekit (by making
  the format closer to Debian's):
  + Fixed the display of the first line, which was not shown in packagekit.
  + Fixed the regression (from 0.5.15lorg2-alt72) in the display of
    all but the first lines (in aptitude and packagekit). (ALT#40826)
  + This has also made packagekit show translated descriptions. (ALT#46251)
  + As a result, there is a cosmetic regression in synaptic: extra blanks.
- Increased the buf for reading to 32k for effectiveness in methods:
  gzip (and other compression types), rsh, ftp.
- Avoid compilation errors with GCC 13 (thx Alexey Sheplyakov). (ALT#46105)

* Tue Feb 21 2023 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt83
- Made a bit nicer and more informative the new Debug::pkgMarkInstall messages,
  which were introduced in 0.5.15lorg2-alt81; renamed and mentioned there
  the new options: Debug::pkgMark-shallow, Debug::pkgMark-allcalls.
- Worked around the problem with printing long messages by making the buffer
  1200 bytes large. (ALT#44941)
- Avoid installing extra packages in some cases when this is really not needed
  to satisfy a request. (Correct cleanup in pkgProblemResolver::DoUpgrade.)

* Fri Sep 02 2022 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt82
- tests:
  + Enhanced to be able to work with test packages containing some files.
    (This will be useful for testing the work with large RPM archives.)
  + Shortened the run time of apt-xxtra-heavy-load-checkinstall.
  + Shortened the run time of other *-checkinstall scripts
    (by shortening the the test with zillion packages).

* Wed Aug 03 2022 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt81
- Fixed bad behavior when satisfying "Conflicts" or "Obsoletes" dependencies
  (discovered in ALT#42415), namely:
  + "Obsoletes" causing the deletion of its "virtual" targets (i.e.,
    providing packages) whereas this behavior is expected for Conflicts only;
  + versioned "Conflicts" (or "Obsoletes") causing the deletion of packages
    with non-matching version.
- Enriched the output of Debug::pkgMarkInstall with the versions of
  the dependency targets and the targets being considered during the search.
- Complemented it with new options (Debug::pkgMarkAllCalls,
  Debug::pkgMarkShallow) -- to understand better why the result of
  resolving a broken dep is unexpected in some cases.

* Thu Jun 02 2022 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt80
- Fixed the new compilation warnings by simplifying the ALT-specific code
  in pkgcache.cc (AllTargets) from 0.5.15lorg2-alt31. (Discovered by gcc12.)

* Mon Apr 18 2022 Vitaly Chikunov <vt@altlinux.org> 0.5.15lorg2-alt79
- wrapper: Undo sub-reaper and provide post-update hook instead.

* Sat Mar 26 2022 Vitaly Chikunov <vt@altlinux.org> 0.5.15lorg2-alt78
- Fix apt-get wrapper under non-systemd systems by turning reaping off.

* Tue Mar 22 2022 Vitaly Chikunov <vt@altlinux.org> 0.5.15lorg2-alt77
- Add wrapper to apt-shell too (closes: #42201).

* Sun Mar 13 2022 Vitaly Chikunov <vt@altlinux.org> 0.5.15lorg2-alt76
- Add apt-get guarding wrapper that will prevent apt-get from exiting before
  all tasks are finished.

* Sat Jan 27 2022 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt75
- Invalidate the in-memory cache of repositories when doing "update" or
  ListUpdate() to be able to detect updates without exiting the process,
  e.g., PackageKit or apt-shell (ALT#41816).
- Added apt-under-pkdirect-checkinstall subpackage
  and added a test for FileList() API via packagekit.

* Sat Dec 04 2021 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt74
- Implemented generic callback system for packagekit, allowing to show progress
  during offline-update to user. (Thx Oleg Solovyov mcpain@)

* Fri Oct 29 2021 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt73
- (tests) Report if a test (marked XFAIL) uneXpectedly passes (XPASS).
- (tests) Run them not in %%check, but in *-checkinstall subpkgs. (To break
  build-dep cycle with apt-repo-tools, whose features are required by the tests,
  but which needs to be recompiled to be linked with libapt.)
- (tests) Done more extensive testing of how apt works with "rpm" repos
  via any of the file, http(s), cdrom methods; including:
  + re-fetching if the saved complete or partial pkglist indices are corrupt
    (see https://bugzilla.altlinux.org/show_bug.cgi?id=40746#c9 );
  + the verification of the checksums of pkglist indices. (The verification
    is tested in two ways:
    * The verification of the checksum of a specific type is tested by faking
      it in the meta-data: for MD5, SHA1, SHA256, BLAKE2b and just the size.
    * Simply testing that a faked pkglist file of the same size is rejected--no
      matter which hashing algorithm is used.)
  + the verification of the checksums of rpm archives. (The verification
    is tested in two ways:
    * The verification of the checksum of a specific type is tested by faking
      it in the meta-data: for MD5, SHA1, SHA256, BLAKE2b.
    * Simply testing that a faked rpm file of the same size is rejected--no
      matter which hashing algorithm is used.)
- (source code; ABI) Reverted a lot of inessential optimizations
  from 0.5.15lorg2-alt72.
- (source code; ABI) Got rid of virtual methods with default parameters
  (because they are confusing for the programmer).
- (source code; ABI) Backported some pieces of the support for the multiplicity
  of checksum (and compression) types from apt-rpm (thx imz@):
  + the type of the compression for "pkglist" indices;
  + the type of the checksum for "pkglist" indices;
  + the type of the checksum for "rpm" archives.
- Added blake2b hash support (thx glebfm@).
- Changed file and copy download methods to always compute checksums
  (thx glebfm@).

* Thu Mar 18 2021 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt72
- Cleaned up the code (thx Dmitry V. Levin ldv@; including
  quite a few commits cherry-picked from http://apt-rpm.org/scm/apt.git):
  + to avoid compilation warnings altogether and some unreliable code;
  + to avoid using any old deprecated RPM API.
- Reverted (for a while) new features with unreliable implementation introduced
  in 0.5.15lorg2-alt70 (dynamic resizing of allocated memory; some support
  for large files). Updated how the other changes look in the history
  (thx darktemplar@). (The soname has been bumped again.)
- API changes:
  + Reverted inessential optimizations that caused incompatibilities with
    the Debian API (introduced in 0.5.15lorg2-alt70).
  + Made pkgCacheFile class lazy and immutable so that it better suits
    the expectations of modern libapt clients such as PackageKit
    and so that it is less prone to memory leaks and other programming errors.
  + And changed some other things (how functions return results) to avoid
    programming errors (which lead to the NULL dereference bugs listed below).
- Fixed some recently introduced and recently discovered bugs:
  + APT now can handle packages without ARCH tag (such as gpg-pubkey, brought
    by 3rd-party packages) without a crash (thx darktemplar@ et al)
    (ALT#38381, ALT#38642).
  + Some crashes with incomplete indices (after the old apt-cdrom or for
    incompatible arch).
- Increased the default APT::Cache-Limit (up to 192M)
  to make the "out of space" failure less probable for packagekit.

* Mon Sep 21 2020 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt71.3
- Fixed copying release information from cdrom (thx Aleksei Nikiforov).
  (Closes: #37531)

* Mon Jul 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.15lorg2-alt71
- Introduced new function ListUpdate for improved packagekit support.
  (Note that the APT::Get::Archive-Cleanup configuration option has no longer
  any effect after this change. It was off by default.)

* Mon Jul 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.15lorg2-alt70
- Ported dynamic memory allocation from Debian.
- Bumped soname due to ABI changes.

* Wed Jul 17 2019 Andrew Savchenko <bircoph@altlinux.org> 0.5.15lorg2-alt69
- Add E2K arch support.

* Thu Jul  4 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt68.1
- Made the treatment of the File Provides and the version ID of
  installed packages "stable": not affected negatively by sources.list.
  Also negative effects of different pkglists from sources.list on each other
  have been mitigated. (A pkglist from sources.list that lacked disttags could
  shadow the File Provides of packages from the database or other pkglists.)

* Wed Jun 05 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt68
- Add disttag to VerStrs (used by APT to identify package versions).

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.15lorg2-alt67
- Print error and disable 'upgrade' by default.
  Using 'dist-upgrade' instead of 'upgrade' is advised.
  Allow enabling 'upgrade' via '--enable-upgrade' option or
  via 'APT::Get::EnableUpgrade' configuration setting (Closes: #30867).

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.15lorg2-alt66
- Fortified https method (Closes: #33732)
- Dropped processing Realm name in http/https methods (Closes: #33236)

* Thu May 30 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt65
- Add buildtime to VerStrs (used by APT to identify package versions).
  This data is used in several manners:
  * by CheckDep() (only when matching a dependency with a real package);
  * rpm_name_conversion() (only when making up an id for a duplicated package);
  * and by *CmpVersion().
  The latter needs buildtime to determine the correct upgrade direction and
  can be called through the API with some externally supplied versions.
  In order to honor buildtime without changing the API and its clients, we pass
  buildtime inside the existing argument. (Also fixes ALT#36528)
- Increase default APT::Cache-Limit in 1.5 times due to the extension of VerStrs
  (ALT#36775).

* Fri May 17 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.15lorg2-alt64
- Ported https support from Debian via https method to apt-https package (Closes: #33732).

* Sat May 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt63
- archtable:
  + added ppc64le;
  + added trivial arch translation (%%_target_cpu -> %%_target_cpu).

* Fri Mar 29 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.15lorg2-alt62
- Implemented --autoremove option for apt-get and apt-shell (Closes: #36322).
- Fixed autoremove in apt-shell to properly process packages with pending removal.

* Fri Dec 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.15lorg2-alt61
- Fixed marking packages with transformed names as autoinstalled.

* Wed Dec 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.15lorg2-alt60
- Fixed releasing rpmdb if it was locked read-only.
- Implemented new interface for querying packages pending to autoremoval.

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.15lorg2-alt59
- Fixed crash on fail to read package file.
- Implemented following actions and commands (closes: #34036):
  "apt-get autoremove", "apt-mark showmanual [package1 ...]", "apt-mark showauto [package1 ...]",
  "apt-mark manual package1 [package2 ...]", "apt-mark auto package1 [package2 ...]",
  "apt-mark showstate [package1 ...]".

* Fri Dec 15 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt58
- cherry-picked from Debian 0.7.22 (git://anonscm.debian.org/git/apt/apt.git)
  some fixes for http download method (ALT: 18925)
  * Fix pipeline handling on http.cc
  (closes: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=413324)
  (thx Otavio Salvador).
  * show error details of failed methods
  * if a process aborts with signal, show signal number
  * in http method: ignore SIGPIPE, we deal with EPIPE elsewhere
  (closes: https://bugs.launchpad.net/ubuntu/+source/apt/+bug/385144)
  (thx Michael Vogt).

* Mon Jul 03 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt57
- Fixed script_slot variable (vseleznv@; ALT#32941).
- Used recently restored librpm rpmRangesOverlap, and
  rpmCheckRpmlibProvides functions.

* Wed Dec 21 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt56
- Added support of lua 5.3.
- Rebuilt with liblua5.3.

* Fri Dec 16 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt55
- Optimized all rpmds operations.

* Mon Nov 21 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt54
- Fixed build with rpm-4.13 (legion@).
- Disabled fancypercents by default.
- Backported fix for logic about package sizes.
- Fixed support of librpm promoteepoch option.
- Bumped soversion.

* Fri Nov 27 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.5.15lorg2-alt53
- doc/: Add a note about APT_CONFIG in the -c description
  (Closes: Debian #578267) (thx David Kalnischkies).

* Fri May 29 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt52
- Fixed apt usage with redefined rpm binary name.

* Thu May 28 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt51
- Bumped soversion.
- Rebuilt for C++11 ABI.

* Tue Mar 31 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt50
- Increased default APT::Cache-Limit:
 + up to 96M on 64bit systems.
 + up to 80M on 32bit systems.

* Fri Nov 28 2014 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt49
- Reintroduced '%%set_verify_elf_method strict'.

* Tue Nov 25 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt48
- Added buildtime to downloaded package name.

* Fri Sep 12 2014 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt47
- Added apt's package NEVRA string to OptionsHash.

* Wed Sep 10 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt46.1
- Bumped soversion.
- Added aarch64 to archtable.

* Fri Jul 04 2014 Gleb Fotengauer-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt46
- apt-pkg/policy.cc: it is ok, if default PinDir doesn't exist
  (reported by rider@).

* Tue Jul 01 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt45.1
- Rebuilt with rpm-4.0.4-alt100.78 (different size of rpmTagTable).

* Tue Jun 24 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.15lorg2-alt45
- Honor buildtime.
- Added support of preferences.d dir.
- apt-pkg/algorithms.cc: mark all installed packages first without auto
  installation in a dist-upgrade (probably fixes
  http://lists.altlinux.org/pipermail/devel/2009-May/171113.html ).

* Tue Mar 11 2014 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt44
- libapt: enlarged integer types in pkgCache::Version (closes: #29514).

* Fri Feb 28 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5.15lorg2-alt43
- use apt-cdrom for general distribution media
- stricted verify-elf removed

* Thu Jan 10 2013 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt42
- Fixed and enabled LFS support (closes: #28214).

* Thu May 24 2012 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt41
- apt-get, apt-shell: when a package could not be found, print the
  unmangled package request string (by Igor Vlasenko; closes: #27364).
- apt-shell: do not abort when commit is cancelled (closes: #13877);
  Unlike one may suppose, this change will not cause the cache of
  accumulated changes to be cleared by cancelled "commit" operation, but
  this is exactly what Vitaly Lipatov has proposed in his comments to #13877.

* Wed May 16 2012 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt40
- Increased default APT::Cache-Limit on x86_64 up to 64M.

* Fri Oct 07 2011 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt39
- Fixed build with rpm >= rpm-4.0.4-alt100.36.

* Sun Feb 13 2011 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt38
- Enhanced ReInstall error diagnostics (closes: #24044).

* Thu Jan 27 2011 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt37
- pkgcache.h: optimized FindPackage() stuff
- depcache.cc: fixed -alt36 optimization

* Tue Jan 25 2011 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt36
- depcache.cc: optimize CheckDep() calls for Now/Install/Candidate versions

* Tue Nov 23 2010 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt35
- Fixed RPATH in apt utilities.
- Applied strict ELF verification rules in this package.

* Thu Nov 04 2010 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt34
- Increased default APT::Cache-Limit up to 48M.

* Wed Aug 18 2010 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt33
- rpmpm.c: fixed rpmdepCheck() call

* Thu May 27 2010 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt32
- acquire-item.cc: added support for xz-compressed pkglists

* Mon Dec 21 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.15lorg2-alt31.1
- NMU:
  + RecordParser::Changelog(), SrcRecordParser::Changelog(): access to
    raw changelog data

* Thu Dec 17 2009 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt31
- rpmversion.cc (CheckDep): optimize out rpmRangesOverlap() call
- pkgcache.cc (AllTargets): optimize out CheckDep() calls
- luaiface.cc: added "savestate" and "restorestate"

* Fri Nov 20 2009 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt30
- added support for changelogs in "apt-cache show"

* Sun Sep 27 2009 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt29
- apt-utils no longer packaged, replaced with apt-repo-tools

* Mon Aug 03 2009 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt28
- apt-cache.cc: fixed "whatdepends" for versioned virtual dependencies

* Mon Jul 13 2009 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt27
- depcache.cc: fixed for gcc-4.4
- buildlib/tools.m4: hackaround glibc soname change
- apt-cache.cc: added APT::Cache::DumpPackages option

* Tue Mar 31 2009 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt26
- rpmpm.cc: try hard to fix package removal

* Thu Mar 26 2009 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt25
- rpmpm.cc: fixed removal of i586-*.32bit packages (Panu Matilainen)

* Tue Mar 24 2009 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt24
- depcache.cc (MarkInstall): mark unambiguous dependencies first

* Mon Jan 19 2009 Stanislav Ievlev <inger@altlinux.org> 0.5.15lorg2-alt23
- open rpm database with O_CREAT flag

* Fri Jan 09 2009 Slava Semushin <php-coder@altlinux.ru> 0.5.15lorg2-alt22.2
- apt-shell: print newline symbol during quit by Ctrl+D
  (Based on feedback for bug #18343 from Ivan A. Melnikov aka iv@)

* Wed Dec 31 2008 Slava Semushin <php-coder@altlinux.ru> 0.5.15lorg2-alt22.1
- apt-shell: show up "list" command by completion (#5953)
- apt-shell: quit from shell by Ctrl+D (#6264, #18343)
- apt-shell: describe -G and -g options in "help list" output (#18256)

* Fri Dec 12 2008 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt22
- Fixed build with g++-4.3.x (Stanislav Ievlev).

* Fri Aug 29 2008 Alexander Myltsev <avm@altlinux.ru> 0.5.15lorg2-alt21
- fix by led@: change type of Package.ID to int (fixes #16900)
- fixes by raorn@:
 - apt-get.cc: protect VerTag (fixes #16311)
 - apt-get.cc: fix memory corruption (fixes #14929)
 - fileutl.cc: change semantics of flExtension() (fixes #15909)

* Sun May 11 2008 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt20
- genpkglist.cc: RPMTAG_FILEFLAGS should not be copied into header list
- lorg-cache-limit.patch: increase cache size limit
- removed old triggers, updated dependencies

* Sun Mar 30 2008 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt19
- lorg-pkgcachegen-selfprov.patch: allow self-referencing provides,
  so that e.g. ocaml-runtime#3.10.2-alt2 can provide ocaml-runtime = 3.10

* Mon Dec 17 2007 Alex V. Myltsev <avm@altlinux.ru> 0.5.15lorg2-alt18
- algorithms.cc: number-aware package name comparison
  (now automake_1.10 > automake_1.9)

* Mon Dec 03 2007 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt17
- genpkglist.cc: rewrite copyStrippedFileList() to avoid inplace
  dirnames edit bug

* Fri Nov 23 2007 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt16
- genpkglist: removed very bad piece of code which could break
  my fine-grained file list stripping algorithm
- genbasedir: made silent by default, added --verbose and --silent
  options (Alex V. Myltsev)

* Tue Oct 30 2007 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt15
- apt-get: Fixed manifest file support (Stanislav Ievlev).

* Wed Oct 24 2007 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt14
- genpkglist: don't strip paths that are owned by 2 or more packages,
  to deal with cross-arch semi-unmets like /usr/share/wallpapers
- apt-get: added support of manifest file (Stanislav Ievlev)

* Sat Aug 11 2007 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt13
- Updated file list stripping algorithm in genpkglist (apt-utils);
  now it keeps files which can resolve file-level dependencies.

* Wed Aug 01 2007 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt12
- Fixed apt-get exit status (#11527)

* Tue Jul 31 2007 Slava Semushin <php-coder@altlinux.ru> 0.5.15lorg2-alt11.1
- Fixed typo in output of help command in apt-shell (#5400)
- Fixed wrong message during remove package(s) in apt-shell (#7618)

* Mon Apr 09 2007 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt11
- Updated 'apt-get install' algorithm for versioned dependencies:
  + fixed wrong usage of ScoreSort condition introduced in previous release;
  + added explicit check if any package satisfying versioned dependency is
    already installed or selected for install; in this case, apt-get will
    not try to install any other package.

* Fri Mar 23 2007 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt10
- Added bzip2 and gzip requirements (#10408).

* Thu Mar 22 2007 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt9
- Updated my previous patch for versioned dependencies, which was half-way
  wrong and incomplete.  For versioned virtual dependencies like python=2.4,
  'apt-get install' will always select real package with the best version
  (which is python-strict#2.4.4-alt8, as for now)

* Sun Dec 31 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt8
- Fixed longstanding problem with versioned virtual packages (Alexey Tourbin),
  see http://lists.altlinux.org/pipermail/devel/2006-December/039317.html

* Thu Nov 30 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt7
- apt-get: More simple-output enhancements (Stanislav Ievlev).

* Tue Oct 10 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt6
- apt-get: Fixed virtual packages handling (Alexey Tourbin).
- apt-get: Implemented simple-output option (Stanislav Ievlev).

* Thu Oct 05 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt5
- pkgCache::PrvIterator:
  + Add default constructor, required for aptitude 0.4.1 (Raorn, #9604).
- rpmRecordParser::BufCat, rpmSrcRecordParser::BufCat:
  + Fix realloc usage (#9409).

* Tue May 16 2006 Alexey Tourbin <at@altlinux.ru> 0.5.15lorg2-alt4
- Patched and rebuilt for lua-5.1.

* Sat Apr 01 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.15lorg2-alt3
- Resolved a few issues introduced after cnc6.

* Wed Mar 29 2006 Anton Farygin <rider@altlinux.ru> 0.5.15lorg2-alt2
- apt-shell: use string for MatchSection.

* Tue Mar 21 2006 Anton Farygin <rider@altlinux.ru> 0.5.15lorg2-alt1
- Updated to 0.5.15lorg2.

* Tue Feb 21 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc6-alt18
- apt-get: Fixed APT::Get::PrintLocalFile for local files (#8902).

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.15cnc6-alt17.1
- Rebuilt with libreadline.so.5.

* Fri Nov 25 2005 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc6-alt17
- apt-utils: Set locale to "C" (#2587).
- apt-utils: Added list of utilities to package description (#3564).
- apt-get: Implemented APT::Get::PrintLocalFile option.

* Fri Jul 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.15cnc6-alt16
- apt-shell: -q option for update added

* Fri Jul 08 2005 Kachalov Anton <mouse@altlinux.ru> 0.5.15cnc6-alt15
- apt-pkg/sourcelist.cc:
  Added support for multiple fingerprints for the same vendor name

* Mon Jun 27 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.15cnc6-alt14
- apt-shell: #5401 fixed (rider@)
- apt-pipe: race during shutting down fixed

* Thu Jun 16 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.15cnc6-alt13
- apt-shell: possible fix of #4707 (rider@)

* Tue May 31 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.15cnc6-alt12
- apt-pipe: inactivity timeout removed
- apt-pipe: do not copy packages from cdrom during install

* Wed May 18 2005 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc6-alt11
- apt-get: corrected virtual package remove algorithm (#6276).
- Updated default cdrom mount point (#6152).

* Tue May 17 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.15cnc6-alt10
- Changed command line parsing order (zerg@, fixes #6815)
- apt-shell: ls -G improvements (rider@)

* Wed May  4 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.15cnc6-alt9
- apt-shell: ls -G redo (rider@)

* Thu Apr 28 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.15cnc6-alt8
- belarusian translation updated
- apt-shell: ls -g/-G implemented (rider@)
- apt-pipe minor cleanups

* Mon Apr 11 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.15cnc6-alt7
- Acquire::CDROM::mount value in apt.conf(5) changed from /mnt/cdrom to /media/cdrom
- apt-pipe utility added

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.15cnc6-alt6.1
- Rebuilt with libstdc++.so.6.

* Tue Aug 31 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc6-alt6
- %_localstatedir/%name: relocated to libapt subpackage (#4697).
- UnmountCdrom(): silently ignore subfs and supermount filesystems (#4806).

* Mon Jul 05 2004 Kachalov Anton <mouse@altlinux.ru> 0.5.15cnc6-alt5
- apt-shell fixes (#3091)

* Mon Jun 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc6-alt4
- apt-shell fixes from Mouse (#4306).

* Sat May 15 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc6-alt3
- apt-pkg/pkgcachegen.cc:
  Remove old sources cache file before creating new one.
- More fixes reported by compiler, patch by Anton V. Denisov.

* Fri May 14 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc6-alt2
- Fixed aclocal warnings, patch by Anton V. Denisov.
- Updated russian translation from Anton Denisov.

* Thu May 13 2004 Kachalov Anton <mouse@altlinux.ru> 0.5.15cnc6-alt1
- Updated to 0.5.15cnc6.
- New:
  + apt-0.5.15cnc6-alt-rpm-order (fix RPM::Order default value)
- Updated:
  + apt-0.5.15cnc6-alt-fixes
  + apt-0.5.15cnc6-alt-defaults
  + apt-0.5.15cnc6-alt-rpm-fancypercent
  + apt-0.5.15cnc6-alt-virtual_scores
- Merged upstream:
  + apt-0.5.15cnc6-alt-install_virtual

* Fri Feb 27 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc5-alt4
- Fixed build with fresh autotools.

* Wed Jan 21 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc5-alt3
- Readded contrib to documentation.
- Updated russian translation from Anton Denisov.

* Mon Jan 19 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc5-alt2
- Added one more %%triggerun to correct apt.conf,
  due to apt methods migration.
- Applied patch from Alexey Tourbin to use systemwide lua5.
- Applied patch from Sviatoslav Sviridov to workaround VendorList bug.

* Fri Jan 16 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc5-alt1
- Specfile cleanup.
- Rediffed patches.
- Fixed --help/--version segfault.
- Fixed some compilation warnings.
- Relocated methods to %_libdir/%name/methods/.

* Thu Jan 15 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.15cnc5-alt0.3
- Updated:
  + apt-0.5.15cnc5-alt-rpm
  + apt-0.5.15cnc5-alt-rpm-fancypercent

* Tue Jan 13 2004 Anton Kachalov <mouse@altlinux.ru> 0.5.15cnc5-alt0.2
- Updated and applied:
  + apt-0.5.15cnc5-alt-install_virtual
  + apt-0.5.15cnc5-alt-virtual_scores
- Removed:
  + apt-0.5.4cnc9-alt-install_virtual_version (merged upstream).

* Fri Dec 26 2003 Anton V. Denisov <avd@altlinux.org> 0.5.15cnc5-alt0.1
- Updated to 0.5.15cnc4.
- Updated alt-rpm.patch.

* Tue Dec 09 2003 Anton V. Denisov <avd@altlinux.org> 0.5.15cnc4-alt0.2
- Updated and applied alt-getsrc.patch.
- Following patches still stay unapplied:
  + alt-install_virtual.patch
  + alt-install_virtual_version.patch
  + alt-virtual_scores.patch

* Mon Dec 08 2003 Anton V. Denisov <avd@altlinux.org> 0.5.15cnc4-alt0.1
- Updated to 0.5.15cnc4.
- Updated alt-distro.patch.
- Updated russian translation.
- Get rid of %_libdir/*.la files.
- Still have disabled patches.

* Tue Nov 25 2003 Anton V. Denisov <avd@altlinux.org> 0.5.15cnc3-alt0.1
- Updated to 0.5.15cnc3
- Temporary disabled patches:
  + apt-0.5.4cnc9-alt-getsrc.patch
  + apt-0.5.5cnc4-alt-install_virtual.patch
  + apt-0.5.5cnc4.1-alt-virtual_scores.patch
- Merged upstream patches:
  + apt-0.5.15cnc1-upstream-pinning-fix.patch
- NOTE:
  + this release can not be used with hasher (until we 'll
    update temporary disabled patches);
  + all packages which uses libapt need to be rebuilt (library version
    changed).
- TODO:
  + check and update our patches (most important);
  + update russian translation.

* Tue Nov 11 2003 Anton V. Denisov <avd@altlinux.org> 0.5.15cnc1-alt0.2
- added apt-0.5.15cnc1-upstream-pinning-fix.patch.
- Updated russian translation.

* Sat Nov 08 2003 Anton V. Denisov <avd@altlinux.org> 0.5.15cnc1-alt0.1
- Updated to 0.5.15cnc1, renumbered patches.
- Removed patches:
  + apt-0.5.5cnc5-panu-nodigest.patch
- Updated patches:
  + alt-distro.patch
  + alt-rpm_cmd.patch
  + alt-defaults.patch
- Merged upstream patches:
  + alt-bz2.patch
  + alt-versionmatch.patch
  + alt-versionmatch2.patch
  + alt-cleanups.patch
  + apt-0.5.12_apt-get_backports.patch
  + apt-0.5.12_apt-cache_backports.patch
  + apt-0.5.12_doc_backports.patch
  + apt-0.5.12_methods_backports.patch
  + apt-0.5.12_apt-pkg_backports.patch
  + apt-0.5.12_acqprogress_backports.patch
  + apt-0.5.12_tests_backports.patch
  + apt-0.5.14_apt_get_and_docs.patch
- Temporary disabled patches:
  + alt-install_virtual_version.patch (need to be updated by author)
- Following patches wasn't accepted by upstream (what to do with it?):
  + alt-packagemanager-CheckRConflicts.patch
  + alt-debsystem.patch
  + alt-install_virtual.patch
  + alt-fixpriorsort.patch
  + alt-rpm-fancypercent.patch
  + alt-virtual_scores.patch
  + alt-parseargs.patch

* Thu Oct 09 2003 Anton V. Denisov <avd@altlinux.org> 0.5.5cnc6-alt0.8
- added BuildRequires: python (fix build in hasher).
- partial merge with upstream APT (0.5.14):
  + apt-0.5.14_apt_get_and_docs.patch

* Wed Oct 08 2003 Anton V. Denisov <avd@altlinux.org> 0.5.5cnc6-alt0.7
- added apt-0.5.5cnc6-alt-cleanups.patch (fixed some compiler warnings)
- sync with apt-0.5.5cnc4.1-alt7:
  + updated alt-fixpriorsort.patch
  + updated alt-rpm-fancypercent.patch
  + updated alt-parseargs.patch (and update it for cnc6)
  + added alt-virtual_scores.patch
  + renamed spec file.

* Tue Oct 07 2003 Anton V. Denisov <avd@altlinux.org> 0.5.5cnc6-alt0.5
- partial merge with upstream APT (0.5.12):
  + apt-0.5.12_apt-cache_backports.patch
  + apt-0.5.12_apt-get_backports.patch
  + apt-0.5.12_doc_backports.patch
  + apt-0.5.12_methods_backports.patch
  + apt-0.5.12_apt-pkg_backports.patch
  + apt-0.5.12_acqprogress_backports.patch
  + apt-0.5.12_tests_backports.patch

* Mon Oct 06 2003 Anton V. Denisov <avd@altlinux.org> 0.5.5cnc6-alt0.4
- sync with apt-0.5.5cnc4.1-alt6:
  + added apt-0.5.5cnc4.1-alt-parseargs.patch
  + added apt-0.5.5cnc6-alt-fixpriorsort.patch

* Fri Sep 05 2003 Anton V. Denisov <avd@altlinux.org> 0.5.5cnc6-alt0.3
- s/$RPM_BUILD_ROOT/%%buildroot/g in spec file.
- Updated BuildRequires in Sisyphus (20030704) env.
- Updated russian translation.
- sync with apt-0.5.5cnc4.1-alt5:
  + added apt-0.5.5cnc4-alt-defaults.patch
  + cleaned up /etc/apt.conf file.
  + updated alt-install_virtual.patch
  + added apt-0.5.5cnc4-alt-versionmatch2.patch
  + do not build static libraries by default.

* Mon Jun 16 2003 Anton V. Denisov <avd@altlinux.org> 0.5.5cnc6-alt0.1
- Updated to 0.5.5cnc6.
- Re-added patches due to upstream changes:
  + alt-debsystem.patch (apt-pkg/deb/debsystem.cc was added again).
- Downgraded patches due to upstream changes:
  + alt-getsrc.patch (apt-pkg/deb/debsrcrecords.h was added again).
- Packaged directories:
  + Dir::Bin::scripts (/usr/lib/apt/scripts);
- Updated %%doc (contrib dir added).

* Fri Jun 06 2003 Anton V. Denisov <avd@altlinux.org> 0.5.5cnc5-alt0.5
- old changelog entries come back as rpm_old_changelog.
- updated %%find_lang call.
- added -I m4 for %%__aclocal call.
- more macroszification.
- My Mother birthday edition.

* Tue Jun 03 2003 Anton V. Denisov <avd@altlinux.org> 0.5.5cnc5-alt0.4
- %%install section reworked (%%makeinstall use).
- %%build section cleaned up.
- %%_libdir/*.la moved to libapt-devel subpackage.
- %name.8 removed from sources.
- Dropped obsolete old patches.
- Dropped old changelog entries.

* Tue Jun 03 2003 Anton V. Denisov <avd@altlinux.org> 0.5.5cnc5-alt0.3
- Updated to 0.5.5cnc5, renumbered patches.
- Added patches:
  + apt-0.5.5cnc5-panu-nodigest.patch
- Updated patches:
  + alt-getsrc
  + alt-rsync
  + alt-tinfo
  + alt-rpm (check this one)
- Removed patches due to upstream changes:
  + alt-debsystem
- Merged upstream patches:
  + alt-i18n-apt-cdrom
  + apt-cnc-20030322-algo
- Updated russian translation.
- Explicitly use autoconf-2.5 and automake-1.7 for build.
- Major changes in spec file (need more changes).
- Updated buildrequires (libbeecrypt-devel and glibc-devel-static added).

* Mon Apr 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc4.1-alt4
- apt-get: substitute virtual package with real one (mouse).
- libapt: ignore serial and check both for version and
  version-release while matching version string (mouse).
- Mouse birthday edition.

* Tue Mar 25 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc4.1-alt3
- Applied cnc-20030322 algorithm changes.
- Updated russian translation (avd).

* Tue Mar 11 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc4.1-alt2
- Fixed -lncurses/-ltinfo linkage.
- Updated buildrequires.

* Sat Mar 08 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc4.1-alt1
- Updated to 0.5.5cnc4.1

* Fri Mar 07 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc4-alt1
- Updated to 0.5.5cnc4, renumbered patches.
- Updated patches:
  + alt-rpm_cmd
- Removed patches due to upstream fixes:
  + alt-APT_DOMAIN
  + alt-specialchars
- Packaged directories:
  + Dir::Etc::sourceparts (/etc/apt/sources.list.d);
  + Dir::State::prefetch (/var/lib/apt/prefetch).
- apt-cdrom: i18n'ed (avd).
- Updated russian translation (avd).

* Fri Feb 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc3-alt1
- Updated to 0.5.5cnc3

* Sun Feb 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc2-alt1
- Updated to 0.5.5cnc2
- Merged upstream patches:
  + alt-rpmlistparser-kernel
  + mattdm-manbuild
- Updated genbasedir (svd).
- Cleaned up genbasedir a bit.
- Cleaned up and updated buildrequires.

* Thu Feb 13 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc1-alt3
- Introduced APT::Ignore-dpkg support and set this flag by default,
  to address #0002119.

* Wed Feb 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc1-alt2
- Updated russian translation (Vyacheslav Dikonov).
- Updated buildrequires.

* Fri Feb 07 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.5cnc1-alt1
- Updated to 0.5.5cnc1
- Fixed build:
  + alt-APT_DOMAIN
  + mattdm-manbuild
- Merged upstream patches:
  + alt-algo
  + alt-replace
  + alt-fixes
  + alt-CachedMD5
  + alt-rename-segfault
  + alt-rpmrecords_epoch
  + alt-lockfix
  + alt-cdrom-unmount
- Updated patches:
  + alt-distro
  + alt-pkgpriorities
  + alt-methods_gpg_homedir
- Removed patches:
  + alt-INLINEDEPFLAG

* Tue Jan 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.4cnc9-alt8
- apt-cdrom: Unmout cdrom in case if package file wasn't found (avd).
- apt-cdrom: Fixed default disk name (#0001886).

* Tue Jan 21 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.4cnc9-alt7
- apt-pkg: fixed RPMTAG_EPOCH handling (#0002019, avd).
- apt-get: try to fix lock problem (#0002013, vsu).
- apt-pkg: added APT::Install::VirtualVersion support (mouse).
- methods/gpg (#0001945):
  + added APT::GPG::Homedir support and enabled it by default;
  + dropped APT::GPG::Pubring support.
- apt-pkg: experimental patch for pkgOrderList::Score (#0001931).

* Fri Jan 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.4cnc9-alt6
- apt: PreReq: %__subst (#0001801).
- apt-get: added APT::Install::Virtual support (mouse).
- apt-cdrom: applied alt-specialchars patch from Anton V. Denisov,
  needs to be tested though.
- apt.conf: added "-adv" and "-linus" kernels to Allow-Duplicated list.

* Thu Dec 26 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.4cnc9-alt5
- apt-pkg/packagemanager.cc (pkgPackageManager::CheckRConflicts):
  Ignore versionless reverse dependencies (mouse).

* Mon Dec 23 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.4cnc9-alt4
- Removed builtin defaults for RPM::Allow-Duplicated and RPM::Hold options
  (was added in 0.5.4cnc9-alt1).
- rpmListParser::Package(): removed "kernel" hack.

* Thu Dec 19 2002 Sviatoslav Sviridov <svd@altlinux.ru> 0.5.4cnc9-alt3
- patch for check .bz2 extension in file method
- fixed possible segfault in pkgAcquire::Item::Rename

* Tue Dec 17 2002 Sviatoslav Sviridov <svd@altlinux.ru> 0.5.4cnc9-alt2
- Updated rsync method:
  + Fixed bug leading to race condition.
  + Acquire::rsync::options:: in apt.config allows specification
    of any user-defined option for /usr/bin/rsync.
  + Support port specification in URIs
- Updated README.rsync

* Tue Dec 03 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.4cnc9-alt1
- Reverted 1 of 4 hunks in sorting order fix, to be compatible with upstream.
  We will use pkgpriorities instead.
- Renamed rpmpriorities to pkgpriorities and moved it to apt-conf package.
- Several compilation fixes.
- Fixed gettextization.
- Set builtin defaults for RPM::Allow-Duplicated and RPM::Hold options.
- Renumbered patches.
- Replaced patch to genbasedir with shell script.
- genbasedir:
  + Added new options: --no-oldhashfile, --newhashfile, --no-newhashfile.
  + Enabled generation of both old and new hashfiles by default.
- Do not use __progname in CachedMD5 implementation.
- Fixed apt upgrade trigger.
- Renamed to apt and built for Sisyphus.

* Mon Dec 02 2002 Kachalov Anton <mouse@altlinux.ru> 0.5.4cnc9-alt0.5
- Fixed replace support

* Tue Nov 26 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.4cnc9-alt0.4
- Updated genbasedir patch.
- Fixed sorting algorithm (mouse).
- rpmpriorities: removed libs and obsolete packages.

* Sat Nov 23 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.5.4cnc9-alt0.3
- utils: add -0.5 suffix to %_cachedir/apt/gen* (to enable caching for the
  corresponting utils; <svd@altlinux.ru>);
- describe --mapi in genbasedir usage message;
- include some empty /etc/apt/*.d/ which can be used;

* Sat Nov 16 2002 Sviatoslav Sviridov <svd@altlinux.ru> 0.5.4cnc9-alt0.2
- patch for add option "--fancypercent" to rpm
- patch for genbasedir
- Fixed dependencies:
  + rsync >= 2.5.5-alt3 (now in sisyphus) for apt-0.5-rsync
  + sed for apt-utils (by genbasedir)
- Updated apt.conf:
  + added option RPM::Order="true"

* Mon Oct 28 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.5.4cnc9-alt0.1
- sync with apt-0.3.19cnc55-alt9:
 + rpmpriorities: updated lists (up to alt9);
 + %_localstatedir/apt: fixed permissions
   (used to be: drwxrws--- root rpm, now: drwxr-xr-x root root);
- apt.conf: APT::GPG::PubringPath -> APT::GPG::Pubring transition
  (the default apt.conf and %%triggerun affected);
  (this is what you have to do to make signed sources work!)
- port getsrc patch (from ALT's apt-0.3 branch);
- new upstream release: apt-0.5.4cnc9 ("early remove" problems are said
  to be solved now).

* Wed Oct 16 2002 Sviatoslav Sviridov <svd@altlinux.ru> 0.5.4cnc8-alt0.1
- new release: apt-0.5.4cnc8

* Tue Sep 17 2002 Svaitoslav Sviridov <svd@altlinux.ru> 0.5.4cnc7-alt0.1
- new release: apt-0.5.4cnc7
- included patch for rsync method

* Sun Aug 11 2002 Anton V. Denisov <avd@altlinux.ru> 0.5.4cnc6-alt0.1
- Updated:
	+ APT-0.5.4cnc6 (bugfix release - fixed some segfaults)

* Wed Aug 07 2002 Anton V. Denisov <avd@altlinux.ru> 0.5.4cnc5-alt0.2
- Fixed:
	+ BuildRequires (updated by new version of buildreq utility)

* Tue Aug 06 2002 Anton V. Denisov <avd@altlinux.ru> 0.5.4cnc5-alt0.1
- Fixed:
	+ Symlinks for ssh and bzip2 methods
	+ Spec file (%name!=apt - I forgot this)
- Updated:
	+ APT-0.5.4cnc5
- Removed:
	+ apt-0.5.4cnc1-alt-enable-rsh-method.patch

* Wed Jul 31 2002 Anton V. Denisov <avd@altlinux.ru> 0.5.4cnc4-alt0.1
- Fixed:
    + apt.conf syntax a little
    + %%doc syntax a little
- Updated:
    + APT-0.5.4cnc4
    + BuildRequires
-Removed:
    + apt-0.5.4cnc3-alt-configure-version.patch

* Sat Jul 27 2002 Anton V. Denisov <avd@altlinux.ru> 0.5.4cnc3-alt0.1
- Fixed:
    + libapt-0.5-devel requires
    + apt.conf syntax
- Updated:
    + APT-0.5.4cnc3
    + apt.conf
    + rpmpriorities
    + APT Development Team e-mail
    + apt-0.5 requires
    + select-genlist.patch for new version
    + Spec file
    + %%doc section
- Added:
    + Patch for some debug in md5 operations.
    + apt-0.5.4cnc3-alt-configure-version.patch

* Fri Jul 19 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.5.4cnc1-alt0.3
- make genbasedir-0.5 call gen{pkg,src}list-0.5 respectively

* Fri Jul 19 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.5.4cnc1-alt0.2
- fix the trigger script;
- add 0.5 to the package names and apt-utils binaries (to make co-existence
  of apt-utils possible).

* Fri Jul 19 2002 Anton V. Denisov <avd@altlinux.ru> 0.5.4cnc1-alt1
- New upstream release.
- Some patches regenerated for new version.
- Spec modified for new version.
- It's a just build for Deadalus - not for actual use.
- I just built it but not test yet.
