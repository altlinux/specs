Name: jirc
Version: 1.1
Release: alt2

Summary: Bridges an IRC channel to a Jabber conference room.
License: GPLv2+
Group: Development/Perl
Url: http://outflux.net/software/pkgs/jirc-bridge/
Packager: Alexey Shabalin <shaba@altlinux.ru>

BuildArch: noarch
Source: %url/download/%name-%version.tar.gz
Patch: jirc-1.1-alt-poe.patch

# Automatically added by buildreq on Sun Nov 20 2011 (-bi)
BuildRequires: perl-Config-Simple perl-Filter-Template perl-Net-Jabber perl-POE-Component-IRC perl-POE-Component-Jabber perl-Pod-Parser perl-devel

%description
This is a Perl POE bot script that connects a Jabber conference room with an IRC channel, relaying conversations. 

%prep
%setup -q -n %name-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README jirc.conf
%_bindir/jirc

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.1-alt2
- disabled dependency on POE::Filter::XML::Utils

* Mon Nov 29 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- 1.1

* Thu Oct 29 2009 Alexey Shabalin <shaba@altlinux.ru> 0.9-alt1
- 0.9

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- First build for Sisyphus
