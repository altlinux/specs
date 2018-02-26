Name: monotone
Version: 1.0
Release: alt1

Summary: Distributed version control system
License: GPL
Group: Development/Tools

Url: http://monotone.ca

Source: %name-%version.tar

BuildRequires: pcre-devel boost-devel libbotan-devel pkg-config libidn-devel liblua5-devel libsqlite3-devel texinfo
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
%configure --enable-ipv6
%make_build

#%%check
#DISABLE_NETWORK_TESTS=1 %make check

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_bindir/*
%_infodir/*
%_man1dir/*
%doc AUTHORS NEWS README UPGRADE HACKING INSTALL

%changelog
* Thu Mar 31 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.0-alt1
- 1.0 release.
- Enable ipv6 support.

* Mon Nov 15 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.99.1-alt1
- Initial build for Sisyphus.

