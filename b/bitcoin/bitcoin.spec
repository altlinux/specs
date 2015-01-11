Name: bitcoin
Version: 0.9.3
Release: alt1.rc1.1

Summary: peer-to-peer network based anonymous digital currency
License: MIT
Group: Networking/Other

Url: http://www.bitcoin.org/
Source: %name-%version.tar

BuildRequires: zlib-devel boost-devel libssl-devel gcc-c++ libdb4.8-devel libdb4.8_cxx-devel
BuildRequires: boost-filesystem-devel boost-interprocess-devel boost-program_options-devel
BuildRequires: libgtk+2-devel libwxGTK3.1-devel boost-asio-devel
BuildRequires: libqt4-devel lcov ccache libminiupnpc-devel
BuildPreReq: libprotobuf-devel protobuf-compiler gcc-objc clang-devel
BuildPreReq: libqrencode-devel boost-signals-devel

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
./autogen.sh
export OBJC=clang
export OBJCXX=clang++
%configure \
	--enable-upnp-default \
	--with-gui=qt4
%make_build V=1

%install
%makeinstall_std
ln -s %name-qt %buildroot%_bindir/%name

%pre
rm -f %_bindir/%name

%files
%_bindir/%{name}*
%doc doc/*

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.9.3-alt1.rc1.1
- rebuild with boost 1.57.0

* Thu Sep 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.rc1
- Version 0.9.3rc1

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.0-alt1.4.qa1
- NMU: rebuilt for updated dependencies.

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.4
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.3
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.2
- Rebuilt with Boost 1.51.0
- Enabled debuginfo

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

