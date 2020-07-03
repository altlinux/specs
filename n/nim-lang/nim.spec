Name: nim-lang
Version: 1.2.4
Release: alt1
License: MIT
Summary: A statically typed compiled systems programming language
Source: nim-%version.tar
Patch: nim-1.0.0-alt-install.patch
Url: https://nim-lang.org
Group: Development/Other

# Automatically added by buildreq on Fri Jul 03 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 perl python2-base sh4
BuildRequires(pre): /proc
BuildRequires: parallel

%description
Nim is a statically typed compiled systems programming language. It
combines successful concepts from mature languages like Python, Ada and
Modula.

%prep
%setup -n nim-%version
%patch -p0
sed -i '/^linux)/,/Error: no C code generated for/{
s/set -x/parallel -j `nproc` <<@@@/
/binDir.nim/i@@@
}
' build.sh
for N in `grep -rl '#!.usr/bin/env python3' *`; do sed -i 's@.usr/bin/env python3@/usr/bin/python3@' $N; done
echo 'will cite' | parallel --citation > /dev/null 2>&1 ||:

%build
sh build.sh
bin/nim c koch
./koch boot -d:release
./koch tools
./koch docs

%install
mkdir -p %buildroot%prefix
sh ./install.sh %buildroot/usr
install koch %buildroot/%_bindir
install bin/* %buildroot/%_bindir/
install -D dist/nimble/nimble.bash-completion %buildroot%_datadir/bash-completion/completions/nimble
install -D dist/nimble/nimble.zsh-completion %buildroot%_datadir/zsh/site-functions/_nimble
install -D tools/nim.bash-completion %buildroot%_datadir/bash-completion/completions/nuim
install -D tools/nim.zsh-completion %buildroot%_datadir/zsh/site-functions/_nim

%files
%doc %_datadir/nim/doc
%doc doc/html examples
%_bindir/*
%_localstatedir/nim/pkgs
%prefix/lib/nim
%_sysconfdir/nim
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*

%changelog
* Fri Jul 03 2020 Fr. Br. George <george@altlinux.ru> 1.2.4-alt1
- Autobuild version bump to 1.2.4
- Package tools

* Tue Sep 24 2019 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build for ALT

