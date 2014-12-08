%define ShortName Scribunto
%define major 1.23
%define revision wmf22

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt1

Summary: The extension allows for embedding scripting languages in MediaWiki

License: GPLv2
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Requires: mediawiki-common >= 1.23

Requires: lua5

# Source-git: https://git.wikimedia.org/git/mediawiki/extensions/%ShortName.git
Source: %name-%version.tar

BuildPreReq: rpm-build-mediawiki >= 0.3

# Automatically added by buildreq on Fri Nov 28 2014
# optimized out: python3-base
#BuildRequires: libdb4-devel python3 ruby ruby-stdlibs

%description
The Scribunto (Latin: "they shall write") extension allows for embedding scripting languages in MediaWiki.
Currently the only supported scripting language is Lua.

%prep
%setup

%build

%install
%mediawiki_ext_install 50 %ShortName
# will use system lua
rm -rf %buildroot/%_mediawikidir/extensions/%ShortName/engines/LuaStandalone/binaries
subst "4i\$wgScribuntoEngineConf['luastandalone']['luaPath'] = '%_bindir/lua';" %buildroot%_mediawiki_settings_dir/50-%ShortName.php

#check
#make tests

%files -f %ShortName.files

%changelog
* Mon Dec 08 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.wmf22-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.wmf22-alt0
- initial build for ALT Linux Sisyphus
