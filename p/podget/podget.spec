Name: podget
Summary: Simple podcast aggregator
Version: 0.6
Release: alt1

Source: http://prdownloads.sourceforge.net/podget/%name-%version.tar.gz
Url: http://podget.sourceforge.net/
License: GPLv2+
Group: Networking/News

BuildArch: noarch

%description
Podget is a simple podcast aggregator with support for RSS and Bittorrent
feeds, folders and categories, and automatic playlist creation.

%prep
%setup
perl -pi -e 's/get_torrents\=0/get_torrents\=1/' podget.sh

%install
mkdir -p %buildroot/%_bindir
cp %name %buildroot/%_bindir

%files
%doc README
%_bindir/%name

%changelog
* Tue Aug 30 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6-alt1
- Initial build

* Thu Jul 22 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6-1mdv2011.0
+ Revision: 557059
- use the tar.gz given by upstream
- update to 0.6
- fix source and %%prep

* Sun Jun 21 2009 Jérôme Brenier <incubusss@mandriva.org> 0.5.8-5mdv2010.0
+ Revision: 387941
- fix license tag

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.5.8-4mdv2009.0
+ Revision: 259131
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5.8-3mdv2009.0
+ Revision: 247051
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5.8-1mdv2008.1
+ Revision: 136426
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jan 11 2007 Lenny Cartier <lenny@mandriva.com> 0.5.8-1mdv2007.0
+ Revision: 107378
- Update to 0.5.8
- Import podget

