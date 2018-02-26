Name: dangerdeep-data
Version: 0.4.0_pre3327
Release: alt1

Summary: Data for dangerdeep
License: GPL
Group: Games/Other

Url: http://dangerdeep.sourceforge.net/
Source: http://prdownloads.sourceforge.net/dangerdeep/%name-%version.zip
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildArch: noarch

# Automatically added by buildreq on Mon Jan 01 2007
BuildRequires: unzip

%description
Danger from the deep (aka dangerdeep) is a Free / Open Source World War II
german submarine simulation. It is currently available for Linux/i386 and
Windows, but since it uses SDL/OpenGL it should be portable to other operating
systems or platforms. (If anyone whishes to port it, please contact us.) This
game is planned as tactical simulation and will be as realistic as our time and
knowledge of physics allows. It's current state is ALPHA, but it is playable.

%prep
%setup -q -n data

%install
install -d %buildroot%_datadir/dangerdeep
cp -r * %buildroot%_datadir/dangerdeep/

%files
%doc LICENSE
%_datadir/dangerdeep
%exclude %_datadir/dangerdeep/LICENSE

%changelog
* Mon Jul 26 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.0_pre3327-alt1
- New version
- Update spec

* Mon Jan 01 2007 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- built for ALT Linux
- spec based on Mandriva 2007 contrib (0.2.0-2mdv2007.0)
  by Guillaume Rousse <guillomovitch@mandriva.org>
