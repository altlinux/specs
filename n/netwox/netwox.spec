Name: netwox
Version: 5.39.0
Release: alt1

Summary: A toolbox for network administrators and network hackers
License: GPL
Group: Networking/Other

Url: http://www.laurentconstantin.com/en/netw/netwox/
Source0: http://www.laurentconstantin.com/common/netw/netwox/download/v5/%name-%version-src.tgz
Source1: html.tar

# Automatically added by buildreq on Thu Feb 16 2006
BuildRequires: libnet2-devel libnetwib-devel libpcap-devel

%description
Netwox is a toolbox for network administrators and network hackers.
Netwox contains over 200 tools using network library netwib.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description docs
Netwox is a toolbox for network administrators and network hackers.
Netwox contains over 200 tools using network library netwib.

This package contains documentation for %name.

%prep
%setup -n %name-%version-src
tar -xf %SOURCE1

%build
cd src
./genemake NETWIBDEF_INSTPREFIX="/usr"
sed -i -e 's,444,644,' -e 's,555,755,g' Makefile
%make_build

%install
install -d %buildroot{%_bindir,%_man1dir}

%make -C src install \
        INSTBIN=%buildroot%_bindir \
        INSTMAN1=%buildroot%_man1dir \
        INSTUSERGROUP="$(id -u):$(id -g)"

rm -f doc/gpl.txt

%files
%_bindir/*
%_man1dir/*
%doc doc misc README.TXT

%files docs
%doc html/*

%changelog
* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.39.0-alt1
- Version 5.39.0

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.34.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Apr 21 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.34.0-alt1
- new version (5.34.0)

* Wed Feb 15 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.33.0-alt1
- Initial build for Sisyphus (adopted spec from PLD)
