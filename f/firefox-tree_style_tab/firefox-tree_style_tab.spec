%define rname	tree_style_tab
%define cid 	treestyletab@piro.sakura.ne.jp
%define ciddir  %firefox_noarch_extensionsdir/%cid

Name: firefox-%rname
Version: 0.15.2014120101
Release: alt1

Summary: Tree Style Tab extension for Firefox
License: MPL 1.1/GPL 2.0/LGPL 2.1
Group: Networking/WWW

Url: https://addons.mozilla.org/en-us/firefox/addon/tree-style-tab/
# reviewed
#Source: https://addons.mozilla.org/firefox/downloads/file/258152/%rname-%version-fx.xpi
# current
Source: http://piro.sakura.ne.jp/xul/xpi/treestyletab.xpi
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-firefox
BuildRequires: unzip

# these are ELF binaries for Mozilla Weave
%define _verify_elf_method skip
%brp_strip_none %ciddir
AutoReq: yes, nolib, noshell

%description
This provides tree-style tab bar. New tabs opened from links etc.
are automatically attached to the current tab. If you often use
many many tabs, it will help your web browsing because you can
understand relations of tabs.

Features:

* You can collapse/expand sub trees. It is convenient for too many tabs.
* When you close a tab which has collapsed sub tree, all of tabs
  in the sub tree will be closed only one action.
* The tree of tabs can be showin at rightside.
* Vertical tab bar cab be shown/hidden automatically.
* You can open new tab between existing tabs, dropping link
  or URL string there.
* You can save/restore the tree of tabs over sessions,
  by Session Manager ( https://addons.mozilla.org/firefox/addon/2324 )
  or other session-management addons.
* Drag and drop is available to modify relations of tabs and to rearrange.
* Tab bar can be moved to leftside, rightside, top, or bottom.
  Horizontal tree is also available.
* This has an API for extension authors to open child tabs for
  existing tabs.
  (See also http://piro.sakura.ne.jp/xul/_treestyletab.html.en#api )

%prep
%setup -c

%install
mkdir -p %buildroot/%ciddir
cp -pr * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then [ ! -d "%ciddir" ] || rm -rf "%ciddir"; fi

%files
%ciddir

%changelog
* Wed Dec 10 2014 Michael Shigorin <mike@altlinux.org> 0.15.2014120101-alt1
- updated for better compatibility with Firefox 34

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 0.14.2014051101-alt1
- built for ALT Linux
