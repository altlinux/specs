%define _unpackaged_files_terminate_build 1
%define jlibexec %prefix/libexec/jonh-jumbo
%define jdata %prefix/share/john-jumbo
%define CONFOPTS --with-systemwide

Name: john-jumbo
Version: 1.9.0
Release: alt6.1964.gcd338a0db

Summary: John the Ripper password cracker core
License: GPLv2
Group: System/Base
Url: http://www.openwall.com/john/
Vcs: https://github.com/openwall/john

Source: %name-%version.tar
Patch: %name-%version-alt.patch

# TODO: john-jumbo-extras has several perl deps not installable in ALT:
#   Crypt::ECB, Crypt::Rhash, Crypt::ScryptKDF, Crypt::UnixCrypt_XS,
#   Digest::BLAKE2, Digest::Keccak, Digest::SHA3, Digest::Tiger.
# TODO: not packaged in ALT.
%add_findreq_skiplist /usr/libexec/jonh-jumbo/7z2john.pl
%add_findreq_skiplist /usr/libexec/jonh-jumbo/lion2john-alt.pl
%add_findreq_skiplist /usr/libexec/jonh-jumbo/pass_gen.pl

# TODO: outdated module paths.
%add_findreq_skiplist /usr/libexec/jonh-jumbo/lib/PDF.pm
%add_findreq_skiplist /usr/libexec/jonh-jumbo/lib/ExifTool.pm
%add_findreq_skiplist /usr/libexec/jonh-jumbo/pdf2john.pl
%add_findreq_skiplist /usr/libexec/jonh-jumbo/sha-test.pl

# Automatically added by buildreq on Thu Jun 04 2020
BuildRequires: bzlib-devel git-core libgmp-devel libgomp-devel libpcap-devel libssl-devel zlib-devel
BuildRequires: rpm-build-python3

# These look like runtime perl deps, but they are required at *build* time:
# /usr/lib/rpm/perl.req runs `perl -c` on every installed *.pl to compute
# Requires:, and `use Foo` inside a script makes the parse fail unless Foo
# is present in the buildroot. Dropping any of these reintroduces
# "find-requires: ERROR: /usr/lib/rpm/perl.req failed".
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
Requires: john-jumbo
# Each *2john.py needs its own narrow Python module (Crypto, scapy, dpkt,
# pyhanko, ldap3, ...). Forcing the union as hard Requires would drag a
# huge dependency tree onto every user. Drop python autoreq; users hit
# ImportError only for the specific tool they invoke.
AutoReq: yes,nopython,nopython3

%description extras
Jumbo version of John the Ripper.

%prep
%setup
%autopatch -p1

cat > john-jumbo.sh <<@@@
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

%build
cd src
%autoreconf

%ifarch %ix86
%add_optflags -no-pie
export LDFLAGS="$LDFLAGS -no-pie"
%endif

for VARIANT in `seq 8`; do
  %configure %CONFOPTS || break
  # Pick the SIMD -m flag (first -m on CFLAGS line); skip -maes/-mpclmul
  # which upstream appends to CPU_BEST_FLAGS but are not what drives the
  # variant chain.
  MAXARCH="`sed -n '/^CFLAGS =/p' Makefile | grep -oE -- '-m[a-z][a-z0-9.]+' | grep -vE -- '-m(aes|pclmul)$' | head -1 | sed 's/^-m//'`"
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
    # Inject the fallback macros into both CFLAGS and CFLAGS_MAIN: john.c
    # (which carries cpu_fallback()) is built via $(CFLAGS_MAIN), not
    # $(CFLAGS), so patching only the latter leaves the fallback chain
    # out of the actual entry-point binary.
    sed -i "s/^CFLAGS\(_MAIN\)\? =/& -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='\"$NEXTJOHN\"'/" Makefile
    %make_build STRIP=/bin/true
  fi
  mv ../run/john ../run/$CURRENTJOHN
done

%install
mkdir -p %buildroot%jlibexec %buildroot%_bindir %buildroot%jdata
cp -a run/* %buildroot%jlibexec
install -m755 -D john-jumbo.sh %buildroot%_bindir/john-jumbo
install -D run/john.zsh_completion %buildroot%_datadir/zsh/site-functions/_john
install -D run/john.bash_completion %buildroot%_sysconfdir/bash_completion.d/john.bashcomp

for N in src/[1-9]*.next; do
  . $N
  echo "%jlibexec/$CURRENTJOHN"
done > %buildroot.john-jumbo.files

. src/1.next

cd %buildroot%jlibexec
ln -s $CURRENTJOHN john
install -D john.conf %buildroot%_sysconfdir/john-jumbo/john.conf
mv rules *.txt *.chr *.conf *.lst %buildroot%jdata/
find * -type l | sed 's@^@%jlibexec/@' >> %buildroot.john-jumbo.files

rm %buildroot%jdata/john.conf && \
  ln -sr %buildroot%_sysconfdir/john-jumbo/john.conf %buildroot%jdata/john.conf

%files -f %buildroot.john-jumbo.files
%doc doc/*
%attr(750,root,wheel) %dir %jlibexec
%attr(750,root,wheel) %dir %_sysconfdir/john-jumbo
%attr(640,root,wheel) %config(noreplace) %_sysconfdir/john-jumbo/*
%jdata
%_bindir/john-jumbo

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
* Sun May 10 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.9.0-alt6.1964.gcd338a0db
- Build a snapshot ~1964 commits past 1.9.0-Jumbo-1: upstream has not
  released since 2019.
- Switch to upstream-tag + cumulative ALT patch layout; %prep no
  longer mutates sources (python3 shebangs, Image::ExifTool, ALT
  install paths and -flto LDFLAGS now live in the cum-patch).
- Fix multi-variant CPU dispatch: pick the first -m on the CFLAGS
  line, and inject CPU_FALLBACK into CFLAGS_MAIN as well.
- extras: drop python autoreq (each *2john.py pulls a different
  narrow module); skip findreq on ccl_chrome_indexeddb.
- Spec cleanup: gear hygiene, dead skiplists/macros gone.

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
