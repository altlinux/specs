Name: jtalk
Version: 20060521
Release: alt1.qa1

Summary: Jtalk is a simple Jabber client
Group: Networking/Instant messaging
License: GPL

Url: http://www.eleves.ens.fr/home/george/info/prg/jtalk/

Source0: %name-%version.tar.bz2

Patch0: %name-%version-alt-ass-needed.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Jan 13 2007
BuildRequires: libloudmouth-devel libpcre-devel libreadline-devel linux-libc-headers 

%description
Jtalk is a Jabber client that provides an interface somewhat similar to the
historic Unix Talk system. Jtalk is distributed under the terms of the GNU
General Public Licence.

Note: jtalk is not a full-featured Jabber client. It focuses only on the
presence and messages. To handle your rooster, undate your information,
create accounts and so on, you need another, more complete, Jabber client.

%prep
%setup -q
%patch0 -p1

%build
%make_build

%install
%make_install DESTDIR=%buildroot PREFIX=%_prefix install

%files
%_bindir/*
%_prefix/libexec/*
%dir %_datadir/doc/jtalk/
%doc %_datadir/doc/jtalk/manual.html


%changelog
* Wed Sep 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 20060521-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * deprecated-packages-info-i18n-common for jtalk
  * postclean-05-filetriggers for spec file

* Sat Jan 13 2007 Igor Zubkov <icesik@altlinux.org> 20060521-alt1
- initial build for Sisyphus


