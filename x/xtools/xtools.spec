Name: xtools
Version: 0.68
Release: alt1

Summary: A collection of small utilities for use with XBPS
License: CC0-1.0
Group: Other
Url: https://git.vuxu.org/xtools
Vcs: https://git.vuxu.org/xtools

Source: %name-%version.tar

BuildArch: noarch

%description
Tools working on the void-packages tree use xdistdir to find it, check
that its output is reasonable first.
xi, xls, xq and xrs prefer the hostdir / binpkgs repo if you run them
from a void-packages checkout.

%prep
%setup

%install
%makeinstall_std PREFIX=%prefix

%files
%_bindir/xtree
%_bindir/xbarf
%_bindir/xbulk
%_bindir/xbump
%_bindir/xchangelog
%_bindir/xcheckmypkgs
%_bindir/xcheckrestart
%_bindir/xchroot
%_bindir/xclash
%_bindir/xdbg
%_bindir/xdeptree
%_bindir/xdiff
%_bindir/xdistdir
%_bindir/xdowngrade
%_bindir/xetcchanges
%_bindir/xgenfstab
%_bindir/xgensum
%_bindir/xgrep
%_bindir/xhog
%_bindir/xi
%_bindir/xilog
%_bindir/xlg
%_bindir/xlint
%_bindir/xlocate
%_bindir/xlog
%_bindir/xls
%_bindir/xmandoc
%_bindir/xmksv
%_bindir/xmypkgs
%_bindir/xnew
%_bindir/xnews
%_bindir/xnodev
%_bindir/xoptdiff
%_bindir/xpcdeps
%_bindir/xpkg
%_bindir/xpkgdiff
%_bindir/xpstree
%_bindir/xq
%_bindir/xrevbump
%_bindir/xrevshlib
%_bindir/xrs
%_bindir/xsrc
%_bindir/xsubpkg
%_bindir/xuname
%_bindir/xvoidstrap
%_man1dir/%name.1.xz
%_man1dir/xtree.1.xz
%_man1dir/xbarf.1.xz
%_man1dir/xbulk.1.xz
%_man1dir/xbump.1.xz
%_man1dir/xchangelog.1.xz
%_man1dir/xcheckmypkgs.1.xz
%_man1dir/xcheckrestart.1.xz
%_man1dir/xchroot.1.xz
%_man1dir/xclash.1.xz
%_man1dir/xdbg.1.xz
%_man1dir/xdeptree.1.xz
%_man1dir/xdiff.1.xz
%_man1dir/xdistdir.1.xz
%_man1dir/xdowngrade.1.xz
%_man1dir/xetcchanges.1.xz
%_man1dir/xgenfstab.1.xz
%_man1dir/xgensum.1.xz
%_man1dir/xgrep.1.xz
%_man1dir/xhog.1.xz
%_man1dir/xi.1.xz
%_man1dir/xilog.1.xz
%_man1dir/xlg.1.xz
%_man1dir/xlint.1.xz
%_man1dir/xlocate.1.xz
%_man1dir/xlog.1.xz
%_man1dir/xls.1.xz
%_man1dir/xmandoc.1.xz
%_man1dir/xmksv.1.xz
%_man1dir/xmypkgs.1.xz
%_man1dir/xnew.1.xz
%_man1dir/xnews.1.xz
%_man1dir/xnodev.1.xz
%_man1dir/xoptdiff.1.xz
%_man1dir/xpcdeps.1.xz
%_man1dir/xpkg.1.xz
%_man1dir/xpkgdiff.1.xz
%_man1dir/xpstree.1.xz
%_man1dir/xq.1.xz
%_man1dir/xrevbump.1.xz
%_man1dir/xrevshlib.1.xz
%_man1dir/xrs.1.xz
%_man1dir/xsrc.1.xz
%_man1dir/xsubpkg.1.xz
%_man1dir/xuname.1.xz
%_man1dir/xvoidstrap.1.xz
%_datadir/zsh/site-functions/*
%_datadir/fish/vendor_completions.d/*
%_datadir/fish/vendor_functions.d/*

%changelog
* Tue Mar 11 2025 Ulysses Apokin <ulysses@altlinux.org> 0.68-alt1
- Initial build for Sisyphus.
