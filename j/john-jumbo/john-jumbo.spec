Name: john-jumbo
Version: 1.9.0
Release: alt5
License: GPLv2
Group: System/Base
Url: http://www.openwall.com/john/
Source: john-%version-jumbo-1.tar.xz
Patch: john-1.9.0-alt-bash_completion.patch
Patch2000: %name-e2k.patch

#set_perl_req_method relaxed
# TODO: fix it!
#   john-jumbo-extras: Depends: perl(Crypt/ECB.pm) but it is not installable
#                    Depends: perl(Crypt/Rhash.pm) but it is not installable
#                    Depends: perl(Crypt/ScryptKDF.pm) but it is not installable
#                    Depends: perl(Crypt/UnixCrypt_XS.pm) but it is not installable
#                    Depends: perl(Digest/BLAKE2.pm) but it is not installable
#                    Depends: perl(Digest/Keccak.pm) but it is not installable
#                    Depends: perl(Digest/SHA3.pm) but it is not installable
#                    Depends: perl(Digest/Tiger.pm) but it is not installable
%add_python_req_skip pysap

%add_python_req_skip dpkt

# TODO: No packages
%add_findreq_skiplist /usr/libexec/jonh-jumbo/7z2john.pl
%add_findreq_skiplist /usr/libexec/jonh-jumbo/lion2john-alt.pl
%add_findreq_skiplist /usr/libexec/jonh-jumbo/pass_gen.pl

# TODO: Too old (new paths)
%add_findreq_skiplist /usr/libexec/jonh-jumbo/lib/PDF.pm
%add_findreq_skiplist /usr/libexec/jonh-jumbo/lib/ExifTool.pm
%add_findreq_skiplist /usr/libexec/jonh-jumbo/pdf2john.pl
%add_findreq_skiplist /usr/libexec/jonh-jumbo/sha-test.pl

# TODO: Syntax error
%add_findreq_skiplist /usr/libexec/jonh-jumbo/rexgen2rules.pl
%add_findreq_skiplist /usr/libexec/jonh-jumbo/leet.pl

Summary: John the Ripper password cracker core

# Automatically added by buildreq on Thu Jun 04 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libcrypt-devel libgpg-error perl pkg-config python-modules python2-base sh4 xz
BuildRequires: bzlib-devel git-core libgmp-devel libgomp-devel libpcap-devel libssl-devel zlib-devel

BuildRequires: rpm-build-python rpm-build-python3

# TODO: this is actually Perl runtime requires, but findreq fails without them
# Excarpted from rpm itself
BuildRequires: perl(Crypt/AuthEnc/CCM.pm)
BuildRequires: perl(Crypt/Cipher/AES.pm)
BuildRequires: perl(Crypt/Cipher/Blowfish.pm)
BuildRequires: perl(Crypt/Digest/RIPEMD128.pm)
BuildRequires: perl(Crypt/Digest/RIPEMD160.pm)
BuildRequires: perl(Crypt/Digest/RIPEMD256.pm)
BuildRequires: perl(Crypt/Digest/RIPEMD320.pm)
BuildRequires: perl(Crypt/Mode/CFB.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Digest.pm)
BuildRequires: perl(Digest/GOST.pm)
BuildRequires: perl(Digest/Haval256.pm)
BuildRequires: perl(Digest/MD2.pm)
BuildRequires: perl(Digest/MD4.pm)
BuildRequires: perl(Digest/MD5.pm)
BuildRequires: perl(Digest/SHA.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(Errno.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Copy.pm)
BuildRequires: perl(File/Glob.pm)
BuildRequires: perl(FileHandle.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(Image/ExifTool/XMPStruct.pl)
BuildRequires: perl(MIME/Base64.pm)
BuildRequires: perl(Math/BigInt.pm)
BuildRequires: perl(Net/LDAP.pm)
BuildRequires: perl(Net/Pcap.pm)
BuildRequires: perl(Net/Radius/Dictionary.pm)
BuildRequires: perl(Net/Radius/Packet.pm)
BuildRequires: perl(Net/SSLeay.pm)
BuildRequires: perl(NetPacket/Ethernet.pm)
BuildRequires: perl(NetPacket/IP.pm)
BuildRequires: perl(NetPacket/UDP.pm)

%description
John the Ripper is a fast password cracker, currently available for many
flavors of Unix, macOS, Windows, DOS, BeOS, and OpenVMS. Historically,
its primary purpose is to detect weak Unix passwords. These days,
besides many Unix crypt(3) password hash types, supported in "-jumbo"
versions are hundreds of additional hashes and ciphers.

%package extras
Group: System/Base
License: GPLv2
Summary: John the Ripper password cracker (jumbo version)
Requires: %name

%description extras
Jumbo version of John the Ripper

%prep
%define jlibexec %prefix/libexec/jonh-jumbo
%define jdata %prefix/share/john-jumbo
%setup -n john-%version-jumbo-1

%patch -p0
%ifarch %e2k
%patch2000 -p1
%endif

# -flto fix
sed -i '/AC_CONFIG_FILES/i LDFLAGS="$CPU_BEST_FLAGS $CFLAGS $LDFLAGS"' src/configure.ac

sed -i 's@\$prefix/bin@%jlibexec@
s@\$prefix/share/john@%jdata@' src/configure.ac

cat > %name.sh <<@@@
#!/bin/sh
export PATH=%jlibexec:\$PATH
case "\$#" in
 0) case "\$SHELL" in 
    *bash) PS1='[JJ: \u@\h \W]\\\$ ' \$SHELL -l;;
    *)
      if [ -x /bin/bash ]; then
	PS1='[JJ: \u@\h \W]\\\$ ' /bin/bash -l
      else
	PS1='[JJ] \\$ ' \$SHELL
      fi;;
    esac;;
 *) exec john "\$@";;
esac
@@@

# Hack
sed -i 's@ExifTool@Image::ExifTool@' run/pdf2john.pl
grep -rl '#! */usr/bin/python *$' * | while read F; do
	sed -i 's/python/python2/g' "$F"
done
grep -rl '#! */usr/bin/env python *$' * | while read F; do
	sed -i 's/python/python2/g' "$F"
done

%build

cd src
%autoreconf

%define CONFOPTS --with-systemwide

%ifarch %ix86
%add_optflags -no-pie
export LDFLAGS="$LDFLAGS -no-pie"
%endif

for VARIANT in `seq 8`; do
  %configure %CONFOPTS || break
  MAXARCH="`sed -n '/CFLAGS =/s/.* -m\([^ ]*\).*/\1/p' Makefile`"
  MAXARCH="`echo $MAXARCH | sed 's/[0-9.]//g'`"
  JOHNMAX="john-$MAXARCH"
  echo "CURRENTJOHN='$JOHNMAX'" > $VARIANT.next
  sed '/CPU_BEST_FLAGS="'"-m$MAXARCH[0-9.]*"'"/,+7{s/yes/no/;s/CPU_BEST_FLAGS=.*/CPU_NOTFOUND=1/;s/SIMD_NAME=.*//;s/ARCH_LINK=.*//}' configure> configure.0
  mv configure $VARIANT.configure
  echo "NEXTJOHN='$JOHNMAX'" >> $((VARIANT-1)).next
  diff $VARIANT.configure configure.0 && break
  mv configure.0 configure
  chmod +x configure
done

for CONFNAME in *.configure; do
  VARIANT=${CONFNAME%%.*}
  NEXTJOHN=""
  . ./"$VARIANT.next"
  make distclean || :
  ln -sf $VARIANT.configure configure
  echo "@@ Making $CURRENTJOHN->$NEXTJOHN"
  if [ -z "$NEXTJOHN" ]; then
    %configure %CONFOPTS
    %make_build STRIP=/bin/true
  else
    %configure %CONFOPTS
    sed -i "s/^CFLAGS =/CFLAGS = -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='\"$NEXTJOHN\"'/" Makefile
    %make_build STRIP=/bin/true
  fi
  mv ../run/john ../run/$CURRENTJOHN
done

%install
%define johndata %_datadir%jonh
mkdir -p %buildroot%jlibexec %buildroot%_bindir %buildroot%jdata
cp -a run/* %buildroot%jlibexec
install -m755 -D %name.sh %buildroot%_bindir/%name
install -D run/john.zsh_completion %buildroot%_datadir/zsh/site-functions/_john
install -D run/john.bash_completion %buildroot%_sysconfdir/bash_completion.d/john.bashcomp

for N in src/[1-9]*.next; do
  . $N
  echo "%jlibexec/$CURRENTJOHN"
done > %buildroot.john-jumbo.files

. src/1.next

cd %buildroot%jlibexec
ln -s $CURRENTJOHN john
install -D john.conf %buildroot%_sysconfdir/%name/john.conf
mv rules *.txt *.chr *.conf *.lst %buildroot%jdata/
find * -type l | sed 's@^@%jlibexec/@' >> %buildroot.john-jumbo.files

rm %buildroot%jdata/john.conf && \
  ln -sr %buildroot%_sysconfdir/%name/john.conf %buildroot%jdata/john.conf

%files -f %buildroot.john-jumbo.files
%doc doc/*
%attr(750,root,wheel) %dir %jlibexec
%attr(750,root,wheel) %dir %_sysconfdir/%name
%attr(640,root,wheel) %config(noreplace) %_sysconfdir/%name/*
%jdata
%_bindir/%name

%files extras
%jlibexec/*
%_sysconfdir/bash_completion.d/john.bashcomp
%_datadir/zsh/site-functions/_john
%exclude %jlibexec/john-*
%exclude %jlibexec/john
%exclude %jlibexec/base64conv
%exclude %jlibexec/gpg2john
%exclude %jlibexec/rar2john
%exclude %jlibexec/unafs
%exclude %jlibexec/undrop
%exclude %jlibexec/unique
%exclude %jlibexec/unshadow
%exclude %jlibexec/zip2john

%changelog
* Wed Sep 08 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.9.0-alt5
- added Elbrus support
- fixed -flto

* Fri May 07 2021 Fr. Br. George <george@altlinux.ru> 1.9.0-alt4
- fix python2/3 findreq

* Thu Apr 22 2021 Egor Ignatov <egori@altlinux.org> 1.9.0-alt3
- fix FTBFS on i586 due to -enalbe-default-pie

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt2
- NMU: make dpkt optional

* Thu Jun 11 2020 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Initial build for ALT
