%def_disable check

Name: monotone
Version: 1.2
Release: alt3.dev.mtn20150211.1

Summary: Distributed version control system
License: GPL
Group: Development/Tools

Url: http://monotone.ca

# get: mtn clone mtn://code.monotone.ca/monotone?net.venge.monotone
# update: mtn pull --update
Source: %name-%version.tar

BuildRequires: pcre-devel boost-devel libbotan-devel pkg-config
BuildRequires: libidn-devel lua-devel libsqlite3-devel texinfo
BuildRequires: zlib-devel gcc-c++

%description
monotone is a free, distributed version control system. It provides
fully disconnected operation, manages complete tree versions, keeps
its state in a local transactional database, supports overlapping
branches and extensible metadata, exchanges work over plain network
protocols, performs history-sensitive merging, and delegates trust
functions to client-side RSA certificates.

%prep
%setup

rm -fR Attic/botan

%build
%autoreconf
%add_optflags -std=gnu++11
%add_optflags -DBOOST_DISABLE_ASSERTS=1 -DBOOST_ENABLE_ASSERT_HANDLER
export CPPFLAGS="%optflags"
%configure --enable-ipv6
%make_build

%check
DISABLE_NETWORK_TESTS=1 make check

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_bindir/*
%_infodir/*
%_man1dir/*
#_sysconfdir/bash_completion.d/*
%_datadir/%name
%doc %_docdir/%name
%doc AUTHORS NEWS README UPGRADE HACKING INSTALL ChangeLog notes/*

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3.dev.mtn20150211.1
- rebuild with new lua 5.3

* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 1.2-alt3.dev.mtn20150211
- Rebuild with new libbotan

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.mtn20150211
- New snapshot

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.mtn20140605
- Deleted bash completion file (ALT #30775)

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev.mtn20140605
- Version 1.2dev

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Version 1.1

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.2
- Fixed build with Boost 1.53.0

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Fixed build with gcc 4.7

* Thu Mar 31 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.0-alt1
- 1.0 release.
- Enable ipv6 support.

* Mon Nov 15 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.99.1-alt1
- Initial build for Sisyphus.

