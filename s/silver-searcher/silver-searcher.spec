Name: silver-searcher
Version: 2.2.0
Release: alt3

Summary: A code searching tool similar to ack, with a focus on speed
License: Apache-2.0
Group: Development/Tools

Url: https://geoff.greer.fm/ag/
# https://github.com/ggreer/the_silver_searcher/
Source: %name-%version.tar

# Automatically added by buildreq on Sun Jun 07 2015
BuildRequires: liblzma-devel libpcre-devel zlib-devel

%description
Ag (silversearcher) is a code searching tool.
It is an order of magnitude faster than ack.
It ignores file patterns from .gitignore and .hgignore.
If there are files in your source repo you don't want to search,
just add their patterns to a .ignore file.
The command name is 33%% shorter than ack, and all keys are on the home row!

%prep
%setup

%build
%autoreconf
%add_optflags -fcommon
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/ag
%_man1dir/ag.1.*
%_datadir/the_silver_searcher/completions/ag.bashcomp.sh
%_datadir/zsh/site-functions/_the_silver_searcher
%doc README.md

%changelog
* Wed Apr 07 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt3
- Fixed FTBFS with -fcommon.

* Wed Jun 19 2019 Michael Shigorin <mike@altlinux.org> 2.2.0-alt2
- fixed build on e2k (looks like clang was overlooked anyways)
- minor spec cleanup

* Sat Aug 18 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.2.0-alt1
- new version 2.2.0

* Sun Oct 01 2017 Mikhail Gordeev <obirvalger@altlinux.org> 2.1.0-alt1
- new version 2.1.0

* Sat Dec 17 2016 Andrey Bergman <vkni@altlinux.org> 1.0.2-alt1
- Version update.

* Mon Oct 12 2015 Andrey Bergman <vkni@altlinux.org> 0.31.0-alt0.1
- Version update.

* Sat Jun 06 2015 Andrey Bergman <vkni@altlinux.org> 0.30.0-alt0.1
- Initial release for Sisyphus.

