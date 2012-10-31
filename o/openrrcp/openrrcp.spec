Name: openrrcp
Version: 0.2.1
Release: alt1
Summary: Realtek Remote Configuration Protocol
Source: %name-%version.tar
Group: Networking/Other
License: GPL

%description
RRCP(Realtek Remote Configuration Protocol) is protocol for making
some specific low-cost dumb ethernet switches act like more expensive
managed switches with no or little hardware modifications.

OpenRRCP is an open-source cross-platform RRCP-based toolset, that is
able to configure and fetch status from such ethernet switches.

%prep
%setup

%build
%make

%install
%make_install -C src PREFIX=%prefix DESTDIR=%buildroot install

%files
%_bindir/*

%changelog
* Wed Oct 31 2012 Afanasov Dmitry <ender@altlinux.org> 0.2.1-alt1
- first build
