Name: monotone
Version: 1.1
Release: alt1

Summary: Distributed version control system
License: GPL
Group: Development/Tools

Url: http://monotone.ca

Source: %name-%version.tar

BuildRequires: pcre-devel boost-devel libbotan-devel pkg-config
BuildRequires: libidn-devel liblua5-devel libsqlite3-devel texinfo
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

%build
%autoreconf
%add_optflags -std=gnu++11
%add_optflags -DBOOST_DISABLE_ASSERTS=1 -DBOOST_ENABLE_ASSERT_HANDLER
%configure --enable-ipv6
%make_build

#check
#DISABLE_NETWORK_TESTS=1 %make check

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_bindir/*
%_infodir/*
%_man1dir/*
%_sysconfdir/bash_completion.d/*
%_datadir/%name
%doc %_docdir/%name
%doc AUTHORS NEWS README UPGRADE HACKING INSTALL ChangeLog notes/*

%changelog
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

