Name:           ipobfs
# VERSION=`git log -1 --format="%as" | tr -- - .`
# git archive HEAD --prefix ipobfs-2021.12/ -o ~/RPM/SOURCES/ipobfs-$VERSION.tar.gz
Version:        2021.12
Release:        alt1
Summary:        IP and trasnsport layer packet mangling tool

URL:            https://github.com/bol-van/ipobfs
Source:         %name-%version.tar.gz
Source1:        %name-initd
Source2:        config.default
Source3:        %name-client@.service
Source4:        %name-server@.service
Group:          Networking/Other
License:        BSD

# Automatically added by buildreq on Sat Aug 24 2024
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libnfnetlink-devel python3-base sh5
BuildRequires: libcap-devel libnetfilter_queue-devel

%description
IPObfs is NFQUEUE based IP and transport packet mangler. You can pick
some packet by firewall filter, modify it by IPObfs anf inhect back to
packet queue.

%prep
#TODO kernel module
%setup
cat > config.example <<@@@
PROTOXOR=0
PORT=<WG server port>
FIREWALL=nft
ROUTE=<WG server>
QUEUE=310
@@@

%build
%make_build -C ipobfs

%install
install -D ipobfs/ipobfs %buildroot%_sbindir/%name
install -D %SOURCE1 %buildroot%_initdir/%name
ln -sr %buildroot%_initdir/%name %buildroot%_initdir/%name.client
ln -sr %buildroot%_initdir/%name %buildroot%_initdir/%name.server
install -D %SOURCE2 %buildroot%_sysconfdir/%name/default
install -D %SOURCE3 %buildroot%_unitdir/`basename %SOURCE3`
install -D %SOURCE4 %buildroot%_unitdir/`basename %SOURCE4`

%files
%doc *.txt config.example
%_sbindir/*
%_sysconfdir/%name
%_initdir/%{name}*
%_unitdir/*

%changelog
* Mon Aug 26 2024 Fr. Br. George <george@altlinux.org> 2021.12-alt1
- Initial build for ALT
