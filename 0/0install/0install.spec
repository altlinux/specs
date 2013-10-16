Name: 0install
Version: 2.4.1
Release: alt1
Summary: Decentralised cross-distribution software installation system
Group: System/Configuration/Packaging
Source: %name-%version.tar.bz2
Url: http://0install.net/
License: LGPLv2
BuildArch: noarch

# Automatically added by buildreq on Thu Jan 17 2013
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-logging
BuildRequires: python-devel python-module-pygobject

%description
Zero Install is a decentralised cross-distribution software installation
system available under the LGPL. It allows software developers to
publish programs directly from their own web-sites, while supporting
features familiar from centralised distribution repositories such as
shared libraries, automatic updates and digital signatures. It is
intended to complement, rather than replace, the operating system's
package management. 0install packages never interfere with those
provided by the distribution.

0install does not define a new packaging format; unmodified tarballs or
zip archives can be used. Instead, it defines an XML metadata format to
describe these packages and the dependencies between them. A single
metadata file can be used on multiple platforms (e.g. Ubuntu, Debian,
Fedora, openSUSE, Mac OS X and Windows), assuming binary or source
archives are available that work on those systems.

0install also has some interesting features not often found in
traditional package managers. For example, while it will share libraries
whenever possible, it can always install multiple versions of a package
in parallel when there are conflicting requirements. Installation is
always side-effect-free (each package is unpacked to its own directory
and will not touch shared directories such as /usr/bin), making it ideal
for use with sandboxing technologies and virtualisation.

%setup_python_module zeroinstall
%package -n %packagename
Group: Development/Python
Summary: Supplemental python module for %name
%description -n %packagename
Supplemental python module for %name

%package -n zsh-completion-%name
Group: Shells
Summary: ZSH completion for %name
%description -n zsh-completion-%name
ZSH completion for %name

%package -n bash-completion-%name
Group: Shells
Summary: Bash completion for %name
%description -n bash-completion-%name
Bash completion for %name

%package -n fish-completion-%name
Group: Shells
Summary: Fish completion for %name
%description -n fish-completion-%name
Fish completion for %name

%prep
%setup

%build
%python_build
# hack crappy installer
sed '
/^cd .*\/files/d
/^\.\/0install/d
/^DOCS=/cDOCS="README.md COPYING"
/^ZSHFUNCTIONS=/s@.*@ZSHFUNCTIONS="share/zsh/Completion/Linux"@
' < install.sh.src > install.sh
ln -s 0install-python-fallback 0install

%install
#python_install
sh install.sh %buildroot%_prefix
%find_lang zero-install

%files
%doc %_defaultdocdir/%name
%_bindir/*
%_man1dir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%files -n %packagename -f zero-install.lang
#_xdgmenusdir/applications-merged/*
%python_sitelibdir/zeroinstall*

%files -n zsh-completion-%name
%_datadir/zsh/Completion/Linux/*

%files -n bash-completion-%name
%_datadir/bash-completion/completions/*

%files -n fish-completion-%name
%_datadir/fish/completions/*

%changelog
* Tue Oct 15 2013 Fr. Br. George <george@altlinux.ru> 2.4.1-alt1
- Autobuild version bump to 2.4.1
- Force not to use ocaml due to incomplete requirements

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 2.3.3-alt1
- Autobuild version bump to 2.3.3
- Drop newly introduced ocaml bindings
- Fix patch

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Autobuild version bump to 2.2
- Fix patch

* Tue Feb 19 2013 Fr. Br. George <george@altlinux.ru> 1.15-alt1
- Autobuild version bump to 1.15
- Fix patch

* Thu Jan 17 2013 Fr. Br. George <george@altlinux.ru> 0.0-alt1
Initial "zero version" build

