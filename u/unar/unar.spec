Name: unar
Version: 1.10.8
Release: alt1
Summary: Multi-format archive extractor
License: LGPLv2.1+
Group: Archiving/Compression
Url: https://github.com/MacPaw/XADMaster
Source: %name-%version.tar.gz
Patch: unar-system_UniversalDetector.patch

# Automatically added by buildreq on Wed Aug 25 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnustep-base-devel libgnustep-base libobjc-devel libp11-kit libstdc++-devel python3-base sh4
BuildRequires: bzlib-devel gcc-c++ gcc-objc libUniversalDetector-devel-static libicu-devel libwavpack-devel python3 zlib-devel

%description
The command-line utilities lsar and unar are capable of listing and extracting
files respectively in several formats including RARv3. unar can serve as a free
and open source replacement of unrar.

%prep
%setup
%patch -p1

%build
%make_build -f Makefile.linux

%install
install -d %buildroot%_bindir
install -pm755 unar lsar %buildroot%_bindir
install -d %buildroot%_mandir/man1
install -pm644 Extra/*.1 %buildroot%_mandir/man1

install -D Extra/lsar.bash_completion %buildroot%_datadir/bash-completion/completions/lsar
install -D Extra/unar.bash_completion %buildroot%_datadir/bash-completion/completions/unar

%files
%doc *.md
%_bindir/*
%_man1dir/*
%_datadir/bash-completion/*

%changelog
* Thu Jan 22 2026 Fr. Br. George <george@altlinux.org> 1.10.8-alt1
- Autobuild version bump to 1.10.8

* Mon Jul 12 2021 Fr. Br. George <george@altlinux.ru> 1.10.7-alt1
- Autobuild version bump to 1.10.7 (Closes: #39069)

* Mon Oct 12 2020 Andrey Cherepanov <cas@altlinux.org> 1.10.1-alt1.1
- NMU: Build without libgnustep-objc2-devel.

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1.10.1-alt1
- Autobuild version bump to 1.10.1

* Sun Feb 28 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.1-alt1.1
- Rebuild with new icu

* Mon Dec 28 2015 Fr. Br. George <george@altlinux.ru> 1.9.1-alt1
- Autobuild version bump to 1.9.1

* Mon Mar 03 2014 Fr. Br. George <george@altlinux.ru> 1.8.1-alt1
- Autobuild version bump to 1.8.1
- Switch to CLANG

* Mon Mar 03 2014 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Initial build from FC

* Sun Dec 29 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.8-1
- upstream release 1.8 (rhbz#1047226)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-4
- fix spurious executable permissions

* Fri Apr 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-3
- revert dir ownership change and requires on bash-completion

* Thu Apr 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-2
- fix dir ownership and add requires on bash-completion.
- fix a couple of typos

* Thu Apr 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-1
- initial spec file. based on spec from Huaren Zhong <huaren.zhong@gmail.com>
