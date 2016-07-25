Name: mscgen
Version: 0.20
Release: alt3
Summary: Message Sequence Chart Renderer
Group: Publishing
License: GPLv2+
# http://www.mcternan.me.uk/mscgen/software/
Source: %name-%version.tar
Patch: mscgen-0.20-bison3.patch
Url: http://www.mcternan.me.uk/mscgen/

# Automatically added by buildreq on Wed Sep 18 2013
# optimized out: fontconfig pkg-config
BuildRequires: flex libgd2-devel

%description
Mscgen is a small program that parses Message Sequence Chart
descriptions and produces PNG, SVG, EPS or server side image maps
(ismaps) as the output. Message Sequence Charts (MSCs) are a way of
representing entities and interactions over some time period and are
often used in combination with SDL. MSCs are popular in Telecoms to
specify how protocols operate although MSCs need not be complicated to
create or use. Mscgen aims to provide a simple text language that is
clear to create, edit and understand, which can also be transformed into
common image formats for display or printing.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc %_defaultdocdir/%name
%_bindir/*
%_man1dir/*

%changelog
* Mon Jul 25 2016 Fr. Br. George <george@altlinux.ru> 0.20-alt3
- Fix build
- Upstream googlecode is gone

* Wed Sep 18 2013 Fr. Br. George <george@altlinux.ru> 0.20-alt2
- Update to SVN r201

* Wed Sep 18 2013 Fr. Br. George <george@altlinux.ru> 0.20-alt1
- Autobuild version bump to 0.20
