%global import_path golang.org/x/crypto

%global commit b35ccbc95a0eaae49fb65c5d627cb7149ed8d1ab
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-golang-x-crypto
Version: 0
Release: alt3.git%abbrev
Summary: Supplementary Go cryptography libraries
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Supplementary Go cryptography libraries

%package devel
Summary: Supplementary Go cryptography libraries
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release
Provides: golang(%import_path/pbkdf2) = %version-%release
Provides: golang(%import_path/md4) = %version-%release
Provides: golang(%import_path/ripemd160) = %version-%release
Provides: golang(%import_path/ocsp) = %version-%release
Provides: golang(%import_path/tea) = %version-%release
Provides: golang(%import_path/ssh) = %version-%release
Provides: golang(%import_path/ssh/test) = %version-%release
Provides: golang(%import_path/ssh/testdata) = %version-%release
Provides: golang(%import_path/ssh/agent) = %version-%release
Provides: golang(%import_path/ssh/terminal) = %version-%release
Provides: golang(%import_path/curve25519) = %version-%release
Provides: golang(%import_path/twofish) = %version-%release
Provides: golang(%import_path/nacl) = %version-%release
Provides: golang(%import_path/nacl/secretbox) = %version-%release
Provides: golang(%import_path/nacl/box) = %version-%release
Provides: golang(%import_path/poly1305) = %version-%release
Provides: golang(%import_path/.gear) = %version-%release
Provides: golang(%import_path/scrypt) = %version-%release
Provides: golang(%import_path/salsa20) = %version-%release
Provides: golang(%import_path/salsa20/salsa) = %version-%release
Provides: golang(%import_path/xts) = %version-%release
Provides: golang(%import_path/bcrypt) = %version-%release
Provides: golang(%import_path/bn256) = %version-%release
Provides: golang(%import_path/xtea) = %version-%release
Provides: golang(%import_path/hkdf) = %version-%release
Provides: golang(%import_path/openpgp) = %version-%release
Provides: golang(%import_path/openpgp/errors) = %version-%release
Provides: golang(%import_path/openpgp/packet) = %version-%release
Provides: golang(%import_path/openpgp/armor) = %version-%release
Provides: golang(%import_path/openpgp/elgamal) = %version-%release
Provides: golang(%import_path/openpgp/s2k) = %version-%release
Provides: golang(%import_path/openpgp/clearsign) = %version-%release
Provides: golang(%import_path/blowfish) = %version-%release
Provides: golang(%import_path/cast5) = %version-%release
Provides: golang(%import_path/sha3) = %version-%release
Provides: golang(%import_path/sha3/testdata) = %version-%release
Provides: golang(%import_path/pkcs12) = %version-%release
Provides: golang(%import_path/pkcs12/internal) = %version-%release
Provides: golang(%import_path/pkcs12/internal/rc2) = %version-%release
Provides: golang(%import_path/otr) = %version-%release

%description devel
Supplementary Go cryptography libraries

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

%files devel
%doc AUTHORS README LICENSE
%go_path/src/*

%changelog
* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 0-alt3.gitb35ccbc9
- Update

* Thu Apr 14 2016 Denis Pynkin <dans@altlinux.org> 0-alt2.git1777f3ba
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.git1f22c010
- Initial package

