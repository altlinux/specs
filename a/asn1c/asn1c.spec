%define _unpackaged_files_terminate_build 1

Name: asn1c
Version: 0.9.28
Release: alt1

Summary: The ASN.1 Compiler
License: BSD-2-Clause
Group: Development/C
Url: https://lionet.info/asn1c/blog/
Vcs: https://github.com/vlm/asn1c

Source0: %name-%version.tar

%description
ASN.1 to C compiler takes the ASN.1 module files (example) and generates the C++ compatible C source code. That code can be used to serialize the native C structures into compact and unambiguous BER/OER/PER/XER-based data files, and deserialize the files back.
Various ASN.1 based formats are widely used in the industry, such as to encode the X.509 certificates employed in the HTTPS handshake, to exchange control data between mobile phones and cellular networks, to perform car-to-car communication in intelligent transportation networks.
The ASN.1 family of standards is large and complex, and no open source compiler supports it in its entirety. The asn1c is arguably the most evolved open source ASN.1 compiler.

%package devel
BuildArch: noarch
Summary: Header files and sources required to build the asn1c generated source.
Group: Development/C
Requires: asn1c = %version-%release

%description devel
The asn1c-devel package contains the header files and sources needed to develop programs that uses asn1c generated source.

%package examples
BuildArch: noarch
Summary: Exmaples for %name
Group: Development/C
Requires: asn1c = %version-%release

%description examples
The asn1c-examples package contains examples file for %name.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build all

%check
%make_build check

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_datadir/%name/
cp -a examples %buildroot%_datadir/%name/

%files
%_bindir/*
%_man1dir/*
%_docdir/*
%dir %_datadir/%name
%_datadir/%name/standard-modules
%_datadir/%name/README
%_datadir/%name/file-dependencies

%files devel
%_datadir/%name/*.h
%_datadir/%name/*.c

%files examples
%dir %_datadir/%name/examples
%_datadir/%name/examples/*

%changelog
* Tue Dec 24 2024 Gedert Korney <kiper@altlinux.org> 0.9.28-alt1
- Initial build.
