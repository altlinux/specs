# this package can not be relocatable 'cause package
# root is to be compiled into binary executables
%define target /usr/lib/plan9
%set_compress_method none

Name: plan9
Version: 1.0
Release: alt1.1
Summary: Plan9 from User Space
License: Lucent Public License Version 1.02
Group: Development/Other
URL: http://swtch.com/plan9port/

Source: %name-%version.tar

# Automatically added by buildreq on Thu Jun 02 2011 (-ba)
BuildRequires: cuetools gv libXext-devel libXt-devel mailx python-module-PEAK-Rules python-module-PasteScript python-module-dap python-module-recaptcha-client xinit

%description
This is the base package, that contains command line only
utilities for Plan9 environment.

Please, note that ALT Linux distribution of Plan9 from User
Space does not contain acid (debugger), lp (printing system)
and upas (mail system) yet. It is in the TODO.

%package 9pfuse
Summary: Plan9 from User Space - FUSE server for 9pfs
License: Lucent Public License Version 1.02
Group: Development/Other
URL: http://swtch.com/plan9port/

%description 9pfuse
FUSE server for 9pfs.

%package wm
Summary: Plan9 from User Space - x11 utilities and rio WM
License: Lucent Public License Version 1.02
Group: Development/Other
URL: http://swtch.com/plan9port/
Requires: %name = %version-%release

%description wm
X11-enabled commands and other stuff, related to windowed
environment. Contains rio (window manager), acme (text
editor) and much more.

%package troff
Summary: Plan9 from User Space - troff & postcript
License: Lucent Public License Version 1.02
Group: Development/Other
URL: http://swtch.com/plan9port/
Requires: %name = %version-%release

%description troff
Troff and postscript files, fonts etc.

%package venti
Summary: Plan9 from User Space - venti backup server & utilities
License: Lucent Public License Version 1.02
Group: Development/Other
URL: http://swtch.com/plan9port/
Requires: %name = %version-%release

%description venti
Venti is a backup server for Plan9 from User Space.

%package man
Summary: Plan9 from User Space - manual files
License: Lucent Public License Version 1.02
Group: Development/Other
URL: http://swtch.com/plan9port/
Requires: %name = %version-%release
BuildArch: noarch

%description man
Manual pag for Plan9 from User Space.


%package devel
Summary: Plan9 from User Space - headers, sources etc.
License: Lucent Public License Version 1.02
Group: Development/Other
URL: http://swtch.com/plan9port/
Requires: %name = %version-%release

%description devel
Development files, including compilator/linker etc. (9c, 9l, 9ar...),
debuggers, source C files, headers, scripts and other stuff required
for Plan9 from User Space development.

%add_findreq_skiplist */tmac.pm
%add_findprov_skiplist */tmac.pm

%prep
%setup

%install
# create directories
mkdir -p %buildroot/%target
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_sysconfdir/X11/wmsession.d
mkdir -p %buildroot/%_iconsdir/hicolor/48x48/apps
mkdir -p %buildroot/%_docdir/%name

# install X11 session and resources
cp -a 09rio %buildroot/%_sysconfdir/X11/wmsession.d
cp -a glenda-48x48.png %buildroot/%_iconsdir/hicolor/48x48/apps/plan9-glenda.png

# install scripts, links, etc...
ln -s %target/bin/9pfuse %buildroot/%_bindir
cp -a 9 rio %buildroot/%_bindir
cp -a userspace/* %buildroot/%target
cp -a README.alt TODO.alt %buildroot/%_docdir/%name

pushd %buildroot/%target

# fix all the interpreters pathes
    find bin src lib include man -type f ! -path 'man/man*' -exec sh -c "
        printf '%%-60s' 'fix {} ... ';
        sed -i '
        s|/usr/bin/sed|/bin/sed|;
        s|#\!/bin/rc|#\!%target/bin/rc|;
        s|/usr/local/plan9|%target|;
        ' '{}';
        printf 'done\n';
    " \;

# do bundled install
    ./INSTALL -r %target

# no need in html docs yet - html in TODO
    find man -type f -name '*html' -exec rm -f '{}' \;

# wrap 9term
    pushd bin
        mkdir wrapped
        mv 9term wrapped
    popd
    pushd +1
        cp -a 9term %buildroot/%target/bin
    pushd +1

# install docs
    cp -a \
        CHANGES \
        CONTRIBUTORS \
        LICENSE \
        README \
        TODO \
    %buildroot/%_docdir/%name

# hack around 'core' and brp-cleanup
    pushd bin
        mv core 9core
    popd

popd

%files
# custom stuff
%_bindir/9

# explicitly pack /bin files
%target/bin/""
%target/bin/9
%target/bin/9660srv
%target/bin/9fs
%target/bin/9p
%target/bin/9pserve
%target/bin/9.rc
%target/bin/aescbc
%target/bin/ascii
%target/bin/asn12dsa
%target/bin/asn12rsa
%target/bin/auxclog
%target/bin/auxstats
%target/bin/awk
%target/bin/B
%target/bin/basename
%target/bin/bc
%target/bin/bundle
%target/bin/bunzip2
%target/bin/bzip2
%target/bin/cal
%target/bin/calendar
%target/bin/cat
%target/bin/cleanname
%target/bin/cmp
%target/bin/comm
%target/bin/date
%target/bin/dc
%target/bin/dd
%target/bin/dial
%target/bin/diff
%target/bin/dns
%target/bin/dnsdebug
%target/bin/dnsquery
%target/bin/dnstcp
%target/bin/dsa2pub
%target/bin/dsa2ssh
%target/bin/dsagen
%target/bin/du
%target/bin/dump9660
%target/bin/E
%target/bin/echo
%target/bin/ed
%target/bin/factor
%target/bin/factotum
%target/bin/file
%target/bin/fmt
%target/bin/fortune
%target/bin/freq
%target/bin/fs/
%target/bin/fsize
%target/bin/g
%target/bin/getflags
%target/bin/grep
%target/bin/gunzip
%target/bin/gview
%target/bin/gzip
%target/bin/hget
%target/bin/hist
%target/bin/hoc
%target/bin/htmlfmt
%target/bin/idiff
%target/bin/import
%target/bin/ipso
%target/bin/join
%target/bin/kill
%target/bin/lc
%target/bin/listen1
%target/bin/look
%target/bin/ls
%target/bin/Mail
%target/bin/mc
%target/bin/md5sum
%target/bin/mk9660
%target/bin/mkdir
%target/bin/mount
%target/bin/mtime
%target/bin/namespace
%target/bin/ndbipquery
%target/bin/ndbmkdb
%target/bin/ndbmkhash
%target/bin/ndbmkhosts
%target/bin/ndbquery
%target/bin/netkey
%target/bin/nobs
%target/bin/p
%target/bin/passwd
%target/bin/pbd
%target/bin/pemdecode
%target/bin/pemencode
%target/bin/plumb
%target/bin/plumber
%target/bin/pr
%target/bin/primes
%target/bin/ps
%target/bin/psu
%target/bin/ramfs
%target/bin/rc
%target/bin/read
%target/bin/readcons
%target/bin/rm
%target/bin/rsa2csr
%target/bin/rsa2pub
%target/bin/rsa2ssh
%target/bin/rsa2x509
%target/bin/rsafill
%target/bin/rsagen
%target/bin/sam
%target/bin/samsave
%target/bin/secstore
%target/bin/secstored
%target/bin/secuser
%target/bin/sed
%target/bin/seq
%target/bin/sftpcache
%target/bin/sha1sum
%target/bin/slay
%target/bin/sleep
%target/bin/sort
%target/bin/spell
%target/bin/split
%target/bin/sprog
%target/bin/srv
%target/bin/ssam
%target/bin/ssh-agent
%target/bin/start
%target/bin/stop
%target/bin/strings
%target/bin/sum
%target/bin/tail
%target/bin/tar
%target/bin/tcs
%target/bin/tee
%target/bin/test
%target/bin/time
%target/bin/touch
%target/bin/tr
%target/bin/u
%target/bin/unicode
%target/bin/uniq
%target/bin/units
%target/bin/unmount
%target/bin/unutf
%target/bin/unzip
%target/bin/u.rc
%target/bin/usage
%target/bin/vmount0
%target/bin/vwhois
%target/bin/wc
%target/bin/xd
%target/bin/yesterday
%target/bin/zip


%target/lib/amspell
%target/lib/bclib
%target/lib/brspell
%target/lib/fortunes
%target/lib/mimetype
%target/lib/unicode
%target/lib/units
%target/lib/words

%target/log/
%target/ndb/
%target/plumb/
%target/proto/

%target/rcmain

%doc %_docdir/%name/*

%files 9pfuse
%_bindir/9pfuse
%target/bin/9pfuse

%files venti
%target/bin/unvac
%target/bin/vac
%target/bin/vacfs
%target/bin/vbackup
%target/bin/vcat
%target/bin/venti/
%target/bin/vmount
%target/bin/vnfs

%files troff
%target/bin/delatex
%target/bin/deroff
%target/bin/doctype
%target/bin/eqn
%target/bin/htmlroff
%target/bin/nroff
%target/bin/pic
%target/bin/proof
%target/bin/psdownload
%target/bin/psfonts
%target/bin/tbl
%target/bin/tpic
%target/bin/tr2post
%target/bin/tref
%target/bin/troff
%target/bin/troff2html
%target/bin/troff2png
%target/lib/hyphen.tex
%target/postscript/
%target/troff/

%files wm
# custom stuff
%_iconsdir/hicolor/48x48/apps/plan9-glenda.png
%_sysconfdir/X11/wmsession.d/09rio
%_bindir/rio

# regular stuff
%target/bin/"
%target/bin/9term
%target/bin/astro
%target/bin/acme
%target/bin/acmeevent
%target/bin/awd
%target/bin/bmp
%target/bin/cmapcube
%target/bin/colors
%target/bin/crop
%target/bin/devdraw
%target/bin/fontsrv
%target/bin/Getdir
%target/bin/gif
%target/bin/grap
%target/bin/graph
%target/bin/ico
%target/bin/iconv
%target/bin/img
%target/bin/jpg
%target/bin/label
%target/bin/mapd
%target/bin/netfileget
%target/bin/netfilelib.rc
%target/bin/netfileput
%target/bin/Netfiles
%target/bin/netfilestat
%target/bin/page
%target/bin/plot
%target/bin/png
%target/bin/ppm
%target/bin/psv
%target/bin/resample
%target/bin/rio
%target/bin/samterm
%target/bin/scat
%target/bin/snarfer
%target/bin/stats
%target/bin/statusbar
%target/bin/tcolors
%target/bin/togif
%target/bin/toico
%target/bin/topng
%target/bin/toppm
%target/bin/tweak
%target/bin/web
%target/bin/win
%target/bin/wintext
%target/bin/wmail
%target/bin/wrapped/9term
%target/bin/xshove
%target/bin/yuv

%target/lib/acme.rc
%target/lib/grap.defines
%target/lib/gv.resource
%target/lib/gv.style
%target/lib/keyboard

%target/face/
%target/font/
%target/sky/

%files man
%target/bin/lookman
%target/bin/man
%target/bin/sig
%target/man/

%files devel
%target/bin/9a
%target/bin/9ar
%target/bin/9c
%target/bin/9core
%target/bin/9l
%target/bin/codereview
%target/bin/codereview.py
%target/bin/db
%target/bin/lex
%target/bin/mk
%target/bin/src
%target/bin/stack
%target/bin/yacc

%target/lib/codereview/
%target/lib/lex.ncform
%target/lib/yaccpar
%target/lib/yaccpars
#target/lib/*.a

%target/include
%target/src
%target/unix

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Sun May 29 2011 Peter V. Saveliev <peet@altlinux.org> 1.0-alt1
- Sisyphus build.

