Name: unar
Version: 1.9.1
Release: alt1
Summary: Multi-format archive extractor
License: LGPLv2+
Group: Archiving/Compression
Url: http://unarchiver.c3.cx/unarchiver/
Source: %name-%version.tar.gz
Patch: unar1.8.1-clang.patch
# NB: source tree moved from "The Unarchiver" to unar-version

# Automatically added by buildreq on Mon Mar 03 2014
# optimized out: libcloog-isl4 libgnustep-base libgnustep-objc2 libgnustep-objc2-devel libgpg-error libobjc-devel libp11-kit libstdc++-devel
BuildRequires: bzlib-devel clang gnustep-base-devel libicu-devel unzip zlib-devel libstdc++-devel libgnustep-objc2-devel

%description
The command-line utilities lsar and unar are capable of listing and extracting
files respectively in several formats including RARv3. unar can serve as a free
and open source replacement of unrar.

%prep
%setup
%patch -p1

%build
%make_build OBJCC=clang CC=clang CXX=clang++ -C XADMaster -f Makefile.linux

%install
install -d %buildroot%_bindir
install -pm755 XADMaster/unar XADMaster/lsar %buildroot%_bindir
install -d %buildroot%_mandir/man1
install -pm644 Extra/*.1 %buildroot%_mandir/man1

install -D Extra/lsar.bash_completion %buildroot%_datadir/bash-completion/completions/lsar
install -D Extra/unar.bash_completion %buildroot%_datadir/bash-completion/completions/unar

%files
%doc License.txt
%_bindir/*
%_man1dir/*
%_datadir/bash-completion/*

%changelog
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
