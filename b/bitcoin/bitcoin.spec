Name: bitcoin
Version: 0.6.0
Release: alt1.1

Summary: peer-to-peer network based anonymous digital currency
License: MIT
Group: Networking/Other

Url: http://www.bitcoin.org/
Source: %name-%version.tar

BuildRequires: zlib-devel boost-devel libssl-devel gcc-c++ libdb4-devel libdb4_cxx-devel
BuildRequires: boost-filesystem-devel boost-interprocess-devel boost-program_options-devel
BuildRequires: libgtk+2-devel libwxGTK2.9-devel boost-asio-devel
BuildRequires: libqt4-devel

%description
Q. What is Bitcoin?
A. Bitcoin is a peer-to-peer currency. Peer-to-peer means that no
central authority issues new money or tracks transactions. These tasks
are managed collectively by the network.

Q. How does Bitcoin work?
A. Bitcoin utilises public-key cryptography. A coin contains the owner's
public key. When a coin is transferred from user A to user B, A adds B's
public key to the coin, and the coin is signed using A's private key. B
now owns the coin and can transfer it further. A is prevented from
transferring the already spent coin to other users because a public list
of all previous transactions is collectively maintained by the network.
Before each transaction the coin's validity will be checked.

%prep
%setup

%build
pushd src
%make_build -f makefile.unix -e PIE=1
popd
qmake-qt4 "USE_UPNP=-"
%make_build

%install
install -pDm0755 %name-qt %buildroot%_bindir/%name
install -pDm0755 src/%{name}d %buildroot%_bindir/%{name}d

%files
%_bindir/%name
%_bindir/%{name}d
%doc doc/*

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.1
- Rebuilt with Boost 1.49.0

* Sat Mar 31 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 0.6.0-alt1
- 0.6.0 (Closes: #26403).

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.1
- Rebuilt with Boost 1.48.0

* Tue Oct 04 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.4.0-alt1
- 0.4.0 (Closes: #26403).

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.21-alt1.1
- Rebuilt with Boost 1.47.0

* Wed May 04 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.21-alt1
- Initial build for Sisyphus.

