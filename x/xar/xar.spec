Name: xar
Version: 1.6.1
Release: alt5

Summary: The XAR project aims to provide an easily extensible archive format
License: BSD-3-Clause
Group: Archiving/Compression
Url: https://github.com/mackyle/xar
Source: %name-%version.tar
#patch: xar-1.5.3-alt-config.patch
Patch1: xar-1.5.3-ext2.patch
Patch2: xar-1.6.1-openssl-1.1.patch
Patch3: xar-1.6.1-alt-char-unsigned.patch
Requires: lib%name = %version-%release

# Automatically added by buildreq on Sat Dec 17 2011
BuildRequires: bzlib-devel libacl-devel libe2fs-devel libssl-devel libxml2-devel xsltproc zlib-devel liblzma-devel
BuildRequires: rsync

%description
The XAR project aims to provide an easily extensible archive format.
Important design decisions include an easily extensible XML table of
contents for random access to archived files, storing the toc at the
beginning of the archive to allow for efficient handling of streamed
archives, the ability to handle files of arbitrarily large sizes,
the ability to choose independent encodings for individual files in
the archive, the ability to store checksums for individual files in
both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

Please note that the code quality of this project is quite poor.
Do not expect that error conditions would be handled properly.

%package -n lib%name
Summary: The eXtensible ARchiver runtime library
Group: System/Libraries

%description -n lib%name
The XAR project aims to provide an easily extensible archive format.
This package contains the eXtensible ARchiver runtime library.

Please note that the code quality of this project is quite poor.
Do not expect that error conditions would be handled properly.

%package -n lib%name-devel
Summary: Development files for the eXtensible ARchiver library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The XAR project aims to provide an easily extensible archive format.

This package contains headers and other development files required to
build XAR-based software.

%prep
%setup
#%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# get rid of RPATH.
sed -ri 's/(RPATH=)".*/\1/' xar/configure.ac
sed '/^\. functions/iset -x' -i xar/test/*
sed 's|^\. functions|. ./functions|' -i xar/test/*

%build
cd xar
autoconf
%configure --disable-static --enable-autogen
%make_build

%install
cd xar
%makeinstall_std

%check
cd xar
# prepare test data
rm -rf test/%_builddir
mkdir -p test-bin
rsync -aH --delete /usr/bin/ test-bin/
%__subst "s|/bin$|$(pwd)/test-bin|g" test/*
%__subst "s|bin |test-bin |g" test/*
%__subst "s| bin$| test-bin|g" test/*

cd test
export "PATH=%buildroot%_bindir:$PATH"
export LD_LIBRARY_PATH="%buildroot%_libdir"
xar --help
find .
./checksums
./compression
./data
./hardlink
./heap

%files
%_bindir/*
%_man1dir/*
%doc xar/LICENSE xar/NEWS xar/INSTALL xar/ChangeLog

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed May 08 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.6.1-alt5
- NMU:
  + Fixed FTBFS on architectures where char is unsigned.
  + Build on all architectures (including LoongArch).
  + Use /usr/bin for test archive. Fixes usrmerge fallout.

* Fri Dec 31 2021 Michael Shigorin <mike@altlinux.org> 1.6.1-alt4
- actually builds on %%e2k

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.1-alt3
- NMU: Fix license.

* Thu Dec 20 2018 Pavel Skrylev <majioa@altlinux.org> 1.6.1-alt2
- Fixed build of failure, got from lost part of PATH.

* Thu Dec 13 2018 Pavel Skrylev <majioa@altlinux.org> 1.6.1-alt1
- Updated original source url.
- Bump to 1.6.1.

* Mon Dec 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt2
- fix ext2 build
- make copy of /bin for test purposes

* Sat Dec 17 2011 Dmitry V. Levin <ldv@altlinux.org> 1.5.3-alt1
- Updated to 1.5.3.
- Made it actually work on x86.
- Fixed RPATH issue.
- Enabled test suite.
- Enabled ACL support.
- Relocated headers back to /usr/include/xar/.
- Updated package descriptions, added a warning about poor code quality.

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt3
- repair build

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Fri Mar 13 2009 Eugene Ostapets <eostapets@altlinux.ru> 1.5.2-alt2
- Move headers from %_includedir/%name to %_includedir

* Fri Mar 06 2009 Eugene Ostapets <eostapets@altlinux.ru> 1.5.2-alt1
- First build for ALTLinux

