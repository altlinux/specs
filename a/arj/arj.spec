Name: arj
Version: 3.10.22
Release: alt6
Epoch: 1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: An compressor and uncompressor for .arj format archive files
License: GPL
Group: Archiving/Compression

URL: http://arj.sourceforge.net
Source: http://testcase.newmail.ru/files/arj-%version.tar.gz
Patch0: http://ftp.debian.org/debian/pool/main/a/arj/arj_%version-6.diff.gz
Patch1: arj-3.10.22-custom-printf.patch
Patch2: arj-3.10.22-missing-protos.patch
Patch3: arj-3.10.22-safe_strcpy.patch

%description
The ARJ program is used to compress and uncompress .arj format archives.
The .arj format archive was mostly used on DOS machines.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

for i in debian/patches/00*.patch; do
  patch -p1 < $i
done

# strcopy doesn't like overlapping
# for f in `egrep -lr 'strcpy\(([a-zA-Z0-9_]+), \1\+' *`; do
# sed -ri 's/strcpy\(([a-zA-Z0-9_]+), \1(\+[^(]*)\)/bcopy(\1\2, \1, strlen(\1\2)+1)/g' $f
# done

%build
cd gnu
autoconf
libtoolize --copy --force
%configure
cd ..

make prepare
# Parallel build OK thanks to Debian patch
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD -m 644 resource/rearj.cfg.example $RPM_BUILD_ROOT%_sysconfdir/rearj.cfg

%files
%_sysconfdir/*
%_bindir/*
%_libdir/arj
%_man1dir/*
%doc doc/*.txt resource/en/*.txt

%changelog
* Wed Jul 13 2011 Fr. Br. George <george@altlinux.ru> 1:3.10.22-alt6
- Do not use srtcpy() for overlapping strings

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 1:3.10.22-alt5
- Rebuild in Sisyphus

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 1:3.10.22-alt4
- Rebuild in Sisyphus

* Mon Jun 15 2009 Victor Forsyuk <force@altlinux.org> 1:3.10.22-alt3
- Fix FTBFS due to conflicting strnlen definition with the glibc headers.
- Added Debian patches.

* Thu Nov 24 2005 Victor Forsyuk <force@altlinux.ru> 1:3.10.22-alt2
- Add Epoch to upgrade from 3.10b (rpm thinks that "3.10.22" < "3.10b").
- Package owns %%_libdir/arj.

* Mon Jul 11 2005 Victor Forsyuk <force@altlinux.ru> 3.10.22-alt1
- 3.10.22

* Tue Jun 07 2005 Victor Forsyuk <force@altlinux.ru> 3.10.21-alt1
- 3.10.21

* Fri Dec 12 2003 Vyacheslav Dikonov <slava@altlinux.ru> 3.10b-alt3
- EXPERIMENTAL build with -fPIC gcc option

* Thu Sep 11 2003 Vyacheslav Dikonov <slava@altlinux.ru> 3.10b-alt2
- BuildPreReq for hasher

* Tue Feb 04 2003 Vyacheslav Dikonov <slava@altlinux.ru> 3.10b-alt1
- Build official Open-source release arj version 3.10b
- ALTLinux build (English)
