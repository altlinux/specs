Name: netwox
Version: 5.34.0
Release: alt1

Summary: A toolbox for network administrators and network hackers
License: GPL
Group: Networking/Other

Url: http://www.laurentconstantin.com/en/netw/netwox/
Source0: http://www.laurentconstantin.com/common/netw/netwox/download/v5/%name-%version-src.tgz
Patch0: %name-config.patch

# Automatically added by buildreq on Thu Feb 16 2006
BuildRequires: libnet2-devel libnetwib-devel libpcap-devel

%description
Netwox is a toolbox for network administrators and network hackers.
Netwox contains over 200 tools using network library netwib.

%prep
%setup -q -n %name-%version-src
%patch0 -p1

%build
cd src
./genemake NETWIBDEF_INSTPREFIX="/usr"
sed -i -e 's,444,644,' -e 's,555,755,g' Makefile
%make

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

%changelog
* Fri Apr 21 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.34.0-alt1
- new version (5.34.0)

* Wed Feb 15 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.33.0-alt1
- Initial build for Sisyphus (adopted spec from PLD)
